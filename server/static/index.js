document.addEventListener("keydown", (event)=>{
    let input_cidade = $("#cidade")[0]
    if (event.key == "Enter" && input_cidade.value.length > 3) {
        location.replace(`http://${window.location.hostname}:${window.location.port}/${input_cidade.value}`)
    }
})