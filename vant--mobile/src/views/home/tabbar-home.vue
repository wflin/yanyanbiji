<template>
  <div class="tab_home" style="height: 100%; overflow: scroll;">
    <header>
      <div class="header_box">
        <form action="#">
          <van-icon name="search" class="iconsearch" />
          <input type="search" placeholder="搜索相关资料" @click="toSearch">
        </form>
        <!--<a @click="login" class="login" v-if="token ==null?true:false">登录</a>-->
        <!--<van-icon name="wangwang" class="icon" v-if="token ==null?false:true" @click.native='seeMsg'/>-->
      </div>
    </header>

    <sign-board></sign-board>

  </div>
</template>

<script>

import SignBoard from "./tabbar-home-sign-board";

export default {
  created() {
    this.token = localStorage.getItem('ssid')
  },


  components: {
    [SignBoard.name]: SignBoard,
  },
  methods: {
    toSearch() {
      this.$router.push({ name: 'search' })
    },
    toDetail(e) {
      this.$router.push({ path: '/bookDetails', query: { id: e } })
    },
    login() {
      this.$router.push('/login')
    },
    // 查看消息列表
    seeMsg() {
      this.$router.push('/message')
    }
  }
}
</script>


<style lang="scss" scoped>
@import '../../assets/scss/var';
.interval_bot {
  margin-bottom: 10px;
}
header {
  width: 100%;
  position: fixed;
  left: 0;
  top: 0;
  height: 40px;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.4);
  .header_box {
    height: 40px;
    position: relative;
    .login {
      width: 50px;
      height: 40px;
      line-height: 40px;
      text-align: center;
      color: #fff;
      position: absolute;
      top: 0;
      right: 0;
      font-size: 15px;
    }
    .icon {
      width: 50px;
      height: 40px;
      line-height: 40px;
      text-align: center;
      color: #fff;
      position: absolute;
      top: 0;
      right: 0;
      font-size: 25px;
    }
    form {
      width: 100%;
      height: 40px;
      position: relative;
      padding: 0 50px 0 20px;
      input {
        width: 90%;
        height: 30px;
        border-radius: 15px;
        margin-top: 5px;
        padding-left: 40px;
        border: 1px solid #f1f1f1;
      }
      .iconsearch {
        position: absolute;
        top: 5px;
        left: 30px;
        line-height: 30px;
      }
    }
  }
}
</style>
