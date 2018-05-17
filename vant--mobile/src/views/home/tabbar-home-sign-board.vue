<template>
	<div class="signboard" style="height: 100%; overflow: scroll;" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="50">
		<div class="banner">
			<van-swipe :autoplay="3000">
				<van-swipe-item v-for="(image, index) in images" :key="index">
					<img v-lazy="image" />
				</van-swipe-item>
			</van-swipe>
		</div>
		<div class="book" v-show="productList.length && questionList.length">
			<div class="title">
				<h4>笔记资料</h4>
				<a @click="toItem">查看全部
					<van-icon name="arrow" />
				</a>
			</div>
			<div class="showCard">
				<div class="card" v-for='(item,index) in productList' @click="toDetail(item.product.id)" :key="index">
					<img slot="header" :src="item.product.pic">
					<div slot="content" class="card-padding">
						<p>
							<small>{{item.product.create_time}}</small>
						</p>
						<p>
							<van-tag mark type="primary">{{item.product.category}}</van-tag>{{item.product.name}}</p>
						<van-row gutter="5">
							<van-col span="12" class="money">￥{{item.product.price/100}}</van-col>
							<van-col>
								<small>已有{{item.comment_num}}人评论</small>
							</van-col>
						</van-row>
					</div>
				</div>
			</div>
		</div>
		<div class="question" v-show="productList.length && questionList.length">
			<ul class="answer">
				<li v-for='(item,index) in questionList' :key="index" @click="seeDetail(item.id)">
					<img slot="header" src="static/img/7.jpg">
					<p class="author">
						<small>研研-</small>
						<small>勤学好问</small>
					</p>
					<h4>{{item.name}}</h4>
					<span>{{item.detail.substring(0,98)}}
						<i v-if="item.detail.length>100">.....</i>
					</span>
					<!-- <div class="call" v-show="myAnswer==item.id?true:false">
					<textarea placeholder="请输入回复内容" v-model="recontent" cols="30" rows="6"></textarea>
					<button class="fr" @click="solute(item.id)">确定</button>
					<button class="fr" @click="cancelAnswer">取消</button> -->
					<!-- 	</div> -->
				</li>
			</ul>
		</div>
		<van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />
		<is-empty v-model="!questionList.length && !productList.length">服务器或网络开小差了,请重新刷新</is-empty>
	</div>
</template>

<script>
const api = new GLOBAL.api()
// import collectImg from '@/assets/images/index_collect.png'
import isEmpty from "@/vue/components/is-empty/";
export default {
	name: "sign-board",
	components: {
		[isEmpty.name]: isEmpty,
	},
	data() {
		return {
			myAnswer: 17000,   //标识回复字段
			images: [
				'https://img.yzcdn.cn/2.jpg',
				'https://img.yzcdn.cn/2.jpg',
				'https://img.yzcdn.cn/2.jpg',
				'https://img.yzcdn.cn/2.jpg'
			],
			// 所有资料查询
			productList: [],
			searchProduct: {
				"cond": {
					"key_word": "",
					"type": 0,
					"category": ""
				},
				"limit": 8,
				"page": 1
			},
			// 所有问题查询
			questionList: [],
			searchAll: {
				"cond": {
					"key_word": "",
					"status": 0,
					"category": ""
				},
				"limit": 8,
				"page": 1
			},
			recontent: '',
			isLoading: false,
		}
	},
	created() {
		this.getproduct()
		this.getallQuestion()
	},
	methods: {
		// 上拉加载
		nextPage() {
			this.searchAll.page += 1;
			this.getallQuestion()
		},
		loadMore() {
			let i = this.searchAll.page * this.searchAll.limit
			if (i < this.questionTotal) {
				this.nextPage()
			}
		},
		getproduct() {
			this.isLoading = true
			let params = {
				url: 'product/all',
				data: this.searchProduct
			}
			api.post(params).then(res => {
				if (res.code === 0) {
					if (res.total > 1) {
						this.productList.push(res.data[0])
						this.productList.push(res.data[1])
					} else {
						this.productList.push(res.data[0])
					}
					this.isLoading = false
				}
			}).catch(() => {
				this.isLoading = false
			})
		},
		// 所有问题查询
		getallQuestion() {
			this.isLoading = true
			let params = {
				url: 'question/all',
				data: this.searchAll
			}
			api.post(params).then(res => {
				if (res.code === 0) {
					if (this.searchAll.page > 1) {
						for (let i in res.data) {
							this.questionList.push(res.data[i])
						}
					} else {
						this.questionList = res.data
					}
					this.questionTotal = res.total
					this.isLoading = false
				}
			}).catch(() => {
				this.isLoading = false
			})
		},
		// 回复问题
		solute(index) {
			this.myAnswer = index;
			if (this.recontent == '') {
				this.showMsg = true
				this.message = '请输入回答内容'
			} else {
				let params = {
					url: 'reply/add',
					data: {
						content: this.recontent,
						question_id: index
					}
				}
				api.post(params).then(res => {
					if (res.code === 0) {
						this.myAnswer = 17000
					}
					this.showMsg = true
					this.message = res.msg
				}).catch()
			}
		},
		//取消回复
		cancelAnswer() {
			this.myAnswer = 17000;
		},
		// 查看全部
		toItem() {
			this.$router.push('/items/list')
		},
		// 前往资料详情界面
		toDetail(e) {
			this.$router.push('/items/detail/' + e)
		},
		// 查看问题详情
		seeDetail(e) {
			this.$router.push('/user/information/setbg/' + e)
		}
	}
}
</script>

<style lang="scss" scoped>
@import '../../assets/scss/var';
.banner {
  img {
    width: 100%;
    height: 180px;
    display: block;
  }
}
.book {
  .title {
    background: #fff;
    padding: 5px 10px;
    height: 40px;
    h4 {
      float: left;
      font-size: 16px;
      font-weight: 400;
      margin: 0;
    }
    a {
      color: #999;
      float: right;
      font-size: 14px;
      .icon {
        font-size: 14px;
      }
    }
  }
  .showCard {
    width: 100%;
    display: flex;
    position: relative;
  }
  .card {
    min-height: 200px;
    width: 50%;
    background: #fff;
    margin-top: 0;
    padding: 0 10px;
    float: left;
    img {
      width: 100%;
      height: 100px;
      border-radius: 8px;
      display: block;
      margin-bottom: 5px;
    }
    p {
      margin-bottom: 5px;
    }
    .van-row {
      position: absolute;
      bottom: 10px;
    }
    .van-col {
      margin-right: 2px;
    }
    .van-tag {
      margin-right: 5px;
    }
    .money {
      color: red;
    }
    small {
      color: #999;
    }
  }
}
.question {
  background: #fff;
  margin-top: 10px;
  .answer {
    li {
      padding: 5px 10px;
      border-bottom: 1px solid #f1f1f1;
      img {
        width: 40px;
        height: 40px;
        border-radius: 20px;
        float: left;
        margin-right: 10px;
      }
      .author {
        line-height: 40px;
      }
      p:nth-child(2n) {
        color: #999;
      }
      h4 {
        color: #409eff;
      }
      .call {
        background: #f1f1f1;
        border-radius: 10px;
        padding: 5px;
        width: 100%;
        height: 125px;
        textarea {
          width: 100%;
          background: #f1f1f1;
        }
        button {
          margin-right: 10px;
          background: none;
          color: #409eff;
        }
      }
    }
  }
}
</style>
