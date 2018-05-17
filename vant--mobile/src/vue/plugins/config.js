let reqUrl = "//106.14.9.214"
let imgUrl = "//106.14.9.214"
let port = ""
let suffix = "/api/yan/v1/"
 // let reqUrl = "//127.0.0.1:8083"
 // let imgUrl = "//127.0.0.1:8083"
 // let port = ""
 // let suffix = "/api/yan/v1/"
export default {

	method: "post",
	// 基础url前缀
	baseURL: reqUrl + port + suffix,
	imgUrl: imgUrl,
	// 请求头信息
	headers: {
		"Content-Type": "application/json;charset=UTF-8"
	},
	//post参数
	data: {},
	params: {},
	//设置超时时间
	timeout: 10000,
	// 携带凭证
	withCredentials: false,
	//返回数据类型
	responseType: "json"
}
