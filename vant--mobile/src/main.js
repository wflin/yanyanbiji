import "@/assets/scss/iconfont/iconfont.css"
import Vue from "vue"
import App from "./App.vue"
import router from "@/vue/router/"
import Vuelidation from "@/vue/plugins/vuelidation"
import valid from "@/vue/mixin/valid"
import VueCountdown from "@/vue/plugins/vue-countdown"
import "@/vue/plugins/global"

//import FastClick from 'fastclick';
import {
	Waterfall,
	Lazyload,
	Toast,
	Tag,
	Dialog,
	Cell,
	CellGroup,
	Field,
	Icon,
	Button,
	Popup,
	loading,
	CellSwipe,
	Swipe,
	SwipeItem,
	Row,
	Radio,
	RadioGroup,
	Col,
	NavBar,
	Sku,
	Stepper,
	Picker,
	Tab,
	Tabs,
	Badge,
	Card
} from "vant"

import util from "@/assets/js/util"
import filters from "@/vue/filter/"

Vue.use(Radio).use(RadioGroup)
// plugins
Vue.use(VueCountdown)
Vue.use(CellSwipe)
// Vue.use(axios);
Vue.use(Vuelidation)
Vue.use(valid)
Vue.use(Stepper)
Vue.use(Picker)
// vue
Vue.use(filters)
Vue.use(util)

// vant
Vue.use(Waterfall)
Vue.use(Badge)
Vue.use(Card)
Vue.use(Tab).use(Tabs)
Vue.use(Lazyload, {
	preLoad: 1.3,
	error: "/static/img/goods_default.png",
	loading: "/static/img/goods_default.png",
	attempt: 1,
	listenEvents: ["scroll"],
	lazyComponent: true
})
Vue.use(Sku)
Vue.use(Dialog)
Vue.use(Tag)
Vue.use(Cell)
Vue.use(CellGroup)
Vue.use(Field)
Vue.use(Icon)
Vue.use(Button)
Vue.use(Popup)
Vue.use(loading)
Vue.use(Swipe).use(SwipeItem)
Vue.use(Row).use(Col)
Toast.setDefaultOptions({
	duration: 1500
})
//FastClick.attach(document.body);
new Vue({
	el: "#app",
	router,
	render: h => h(App)
})
