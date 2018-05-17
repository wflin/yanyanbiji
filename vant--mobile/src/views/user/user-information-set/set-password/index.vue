<template>
  <div class="setPwd">
    <van-tabs :active="index" @click="handleTabClick">
      <van-tab v-for="(item,index) in list" :key="index" :title="item"></van-tab>
    </van-tabs>
    <van-cell-group v-show="index === 0">
      <van-field v-model="loginform.old_password" label="原密码" placeholder="请输入原密码" />
      <van-field v-model="loginform.password" label="新密码" placeholder="请输入新密码" />
      <van-field v-model="loginform.password2" label="确认密码" placeholder="请再次输入密码" />
    </van-cell-group>
    <md-field-group class="register_submit" v-show="index === 1">
      <md-field v-model="moneyform.telphone" icon="mobile" placeholder="请输入手机号" />
      <md-field v-model="moneyform.code" icon="mobile" placeholder="请输入验证码">
        <div slot="rightIcon" class="getCode red">
          <countdown v-if="counting" :time="60000" @countdownend="countdownend">
            <template slot-scope="props">{{ +props.seconds || 60 }}秒后获取</template>
          </countdown>
          <span v-else @click="getCode">获取验证码</span>
        </div>
      </md-field>
      <md-field v-model="moneyform.pay_password" icon="lock" placeholder="请输入密码" />
      <md-field v-model="moneyform.password2" icon="lock" placeholder="请再次确认密码" />
    </md-field-group>
    <van-button size="normal" v-show="index === 0" class="btn" type="primary" @click="saveChange('login')">保存</van-button>
    <van-button size="normal" v-show="index === 1" class="btn" type="primary" @click="saveChange('money')">保存</van-button>
  </div>
</template>


<script>
import field from '@/vue/components/field/';
import fieldGroup from '@/vue/components/field-group/';
import { Toast } from 'vant';
const api = new GLOBAL.api()
export default {
  data() {
    return {
      loginform: {
        password: '',
        password2: '',
        old_password: ''
      },
      moneyform: {
        telphone: '',
        pay_password: '',
        code: '',
        password2: ''
      },
      index: 0,
      list: ["登录密码", "支付密码"],
      demo2: '登录密码',
      //提示信息
      show: true,
      count: '',
      time: null,
      counting: false,
    }
  },
  created() {
  },
  methods: {
    // 重置密码
    saveChange(e) {
      let url, data
      if (e === 'login') {
        if (this.loginform.password == '' || this.loginform.password2 == '' || this.loginform.old_password == '') {
          Toast({ position: 'center', message: '请将信息填写完整' })
          return
        } else if (this.loginform.password2 !== this.loginform.password) {
          Toast({ position: 'center', message: '两次输入密码不一致' })
          this.loginform.password2 = ''
          this.loginform.password = ''
          return
        } else {
          url = '/password/modify'
          data = this.loginform
        }
      } else if (e === 'money') {
        let moneyform = JSON.parse(JSON.stringify(this.moneyform))
        if (moneyform.telphone == '' || moneyform.password2 == '' || moneyform.pay_password == '' || moneyform.code == '') {
          Toast({ position: 'center', message: '请将信息填写完整' })
          return
        } else if (moneyform.password2 !== moneyform.pay_password) {
          Toast({ position: 'center', message: '两次输入密码不一致' })
          this.moneyform.password2 = ''
          this.moneyform.pay_password = ''
          return
        } else {
          delete (moneyform.password2)
          delete (moneyform.telphone)
          url = 'payword/forget'
          data = moneyform
        }
      }
      let params = {
        url: url,
        data: data
      }
      api.post(params).then((res) => {
        Toast({ position: 'center', message: res.msg })
        if (res.code === 0) {
          this.$router.push({ name: "user" })
        }
      })
    },
    // 获取验证码
    getCode() {
      let telephone = this.moneyform.telephone
      if (!telephone) {
        Toast({ position: 'center', message: '请填写手机号码' })
        return
      } else if (!GLOBAL.rules.phone.test(telephone)) {
        Toast({ position: 'center', message: '手机号码格式不正确！' })
        return
      }
      let params = {
        url: 'user/code',
        params: {
          telephone: telephone
        }
      }
      api.get(params).then((res) => {
        if (res.code === 0) {
          this.counting = true;
        }
      })
    },
    handleTabClick(e) {
      this.index = e
    },
    countdownend() {
      this.counting = false;
    }
  },
  components: {
    [field.name]: field,
    [fieldGroup.name]: fieldGroup,
  }
}
</script>
<style lang="scss" rel='stylesheet/scss' scoped>
.register_submit {
  background: #fff;
  padding: 10px 0;
}
.btn {
  width: 90%;
  margin-left: 5%;
  margin-top: 60px;
}
</style>
