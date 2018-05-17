<template>
  <div class="msgList">
    <van-cell-swipe :right-width="65" v-for="(item,index) in msgList" :key="index">
      <ul>
        <li @click="contact(item.send_id)">
          <div class="left">
            <img :src="item.send_user.pic" alt="" v-if="item.send_user.pic !=''">
            <img src="static/img/7.jpg" alt="" v-else>
            <div class="msgnum" v-if="item.status == 0"></div>
          </div>
          <div class="right">
            <h4>{{item.send_user.username}}</h4>
            <p v-if="item.status == 0">点击查看新消息</p>
            <p v-if="item.status == 1">暂无新消息</p>
          </div>
        </li>
      </ul>
      <div slot="right" class="rigthDetail" @click="deleteDetail(index)">删除</div>
    </van-cell-swipe>
    <is-empty v-model="!msgList.length">暂无消息</is-empty>
  </div>
</template>

<script>
const api = new GLOBAL.api()
import IsEmpty from "@/vue/components/is-empty/";
export default {
  data() {
    return {
      search: {
        page: 1,
        limit: 10
      },
      msgList: []
    }
  },
  created() {
    this.getList()
  },
  methods: {
    // 获取消息列表
    getList() {
      let params = {
        url: 'chat/status',
        data: this.search
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          this.msgList = res.data
        }
      })
    },
    deleteDetail(e) {
      console.log(e)
    },
    // 跳转到聊天页面
    contact(e) {
      this.$router.push({ path: "/message/eachMsg", query: { sellid: e } })
    }
  },
  components: {
    [IsEmpty.name]: IsEmpty,
  }
}
</script>


<style lang="scss" scoped>
.msgList {
  background: #fff;
  ul {
    li {
      padding: 5px;
      border: 1px solid #f1f1f1;
      display: flex;
      flex: 1;
      .left {
        position: relative;
        img {
          display: block;
          width: 48px;
          height: 48px;
        }
        .msgnum {
          width: 12px;
          height: 12px;
          content: '';
          position: absolute;
          top: -3px;
          left: 40px;
          background: #f44;
          border-radius: 9px;
          font-size: 10px;
          transform: scale(0.8);
          box-sizing: border-box;
        }
      }
      .right {
        margin-left: 20px;
        h4 {
          margin: 0;
          color: #38f;
        }
        p {
          padding: 5px 0;
          font-size: 12px;
        }
      }
    }
  }
  .rigthDetail {
    background: #f44;
    width: 65px;
    height: 60px;
    line-height: 60px;
    color: #fff;
    text-align: center;
  }
}
</style>
