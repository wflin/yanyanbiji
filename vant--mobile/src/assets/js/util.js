const getLocalStorage = (...args) => {
	let storage = {}
	for (let arg of args) {
		storage[arg] = window.localStorage.getItem(arg) || ""
	}
	return storage
}

const setLocalStorage = data => {
	for (let prop in data) {
		window.localStorage.setItem(prop, data[prop])
	}
}

const removeLocalStorage = (...args) => {
	for (let arg of args) {
		window.localStorage.removeItem(arg)
	}
}

const debounce = (func, wait, immediate) => {
	let timeout, args, context, timestamp, result
	return function() {
		context = this
		args = arguments
		timestamp = new Date()
		const later = () => {
			const last = new Date() - timestamp
			if (last < wait) {
				timeout = setTimeout(later, wait - last)
			} else {
				timeout = null
				result = func.apply(context, args)
			}
		}
		if (!timeout) {
			timeout = setTimeout(later, wait)
		}
		return result
	}
}
const throttle = (func, wait, options) => {
	var timeout, context, args, result
	var previous = 0
	if (!options) options = {}

	var later = function() {
		previous = options.leading === false ? 0 : new Date()
		timeout = null
		result = func.apply(context, args)
		if (!timeout) context = args = null //显示地释放内存，防止内存泄漏
	}

	var throttled = function() {
		var now = new Date()
		if (!previous && options.leading === false) previous = now
		var remaining = wait - (now - previous)
		context = this
		args = arguments
		if (remaining <= 0 || remaining > wait) {
			if (timeout) {
				clearTimeout(timeout)
				timeout = null
			}
			previous = now
			result = func.apply(context, args)
			if (!timeout) context = args = null
		} else if (!timeout && options.trailing !== false) {
			timeout = setTimeout(later, remaining)
		}
		return result
	}

	throttled.cancel = function() {
		clearTimeout(timeout)
		previous = 0
		timeout = context = args = null
	}

	return throttled
}

const getLocationParam = function(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)")
	var r = window.location.search.substr(1).match(reg)
	if (r != null) return decodeURIComponent(r[2])
	return ""
}

export {
	getLocalStorage,
	setLocalStorage,
	removeLocalStorage,
	getLocationParam,
	debounce,
	throttle
}

export default {
	install(Vue) {
		Object.defineProperties(Vue.prototype, {
			$util: {
				value: {
					getLocalStorage,
					setLocalStorage,
					removeLocalStorage,
					getLocationParam,
					debounce,
					throttle
				}
			}
		})
	}
}
