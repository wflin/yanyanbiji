<template>
	<div class="payment">

		<div class="time_down payment_group">
			剩余付款时间:
			<span class="red">59分59秒</span>
		</div>

		<van-cell-group class="payment_group">
			<van-cell title="实付金额">
				<span class="red">{{totalMoney | yuan}}</span>
			</van-cell>
		</van-cell-group>

		<div class="pay_way_group">
			<div class="pay_way_title">选择支付方式</div>
			<van-radio-group v-model="payWay">
				<van-cell-group>
					<van-cell>
						<van-radio name="ali">
							<div>
								<p class="yanyan">妍</p>
								<div class="show">
									<p>余额支付</p>
									<p>Balance</p>
								</div>
							</div>
							<!-- <img src="../../../assets/images/ali_pay.png" alt="支付宝" width="82" height="29"> -->
						</van-radio>
					</van-cell>

					<!-- <van-cell>
						<van-radio name="wx">
							<img src="../../../assets/images/wx_pay.png" alt="微信支付" width="113" height="23">
						</van-radio>
					</van-cell> -->
				</van-cell-group>
			</van-radio-group>
		</div>

		<van-button class="pay_submit" @click="paySubmit" :loading="isSubmit" type="primary" bottomAction>去支付</van-button>
	</div>
</template>

<script>
import {
	Radio, RadioGroup, Toast
} from 'vant';
const api = new GLOBAL.api()

export default {
	name: "payment",

	data() {
		return {
			isSubmit: false,
			payWay: "ali",
			totalMoney: 0
		}
	},

	created() {
		this.totalMoney = Number(this.$route.query.totalMoney)
	},
	methods: {
		paySubmit() {
			let data = []
			if (this.$route.query.area == 'once') {
				let item = JSON.parse(localStorage.getItem('buyone'))
				for (let i in item) {
					data.push({ "product_id": item[i].id, "product_num": item[i].num })
				}
			} else {
				let item = JSON.parse(localStorage.getItem('actulBuy'))
				for (let i in item) {
					data.push({ "product_id": item[i].id, "product_num": item[i].num })
				}
			}
			let params = {
				url: '/order/add',
				data: {
					items: data
				}
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					// 购买成功后清空缓存
					Toast({ type: 'success', position: 'center', message: '购买成功，可前往我的订单里查询~' })
					localStorage.removeItem('buyone')
					let actulBuy = JSON.parse(localStorage.getItem('actulBuy'))
					let mycarts = JSON.parse(localStorage.getItem('mycarts'))
					for (let i in actulBuy) {
						for (let j in mycarts) {
							if (actulBuy[i].id === mycarts[j].id) {
								mycarts.splice(j, 1)
							}
						}
					}
					localStorage.setItem('mycarts', JSON.stringify(mycarts))
					localStorage.removeItem('actulBuy')
					// this.$router.push('index')
					this.$router.push({
						name: "paymentStatus",
						params: {
							status: "success"
						}
					})
				} else {
					Toast({ position: 'center', message: res.msg })
				}
			})
		}
	},

	components: {
		[Radio.name]: Radio,
		[RadioGroup.name]: RadioGroup,
	}
}

</script>

<style lang="scss" scoped>
.payment_group {
  margin-bottom: 10px;
}

.time_down {
  background-color: #fffeec;
  padding: 10px 15px;
}

.pay_submit {
  position: fixed;
  bottom: 0;
  width: 100%;
}

.pay_way_group img {
  vertical-align: middle;
}

.pay_way_title {
  padding: 15px;
  background-color: #fff;
}
.yanyan {
  width: 35px;
  font-size: 20px;
  line-height: 35px;
  background: #06aaff;
  text-align: center;
  color: #fff;
  border-radius: 6px;
  float: left;
  margin-right: 10px;
}
.show {
  float: left;
  line-height: 20px;
  p:first-child {
    font-size: 16px;
  }
  p:last-child {
    letter-spacing: 2px;
  }
}
</style>
