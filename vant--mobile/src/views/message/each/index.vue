<template>
	<div class="eachMsg" style="height: 100%; overflow: scroll;" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="50">
		<div @click="getDetail(goods.product.id)">
			<van-card :title="goods.product.name" :desc="goods.product.detail" num="1" :price="goods.product.price/100" :thumb="goods.product.pic" v-if="goods !== ''" />
		</div>
		<ul class="msg" v-if="userinfo">
			<li v-for="talk in replyList" :key="talk.id" :class="talk.type === 0?'send':'get'" v-if="talk.content!==''">
				<div class="user" v-show="talk.type === 0">
					<img src="static/img/7.jpg" alt="" v-if="!userinfo.pic">
					<img :src="userinfo.pic" alt="" v-else>
					<p>{{userinfo.username}}</p>
				</div>
				<div class="textarea">
					<van-field v-model="talk.content" type="textarea" rows="1" autosize />
				</div>
				<div class="user" v-show="talk.type === 1">
					<img src="static/img/7.jpg" alt="">
				</div>
			</li>
		</ul>
		<van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />
		<div class="footer">
			<van-cell-group>
				<van-field v-model="message" type="textarea" rows="1" placeholder="最多可输入150个字" autosize maxlength="150" />
			</van-cell-group>
			<van-button type="primary" @click="sendMsg">发送</van-button>
		</div>
	</div>
</template>

<script>
const api = new GLOBAL.api()
import { Toast } from 'vant';
export default {
	data() {
		return {
			goods: '',
			message: '',
			search: {
				get_id: '',
				send_id: '',
				page: 1,
				limit: 7
			},
			isLoading: false,
			replyList: [],
			userinfo: {
				"username": "",
				"school": "",
				"address": "",
				"pic": ""
			},
			replyTotal: '',
			timeout: ''
		}
	},
	created() {
		if (this.$route.query.productid) {
			this.getproDetail()
		}
		this.getSelfMsg()
		this.search.get_id = this.$route.query.sellid
		this.timeout = setInterval(function () {
			window.location.reload()
		}, 180000)
	},
	// 离开页面销毁定时刷新
	destroyed() {
		window.clearInterval(this.timeout)
	},

	methods: {
		// 上拉加载
		nextPage() {
			this.search.page += 1;
			this.getchatList()
		},
		loadMore() {
			let i = this.search.page * this.search.limit
			if (i < this.replyTotal) {
				this.nextPage()
			}
		},
		// 先获取产品信息和商家信息
		getproDetail() {
			let params = {
				url: 'product/detail',
				data: {
					id: this.$route.query.productid
				}
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					this.goods = res.data
				}
			})
		},
		//商品跳转
		getDetail(e) {
			this.$router.push('/items/detail/' + e)
		},
		//发送消息给卖家
		sendMsg() {
			if (this.message == '' || this.message == null) {
				Toast({ position: 'center', message: '不能发送空消息' })
			} else {
				let params = {
					url: 'chat/add',
					data: {
						get_id: this.$route.query.sellid,
						content: this.message
					}
				}
				api.post(params).then((res) => {
					if (res.code === 0) {
						this.message = ''
					} else {
						this.$toast(res.msg)
					}
				})
			}
		},
		// 获取消息记录
		getchatList() {
			this.isLoading = true
			let params = {
				url: 'chat/list',
				data: this.search
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					if (this.search.page > 1 && res.data.length) {
						for (let i in res.data) {
							this.replyList.push(res.data[i])
						}
					} else {
						this.replyList = res.data
					}
					this.replyTotal = res.total
					this.isLoading = false
				}
			})
		},
		// 获取个人信息
		getSelfMsg() {
			let params = {
				url: 'user/info',
				data: {}
			}
			api.post(params).then((res) => {
				if (res.code === 0) {
					let data = res.data
					this.search.send_id = data.id
					this.userinfo = {
						"username": data.username,
						"school": data.school,
						"address": data.address,
						"pic": data.pic
					}
					this.getchatList()
				}
			})
		},
	}
}
</script>


<style lang="scss" scoped>
.eachMsg {
  .send {
    margin-top: 20px;
    display: flex;
    flex: 1;
    width: 100%;
    .user {
      min-width: 50px;
      margin-left: 10px;
      img {
        display: block;
        width: 50px;
        height: 40px;
      }
      p {
        font-size: 12px;
        color: #999;
      }
    }
    .textarea {
      margin-left: 20px;
      width: 70%;
      position: relative;
    }
    .textarea::before {
      content: '';
      position: absolute;
      border-width: 8px;
      border-style: solid;
      border-color: transparent white transparent transparent;
      top: 25%;
      right: 100%;
    }
  }
  .get {
    margin: 15px 10px;
    display: flex;
    flex: 1;
    .user {
      min-width: 50px;
      margin-left: 10px;
      img {
        display: block;
        width: 50px;
        height: 40px;
      }
      p {
        font-size: 12px;
        color: #999;
        text-align: center;
      }
    }
    .textarea {
      margin-left: 20px;
      width: 100%;
      position: relative;
    }
    .textarea::after {
      content: '';
      position: absolute;
      border-width: 8px;
      border-style: solid;
      border-color: transparent transparent transparent white;
      top: 25%;
      left: 100%;
    }
  }
  .footer {
    position: fixed;
    bottom: 0;
    right: 0;
    left: 0;
    .van-cell-group {
      width: 80%;
      float: left;
    }
    .van-button {
      float: right;
      width: 20%;
    }
  }
}
</style>
