<template>
	<div class="item_list" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="100">

		<form action="/search" class="fixedTop">
			<van-search placeholder="请输入商品名称" v-model="searchVal" @search="getProduct(1)" showAction>
				<div slot="action" @click="onSearch">取消</div>
			</van-search>
		</form>

		<div v-for="item in productList" :key="item.product.id" @click="seeDetail(item.product.id)" class="cardList" v-show="productList.length">
			<van-card :title="item.product.name" :desc="item.product.detail" :price="item.product.price/100" :thumb="item.product.pic">
				<div slot="footer">
					<van-tag mark type="primary">{{item.product.category}}</van-tag>
					<van-tag plain>运费:{{item.product.logistics_price/100}}元</van-tag>
				</div>
			</van-card>
		</div>

		<van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />

		<is-empty v-model="!productList.length">抱歉,没有找到符合条件商品</is-empty>

		<!-- <van-popup
			v-model="noMore"
			position="bottom"
			:overlay="false"
		>没有更多了</van-popup> -->

		<!-- <transition name="fade">
			<van-icon name="arrowupcircle" class="backTop" @click.native="backTop" v-show="showArrow"></van-icon>
		</transition> -->
	</div>
</template>

<script>
const api = new GLOBAL.api()
import IsEmpty from "@/vue/components/is-empty/";
import { Search, Loading, } from 'vant';

export default {
	name: "Item-list",
	props: {
		keyword: {
			type: String,
			default: ""
		},
	},

	data() {
		return {
			searchVal: "",
			showArrow: false,
			productList: [],
			productTotal: 0,
			searchProduct: {
				"cond": {
					"key_word": "",
					"type": 0,
					"category": ""
				},
				"limit": 8,
				"page": 1
			},
			isLoading: false
		}
	},

	activated() {
		this.searchVal = this.keyword;
		this.getProduct();
	},

	created() {
		this.searchVal = this.$route.keyword
	},

	methods: {
		// 上拉加载
		nextPage() {
			this.searchProduct.page += 1;
			this.getProduct()
		},
		loadMore() {
			let i = this.searchProduct.page * this.searchProduct.limit
			if (i < this.productTotal) {
				this.nextPage()
			}
		},
		getProduct() {
			this.isLoading = true
			this.searchProduct.cond.key_word = this.searchVal
			let params = {
				url: 'product/all',
				data: this.searchProduct
			}
			api.post(params).then(res => {
				if (res.code === 0) {
					if (this.searchProduct.page > 1) {
						for (let i in res.data) {
							this.productList.push(res.data[i])
						}
					} else {
						this.productList = res.data
					}
					this.productTotal = res.total
					this.isLoading = false
				}
			}).catch(() => {
				this.isLoading = false
			})
		},
		itemClick(i) {
			this.$router.push({ name: "detail", params: { itemId: i } });
		},
		onSearch() {
			this.searchVal = ''
			this.$router.replace({ path: "/items/search/result", params: { keyword: this.searchVal } })
			this.getProduct(1)
		},
		seeDetail(e) {
			this.$router.push('/items/detail/' + e)
		}
	},

	components: {
		[Search.name]: Search,
		[Loading.name]: Loading,
		[IsEmpty.name]: IsEmpty,
	}
}
</script>

<style lang="scss" scoped>
@import '../../../assets/scss/var';

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s;
}

.item_list {
  box-sizing: border-box;
}
// .fixedTop{
// 	position: fixed;
// 	width: 100%;
// 	top: 0;
// 	z-index: 999;
// }
.cardList {
  margin-bottom: 10px;
}
.items_loading {
  margin: 0 auto;
}
.backTop {
  position: fixed;
  right: 20px;
  bottom: 20px;
  font-size: 24px;
}
</style>
