<template>
	<div class="item_detail">
		<img v-lazy="goods.product.pic" v-if="goods" />
		<van-cell-group class="item_cell_group" v-if="goods">
			<van-cell class="item_info">
				<div>
					<span class="item_price">{{ goods.product.price | yuan }}</span>
					<span class="item_market_price">{{goods.product.price | yuan}}</span>
				</div>
				<div class="item-title">
					<van-tag plain type="danger">{{goods.product.category}}</van-tag>
					{{ goods.product.name }}
				</div>
				<div class="item_intro">资料类型：{{goods.product.type ==0?'纸质资料':'下载资料'}}</div>
				<div class="item_dispatch">运费:{{goods.product.logistics_price}}&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp发布时间: {{goods.product.create_time}}</div>
			</van-cell>
		</van-cell-group>

		<div class="item_desc" v-if="goods">
			<div class="item_desc_title">商品详情</div>
			<div class="item_desc_wrap">{{goods.product.detail}}</div>
		</div>
		<div class="item_desc" v-if="goods">
			<div class="item_desc_title1">宝贝评价({{goods.comment_num}})</div>
		</div>
		<van-goods-action>
			<van-goods-action-mini-btn @click="doContact(goods)" icon="chat" iconClass="red afterTag" />
			<van-goods-action-mini-btn @click="toCart" icon="cart" />
			<van-goods-action-mini-btn @click="addCollect" icon="shoucang" />
			<van-goods-action-big-btn @click="addCart" text="加入购物车" />
			<van-goods-action-big-btn primary @click="doBuyNow" text="立即购买" />
		</van-goods-action>

	</div>
</template>

<script>
import {
	GoodsAction,
	GoodsActionBigBtn,
	GoodsActionMiniBtn,
	Toast
} from 'vant';

const api = new GLOBAL.api()
export default {

	data() {
		return {
			url: GLOBAL.config.imgUrl,
			cartInfo: "",
			selectSku: {
				selectedNum: 1,
				selectedSkuComb: {}
			},
			addressVal: {
				id: null,
				area_name: "",
				district: "",
				city: "",
				province: ""
			},
			goods: null,
			myCarts: [],
			token: ''
		}
	},

	created() {
		let ssid = localStorage.getItem('ssid')
		if (ssid !== null) {
			this.token = 1      // 1表示已登录
		} else {
			this.token = 0
		}
		this.getproDetail();
		let myCarts = JSON.parse(localStorage.getItem('mycarts'));
		if (myCarts !== null) {
			this.myCarts = JSON.parse(localStorage.getItem('mycarts'));
			for (let i in myCarts) {
				this.cartInfo += Number(myCarts[i].num)
			}
		}
	},

	methods: {
		// 获取商品详情
		getproDetail() {
			let params = {
				url: 'product/detail',
				data: {
					id: this.$route.params.itemId
				}
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					this.goods = res.data
				}
			})
		},

		doBuyNow() {
			if (this.token !== 1) {
				Toast({ position: 'center', message: '请先登录~' })
				return false
			}
			let buyone = []
			buyone.push({ 'goods': this.goods.product, 'num': 1, id: this.goods.product.id })
			localStorage.setItem('buyone', JSON.stringify(buyone))
			this.$router.push({ name: 'placeOrderEntity', query: { "totalMoney": this.goods.product.price, 'area': 'once' } })
		},
		addCart() {
			if (this.token !== 1) {
				Toast({ position: 'center', message: '请先登录~' })
				return false
			}
			let goods = this.goods
			let myCarts = this.myCarts
			if (myCarts.length == 0) {
				myCarts.push({ 'goods': goods.product, 'num': 1, id: goods.product.id })
			} else {
				for (let i in myCarts) {
					if (myCarts[i].id == goods.product.id) {
						myCarts[i].num++
					} else {
						myCarts.push({ 'goods': goods.product, 'num': 1, id: goods.product.id })
					}
				}
			}
			localStorage.setItem('mycarts', JSON.stringify(myCarts))
			Toast({ type: 'success', position: 'center', message: '添加成功，在购物车等亲~' })
		},
		doContact(e) {
			// this.showContact = true;
			this.$router.push({ path: '/message/eachMsg', query: { sellid: e.user.id, productid: e.product.id } })
		},
		toCart() {
			this.$router.push({
				name: "cart"
			})
		},
		addCollect() {
			this.$toast({
				message: "已添加至我的收藏",
				duration: 1500
			});
		},
	},

	components: {
		[GoodsAction.name]: GoodsAction,
		[GoodsActionBigBtn.name]: GoodsActionBigBtn,
		[GoodsActionMiniBtn.name]: GoodsActionMiniBtn,
	},
}

</script>

<style lang="scss" scoped>
@import '../../../assets/scss/var';
@import '../../../assets/scss/mixin';

.item_detail {
  img {
    width: 100%;
    height: auto;
    max-height: 240px;
  }
}

.item_cell_group {
  margin-bottom: 15px;
}

.item_price {
  font-size: 20px;
  color: $red;
  margin-right: 10px;
}

.item_market_price {
  color: $font-color-gray;
  text-decoration: line-through;
  font-size: $font-size-small;
}

.item-title {
  line-height: 1.4;
}

.item_dispatch {
  font-size: $font-size-small;
  color: $font-color-gray;
}

.item_intro {
  line-height: 18px;
  margin: 5px 0;
  font-size: $font-size-small;
  color: $font-color-gray;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
}

.item_desc {
  background-color: #fff;
  p {
    padding: 0 10px;
  }
  img {
    max-width: 100%;
  }
}

.item_desc_title {
  @include one-border;
  padding: 10px;
  text-align: left;
}
.item_desc_title1 {
  @include one-border;
  padding: 10px;
  text-align: left;
  margin-top: 10px;
}
.item_desc_wrap {
  padding: 10px;
  min-height: 100px;
}
</style>
