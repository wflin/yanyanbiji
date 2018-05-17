<template>
  <div class="qusetionDetail">
    <div class="container1">
      <div class="comment">
        <ul class="card">
          <li>
            <h3>
              <span class="ques">问</span>{{detailList.name}}</h3>
            <p>{{detailList.detail}}</p>
            <p>
              <small>提问于:{{detailList.create_time}}</small>
              <span class="fr money">￥{{detailList.price/100}}</span>
            </p>
          </li>
        </ul>
        <ul class="card">
          <li v-for="item in answerList" :key="item.id">
            <p>
              <span class="ques">答</span>
              <small>{{item.create_time}}</small>
            </p>
            <p>{{item.content}}</p>
            <div class="changeStu">
              <van-icon name="shoucang-full">点赞数:&nbsp{{item.thumbs_num}}</van-icon>
              <van-button size="mini" @click.native="collect(item.id)" v-if="item.status === 0">采纳</van-button>
              <van-tag type="success" v-if="item.status === 1">已采纳</van-tag>
              <!-- <van-button size="mini" type="primary"  @click.native="collect(item.id)" v-if="collection.length != 0">已采纳</van-button> -->
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
const api = new GLOBAL.api()
export default {
  data() {
    return {
      collection: [],
      detailList: {},
      answerList: [],
      showloading: false,
    }
  },
  created() {
    this.getDetail()
    this.getAnswer()
  },
  methods: {
    // 采纳
    collect(e) {
      let params = {
        url: 'reply/agree',
        data: {
          id: e
        }
      }
      api.post(params).then((res) => {
        if (res.code === 0) {
          window.location.reload()
        }
        Toast({ position: 'top', message: res.msg })
      })
    },
    // 获取问题详情
    getDetail() {
      this.showloading = true
      let params = {
        url: 'question/detail',
        data: {
          id: this.$route.query.id
        }
      }
      api.post(params).then((res) => {
        this.showloading = false
        if (res.code === 0) {
          this.detailList = res.data
        }
      })
    },
    // 查询此问题的回复
    getAnswer() {
      this.showloading = false
      let params = {
        url: 'reply/list',
        data: {
          question_id: this.$route.query.id,
          limit: 8,
          page: 1
        }
      }
      api.post(params).then((res) => {
        this.showloading = false
        if (res.code === 0) {
          this.answerList = res.data
        }
      })
    },

  }
}
</script>
<style lang="scss" rel='stylesheet/scss' scoped>
.qusetionDetail {
  background: #fff;
  .container1 {
    .comment {
      ul {
        li {
          padding: 5px;
          border: 1px solid #f1f1f1;
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
    }
  }
  .money {
    color: red;
  }
}
</style>
