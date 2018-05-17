<template>
	<div class="user_module">
		<van-cell-group>
      <van-cell icon="kefu" title="我的发布" to="/user/server" isLink />
			<van-cell icon="shoucang" title="我的收藏" to="/user/collect" isLink />
			<van-cell icon="team" title="我的提问" to="/user/team" isLink />
			<van-cell icon="gold-bean" title="我的钱包" isLink  to="/user/invitation" />
			<van-cell icon="dingwei" title="收货地址" to="/user/address" isLink />
			<van-cell icon="lock" title="密码设置" to="/user/information/setPassword" isLink />
		</van-cell-group>
	</div>
</template>

<script>
	export default {
		name: "user-module",
	}
</script>


<style scoped lang="scss">
	.user_module{
		background-color: #fff;
	}

</style>
