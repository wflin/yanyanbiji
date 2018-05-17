<template>
	<div class="tab_class">
		<van-cell-group>
			<van-field v-model="addProduct.name" label="标题" placeholder="请输入标题" />
			<van-field v-model="addProduct.category" label="分类" placeholder="请输入分类(如:文学)" />
			<van-radio-group v-model="addProduct.type">
				<van-cell-group>
					<van-cell>
						<span>纸质材料</span>
						<van-radio :name="0" class='choose'></van-radio>
					</van-cell>
					<van-cell>
						<span>下载材料</span>
						<van-radio :name="1" class='choose'></van-radio>
					</van-cell>
				</van-cell-group>
			</van-radio-group>
			<van-field v-model="addProduct.price" label="价格" placeholder="请输入价格" />
			<van-field v-model="addProduct.detail" label="详情" type="textarea" placeholder="请输入详情" rows="1" autosize/>
			<div class="picUp">
				<p>资料图片</p>
				<Uploader :opr="'file'" :imgSrc='addProduct.pic' :morepic="'one'" @getimgUrl="getimgUrl" class="uploader"></Uploader>
			</div>
		</van-cell-group>
		<van-button type="primary" size="small" class="btn" @click="publish">提交</van-button>
	</div>
</template>

<script>
import Uploader from "@/vue/components/uploader/";
const api = new GLOBAL.api()
import { Toast } from 'vant';
export default {
	components: {
		Uploader
	},
	data() {
		return {
			addProduct: {
				"name": "",
				"describe": "",
				"detail": "",
				"type": "",
				"pic": "",
				"category": "",
				"price": ""
			},
		}
	},

	created() {
		this.getproDetail()
	},

	methods: {
		// 获取产品详情
		getproDetail() {
			let params = {
				url: 'product/detail',
				data: {
					id: this.$route.query.id
				}
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					this.addProduct = res.data.product
				}
			})
		},
		// 获取图片地址
		getimgUrl(e) {
			this.addProduct.pic = e[0].src
		},
		// 发布
		publish() {
			let addProduct = this.addProduct
			if (addProduct.name === '' || addProduct.detail === '' || addProduct.price === '' || addProduct.category === ''
				|| addProduct.type === '' || addProduct.pic === '') {
				Toast({ position: 'center', message: '请将信息填写完整' })
			} else if (!GLOBAL.rules.price.test(this.addProduct.price)) {
				Toast({ position: 'center', message: '请输入正确的价格' })
			} else {
				let params = {
					url: 'product/modify',
					data: this.addProduct
				}
				api.post(params).then((res) => {
					if (res.code === 0) {
						Toast({ position: 'top', message: '提交成功' })
						this.$router.push('/user/server')
					} else {
						Toast({ position: 'top', message: res.msg })
					}
				})
			}
		},
	},
}
</script>


<style lang="scss" scoped>
.choose {
  float: right;
}
.btn {
  width: 80%;
  margin: 40px 10% 0 10%;
}
.picUp {
  height: 90px;
  padding: 0;
  overflow-y: auto;
  img {
    width: 80px;
    height: 80px;
    display: block;
    margin: 5px 15px 5px 0;
    float: right;
  }
  p {
    padding: 8px 15px;
    margin: 0;
    float: left;
  }
  .uploader {
    margin: 8px 20px 8px 0;
    width: 80px;
    float: right;
  }
}
</style>
