const button = document.getElementById('button')

function validate(email) {
    if (email != '') {
        if(email.match(/^[^@]+@[\w\.]{2,10}\.[\w]{2,5}$/i)) {
            button.disabled = false
            button.classList.remove('disabled')
            return
        }
        button.disabled = true
        button.classList.add('disabled')
    }
}

function correct() {
    swal({
        title: 'Congratulations!',
        text: 'This is a correct Email',
        icon: 'success',
        button: {
            visible: false
        }
    })
}