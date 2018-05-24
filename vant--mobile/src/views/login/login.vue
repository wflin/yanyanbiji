<template>
	<div class="login">
		<login-header />
		<login-request />
	</div>
</template>

<script>
	import loginHeader from './login-header';
	import loginRequest from './login-request';
	
	export default {
		
		components: {
			[loginHeader.name]: loginHeader,
			[loginRequest.name]: loginRequest,
		}
	}
</script>


<style lang="scss" scoped>
	.login{
		position: relative;
		background-color: #fff;
	}
	
</style>