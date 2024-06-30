let d_name = document.getElementById("name-show")
let d_age = document.getElementById("age-show")
let d_gender = document.getElementById("gender-show")
let d_type = document.getElementById("type-show")
let d_detail = document.getElementById("detail")
let d_image = document.getElementById("image")

let full_name = document.getElementById("name")
let image = document.getElementById("person")
let age = document.getElementById("age")
let male = document.getElementById("male")
let female = document.getElementById("female")
let other = document.getElementById("other")
let type = document.getElementById("type")
let info = document.getElementById("info")

let error = document.getElementById("error")



d_type.querySelector("span").innerHTML = type.value;


full_name.addEventListener("change",()=>{
    d_name.querySelector("span").innerHTML=full_name.value
})
age.addEventListener("change",()=>{
    d_age.querySelector("span").innerHTML=age.value
})
info.addEventListener("change",()=>{
    d_detail.innerHTML=info.value
})
image.addEventListener("change",(event)=>{
    d_image.querySelector("img").src= URL.createObjectURL(event.target.files[0])
})

male.addEventListener("click",()=>{
    d_gender.querySelector("span").innerHTML = "Male"
})
female.addEventListener("click",()=>{
    d_gender.querySelector("span").innerHTML = "Female"
})
other.addEventListener("click",()=>{
    d_gender.querySelector("span").innerHTML = "Other"
})

error.style.display="none"
function validate(){
    if (image.value =="" || image.value.length<=0 || image.value==null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please upload the image of the person </li>"
        return false
    }
    if (full_name.value =="" || full_name.value.length<=0 || full_name.value==null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter Full Name of the person </li>"
        return false
    }
    if (age.value =="" || age.value.length<=0 || age.value==null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter Age of the person </li>"
        return false
    }
    if(!male.checked && !female.checked && !other.checked){
        error.style.display = "block"
        error.innerHTML = "<li> Please select the gender of the person </li>"
        return false
        
    }
    if (info.value =="" || info.value.length<=0 || info.value==null) {
        error.style.display = "block"
        error.innerHTML = "<li> Please enter the detail description of the person </li>"
        return false
    }
}


