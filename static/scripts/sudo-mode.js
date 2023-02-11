var redirect = document.URL.split("?redirect=")[1] || "/"

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

_("#passwordInput").addEventListener("keydown", (e) => {
    if (e.keyCode == 13) submit();
})

_(".confirm").addEventListener("click", submit);

function submit() {
    console.log("csudo")
    postData("/csudo", { password: _("#passwordInput").value })
        .then(data => {
            console.dir(data);
            setTimeout(() => window.location = redirect, 1000)
        })
}