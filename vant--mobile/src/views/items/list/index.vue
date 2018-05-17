<template>
	<div class="item_list" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="100">

		<form action="/search">
			<van-search placeholder="请输入商品名称" v-model="searchVal" @search="getList(1)" showAction>
				<div slot="action" @click="cancel">取消</div>
			</van-search>
		</form>

		<van-tabs @click="handleTabClick" @disabled="handleTabClick">
			<van-tab v-for="tab in tabsItem" :title="tab.name" :key="tab.type" :disabled="tab.sort === false">
			</van-tab>
		</van-tabs>

		<van-popup class="filterItem" v-model="filterItemShow" position="right">
			<ul>
				<li v-for="(li, i) in filterItem" :key="i" :class="{filter_active: li.isActive}">
					{{li.name}}
					<van-icon name="success" v-show="li.isActive" class="float-r" />
				</li>
			</ul>
		</van-popup>
		<div v-for="item in productList" :key="item.id" @click="seeDetail(item.product.id)">
			<van-card :title="item.product.name" :desc="item.product.detail" :price="item.product.price/100" :thumb="item.product.pic">
				<div slot="footer">
					<van-tag mark type="primary">{{item.product.category}}</van-tag>
					<van-tag plain>运费:{{item.product.logistics_price/100}}元</van-tag>
				</div>
			</van-card>
		</div>
		<!--<item-group>-->
		<!--<item-card-hori-->
		<!--v-for="(item, i) in productList"-->
		<!--:key="i"-->
		<!--:goods="item"-->
		<!--@click="itemClick(item.id)"-->
		<!--/>-->
		<!--</item-group>-->

		<van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />

		<is-empty v-if="productList.length == 0">抱歉,没有找到符合条件商品</is-empty>

	</div>
</template>

<script>
const api = new GLOBAL.api()
import IsEmpty from "@/vue/components/is-empty/";
import { Search, Loading, Tab, Tabs } from 'vant';


export default {
	name: "Item-list",
	props: {
		keyword: {
			type: String,
			default: ""
		}
	},


	data() {
		return {
			isLoading: false,
			tabsItem: [
				{ name: "默认", sort: "" },
				{ name: "销量", sort: "sold_quantity" },
				{ name: "最新", sort: "created_at" },
				{ name: "筛选", sort: '' }
			],
			sortVal: "",
			searchProduct: {
				"cond": {
					"key_word": "",
					"type": 0,
					"category": ""
				},
				"limit": 6,
				"page": 1
			},
			filterItem: [{
				name: "全部",
				filterType: 2,
				isActive: true,
			}, {
				name: "店铺商品",
				filterType: 0,
				isActive: false,
			}],
			searchVal: "",
			filterItemShow: false,
			showArrow: false,
			productList: [],
			proTotal: ''
		}
	},

	activated() {
		this.searchVal = this.keyword;
	},

	created() {
		this.getList()
	},

	methods: {
		// 上拉加载
		nextPage() {
			this.searchProduct.page += 1;
			this.getList()
		},
		loadMore() {
			let i = this.searchProduct.page * this.searchProduct.limit
			if (i < this.proTotal) {
				this.nextPage()
			}
		},
		getList(e) {
			this.isLoading = true
			if (e) {
				this.searchProduct.page = 1
			}
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
					this.isLoading = false
					this.proTotal = res.total
				}
			}).catch()
		},
		handleTabClick(index) {
			if (index === 3) {
				this.filterItemShow = true;
			} else {
				const sortVal = this.tabsItem[index].sort;
				if (sortVal !== this.sortVal) {
					this.sortVal = sortVal;
					// this.getList(1);
				}
			}
		},
		cancel() {
			this.searchVal = ''
			this.getList(1)
		},
		seeDetail(e) {
			this.$router.push('/items/detail/' + e)
		}
	},

	components: {
		[Tab.name]: Tab,
		[Tabs.name]: Tabs,
		[Search.name]: Search,
		[Loading.name]: Loading,
		[IsEmpty.name]: IsEmpty,
	}
}
</script>

<style lang="scss" scoped>
@import '../../../assets/scss/var';
.van-card {
  margin-bottom: 10px;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s;
}

.item_list {
  height: 100%;
  /*box-sizing: border-box;*/
  overflow-x: hidden;
  overflow-y: scroll;
  padding-bottom: 0;
}
.fixedTop {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 999;
}

.items_loading {
  margin: 0 auto;
}
.filterItem {
  width: 40%;
  height: 100%;
  li {
    padding: 10px;
    &.filter_active {
      color: $red;
    }
  }
}
.backTop {
  position: fixed;
  right: 20px;
  bottom: 20px;
  font-size: 24px;
}
</style>
