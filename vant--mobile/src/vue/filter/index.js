import moment from 'moment';
moment.locale('zh-cn');

export const dateFormat = (value, format = 'YYYY-MM-DD') => {
	return value ? moment(value * 1000).format(format) : '';
}

export const yuan = (value) => {
	return !isNaN(value) ? '¥' + (value / 100).toFixed(2) : value;
}

export default {
	install(Vue) {
		Vue.filter('yuan', yuan)
		Vue.filter('dateFormat', dateFormat)
	},
}
