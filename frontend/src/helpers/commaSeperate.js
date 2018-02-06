export default (number=0) => {
	let s = number.toString()
	let len = s.length
	if(len === 1) {
		s = `0,0${s}`
	} else if (len === 2) {
		s = `0,${s}`
	} else {
		len -= 2
		s = s.slice(0, len) + ',' + s.slice(len, s.length)
		// Using a C style hack to update the variable in the while body
		while ((len -= 3) > 0) {
			s = s.slice(0, len) + '.' + s.slice(len, s.length)
		}
	}
	return s;
}