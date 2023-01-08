try {
    _("#email_input").addEventListener("keydown", (e) => {
        const keycode = e.keyCode;
        if (keycode == 13) {
            const email = _("#email_input").value;
            const valid = validateEmail(email);
            _("#modal_erroremail").css("scale", "1")
            _(".shade").css("scale", "1")
            if (valid) {
                _(".modalTitle").iText("Email submitted")
                _(".modalDesc").iText("Thank you for giving us your email! We look forward to seeing you use codestack in the future!")
                email = ''
            } else {
                _(".modalTitle").iText("Invalid email")
                _(".modalDesc").iText("The inputted email is invalid. Please try agian.")
                email = ''
            }
        }
    })

    _("#applyEmailBtn").addEventListener("click", (e) => {
        const email = _("#email_input").value;
        const valid = validateEmail(email);
        _("#modal_erroremail").css("scale", "1")
        _(".shade").css("scale", "1")
        if (valid) {
            _(".modalTitle").iText("Email submitted")
            _(".modalDesc").iText("Thank you for giving us your email! We look forward to seeing you use codestack in the future!")
            email = ''
        } else {
            _(".modalTitle").iText("Invalid email")
            _(".modalDesc").iText("The inputted email is invalid. Please try again.")
            email = ''
        }
    })

    function validateEmail(email) {
        return new RegExp(/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i)
            .test(
                String(email)
                    .toLowerCase()
            )
    }


} catch (err) {
    alert(err)
}
