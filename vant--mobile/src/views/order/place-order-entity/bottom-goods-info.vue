<template>
	<div class="order-goods">
		<van-card v-for="item in goods" :key="item.id" :title="item.goods.name" :desc="item.goods.detail" :num="item.num" :price="item.goods.price/100" :thumb="item.goods.pic">
			<div slot="footer">
				生成日期 {{item.goods.create_time}}
			</div>
		</van-card>

		<van-cell-group>
			<van-field v-model="remark" placeholder="请输入备注" label="订单备注">
				<template slot="icon">
					3/50
				</template>
			</van-field>

			<van-cell title="商品金额">
				<span class="red">{{total_money | yuan}}</span>
			</van-cell>
			<van-cell title="邮费" value="¥0.00"></van-cell>
			<van-cell title="税费" value="¥0.00"></van-cell>
			<van-cell title="多件随机优惠">
				<span class="red">{{0 | yuan}}</span>
			</van-cell>
		</van-cell-group>
	</div>
</template>

<script>
import { Card } from 'vant';
export default {

	name: "bottom-goods-info",

	data() {
		return {
			remark: "",
			total_money: '',
			goods: []
		}
	},

	components: {
		[Card.name]: Card,
	},
	created() {
		if (this.$route.query.area === 'cart') {
			this.goods = JSON.parse(localStorage.getItem('actulBuy'));
		} else {
			this.goods = JSON.parse(localStorage.getItem('buyone'));
		}
	}
}
</script>
<style lang="scss" scoped>
.order-goods {
  background-color: #fff;
}
</style>
