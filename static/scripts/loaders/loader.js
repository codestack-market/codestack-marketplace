// Opacity to 1 for body transition
// _ is prefix for forge query (/static/scripts/utils/forge.js)

document.body.onload = function () {
    document.body.style.opacity = "1";
}

const bc = new BroadcastChannel("cmLogout")
bc.onmessage = (event) => {
    alert(event.data)
    if (event.data == "logoutTrue") {
        window.location = ''
    }
}

window.addEventListener("error", (e) => {
    try {
        if (!document.body.contains(document.querySelector(".errorModal"))) {
            const errorModal = document.createElement("div")
            errorModal.classList.add("errorModal")
            errorModal.classList.add("modalPopup")
            errorModal.innerHTML = `
            <br>
            <span class="modalTitle">An error has occured!</span>
            <br>
            <p class="modalDesc underline" style="color: lightgray;">Error Details</p>
            <p class="modalDesc"><code>${e.message}</code></p>
            <p class="modalDesc"><code>${e.filename.replace("https://codestack.ga", "")||e.filename.replace("http://codestack.ga", "")} (Line ${e.lineno}, col ${e.colno})</code></p>
            <p class="modalDesc" style="position: absolute; bottom: 15%;">Refreshing may help. If this error keeps happening, contact <a href="https://codestack.ga/support" style="color: blue">support</a></p>
            <button class="modalOk" onclick="this.parentElement.style.scale = '0'; document.querySelector('.shade').style.scale = '0'">Ok</button>
        `
            document.body.appendChild(errorModal)
            errorModal.style.scale = "1"
        } else {
            document.querySelector(".errorModal").style.scale = 1;
        }

        if (document.body.contains(document.querySelector(".shade"))) {
            document.querySelector(".shade").style.scale = 1;
        } else {
            const shade = document.createElement("div")
            shade.classList.add("shade")
            document.body.appendChild(shade)
            shade.style.scale = 1;
        }
    }
    catch (err) {
        alert(err)
    }

})

/*

when recieve data of logged in or not

if logged in:
    _("#loginTBarOption").iHtml = username;
    _("#loginTBarOption").onclick = // set into dropbar to view account options
else:
    // keep same data.
*/