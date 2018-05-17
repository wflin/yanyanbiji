<template>
	<div>
		<md-field-group>
			<md-field v-model="loginform.telephone" icon="username" right-icon="clear-full" placeholder="请输入电话号码" @right-click="clearText" />

			<md-field v-model="loginform.password" icon="lock" placeholder="请输入密码" :type="visiblePass ? 'text' : 'password'" :right-icon="visiblePass ? 'eye-open' : 'eye-close'" @right-click="visiblePass = !visiblePass" />

			<div class="clearfix">
				<div class="float-r">
					<router-link to="/login/forget">忘记密码</router-link>
				</div>
			</div>

			<van-button size="large" type="danger" :loading="isLogining" @click="loginSubmit">登录</van-button>
			<van-button size="large" type="primary" :loading="isLogining" @click="webChatLogin">微信登录</van-button>
		</md-field-group>

		<div class="register clearfix">
			<div class="float-l connect">
				<span>联系客服</span>
			</div>
			<div class="float-r">
				<router-link to="/login/registerSubmit">免费注册</router-link>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
const api = new GLOBAL.api()
import field from '@/vue/components/field/';
import fieldGroup from '@/vue/components/field-group/';
import { Toast } from 'vant';

export default {
	name: "login-request",
	data() {
		return {
			loginform: {
				telephone: '',
				password: ''
			},
			visiblePass: false,
			isLogining: false,
		}
	},
	methods: {
		clearText() {
			this.account = "";
		},
		webChatLogin(){
			let params = {
				url: 'https://open.weixin.qq.com/connect/oauth2/authorize?'+
				'appid=wx9d97a14a87a82e17'+
				'&redirect_uri=http%3A%2F%2Fwww.yanyanbiji.com&'+
				'response_type=code&scope=snsapi_base&state=STATE&wechat_redirect'
			}
            api.get(params).then((res) => {
				console.log('ddd')
			})
		},
		loginSubmit() {
			let url = GLOBAL.config.baseURL + 'user/login',
				telephone = this.loginform.telephone,
				password = this.loginform.password
			// 登录前判断用户名、密码是否为空
			if (!telephone || !password) {
				Toast({ position: 'top', message: '请将信息填写完整' })
				return
			} else if (!GLOBAL.rules.phone.test(telephone)) {
				Toast({ position: 'top', message: '手机号码格式不正确！' })
				return
			}
			let instance = axios.create({
				baseURL: '',
				headers: {}
			})
			let params = {
				telephone: telephone,
				password: password,
			}
			instance.post(url, params).then(res => {
				if (res.data.code === 0) {
					let token = res.headers.authorization
					localStorage.setItem('ssid', token)
					this.$router.push('/index')
				} else {
					this.$toast(res.data.msg)
				}
			})
		},
	},
	components: {
		[field.name]: field,
		[fieldGroup.name]: fieldGroup,
	}
}

</script>

<style lang="scss" scoped>
@import '../../assets/scss/var';
@import '../../assets/scss/mixin';
.register {
  padding-top: 40px;
  color: $font-color-gray;
  a {
    color: $font-color-gray;
  }
  > div {
    width: 50%;
    box-sizing: border-box;
    padding: 0 20px;
  }
  .connect {
    @include one-border(right);
    text-align: right;
  }
}
</style>
