<template>
  <div class="vue-uploader">
    <div class="myPosition">
      <!--   <div :class="morepic == 'one'?'pic':'pics'" v-if="morepic == 'one'&&files.length == 0 ||morepic != 'one'">
          <p>+</p>
        </div> -->
      <ul>
        <li :class="morepic == 'one'?'pic':'pics'" v-if="(morepic === 'one'&&files.length === 0) ||morepic != 'one'">
          <p>+</p>
        </li>
        <li v-if="files.length != 0" v-for="(files,index) of files">
          <div :class="morepic == 'one'?'myPic':'myPics'">
            <img :src="files.src" alt="" :class="touchIt == index?'back':'noBack'" @click="operate(index)">
            <div class="del" v-show="touchIt == index?true:false">
              <a :href="files.src" target="_blank">查看原图</a>
              <!-- <i class="iconfont icon-shanchu"></i> -->
            </div>
          </div>
        </li>
      </ul>
    </div>
    <input type="file" accept="image/jpg,image/jpeg,image/png" @change="fileChanged" ref="file" :multiple="more">
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    props: {
      opr: {
        type: String,
        required: true
      },
      // 这个参数用来告诉子组件我需要的是单张上传还是多张上传
      morepic:{
        type: String,
        required: true
      },
      imgSrc:''
    },
    watch:{
      imgSrc:function(val, oldVal){
        const imgList = []
        imgList.push({src:val});
        this.files = imgList.splice(0,1)
      }
    },
    data() {
      return {
        status: 'ready',
        files: [],
        point: {},
        percent: 0,
        more:false ,  //是否能多张图片上传
        touchIt:17000,  //点击图片
      }
    },
    created(){
      if(this.morepic == "one"){
        this.more = false;
      }else{
        this.more = true;
      }
    },
    methods: {
      submit(a) {
        const formData = new FormData();
        for(let i=0;i<a.length;i++){
          formData.append(this.opr, a[i]);
        }
        var params = {
          url:GLOBAL.config.baseURL + 'upload',
          data:formData,
          config:{
            headers:{'Content-Type':'multipart/form-data'},
            onUploadProgress: function (evt) {
              console.log(Math.round((evt.loaded * 100) / evt.total)+ '%')
            }
          }
        };
        axios.post(params.url,params.data,params.config).then(response =>{
          if(response.code === 0){
            for(let i=0;i<response.data.file_url.length;i++){
              console.log(this.files.length)
              this.files[i].src = GLOBAL.config.imgUrl + response.data.file_url[i];
              this.$emit('getimgUrl',this.files)
            }
          }
        });
      },
      fileChanged(event) {
        const list = this.$refs.file.files;
        for (let i = 0; i < list.length; i++) {
          if (!this.isContain(list[i])) {
            const item = {
              name: list[i].name,
              size: list[i].size,
              file: list[i]
            };
            this.html5Reader(list[i], item);
            this.files.push(item);
          }
        }
        this.submit(event.target.files);
      },
      // 将图片文件转成BASE64格式
      html5Reader(file, item){
        const reader = new FileReader();
        reader.onload = (e) => {
          this.$set(item, 'src', e.target.result)
        };
        reader.readAsDataURL(file)
      },
      isContain(file) {
        this.files.forEach((item) => {
          if(item.name === file.name && item.size === file.size) {
            return true
          }
        });
        return false
      },
      operate(e){
        this.touchIt = e;
      },
    }
  }
</script>
<style lang="scss" rel='stylesheet/scss' scoped>
  .vue-uploader{
    position:relative;
  }
  .myPosition{
    position: absolute;
    top:0;
    left:0;
    margin-left:15px;
    .pic{       //一张图片
      width:70px;
      height:70px;
      border:1px solid #ccc;
      p{
        color:#ccc;
        font-size:40px;
        text-align:center;
        height: 70px;
        line-height: 60px;
      }
    }
    .pics{    //多张图片
      width:80px;
      height:80px;
      border:1px solid #ccc;
      margin-right:15px;
      p{
        color:#ccc;
        font-size:40px;
        text-align:center;
        height: 80px;
        line-height: 70px;
      }
    }
    ul{
      li{
        position: relative;
        float:left;
        .myPic{    //一张图片
          width:70px;
          height:70px;
          img{
            width:100%;
            height:100%;
          }
        }
        .myPics{     //多张图片
          width:80px;
          height:80px;
          margin:0 15px 15px 0;
          position:relative;
          img{
            width:100%;
            height:100%;
          }
          .back{
            filter: contrast(0.5);   //给图片加滤镜
          }
          .del{
            position:absolute;
            top:30%;
            color:#fff;
            left:15%;
            a{
              color:#fff;
              font-size:14px;
            }
          }
        }
      }
    }
  }
  input{
    position: absolute;
    left: 15px;
    width: 70px;
    height: 70px;
    opacity: 0;
    cursor: pointer;
    z-index: 5;
  }
</style>
