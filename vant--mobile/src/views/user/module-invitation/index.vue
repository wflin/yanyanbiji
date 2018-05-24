<template>
	<div class="user_invitation">
		<p class="icon"><van-icon name="coupon" class="iconfont"/></p>
	    <p>我的余额</p>
	    <h2>￥123</h2>
		<van-button type="primary" class="btn">充值</van-button>
		<van-button type="default" class="btn">提现</van-button>
	</div>
</template>

<script>
	
	export default {
	}
</script>

<style lang="scss" scoped>
.user_invitation{
  text-align:center;
  background:#fff;
  .icon{
    height:100px;
    margin-top:40px;
    .iconfont{
      font-size:100px;
      color:#f7971e;
    }
  }
  h2{
    margin-bottom:15px;
  }
  .btn{
  	width:80%;
  	margin-bottom:10px;
  }
}
</style>