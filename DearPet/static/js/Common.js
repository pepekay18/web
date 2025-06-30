//=================================
// 商城通用Js
//=================================


/*#region ==========页面初始化加载==========*/
//默认方法
function l(val) { return val; }

//加载layer自定义样式
$(function () {
    layer.config({
        extend: 'ios/layer.css',
        skin: 'layer-ext-ios',
    });
})

//动态加载js和css文件
var LoadExtentFile = {
    css: function (path) {
        if (!path || path.length === 0) {
            throw new Error('');
        }
        var head = document.getElementsByTagName('head')[0];
        var link = document.createElement('link');
        link.href = path;
        link.rel = 'stylesheet';
        link.type = 'text/css';
        head.appendChild(link);
    },
    js: function (path) {
        if (!path || path.length === 0) {
            throw new Error('');
        }
        var head = document.getElementsByTagName('head')[0];
        var script = document.createElement('script');
        script.src = path;
        script.type = 'text/javascript';
        head.appendChild(script);
    }
}

////加载提示插件
//LoadExtentFile.js("/scripts/layer/Common.js");
//LoadExtentFile.css("/scripts/weui/weui.css");
//LoadExtentFile.js("/scripts/weui/weui.min.js");
/*#endregion */


/*#region ==========公共方法==========*/
//切换验证码
function SwitchCode() {
    $("#verifyCode").children("img").eq(0).attr("src", "/Ajax/verify_code.ashx?time=" + Math.random());
    return false;
}

//切换验证码
function ToggleCode(obj, codeurl) {
    $(obj).children("img").eq(0).attr("src", codeurl + "?time=" + Math.random());
    return false;
}

//读取单选按钮选中的值
function getradio(radio) {
    var outstr = "";
    $("input[name='" + radio + "']:checked").each(function () {
        outstr = this.value;
    });
    return outstr;
}

//获取checkboxlist的值
function getcheckbox(name) {
    var outstr = "";
    $("input[name='" + name + "']:checked").each(function () {
        outstr += this.value + ",";
    });
    if (outstr != "") {
        outstr = "," + outstr;
    }
    return outstr;
}

//获取页面名称
function PageName() {
    var a = location.href;
    var b = a.split("/");
    var c = b.slice(b.length - 1, b.length).toString(String).split(".");
    return c.slice(0, 1);
}

//读取链接后面的参数
function GetQS(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return "";
}

//导航切换，一般用在li【ID，点击元素this，导航选中样式，盒子样式】
function TabSwitch(navid, clickele, clickclass, boxcss) {
    $(clickele).parent().children().removeClass(clickclass);
    $(clickele).addClass(clickclass);
    $("." + boxcss).addClass("hidden");
    $("#" + boxcss + navid).removeClass("hidden");
}

//显示隐藏分享提示
function wxshare(id) {
    if ($("#" + id).hasClass("hidden")) {
        $("#" + id).removeClass("hidden");
    }
    else {
        $("#" + id).addClass("hidden");
    }
}

//显示隐藏元素
function ShowHide(id) {
    if ($(id).hasClass("hidden")) {
        $(id).removeClass("hidden");
    }
    else {
        $(id).addClass("hidden");
    }
}
/*#endregion */


/*#region ==========ajax方法==========*/
//ajax执行状态
var ajaxing = 0;

//通用ajax基础方法
function ajaxpost(type, ajaxstr, posturl) {
    if (ajaxing != 0) {
        return "-100";
    }
    var datastr = "type=" + type + "&" + ajaxstr;
    var outstr = "-99"; //不想提示数据变化就改了
    $.ajax({
        async: false,
        type: "POST",
        dataType: "text",
        url: posturl,
        data: datastr,
        beforeSend: function (data) { ajaxing = 1; },
        success: function (data) {
            ajaxing = 0; outstr = data;
        },
        error: function (data) {
            ajaxing = 0; outstr = "-99"; //不想提示数据变化就改了
        }
    });
    return outstr;
}

