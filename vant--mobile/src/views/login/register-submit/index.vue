<template>
	<md-field-group class="register_submit">
		<h2>输入手机号,快速注册</h2>
		<md-field v-model="registe.telephone" icon="mobile" placeholder="请输入手机号" />
		<md-field v-model="registe.code" icon="mobile" placeholder="请输入验证码">
			<div slot="rightIcon" class="getCode red">
				<countdown v-if="counting" :time="60000" @countdownend="countdownend">
					<template slot-scope="props">{{ +props.seconds || 60 }}秒后获取</template>
				</countdown>
				<span v-else @click="getCode">获取验证码</span>
			</div>
		</md-field>
		<md-field v-model="registe.password" icon="lock" placeholder="请输入密码" />
		<md-field v-model="registe.repassword" icon="lock" placeholder="请再次确认密码" />

		<div class="register_submit_btn">
			<van-button type="danger" size="large" @click="registerSubmit">确定</van-button>
		</div>
		<div class="register_footer">
			已有账号?
			<router-link to="/login" class="red">登录</router-link>
		</div>
	</md-field-group>

</template>

<script>
import field from '@/vue/components/field/';
import fieldGroup from '@/vue/components/field-group/';
const api = new GLOBAL.api()
import { Toast } from 'vant';
export default {
	data() {
		return {
			counting: false,
			registe: {
				'telephone': '',
				'repassword': '',
				'password': '',
				'code': ''
			},
		}
	},

	methods: {
		registerSubmit() {
			let registe = this.registe
			if (registe.telephone == '' || registe.password == '' || registe.code == '') {
				Toast({ position: 'top', message: '请将信息填写完整' })
			} else if (registe.password != registe.repassword) {
				Toast({ position: 'top', message: '两次输入密码不一致' })
			} else if (!GLOBAL.rules.phone.test(this.registe.telephone)) {
				Toast({ position: 'top', message: '手机号码格式错误' })
			} else if (!GLOBAL.rules.code.test(this.registe.code)) {
				Toast({ position: 'top', message: '验证码格式错误' })
			} else {
				let params = {
					url: 'user/register',
					data: {
						telephone: this.registe.telephone,
						code: this.registe.code,
						password: this.registe.password,
					}
				}
				api.post(params).then((res) => {
					Toast({ position: 'top', message: res.msg })
					if (res.code === 0) {
						this.$router.push('/login')
					}
				})
			}
		},

		getCode() {
			let telephone = this.registe.telephone
			if (!telephone) {
				Toast({ position: 'top', message: '请填写手机号码' })
				return
			} else if (!GLOBAL.rules.phone.test(telephone)) {
				Toast({ position: 'top', message: '手机号码格式不正确！' })
				return
			}
			let params = {
				url: 'user/code',
				params: {
					telephone: telephone
				}
			}
			api.get(params).then((res) => {
				if (res.code === 0) {
					this.counting = true;
				} else {
					this.$toast(res.msg)
				}
			})
		},
		countdownend() {
			this.counting = false;
		}
	},

	components: {
		[field.name]: field,
		[fieldGroup.name]: fieldGroup,
	}
}
</script>


<style lang="scss" scoped>
@import '../../../assets/scss/var';
@import '../../../assets/scss/mixin';

.register_submit {
  padding-top: 40px;
  background-color: #fff;
}

.register_submit_btn {
  padding-top: 30px;
}
.register_footer {
  text-align: right;
  color: $font-color-gray;
}
.getCode {
  @include one-border(left);
  text-align: center;
}
h2 {
  text-align: center;
  margin-bottom: 20px;
}
.time_down {
  color: $red;
}
</style>