let password = document.querySelector('#password');
let password_visible = document.querySelector('#password_visible')

// let text = document.querySelector('#text')
// console.log(text.type)

password_visible.addEventListener("click" , function(){
    if(password.type == "password"){
        password.type = "text";
        // console.log(password_visible.src)
        password_visible.src = "static/media/off.svg";
        // console.log(password_visible.src)
        
    }
    else{
        password.type = "password";
        // console.log(password_visible.src)
        password_visible.src = "static/media/on.svg";
        // console.log(password_visible.src)

    }
});