//通用ajax基础方法
function ajaxsend(posturl, datastr, method, datatype, isload) {
    if (posturl == '') { posturl = window.location.href; }
    if (ajaxing != 0) { return; }
    if (datatype != "json" && datatype != "text") { datatype = "text"; }
    $.ajax({
        type: "POST", dataType: datatype,
        url: posturl, data: datastr,
        beforeSend: function (data) {
            if (isload) {
                layer.load(2, { shade: false, time: 30000 });
            }
            ajaxing = 1;
        },
        success: function (data) {
            layer.closeAll('loading');
            ajaxing = 0;
            method(data);
        },
        error: function (data) {
            layer.closeAll('loading');
            ajaxing = 0;
            //Tip("Network error,please check your network connection.")
            console.log('Error：</br>' + JSON.stringify(data));
        }
    });
}

//通用ajax基础方法
function ajaxsending(posturl, datastr, method, datatype, isload) {
    if (posturl == '') { posturl = window.location.href; }
    if (datatype != "json" && datatype != "text") { datatype = "text"; }
    $.ajax({
        type: "POST", dataType: datatype,
        url: posturl, data: datastr,
        beforeSend: function (data) {
            if (isload) {
                layer.load(2, { shade: false, time: 30000 });
            }
        },
        success: function (data) {
            layer.closeAll('loading');
            method(data);
        },
        error: function (data) {
            layer.closeAll('loading');
            //Tip("Network error,please check your network connection.")

            console.log('Error：</br>' + JSON.stringify(data));
        }
    });
}

//展示ajax
function AjaxWeb(type, ajaxstr) {
    return ajaxpost(type, ajaxstr, "/Ajax/Ajax_Web.ashx");
}
/*#endregion */


/*#region ==========设备判断==========*/
//手机检测跳转
function CheckMobileLink() {
    if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios)/i))) {
        top.location = '/WeixinShop/index.html';
    }
}

//PC端检测跳转
function CheckPcLink() {
    if (!(navigator.userAgent.match(/(iPhone|iPod|Android|ios)/i))) {
        top.location = '/index.html';
    }
}

//判断是否手机端
function IsFromMobile() {
    if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios)/i))) {
        return true;
    }
    else {
        return false;
    }
}

//判断是否微信
function IsFromWeiXin() {
    var ua = window.navigator.userAgent.toLowerCase();
    if (ua.match(/MicroMessenger/i) == 'micromessenger') {
        return true;
    }
    else {
        return false;
    }
}

//是否ie浏览器
function IsIE() {
    if (!!window.ActiveXObject || "ActiveXObject" in window) return true;
    else return false;
}
/*#endregion */


