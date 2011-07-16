function test() {
	return "Hello";
}

function setvalue(id) {
	var objCtrl = document.getElementById(id);
	var obj = document.getElementById('voted');
	try {
		obj.Text = objCtrl.value;
	} catch (e) {
		alert(e);
	}
}

var myMsg = [ 'info', 'error', 'warning', 'success' ];
function hideAllMessage() {
	var msgHeight = new Array();

	for ( var i = 0; i < myMsg.length; i++) {
		msgHeight[i] = $('.' + myMsg[i]).outerHeight(); // fill array
		$('.' + myMsg[i]).css('top', -messagesHeights[i]); // move element outside viewport
	}
}

function showMessage(type) {
	$('.' + type + '-trigger').click(function() {
		hideAllMessages();
		$('.' + type).animate({
			top : "0"
		}, 500);
	});
}

$(document).ready(function() {
	hideAllMessage();
	
	for(var i=0;i<myMsg.length;i++)
    {
       showMessage(myMsg[i]);
    }
	alert("aa");
	$('.message').click(function(){
        $(this).animate({top: -$(this).outerHeight()}, 500);
	});
});