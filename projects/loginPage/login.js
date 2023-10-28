function login(){
    var username=document.getElementByID("user").value;
    var password=document.getElementByID("pass").value;

    if (username =='' || password ==''){
        alert("enter username or password");
        return false;
    }
    if (username =='pass' && password=='user'){
        window.open("file://C:/Users/User/Desktop/ismylsmylv/codes/sites/loginPage/login.css");
        return true;
    }
    if (username=='pass' || password=='user'){
        alert('login incorrect');
        return false;
    }
}