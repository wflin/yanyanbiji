const login = () => import(/* webpackChunkName: "login" */ '@/views/login/login');
const registerSubmit = () => import(/* webpackChunkName: "register-submit" */ '@/views/login/register-submit/');
const forget = () => import(/* webpackChunkName: "forget" */ '@/views/login/forget/');


export default [{
			path: "/login",
			name: "login",
			component: login
	},{
			path: "/login/registerSubmit",
			name: "registerSubmit",
			component: registerSubmit
	},{
			path: "/login/forget",
			name: "forget",
			component: forget
	}]