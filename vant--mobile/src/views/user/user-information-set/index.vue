<template>
  <div class="msg">
    <div class="pic">
      <p>头像</p>
      <Uploader :opr="'file'" :imgSrc='userinfo.pic' :morepic="'one'" @getimgUrl="getimgUrl" class="uploader"></Uploader>
    </div>
    <van-cell-group>
      <van-field v-model="userinfo.username" label="姓名" icon="clear" placeholder="请输入姓名" />
      <van-field v-model="userinfo.school" label="学校" icon="clear" placeholder="请输入学校" />
      <van-field v-model="userinfo.address" label="详细地址" icon="clear" placeholder="请输入详细地址" />
    </van-cell-group>
    <van-button size="normal" type="primary" class="btn" @click="changeMyself">提交</van-button>
  </div>
</template>

<script>
  import Uploader from "@/vue/components/uploader/";
  const api = new GLOBAL.api()
  import { Toast } from 'vant';
  export default {
    components:{
      Uploader
    },
    data(){
      return {
        userinfo:{
          "username":"",
          "school":"",
          "address":"",
          "pic":""
        },
      }
    },
    created(){
      this.getSelfMsg()
    },
    methods: {
      // 获取个人信息
      getSelfMsg(){
        let params = {
          url:'user/info',
          data:{}
        }
        api.post(params).then((res)=>{
          if(res.code === 0){
            let data = res.data
            this.userinfo={
              "username":data.username,
              "school":data.school,
              "address":data.address,
              "pic":data.pic
            }
          }
        })
      },
      // 用户信息修改
      changeMyself(){
        let userinfo = this.userinfo
        if(userinfo.username === '' ||userinfo.school === ''||userinfo.address === ''
         ){
          Toast({position:'center',message:'请将信息填写完整'})
        }else{
          let params = {
            url:'user/modify',
            data:this.userinfo
          }
          api.post(params).then((res)=>{
            Toast({position:'top',message:res.msg})
            if(res.code === 0){
              this.getSelfMsg()
            }
          })
        }
      },
      // 获取图片地址
      getimgUrl(e){
        this.userinfo.pic = e[0].src
      },
    },

  }
</script>


<style lang="scss" scoped>
  @import "../../../assets/scss/var";
  @import "../../../assets/scss/mixin";
  .pic{
    height:80px;
    img{
      width:70px;
      height:70px;
      display:block;
      margin:5px 15px 5px 0;
      float:right;
    }
    p{
      float:left;
      line-height:80px;
      padding-left:15px;
    }
    .uploader{
      float:right;
      margin:5px 20px 5px 0;
      width:70px;
    }
  }
  .msg{
    background:#fff;
  }
  .btn{
    width: 80%;
    margin-top:60px;
    margin-left:10%;
  }
</style>
