<template>
	<div class="user_team" v-waterfall-lower="loadMore" waterfall-disabled="disabled" waterfall-offset="50">
		<van-cell-group>
			<van-cell :title="'我的提问'+'('+queCount+')'">
				<div>
					<a @click="showQue= true">添加提问</a>
				</div>
			</van-cell>
		</van-cell-group>
		<van-cell-group>
			<div class="comment" v-if="questionList.length != 0">
				<ul v-for='item in questionList'>
					<li class="del">
						<div class="head">
							<van-button type="danger" class="fr" size="mini" @click.native="deleteQuestion(item .id)">删除</van-button>
						</div>
						<div @click="seeDetail(item .id)" class="detail">
							<h2>{{item.name}}</h2>
							<span>{{item.detail.substring(0,122)}}
								<i v-if="item.detail.length>120">......</i>
							</span>
						</div>
					</li>
				</ul>
			</div>
		</van-cell-group>
		<van-dialog v-model="showQue" :showCancelButton=true @confirm="addQues" @cancel="closeDialog">
			<van-field v-model="Addques.name" label="标题" maxlength="50" placeholder="请输入标题" />
			<van-field v-model="Addques.category" label="分类" placeholder="请输入分类（如:文学）" />
			<van-field v-model="Addques.price" label="问题价格" placeholder="请输入问题价格" />
			<van-field v-model="Addques.detail" label="问题详情" type="textarea" placeholder="请输入问题详情(最多200字)" cols="6" rows="1" class="textarea" maxlength="200" autosize/>
		</van-dialog>
		<van-loading type="gradient-circle" color="black" class="items_loading" v-show="isLoading" />
		<is-empty v-model="!questionList.length">暂无提问</is-empty>
	</div>
</template>

<script>
const api = new GLOBAL.api()
import isEmpty from "@/vue/components/is-empty/";
export default {
	components: {
		[isEmpty.name]: isEmpty,
	},
	data() {
		return {
			questionList: [],
			// 查询条件
			search: {
				"cond": {
					"key_word": "",
					"status": 0,
					"category": ""
				},
				"limit": 8,
				"page": 1
			},
			// 提价提问
			Addques: {
				"name": "",
				"detail": "",
				"category": "",
				"price": ""
			},
			showQue: false,
			columns: ['文学', '理学', '法学'],
			queCount: 0,
			isLoading: false
		}
	},
	created() {
		this.getQuestionList()
	},
	methods: {
		// 上拉加载
		nextPage() {
			this.search.page += 1;
			this.getQuestionList()
		},
		loadMore() {
			let i = this.search.page * this.search.limit
			if (i < this.queCount) {
				this.nextPage()
			}
		},
		// 获取提问列表
		getQuestionList() {
			this.isLoading = true
			let params = {
				url: 'question/list',
				data: this.search
			}
			api.post(params).then(res => {
				if (res.code === 0) {
					if (this.search.page > 1) {
						for (let i in res.data) {
							this.questionList.push(res.data[i])
						}
					} else {
						this.questionList = res.data
					}
					this.queCount = res.total
					this.isLoading = false
				}
			}).catch(() => {
				this.isLoading = false
			})
		},
		// 提问
		addQues() {
			this.showQue = true
			let Addques = this.Addques
			if (Addques.name == '' || Addques.detail == '' || Addques.price == '' || Addques.category == '') {
				this.$toast('请将信息填写完整');
			} else if (!GLOBAL.rules.price.test(this.Addques.price)) {
				this.$toast('请输入正确的价格');
			} else {
				Addques.price = this.Addques.price * 100
				let params = {
					url: 'question/add',
					data: Addques
				}
				api.post(params).then((res) => {
					if (res.code === 0) {
						this.getQuestionList()

					}
					this.showQue = false
					this.$toast(res.msg);
					this.Addques = {
						"name": "",
						"detail": "",
						"category": "",
						"price": ""
					}

				})
			}
		},
		// 跳转至问题详情
		seeDetail(e) {
			this.$router.push({ path: '/user/queDetail', query: { id: e } })
		},
		// 删除问题
		deleteQuestion(e) {
			let params = {
				url: 'question/delete',
				data: {
					id: e
				}
			}
			api.post(params).then(res => {
				this.showMsg = true
				this.message = res.msg
				if (res.code === 0) {
					this.getQuestionList()
				}
			}).catch()
		},
		// 关闭模态框
		closeDialog() {
			this.Addques = {
				"name": "",
				"detail": "",
				"category": "",
				"price": ""
			}
		}
	}
}
</script>

<style lang="scss" scoped>
.user_team {
  // background-color: #fff;
}
.van-cell-group {
  background: #f1f1f1;
}
.comment {
  ul {
    margin-bottom: 10px;
    background: #fff;
  }
  .del {
    word-wrap: break-word;
    word-break: normal;
    overflow-y: auto;
    // border: 1px solid #f1f1f1;
    padding: 10px;
    position: relative;
    .head {
      position: absolute;
      right: 20px;
    }
  }
  .detail {
    h2 {
      margin-bottom: 8px;
    }
    min-height: 80px;
    max-height: 140px;
  }
}
</style>
