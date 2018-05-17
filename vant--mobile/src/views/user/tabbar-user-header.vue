<template>
	<div class="user_header" :style="{backgroundImage: `url(${background_image})`}">
		<van-icon name="set" class="user_set" @click="toSetting" />
		<div class="user_avatar">
			<img :src="avatar" @click="toLogin" alt="头像" width="55" height="55" v-if="!userinfo.pic">
			<img :src="userinfo.pic" @click="toLogin" alt="头像" width="55" height="55" v-if="userinfo.pic">
		</div>
		<div>{{userinfo.username}}</div>
	</div>
</template>

<script>
import avatar_default from "../../assets/images/avatar_default.png";
import bg_default from "../../assets/images/user_head_bg.png";
const api = new GLOBAL.api()
export default {
	name: "user-header",

	props: {
		isLogin: {
			type: Boolean,
			default: false
		}
	},

	data() {
		return {
			userinfo: {
				"username": '',
				"school": '',
				"address": '',
				"pic": ''
			},
			avatar: avatar_default,
			background_image: bg_default
		}
	},

	created() {
		this.getSelfMsg()
	},
	methods: {
		// 获取个人信息
		getSelfMsg() {
			let params = {
				url: '/user/info',
				data: {}
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					let data = res.data
					this.userinfo = {
						"username": data.username,
						"school": data.school,
						"address": data.address,
						"pic": data.pic
					}
				}
			})
		},
		toSetting() {
			this.$router.push({ name: "user-information" })
		},
		toLogin() {
			this.$router.push({ name: "user-information" })
		}
	}
}

</script>

<style lang="scss" scoped>
.user_header {
  position: relative;
  background-repeat: no-repeat;
  background-size: cover;
  height: 130px;
  box-sizing: border-box;
  text-align: center;
  color: #fff;
  padding-top: 30px;
}

i.user_set {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
}
.user_avatar {
  margin-bottom: 10px;
  img {
    border: 0;
    border-radius: 50%;
    margin: auto;
  }
}
</style>
