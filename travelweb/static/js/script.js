user = {
  userName : "rbrasil",
  password : "dr12wex1"
}

imagens = {
  success : "https://assets-global.website-files.com/5fca17506a3949d6fbceff20/5fca2a81b4c3b34e11f0730b_gavin_01.png",
  danied : "https://www.pngkey.com/png/full/448-4483798_download-icon-user-png-clipart-computer-icons-user.png"
}

function Login(){
  var userImg = document.getElementById('gavi');
  var welcome = document.getElementById('welcome');
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  if(username == user.userName && password == user.password){
    welcome.innerText = user.userName;
    welcome.style.color = "green";
    userImg.src = imagens.success;
  }else{
   welcome.innerText = "ALgo deu errado"
   welcome.style.color = "red";
    userImg.src = imagens.danied;
  }
}

var login = document.getElementById("login").addEventListener('click', Login);