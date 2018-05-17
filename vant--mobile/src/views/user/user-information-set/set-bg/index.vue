<template>
  <div class="set_bg">
    <div class="question">
      <h1 class="ask">{{detailList.name}}</h1>
      <h3 class="ask">{{detailList.detail}}</h3>
      <p @click="bestAnswer">我有更好的回答
        <span class="icon" v-if="bestAns===false">▽</span>
        <span class="icon" v-if="bestAns===true">△</span>
      </p>
      <!--       <p @click="bestAnswer">我有更好的回答<span class="icon">△</span></p> -->
      <div class="best" v-show="bestAns">
        <div class="answer">
          <textarea type="text" v-model="recontent"></textarea>
        </div>
        <van-button size="small" type="primary" class="btn" @click="solute(detailList.id)">发布</van-button>
      </div>
    </div>
    <ul class="card">
      <li v-for="item in answerList" :key="item.id">
        <p class="ansContent">{{item.content}}</p>
        <div class="changeStu">
          <van-icon name="shoucang-full" v-for="i in item.thumbs_num" :key="i"></van-icon>
          <span>点赞数:&nbsp{{item.thumbs_num}}</span>
          <van-button size="mini" @click.native="collect(item.id)">点赞</van-button>
          <!-- <van-tag type="success " v-show="agree==item.id ">已点赞</van-tag> -->
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
import { Toast } from 'vant';
const api = new GLOBAL.api()
export default {
  data() {
    return {
      detailList: {},
      bestAns: false,
      recontent: '',
      answerList: [],
      collection: [],
      agree: ''
    }
  },
  created() {
    this.getDetail()
    this.getAnswer()
  },
  methods: {
    // 获取问题详情
    getDetail() {
      let params = {
        url: 'question/detail',
        data: {
          id: this.$route.params.questionId
        }
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          this.detailList = res.data
        }
      })
    },
    // 点赞
    collect(e) {
      let params = {
        url: 'reply/thumb',
        data: {
          id: e
        }
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          this.agree = e
          window.location.reload()
        }
        Toast({ position: 'top', message: res.msg })
      })
    },
    // 回复问题
    solute(index) {
      this.myAnswer = index;
      if (this.recontent == '') {
        Toast({ position: 'top', message: '请输入回复内容' })
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
            this.bestAns = false
            this.getAnswer()
          }
          Toast({ position: 'top', message: res.msg })
        }).catch()
      }
    },
    // 查询此问题的回复
    getAnswer() {
      let params = {
        url: 'reply/list',
        data: {
          question_id: this.$route.params.questionId,
          limit: 8,
          page: 1
        }
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          this.answerList = res.data
        }
      })
    },
    bestAnswer() {
      this.bestAns = !this.bestAns
      this.recontent = ''
    }
  }
}
</script>
<style lang="scss" rel='stylesheet/scss' scoped>
.question {
  background: #fff;
  width: 100%;
  .ask {
    padding: 10px;
    word-wrap: break-word;
  }
  p {
    font-size: 20px;
    text-align: center;
    border-top: 1px solid #f1f1f1;
    padding: 10px 0;
    margin-top: 10px;
  }
  textarea {
    display: block;
    padding: 10px;
    border: 1px solid #c9c9c9;
    height: 120px;
    width: 86%;
    overflow-y: scroll;
    word-break: break-all;
    margin: 10px auto;
  }
  .answer {
    text-align: center;
  }
  .best {
    background: #fff;
    height: 190px;
  }
  .btn {
    float: right;
    margin-right: 4%;
  }
  .icon {
    font-size: 20px;
    margin-left: 10px;
  }
}
ul {
  li {
    padding: 5px;
    border: 1px solid #f1f1f1;
  }
  .ansContent {
    word-break: break-all;
    word-wrap: break-word;
  }
  .ques {
    color: #409eff;
    margin-right: 5px;
  }
  small {
    color: #999;
  }
  .changeStu {
    margin-top: 20px;
  }
  i {
    border: 1px solid #f1f1f1;
    margin-right: 10px;
    padding: 5px 8px;
    border-radius: 8px;
  }
}
.card {
  margin-top: 10px;
  background: #fff;
}
</style>