/*#region ==========cookie方法==========*/
//写入cookie，按分钟
function SetTimeCookie(name, value, minute) {
    var exp = new Date();
    exp.setTime(exp.getTime() + minute * 60 * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
}
//写入cookie
function SetCookie(name, value) {
    var Days = 1;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
}
//写入cookie
function SetCookieSecond(name, value, Second) {
    var exp = new Date();
    exp.setTime(exp.getTime() + Second * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
}
///删除cookie
function DelCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = GetCookie(name);
    if (cval != null) document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}
//读取cookie
function GetCookie(name) {
    var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
    if (arr != null)
        return unescape(arr[2]);
    return null;
}
/*#endregion */


/*#region ==========数据转换==========*/
//转换为数字，否则返回默认值
function StrToInt(expression, defvalue) {
    if (expression == null || expression == "") {
        return defvalue;
    }
    var rtn = parseInt(expression.toString());
    if (isNaN(rtn)) {
        return defvalue;
    }
    return rtn;
}

//转换为数字，否则返回默认值
function StrToFloat(expression, defvalue) {
    if (expression == null || expression == "") {
        return defvalue;
    }
    var rtn = parseFloat(expression.toString());
    if (isNaN(rtn)) {
        return defvalue;
    }
    return parseFloat(rtn.toFixed(2));
}
/*#endregion */


/*#region ==========验证方式==========*/
//判断是否有汉字
function CheckChinese(str) {
    if (escape(str).indexOf("%u") < 0) { return true; }
    else { return false; }
}

//判断账号名格式
function CheckAccount(str) {
    var myregstr = /^([a-zA-Z]|[a-zA-Z0-9]|[._]){6,20}$/;
    if (!myregstr.test(str)) { return false; }
    else { return true; }
}

//判断邮箱
function CheckEmail(str) {
    //var myregstr = /^([a-zA-Z0-9]+[_|\_|\.|\-]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    //             /^([a-zA-Z0-9]+[_|\_|\.|\-]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    //var myregstr = /^([a-zA-Z0-9]+[_|\_|\.|\-]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.|\-]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    var myregstr = /^([a-zA-Z0-9]+[_|\_|\.|\-]?)*[a-zA-Z0-9+._-]+@([a-zA-Z0-9]+[_|\_|\.|\-]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,5}$/;
    if (!myregstr.test(str)) { return false; }
    else { return true; }
}

//判断手机
function CheckMobile(str) {
    var myregstr = /^(10[0-9]|11[0-9]|12[0-9]|13[0-9]|14[0-9]|15[0-9]|16[0-9]|17[0-9]|18[0-9]|19[0-9])\d{8}$/;
    myregstr = /^\d{6,11}$/;
    if (!myregstr.test(str)) { return false; }
    else { return true; }
}

//判断固话
function CheckPhone(str) {
    var myregstr = /^([0-9]{3,4}-)?[0-9]{7,8}$/;
    if (!myregstr.test(str)) { return false; }
    else { return true; }
}

//验证身份证号码
function CheckIdentity(num) {
    num = num.toUpperCase();
    if (!(/(^\d{15}$)|(^\d{17}([0-9]|X)$)/.test(num))) {
        return false;
    }
    var len, re;
    len = num.length;
    if (len == 15) {
        re = new RegExp(/^(\d{6})(\d{2})(\d{2})(\d{2})(\d{3})$/);
        var arrSplit = num.match(re);
        var dtmBirth = new Date('19' + arrSplit[2] + '/' + arrSplit[3] + '/' + arrSplit[4]);
        var bGoodDay;
        bGoodDay = (dtmBirth.getYear() == Number(arrSplit[2])) && ((dtmBirth.getMonth() + 1) == Number(arrSplit[3])) && (dtmBirth.getDate() == Number(arrSplit[4]));
        if (!bGoodDay) {
            return false;
        }
        else {
            var arrInt = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
            var arrCh = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
            var nTemp = 0, i;
            num = num.substr(0, 6) + '19' + num.substr(6, num.length - 6);
            for (i = 0; i < 17; i++) {
                nTemp += num.substr(i, 1) * arrInt[i];
            }
            num += arrCh[nTemp % 11];
            return true;
        }
    }
    if (len == 18) {
        re = new RegExp(/^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$/);
        var arrSplit = num.match(re);
        var dtmBirth = new Date(arrSplit[2] + "/" + arrSplit[3] + "/" + arrSplit[4]);
        var bGoodDay;
        bGoodDay = (dtmBirth.getFullYear() == Number(arrSplit[2])) && ((dtmBirth.getMonth() + 1) == Number(arrSplit[3])) && (dtmBirth.getDate() == Number(arrSplit[4]));
        if (!bGoodDay) {
            return false;
        }
        else {
            var valnum;
            var arrInt = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
            var arrCh = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
            var nTemp = 0, i;
            for (i = 0; i < 17; i++) {
                nTemp += num.substr(i, 1) * arrInt[i];
            }
            valnum = arrCh[nTemp % 11];
            if (valnum != num.substr(17, 1)) {
                return false;
            }
            return true;
        }
    }
    return false;
}
/*#endregion */


/*#region ==========收藏首页==========*/
//添加收藏
function AddFavorite(url, title) {
    try { window.external.addFavorite(url, title); }
    catch (e) {
        try { window.sidebar.addPanel(title, url, ""); }
        catch (e) { alert("加入收藏失败，请使用Ctrl+D进行添加"); }
    }
}

//设为首页 <a onclick="SetHome(this,window.location)">设为首页</a>
function SetHome(obj, vrl) {
    try {
        obj.style.behavior = 'url(#default#homepage)'; obj.setHomePage(vrl);
    }
    catch (e) {
        if (window.netscape) {
            try {
                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
            }
            catch (e) {
                alert("此操作被浏览器拒绝！\n请在浏览器地址栏输入“about:config”并回车\n然后将 [signed.applets.codebase_principal_support]的值设置为'true',双击即可。");
            }
            var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);
            prefs.setCharPref('browser.startup.homepage', vrl);
        }
    }
}
/*#endregion */


