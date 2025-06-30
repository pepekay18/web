$(document).ready(function() {

	var bodyheight = $(window).height();
	$(".leftcontrol").css("height", bodyheight + "px");

	$(window).scroll(function() {
		var top = $(window).scrollTop();
		if (top > 0) {
			$('.logoheader').addClass("active");
		} else {
			$('.logoheader').removeClass("active");
		}
	});
	$(".showpass").click(function () {
		var input = $(this).parent().parent().find("input");
		if ($(input).attr('type') == 'password') {
			$(input).attr('type', 'text')
		} else {
			$(input).attr('type', 'password')

		}
	})

});

$(window).resize(function() {
	var bodyheight = $(window).height();
	$(".leftcontrol").css("height", bodyheight + "px");
});

function openlogoheader() {
	$(".leftcontrol").toggleClass("open");
	$(".leftcontrolbg").toggleClass("hidden");
}

// if ( !( /msie [6|7|8|9]/i.test( navigator.userAgent ) ) ) {
// new WOW().init();
// };

var posturl = "/Ajax/Ajax_Tag.ashx";
function Post(data,operate,method) {
	ajaxsending(posturl, data+"&type="+operate, method, 'json', true);
}

var DefaultTitle = "";
function Tip(msg, title) {
	if (!title) { title = DefaultTitle; }
	$.modal({
		title: title,
		text: msg,
		buttons: [
			{ text: "OK", className: "comfirm" ,onClick: function () { } },
		]
	});

}

function TipGoto(msg, url, title) {
	if (!title) { title = DefaultTitle; }
	$.modal({
		title: title,
		text: msg,
		buttons: [
			{ text: "OK", className: "comfirm", onClick: function () { window.location.href = url; } },
		]
	});
}
function TipConfirm(msg,methon, title) {
	if (!title) { title = DefaultTitle; }
	$.modal({
		title: title,
		text: msg,
		buttons: [
			{ text: "Cancel", className: "default" },
			{ text: "OK", className: "comfirm", onClick: methon },
		]
	});
}
function TipRefresh(msg, title) {
	if (!title) { title = DefaultTitle; }
	$.modal({
		title: title,
		text: msg,
		buttons: [
			{ text: "OK", className: "comfirm", onClick: function () { window.location.reload(); } },
		]
	});
}
function TipBack(msg, title) {
	if (!title) { title = DefaultTitle; }
	$.modal({
		title: title,
		text: msg,
		buttons: [
			{ text: "OK", className: "comfirm", onClick: function () { window.history.back(); } },
		]
	});
}
function LoginCheck(data) {
	if (data.code == -99) {
		TipGoto(data.msg, data.key);
	}
}
