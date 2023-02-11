function hideModal() {
    console.log(_(".modalOk").disabled)
    if (_(".modalOk").disabled == true) return;
    _(".modalPopup").css("scale", "0")
    _(".shade").css("scale", "0")
}

function validateEmail(email) {
    return new RegExp(/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i)
        .test(
            String(email)
                .toLowerCase()
        )
}

function validatePhone(phone) {
    return new RegExp(/^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/)
        .test(
            String(phone)
                .toLocaleLowerCase()
        )
}