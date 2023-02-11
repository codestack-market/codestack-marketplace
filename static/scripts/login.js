try {
    _("#email_input").addEventListener("keydown", (e) => {
        const keycode = e.keyCode;
        if (keycode == 13) {
            var email = _("#email_input").value;
            const valid = validateEmail(email);
            _("#modal_erroremail").css("scale", "1")
            _(".shade").css("scale", "1")
            if (valid) {
                _(".modalTitle").iText("Sending to server...")
                _(".modalDesc").iText("Please wait a moment...")
                _(".modalOk").setAttribute("disabled", true)
                postData("/soon", { email: email })
                    .then((data) => {
                        console.dir(data);
                        _(".modalTitle").iText("Email submitted")
                        _(".modalDesc").iText("Thank you for giving us your email! We look forward to seeing you use codestack in the future!")
                        email = ''
                        _(".modalOk").removeAttribute("disabled")
                    })
                    .catch(err => {
                        _(".modalTitle").iText("An error has occured")
                        _(".modalDesc").iHtml("<span style='font-family: monospace; font-size: 13px;'>" + err + "</span>")
                        console.error(err);
                        _(".modalOk").removeAttribute("disabled")
                    })
            } else {
                _(".modalTitle").iText("Invalid email")
                _(".modalDesc").iText("The inputted email is invalid. Please try agian.")
                email = ''
            }
        }
    })

    _("#applyEmailBtn").addEventListener("click", (e) => {
        var email = _("#email_input").value;
        const valid = validateEmail(email);
        _("#modal_erroremail").css("scale", "1")
        _(".shade").css("scale", "1")
        if (valid) {
            _(".modalTitle").iText("Sending to server...")
            _(".modalDesc").iText("Please wait a moment...")
            _(".modalOk").setAttribute("disabled", true)
            postData("/soon", { email: email })
                .then((data) => {
                    console.dir(data);
                    _(".modalTitle").iText("Email submitted")
                    _(".modalDesc").iText("Thank you for giving us your email! We look forward to seeing you use codestack in the future!")
                    email = ''
                    _(".modalOk").removeAttribute("disabled")
                })
                .catch(err => {
                    _(".modalTitle").iText("An error has occured")
                    _(".modalDesc").iHtml("<span style='font-family: monospace; font-size: 13px;'>" + err + "</span>")
                    console.error(err);
                    _(".modalOk").removeAttribute("disabled")
                })
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

    async function postData(url = '', data = {}) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return response.json();
    }
} catch (err) {
    console.error(err)
}
