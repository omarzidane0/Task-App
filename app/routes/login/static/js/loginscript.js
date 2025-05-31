  const form = document.getElementById("login")
  const username = document.getElementById("username")
  const password = document.getElementById("password")
  const errmsg = document.getElementById("errMsg")

  form.addEventListener("submit" , function(event){
    if(username.value.trim() === "" || password.value.trim() === ""){
    event.preventDefault();
    errmsg.textContent = "Please fill all the fields"
  }
  })