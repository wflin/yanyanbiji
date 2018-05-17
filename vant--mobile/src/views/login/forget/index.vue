<template>
	<md-field-group class="foget_view">
		<md-field v-model="resetForm.telephone" icon="mobile" placeholder="请输入手机号" />

		<md-field v-model="resetForm.code" icon="lock" placeholder="请输入短信验证码">
			<div slot="rightIcon" class="getCode red">
				<countdown v-if="counting" :time="60000" @countdownend="countdownend">
					<template slot-scope="props">{{ +props.seconds || 60 }}秒后获取</template>
				</countdown>
				<span v-else @click="getCode">获取验证码</span>
			</div>
		</md-field>
		<md-field v-model="resetForm.password" icon="lock" placeholder="请输入新密码" />

		<md-field v-model="resetForm.password2" type="password" icon="lock" placeholder="请再次输入密码" />

		<div class="foget_submit">
			<van-button size="large" type="danger" @click="submitCode">提交</van-button>
		</div>
	</md-field-group>
</template>

<script>
import field from '@/vue/components/field/';
import fieldGroup from '@/vue/components/field-group/';
import { Toast } from 'vant';
const api = new GLOBAL.api()
export default {

	data() {
		return {
			counting: false,
			resetForm: {
				telephone: "",
				code: "",
				password: '',
				password2: ''
			}
		}
	},

	methods: {
		submitCode() {
			let registe = this.resetForm
			if (registe.telephone == '' || registe.pay_password == '' || registe.code == '') {
				Toast({ position: 'top', message: '请将信息填写完整' })
			} else if (registe.password != registe.password2) {
				Toast({ position: 'top', message: '两次输入密码不一致' })
			} else if (!GLOBAL.rules.phone.test(registe.telephone)) {
				Toast({ position: 'top', message: '手机号码格式错误' })
			} else {
				let params = {
					url: 'password/forget',
					data: this.resetForm
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
			let telephone = this.resetForm.telephone
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

div.foget_view {
  background-color: #fff;
  padding-top: 30px;
}

div.foget_submit {
  padding-top: 30px;
  padding-bottom: 20px;
}

.getCode {
  @include one-border(left);
  text-align: center;
}

.time_down {
  color: $red;
}
</style>

