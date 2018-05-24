/**
 * Created by root on 2017/4/22.
 **/
// import router from 'src/router/index.js'
import axios from 'axios'
import config from './config.js'


class API {
  post(params) {
    config.data = params.data
    config.method = 'post'
    config.params = ''
    return axios.post(params.url,config.data,config)
  }
  get(params) {
    config.params = params.params
    config.method = 'get'
    config.data = ''
    return axios.get(params.url,config)
  }
  toLogin() {
    localStorage.removeItem('ssid')
    router.push('/index')
  }
}

const api = new API()

// 请求拦截
axios.interceptors.request.use(function (config) {
  //获取ssid并随请求发出
  var ssid = localStorage.getItem('ssid')
  if(ssid){
    config.headers.authorization = ssid
  }
  return config
}, function (error) {
  return Promise.reject(error)
});

// 响应拦截
axios.interceptors.response.use(function (response) {
  var data
  // IE9时response.data是undefined，因此需要使用response.request.responseText(Stringify后的字符串)
  if(response.data == undefined){
    data = response.request.responseText
  } else{
    data = response.data
  }
  // 判断data不是Object时，解析成Object
  if(!(data instanceof Object)){
    data = JSON.parse(data)
  }
  // 登录注册操作时把header.authorization返回
  let login_pattern = new RegExp('login')
  if(login_pattern.test(response.config.url)){
    data.authorization = response.headers.authorization;
    if(data.authorization){
      axios.defaults.headers.common['authorization'] = data.authorization;
    }
  }
  // AJAX结果判断
  if(data.code === 1){

  } else if(data.code === 403){

    // api.toLogin()
  } else if(data.code === 4008) {

    api.toLogin()
  } else if(data.code === 4009){

  }
  return data
}, function (error) {
  return Promise.reject(error)
});

export default API
