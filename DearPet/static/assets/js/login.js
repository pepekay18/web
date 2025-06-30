var loginurl = "/Ajax/Ajax_Login.ashx";



function Login() {
    var AccountName = $.trim($("#txt_AccountName").val());
    var AccountPassword = $.trim($("#txt_AccountPassword").val());
    var BindLang = $.trim($("#txt_BindLang").val());
    var datastr = "type=UserLogin&AccountName=" + escape(AccountName) + "&AccountPassword=" + escape(AccountPassword) + "&BindLang=" + escape(BindLang);
    ajaxsend(loginurl, datastr, function (data) {
        switch (data.code) {
            case 1: window.location.href = 'LoginSuccess.aspx'; localStorage.setItem('slang', BindLang); break;
            default: Tip(data.msg); break;
        }
    }, "json", true);
}

function SignUp() {
    var Name = $.trim($("#txt_Name").val());
    var AccountName = $.trim($("#txt_AccountName").val());
    var AccountPassword1 = $.trim($("#txt_AccountPassword1").val());
    var BindLang = $.trim($("#txt_BindLang").val());
    //var AccountPassword2 = $.trim($("#txt_AccountPassword2").val());

    var Verify = $.trim($("#txt_Verify").val());
    if (Verify == "") {
        TipsForm("Please enter the verification code.", "txt_Verify", 3); return;
    }
    if (!CheckEmail(AccountName)) {
        TipsForm("Please enter a right email address.", "txt_AccountName", 3); return;
    }

    //if (AccountPassword1 != AccountPassword2) {
    //    Tip("Please enter same password twice."); return;
    //}
    if (AccountPassword1.length < 6) {
        Tip("The password length cannot be less than 6 bits."); return;
    }
    var datastr = "type=UserSignUp&AccountName=" + escape(AccountName) + "&AccountPassword=" + escape(AccountPassword1) + "&Name=" + escape(Name) + "&Verify=" + escape(Verify) + "&BindLang=" + escape(BindLang);
    ajaxsend(loginurl, datastr, function (data) {
        switch (data.code) {
            case 1: window.location.href = 'LoginSuccess.aspx'; break;
            default: Tip(data.msg); break;
        }
    }, "json", true);
}

function InfoAdd() {
    var AccountName = $.trim($("#txt_AccountName").val());
    var Verify = $.trim($("#txt_Verify").val());
    if (Verify == "") {
        TipsForm("Please enter the verification code.", "txt_Verify", 3); return;
    }

    var datastr = "type=InfoAdd&AccountName=" + escape(AccountName) + "&Verify=" + escape(Verify);
    ajaxsend(loginurl, datastr, function (data) {
        switch (data.code) {
            case 1: TipGoto(data.msg, "LoginSuccess.aspx"); break;
            default: Tip(data.msg); break;
        }
    }, "json", true);
}

function ResetPass() {
    var AccountName = $.trim($("#txt_AccountName").val());
    var AccountPassword1 = $.trim($("#txt_AccountPassword1").val());
    //var AccountPassword2 = $.trim($("#txt_AccountPassword2").val());
    var Verify = $.trim($("#txt_Verify").val());

    if (!CheckEmail(AccountName)) {
        TipsForm("Please enter a right email address.", "txt_AccountName", 3); return;
    }
    if (6 > AccountPassword1.length || AccountPassword1.length > 20) {
        TipsForm("The password length cannot be less than 6 bits.", "txt_AccountPassword1", 3); return;
    }
    //if (AccountPassword1 != AccountPassword2) {
    //    Tip("Please enter same password twice."); return;
    //}
    if (Verify == "") {
        TipsForm("Please enter the verification code.", "txt_Verify", 3); return;
    }

    var datastr = "type=ResetPass&AccountName=" + escape(AccountName) + "&AccountPassword=" + escape(AccountPassword1) + "&Verify=" + escape(Verify);
    ajaxsend(loginurl, datastr, function (data) {
        ajaxback(data);
        if (data.code == 1) {
            TipGoto(data.msg, "Login.aspx");
        }
        else {
            Tip(data.msg);
        }
    }, "json", true);
}
