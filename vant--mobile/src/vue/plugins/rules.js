let phone = /^1[3|4|5|8][0-9]\d{4,8}$/
let code = /^\d{4,6}$/
let price = /^(0|[1-9][0-9]{0,9})(\.[0-9]{1,2})?$/

export default {
	phone: phone,
	code: code,
	price: price
}
