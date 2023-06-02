document.addEventListener("keydown", (event)=>{
    let input_cidade = $("#cidade")[0]
    if (event.key == "Enter") {
        location.replace("http://192.168.1.2:8080/"+input_cidade.value)
    }
})