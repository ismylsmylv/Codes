   function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "" || password == "") {
      alert("Please enter a username and password.");
      return false;
    }
    if (username != "ceres" || password != "ceres") {
      alert("Incorrect username or password.");
      return false;
    }
    if (username == "ceres" && password == "ceres") {
      window.open("file:///home/ismylsmylv/projects/CodesShared/ismylsmylv/homework/form.html");
      return true;
    }
  }

//file:///home/ismylsmylv/projects/CodesShared/ismylsmylv/homework/form.html
////window.location.href = "https://www.google.com";
//https://ismylsmylv.github.io/