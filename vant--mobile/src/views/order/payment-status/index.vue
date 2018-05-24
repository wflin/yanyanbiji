<template>
	<div class="payment_status">
		<div class="status_top">
			<van-icon :name="statusIcon" :class="statusClass" />
			<div>{{statusText}}</div>
		</div>

		<div class="status_text" v-if="isSuccess">
			<span class="red">{{count}}秒</span>后返回到首页, 您也可以到个人中心里查看订单详情</div>
		<div class="status_text" v-else>系统繁忙, 支付遇到问题, 请您稍后再试!</div>

		<div class="status_goLink">
			<router-link class="red" :to="{name: 'home'}">返回首页
				<van-icon name="arrow" />
			</router-link>
		</div>
	</div>
</template>

<script>
export default {
	name: "payment-status",

	props: {
		status: String
	},

	data() {
		return {
			isSuccess: true,
			count: '',
			time: null
		}
	},

	computed: {
		statusText() {
			return this.isSuccess ? '支付成功' : '支付失败'
		},
		statusIcon() {
			return this.isSuccess ? 'checked' : 'fail'
		},
		statusClass() {
			return this.isSuccess ? 'success_icon' : 'fail_icon'
		},
	},

	activated() {
		this.isSuccess = this.status === "success";
	},
	created() {
		this.getCode()
	},
	// 销毁倒计时
	destroyed() {
		window.clearInterval(this.timer)
	},
	methods: {
		// 倒计时
		getCode() {
			const TIME_COUNT = 5;
			if (!this.timer) {
				this.count = TIME_COUNT;
				this.timer = setInterval(() => {
					if (this.count > 0 && this.count <= TIME_COUNT) {
						this.count--;
					} else {
						clearInterval(this.timer);
						this.timer = null;
						this.$router.push('/index')
					}
				}, 1000)
			}
		}
	}

}

</script>


<style lang="scss" scopd>
@import '../../../assets/scss/var';

.payment_status {
  padding-top: 30px;
  box-sizing: border-box;
  background-color: #fff;
  text-align: center;
}

.status_top {
  margin-bottom: 15px;
  i {
    margin-bottom: 5px;
  }
  > div {
    font-size: 18px;
  }
}

.status_text {
  color: $font-color-gray;
  margin-bottom: 50px;
}

.status_icon {
  font-size: 80px;
}

i.success_icon {
  @extend .status_icon;
  color: #06bf04;
}

i.fail_icon {
  @extend .status_icon;
  color: #f44;
}
</style>