/*#region ========== 提示框 ==========*/
var layertitle = "提示";
var layerbtn1 = "确定";
var layerbtn2 = "关闭";

//常用提示
function Tips(conts, title) {
    conts = l(conts);
    if (conts.length < 100)
        layer.msg(conts);
    else {
        if (!title) { title = layertitle; }
        layer.alert(conts, { title: title, btn: [layerbtn1], btnAlign: 'c', shade: 0.1, shadeClose: true });
    }
}
//提示图片
function TipsImg(conts, imgurl) {
    conts = l(conts);
    var imgjson = {
        "title": conts, "id": 123, "start": 0,
        "data": [
            { "alt": conts, "pid": 111, "src": imgurl, "thumb": imgurl }
        ]
    }
    layer.photos({ photos: imgjson, anim: 5 });
}


//提示确定跳转，父页面跳转
function TipsLink(conts, url, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        end: function () { window.parent.location.href = url; }
    });
}
//提示确定跳转，本页面跳转
function TipsGoto(conts, url, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        end: function () { window.location.href = url; }
    });
}
//提示确定刷新父页面
function TipsReload(conts, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        end: function () { window.parent.location.reload(); }
    });
}
//提示确定刷新本页面
function TipsRefresh(conts, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        end: function () { window.location.reload(); }
    });
}
//提示确定返回上页面
function TipsBack(conts, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        end: function () { window.history.back(); }
    });
}


//提交确认提示
function TipsPostBack(btnid, conts, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        yes: function (index, layero) {
            __doPostBack(btnid, '');
            layer.close(index);
        },
        btn2: function (index, layero) { }
    });
    return false;
}
//确认执行方法
function TipsConfirm(conts, method, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1, layerbtn2], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        yes: function (index, layero) {
            method();
            layer.close(index);
        },
        btn2: function (index, layero) { }
    });
    return false;
}
//表单小提示
function TipsForm(conts, objId, fangx) {
    conts = l(conts);
    if (fangx == null || fangx == "") {
        fangx = 3;
    }
    layer.tips(conts, '#' + objId, { tips: [fangx, '#FF5722'], time: 5000 });
    $("#" + objId).focus();
}


//提示确定关闭框架
function TipsClose(conts, title) {
    conts = l(conts);
    if (!title) { title = layertitle; }
    layer.msg(conts, {
        time: 30000, btn: [layerbtn1], btnAlign: 'c', shade: 0.1, shadeClose: true, title: title,
        end: function () { CloseFrame(); }
    });
}
//关闭一个窗口
function CloseFrame() {
    var index = parent.layer.getFrameIndex(window.name);
    parent.layer.close(index);
}
/*#endregion */


/*#region ==========商城常用==========*/
//登录检测
function ajaxback(data) {
    if (data.code == -99) {
        window.location.href = data.key;
    }
}

//$(document).ready(function () {
//    修复ios软键盘弹出造成点击事件失效
//    var isreset = true;
//    var u = navigator.userAgent;
//    var isios = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);
//    function scrolltop() {
//        console.log("scrolltop");
//        isreset = true;
//        setTimeout(function () {
//            if (isreset) {
//                window.scrollTo(0, 0);
//            }
//        }, 300);
//    }
//    if (isios) {
//        console.log("isios");
//        document.body.addEventListener('focusin', function () {
//            isreset = false;
//        });
//        document.body.addEventListener('focusout', scrolltop);
//    }
//});
/*#endregion */