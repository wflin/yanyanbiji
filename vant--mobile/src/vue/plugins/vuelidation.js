import Vuelidation, { defaultOptions } from 'vuelidation';

defaultOptions.methods = {
	mobile(value, args){
		let msg = "请填入正确的手机号码";
		let valid = /^1[0-9]{10}$/.test(value);
		return [valid, msg];
	}
}

export default Vuelidation