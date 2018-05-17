<template>
  <div>
    <van-tabs :active="active">
      <van-tab v-for="(item,index) in titles" :key="index" :title="item" @chick="choose">
        <div v-for="item in pushList" :key="item.id" v-if="item.status == index">
          <van-card :title="item.name" :desc="item.detail" num="2" :price="item.price/100" :thumb="item.pic">
            <div slot="footer">
              <van-button size="mini" v-if="item.status==1" @click="pushshow(item.id,0)">上架</van-button>
              <van-button size="mini" v-if="item.status==0" @click="pushshow(item.id,1)">下架</van-button>
              <van-button size="mini" @click="editPush(item.id)">编辑</van-button>
              <van-button size="mini" type="danger" @click="delPush(item.id)">删除</van-button>
            </div>
          </van-card>
        </div>
      </van-tab>
    </van-tabs>
    <is-empty v-model="!pushList.length">您还未发布任何资料哦~</is-empty>
  </div>
</template>

<script>
import { Toast } from 'vant';
const api = new GLOBAL.api()
import isEmpty from "@/vue/components/is-empty/";
export default {
  data() {
    return {
      pushList: [],
      active: 0,
      titles: ['已上架', '已下架'],
    }
  },
  created() {
    this.getmyPush()
  },
  methods: {
    // 获取自己发布的信息
    getmyPush() {
      let params = {
        url: '/product/list',
        data: {
          limit: 8,
          page: 1
        }
      }
      api.post(params).then(res => {
        if (res.code === 0) {
          this.pushList = res.data
        } else {
          Toast({ position: 'top', message: res.msg })
        }
      }).catch()
    },
    // 上下架
    pushshow(a, b) {
      let params = {
        url: '/product/modify',
        data: {
          id: a,
          status: b
        }
      }
      api.post(params).then(res => {
        if (res.code === 0) {
          this.getmyPush()
        }
        Toast({ position: 'top', message: res.msg })
      }).catch()
    },
    //前往商品详情页面(暂时未用)
    toDetail(e) {
      this.$router.push('/items/detail/' + e)
    },
    delPush(e) {
      let params = {
        url: '/product/delete',
        data: {
          id: e,
        }
      }
      api.post(params).then(res => {
        if (res.code === 0) {
          this.getmyPush()
        }
        Toast({ position: 'top', message: res.msg })
      }).catch()
    },
    editPush(e) {
      this.$router.push({ path: '/user/autonym/edit', query: { id: e } })
    },
    choose(e) {
      console.log(e)
    }
  },
  components: {
    [isEmpty.name]: isEmpty,
  },
}
</script>
<style scoped lang="scss">
.van-card {
  margin-top: 10px;
}
</style>
