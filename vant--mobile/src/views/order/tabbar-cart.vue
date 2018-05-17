<template>
	<div class="tab-cart">
		<div class="editor_head" v-show="goods.length">
			<van-icon :name="isEditor ? 'success' : 'editor'" />
			<span @click="isEditor = !isEditor">{{isEditor ? '完成' : '编辑'}}</span>
		</div>

		<van-checkbox-group class="card-goods" v-model="checkedGoods">
			<div v-for="(item, i) in goods" class="card-goods__item">
				<van-checkbox :key="item.id" :name="item.id">
				</van-checkbox>

				<van-card :desc="item.goods.name" :num="item.num" :thumb="item.goods.pic">
					<div class="van-card__row" slot="title">
						<div class="van-card__title">
							<van-tag plain type="danger">{{item.goods.category}}</van-tag>{{item.title}}</div>
						<div class="van-card__price">{{item.goods.price | yuan}}</div>
					</div>
					<div slot="footer" v-if="isEditor">
						<van-stepper v-model="item.num" disableInput/>
					</div>
					<div slot="footer" v-else>生成日期{{item.goods.create_time}}</div>
				</van-card>

				<div class="cart_delete" v-if="isEditor" @click="deleteCart(i)">删除</div>
			</div>
		</van-checkbox-group>

		<div class="clear_invalid" v-if="goods.length" @click="clearInvalid">
			<van-icon name="lajitong" /> 清除失效商品
		</div>

		<is-empty v-model="!goods.length">您的购物车空空如也~</is-empty>

		<van-submit-bar style="bottom: 50px" :price="totalPrice" :disabled="!checkedGoods.length" :buttonText="submitBarText" :loading="isSubmit" label="总计" @submit="cartSubmit">
			<van-checkbox v-model="checkedAll" @change="setCheckAll" style="padding: 0 10px;">全选</van-checkbox>
		</van-submit-bar>

	</div>
</template>

<script>
import {
	Checkbox, CheckboxGroup, Card, SubmitBar, Stepper, Toast
} from 'vant';

import isEmpty from "@/vue/components/is-empty/";

export default {
	data() {
		return {
			isEditor: false,
			checkedAll: false,
			isSubmit: false,
			checkedGoods: [],
			goods: [],
		};
	},

	activated() {
		this.checkedAll = false;
		this.isEditor = false;
		this.isSubmit = false;
	},

	computed: {
		submitBarText() {
			const count = this.checkedGoods.length;
			return this.isEditor ? "删除" : '结算' + (count ? `(${count})` : '');
		},
		totalPrice() {
			return this.goods.reduce((total, item) => total + (this.checkedGoods.indexOf(item.id) !== -1 ? item.goods.price * item.num : 0), 0);
		},
	},
	created() {
		let goods = JSON.parse(localStorage.getItem('mycarts'));
		if (goods !== null) {
			this.goods = JSON.parse(localStorage.getItem('mycarts'));
		}
	},
	methods: {
		cartSubmit() {
			if (this.isEditor) {
				this.$dialog.confirm({ message: "确定删除所选商品吗?", cancelButtonText: "再想想" }).then(() => {
					this.goods = this.goods.filter(goods => (this.checkedGoods.indexOf(goods.id) == -1));
					this.checkedGoods = [];
					this.checkedAll = false;
					this.isEditor = !this.goods.length;
				})
			} else {
				console.log(this.checkedGoods)
				console.log(this.goods)
				let actulBuy = []
				for (let i in this.goods) {
					for (let n in this.checkedGoods) {
						if (this.goods[i].id == this.checkedGoods[n]) {
							actulBuy.push(this.goods[i])
							localStorage.setItem('actulBuy', JSON.stringify(actulBuy))
						}
					}
				}
				this.isSubmit = true;
				this.$router.push({ name: "placeOrderEntity", query: { "totalMoney": this.totalPrice, 'area': 'cart', 'choose': this.checkedGoods } })
			}
		},
		formatPrice(price) {
			return (price / 100).toFixed(2);
		},
		setCheckAll(val) {
			this.checkedGoods = val ? this.goods.filter(goods => !goods.status).map(goods => goods.id) : [];
		},
		deleteCart(i) {
			this.$dialog.confirm({ message: "确定删除所选商品吗", cancelButtonText: "再想想" }).then(() => {
				let goodsId = this.goods.splice(i, 1)[0].id;
				localStorage.setItem('mycarts', JSON.stringify(this.goods))
				this.$nextTick(() => {
					this.deleteNext(goodsId)
				})
			})
		},
		deleteNext(goodsId) {
			this.isEditor = !!this.goods.length;
			this.checkedGoods.forEach((goods, i) => {
				if (goods.id == goodsId) {
					this.checkedGoods.splice(i, 1);
					return false;
				}
			})
		},
		clearInvalid() {
			Toast({ position: 'center', message: '暂无无效商品可以清除哦~' })
			// this.$dialog.confirm({message: "确定清除所有失效商品吗?", cancelButtonText: "再想想"}).then(() => {
			// 	this.goods = this.goods.filter(goods => goods.status)
			// })
		}
	},

	components: {
		[Card.name]: Card,
		[Stepper.name]: Stepper,
		[isEmpty.name]: isEmpty,
		[Checkbox.name]: Checkbox,
		[SubmitBar.name]: SubmitBar,
		[CheckboxGroup.name]: CheckboxGroup,
	},
}

</script>


<style lang="scss" scoped>
@import '../../assets/scss/var';
@import '../../assets/scss/mixin';

.tab-cart {
  padding-bottom: 50px;
  box-sizing: border-box;
}

.editor_head {
  @include one-border;
  text-align: right;
  padding: 10px;
  font-size: $font-size-normal;
  background-color: #fff;
}

.card-goods {
  background-color: $bg-color;
  .card-goods__item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    background-color: #fff;
  }
  .cart_delete {
    line-height: 100px;
    padding: 0 10px;
    color: #fff;
    background-color: $red;
  }
  .card-goods__footer {
    font-size: $font-size-normal;
    color: $font-color-gray;
  }
}

.clear_invalid {
  width: 120px;
  color: $font-color-gray;
  border: 1px solid $font-color-gray;
  margin: 0 auto;
  text-align: center;
  padding: 5px 3px;
  margin-top: 20px;
  border-radius: 3px;
}
</style>
