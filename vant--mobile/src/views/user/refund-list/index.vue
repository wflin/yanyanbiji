<template>
	<div class="order_list">
		<div class="receive" v-if="items.buyer">
			<div class="one">
				<p>收货人：{{items.buyer.username}}
					<span>{{items.buyer.telephone}}</span>
				</p>
			</div>
			<div>收货地址:{{items.buyer.school}}{{items.buyer.address}}</div>
		</div>
		<van-panel class="order_list--panel" :title="'卖家: ' + items.seller.username" :status="items.seller.telephone" v-if="items.product && items.order && items.seller">
			<div>
				<van-card class="order_list--van-card" :title="items.product.name" :desc="items.product.detail" :num="items.order.product_num" :price="(items.order.product_amount / 100).toFixed(2)" :thumb="items.product.pic" @click.native="toDetail(items.product.id)" />
				<div class="order_list--total">
					<p>商品总价
						<span>{{items.order.product_amount*items.order.product_num | yuan}}</span>
					</p>
					<p>运费
						<span>{{items.order.logistics_amount | yuan}}</span>
					</p>
				</div>
			</div>
			<div class="money">
				<p>实付款：
					<span>{{items.order.product_amount*items.order.product_num | yuan}}</span>
				</p>
			</div>
		</van-panel>
		<div v-if="items.order" class="number">
			<p>订单编号
				<span>{{items.order.order_num}}</span>
			</p>
			<p>创建时间
				<span>{{items.order.create_time}}</span>
			</p>
		</div>
		<van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />

		<is-empty v-model="!items.product">服务器开小差了，请尝试刷新</is-empty>

	</div>
</template>

<script>
import { Tab, Tabs, Panel, Card } from 'vant';
const api = new GLOBAL.api()
import IsEmpty from "@/vue/components/is-empty/";

export default {
	name: 'order-list',


	data() {
		const shop_id = this.$util.getLocationParam("shop_id")
		return {
			shop_id,
			activeIndex: 0,
			items: {},
			isLoading: false
		}
	},


	created() {
		this.getOrderDetail();
	},

	methods: {
		getOrderDetail() {
			this.isLoading = true
			let params = {
				url: 'order/detail',
				data: {
					id: this.$route.query.id
				}
			}
			api.post(params).then((res) => {
				if (res.code !== 0) {
					this.$toast(res.msg)
				} else {
					this.isLoading = false
					this.items = res.data
				}
			})
		},
		// 前往资料详情界面
		toDetail(e) {
			this.$router.push('/items/detail/' + e)
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
  .receive {
    padding: 10px 15px;
    background: #fff;
    .one {
      margin-bottom: 10px;
      span {
        float: right;
        color: steelblue;
      }
    }
  }
}
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
    margin: 10px 0;
  }

  &--van-card {
    background-color: #fafafa;
  }

  &--total {
    padding: 10px 15px;
    font-size: 12px;
    color: #999;
    span {
      float: right;
    }
  }
  .money {
    border-top: 1px solid #f1f1f1;
    padding: 10px 15px;
    span {
      float: right;
      color: red;
    }
  }
  .number {
    background: #fff;
    font-size: 12px;
    padding: 10px 15px;
    p:first-child {
      margin-bottom: 10px;
    }
    span {
      float: right;
    }
  }
}
</style>
