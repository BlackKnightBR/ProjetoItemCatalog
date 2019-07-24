var email =  $("#userEmail").html();
var loginTab = $('#loginTab').detach();
var glogout = $('#Glogout').detach();
var dbLogout = $('#DBlogout').detach();
var dbLogin = $('#DBlogin').detach();
var signUp = $('#SignUp').detach();

function start() {
  if(email !== "Log in!"){
    $('#DBlogin').detach();
    $('#SignUp').detach();
    $('#loginTab').detach();
    $('#Glogout').detach();
    $('#buttons').prepend(dbLogout);
  } else {
    $('#buttons').prepend(signUp);
    $('#buttons').prepend("<br>");
    $('#buttons').prepend(dbLogin);
  }
}

function loginTabShow(){
  $('#buttons').prepend(loginTab);
  $('#DBlogin').detach();
  $('#SignUp').detach();
}

function buttonHide(){
  $('#loginTab').detach();
  $('#buttons').prepend(signUp);
  $('#buttons').prepend("<br>");
  $('#buttons').prepend(dbLogin);
}

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  var mail = profile.getEmail();
  $('#buttons').append(glogout);
  $('#SignUp').detach();
  $('#DBlogin').detach();
  $('#userGoogle').text(mail);
  $("#userEmail").html('');
  $.ajax({
    type: 'POST',
    url: '/gconnect',
    data: {mail:mail},
  });
  logedIn = true;
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
  });
  $('#Glogout').detach();
  $('#buttons').prepend(signUp);
  $('#buttons').prepend("<br>");
  $('#buttons').prepend(dbLogin);
  $('#userGoogle').text('');

}

start();
