<template>
	<div class="store_header">
		<!-- <van-nav-bar title="标题" left-text="返回" left-arrow>
  			<van-icon name="search" slot="right" />
		</van-nav-bar> -->
		<img src="../../assets/images/avatar_default.png" alt="头像" width="55" height="55">
	</div>
</template>


<script>
	export default {
		name: "login-header"
	}
</script>

<style lang="scss" scoped>
	.store_header{
		// text-align: center;
		margin:0 auto;
		padding: 30px 0;
		img{
			border-radius:30px;
			margin:0 auto;
		}
	}
</style>