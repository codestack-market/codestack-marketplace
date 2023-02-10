// Opacity to 1 for body transition
// _ is prefix for forge query (/static/scripts/utils/forge.js)

document.body.onload = function() {
    document.body.style.opacity = "1";
}

const bc = new BroadcastChannel("cmLogout")
bc.onmessage = (event) => {
    alert(event.data)
    if (event.data == "logoutTrue") {
        window.location = ''
    }
}

/*

when recieve data of logged in or not

if logged in:
    _("#loginTBarOption").iHtml = username;
    _("#loginTBarOption").onclick = // set into dropbar to view account options
else:
    // keep same data.
*/