function test() {
	return "Hello";
}

function setvalue(id) {
	var objCtrl = document.getElementById(id)
	var obj = document.getElementById('voted')
	try {
		obj.Text = objCtrl.value
	} catch (e) {
		alert(e)
	}
	
}