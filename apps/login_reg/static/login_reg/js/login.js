function onSuccess(googleUser) {
    var csrftoken = Cookies.get('csrftoken');

    var profile = googleUser.getBasicProfile();
    var userName = profile.getName();
    console.log(userName);
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    $.ajax("http://localhost:8000/login/sign_in_user/", {
        type : 'POST',
        data : {'google' : userName},
        success: function () {
            window.location.href = "http://localhost:8000/home/";
        }
    })
}
function onFailure(error) {
    console.log(error);
}
function renderButton() {
    gapi.signin2.render('my-signin2', {
        'scope': 'profile email',
        'width': 238,
        'height': 41,
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
    });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}






