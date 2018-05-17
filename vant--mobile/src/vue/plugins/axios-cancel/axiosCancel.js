import axios from 'axios';
import qs from 'Qs';
import { Dialog, Toast } from 'vant';

let instance = axios.create({
	timeout: 5000,
	baseURL: process.env.NODE_ENV === "development" ? '/api' : ""
});

instance.interceptors.request.use( (config) => {
	!config.hideLoading && Toast.loading({mask: true});
	if (config.method === 'post' || config.method === 'put') {
		config.data = qs.stringify(config.data);
	}
	if (!config.headers.Authorization) {
		config.headers.Authorization = 'Bearer ' + window.localStorage.getItem('Authorization') || '';
	}
	return config;
}, (err) => {
	return Promise.reject(err);
});


instance.interceptors.request.use( config => {
	console.log(1);
	return config
})

instance.interceptors.response.use( (res) => {
	Toast.clear();
	if (!res.data.success) {
		switch (res.data.code) {
			case 422:
				var flag = Array.isArray(res.data.data) && res.data.data.length;
				Dialog.alert({message: flag ? res.data.data[0].message : res.data.message})
				break;
			case 401:
				break;
			case 404:
				break;
		}
		return Promise.reject(res);
	}
	return res;
}, (error) => {
	Dialog.alert({
	  title: '警告',
	  message: error.message
	})
	return Promise.reject(error);
});


export default instance