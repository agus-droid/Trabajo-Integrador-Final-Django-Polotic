function showPassword() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
    }

const add = document.getElementById('add')
const remove = document.getElementById('remove')
const quantity = document.getElementById('quantity')
add.addEventListener('click', function(){
    quantity.value = parseInt(quantity.value)+1
})
remove.addEventListener('click', function(){
    value=parseInt(quantity.value)
    if (value!=1){
        value -=1
    }
    quantity.value = value
})