import Vue from "vue"
import { Toast } from "vant"
import Router from "vue-router"

import home from "./home"
import items from "./items"
import user from "./user"
import order from "./order"
import login from "./login"
import message from "./message"

Vue.use(Router)

let RouterModel = new Router({
	routes: [...home, ...items, ...user, ...order, ...login, ...message]
})

RouterModel.beforeEach((to, from, next) => {
	const { ssid } = Vue.prototype.$util.getLocalStorage("ssid")
	if (!ssid) {
		if (to.meta.login) {
			Toast({ position: "top", message: "没有操作权限,请先登录" })
			RouterModel.push({ path: "/login", query: { redirect: to.name } })
			return
		}
	}
	next()
})

RouterModel.afterEach((to, from) => {})

export default RouterModel
