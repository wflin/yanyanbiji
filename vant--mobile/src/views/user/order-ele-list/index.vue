<template>
  <div class="order_list" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="100">
    <van-tabs sticky :active="activeIndex" :swipe-threshold="5" @click="handleTabClick">
      <van-tab v-for="tab in tabsItem" :title="tab.name" :key="tab.type">
      </van-tab>
    </van-tabs>

    <van-panel v-for="(el, i) in orderData" class="order_list--panel" :key="i" :title="'订单编号: ' + el.order.order_num">
      <div>
        <van-card class="order_list--van-card" :title="el.product.name" :desc="el.product.detail" :num="el.order.product_num" :price="(el.order.product_amount / 100).toFixed(2)" :thumb="el.product.pic" @click.native="toOrderDetail(el.order.id)" />
        <div class="order_list--total">
          合计: {{el.order.product_amount*el.order.product_num | yuan}}（含运费{{el.order.logistics_amount | yuan}}）
        </div>
      </div>
      <div slot="footer" class="order_list--footer_btn">
        <van-button size="small" type="danger" @click="reminderOrder()" v-if="search.cond.status == 0">提醒发货</van-button>
        <van-button size="small" @click="closeOrder(el.order.id)" v-if="search.cond.status == 0">关闭订单</van-button>
        <van-button size="small" type="danger" @click="sureOrder(el.order.id)" v-if="search.cond.status == 2">确认收货</van-button>
        <van-button size="small" v-if=" search.cond.status == 3 || search.cond.status == 4 " @click="toOrderDetail(el.order.id)">查看详情</van-button>
      </div>
    </van-panel>

    <van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />

    <is-empty v-model="!orderData.length">抱歉,没有找到符合条件的订单</is-empty>
  </div>
</template>

<script>
const api = new GLOBAL.api()
import { Tab, Tabs, Panel, Card, Dialog } from 'vant';
import IsEmpty from "@/vue/components/is-empty/";

export default {
  name: 'order-list',
  props: {
    active: {
      type: [String, Number],
      default: 0
    }
  },

  data() {
    const activeIndex = this.active;
    return {
      activeIndex,
      items: [],
      isLoading: false,
      orderData: [],
      myStatus: '',
      tabsItem: [{
        name: "未发货",
        status: 0,
      }, {
        name: "已发货",
        status: 1,
      }, {
        name: "待收货",
        status: 2,
      }, {
        name: "已完成",
        status: 3,
      }, {
        name: "交易关闭",
        status: 4,
      }],
      // 查询
      search: {
        "cond": {
          "type": "buy",
          "product_name": "",
          "status": ''
        },
        "limit": 8,
        "page": 1
      },
      orderTotal: ''
    }
  },

  created() {
    this.search.cond.status = this.$route.params.active
    this.getOrderList();
  },

  methods: {
    // 上拉加载
    nextPage() {
      this.search.page += 1;
      this.getOrderList()
    },
    loadMore() {
      let i = this.search.page * this.search.limit
      if (i < this.orderTotal) {
        this.nextPage()
      }
    },
    // 订单列表查询
    getOrderList() {
      this.isLoading = true
      let params = {
        url: 'order/list',
        data: this.search
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          if (this.search.page > 1) {
            for (let i in res.data) {
              this.orderData.push(res.data[i])
            }
          } else {
            this.orderData = res.data
          }
          this.isLoading = false
          this.orderTotal = res.total
        }
      })
    },
    // 确认收货
    sureOrder(e) {
      this.changeOrder(e, 3)
      this.$toast('收货成功')
    },
    // 关闭订单
    closeOrder(e) {
      Dialog.alert({
        title: '警告',
        message: '关闭订单后此订单将不再生效！',
        showCancelButton: '取消'
      }).then(() => {
        this.changeOrder(e, 4)
      }).catch(() => {
        // on cancel
      });
    },
    // 修改订单状态
    changeOrder(a, b) {
      let params = {
        url: 'order/status',
        data: {
          id: a,
          status: b
        }
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          this.getOrderList()
        }
        this.$toast(res.msg)
      })
    },

    reminderOrder() {
      this.$toast("已提醒卖家发货, 请耐心等待哦~");
    },

    handleTabClick(index) {
      this.$router.replace({ name: "user-order-ele-list", params: { active: index } })
      this.search.cond.status = this.$route.params.active
      this.search.page = 1
      this.getOrderList()
    },
    toOrderDetail(i) {
      this.$router.push({ path: '/user/refund/list/', query: { id: i } })
    },
  },
  components: {
    [Tab.name]: Tab,
    [Tabs.name]: Tabs,
    [Panel.name]: Panel,
    [Card.name]: Card,
    [IsEmpty.name]: IsEmpty,
  }
}

</script>

<style lang="scss" scoped>
.order_list {
  padding-bottom: 0;
  height: 100%;
  box-sizing: border-box;
  overflow-x: hidden;
  overflow-y: scroll;
  &--footer_btn {
    text-align: right;
  }
  &--panel {
    margin-bottom: 10px;
  }

  &--van-card {
    background-color: #fafafa;
  }

  &--total {
    text-align: right;
    padding: 10px;
  }
}
</style>
