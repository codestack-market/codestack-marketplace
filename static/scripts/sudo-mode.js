async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
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
        })
}