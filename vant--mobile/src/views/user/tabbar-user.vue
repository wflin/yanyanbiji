<template>
	<div class="tabbar-user">
		<user-header/>
		<order-group />
		<ecoupon-group />
		<user-module />
		<van-button size="large" class="tabbar-user__quit" v-if="isLogin" @click="quit">退出当前账户</van-button>
	</div>
</template>

<script>
import { Toast } from 'vant';
import userHeader from "./tabbar-user-header";
import orderGroup from "./tabbar-user-order";
import ecouponGroup from "./tabbar-user-ecoupon";
import userModule from "./tabbar-user-module";
const api = new GLOBAL.api()
export default {

	data() {
		return {
			isLogin: false,
		}
	},

	activated() {
		this.getLoginStatus();
	},
	created() {
		let islogin = localStorage.getItem('ssid');
		if (islogin == null) {
			this.isLogin = false
		} else {
			this.isLogin = true
		}
	},
	methods: {
		quit() {
			let params = {
				url: '/user/logout',
			}
			api.get(params).then(res => {
				Toast({ position: 'top', message: res.msg })
				if (res.code === 0) {
					this.$util.removeLocalStorage('ssid')
					// window.location.href = '/index'
					this.$router.push('/index')
				}
			}).catch()
		},
		getLoginStatus() {
			this.isLogin = !!localStorage.getItem('ssid');
		}
	},

	components: {
		[userHeader.name]: userHeader,
		[orderGroup.name]: orderGroup,
		[ecouponGroup.name]: ecouponGroup,
		[userModule.name]: userModule,
	}
}

</script>


<style scoped lang="scss">
.tabbar-user {
  > div {
    margin-bottom: 10px;
  }
  &__quit {
    border: 0;
    border-radius: 0;
  }
}
</style>
