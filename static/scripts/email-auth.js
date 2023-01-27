if (!document.URL.includes("?id=")) {
    window.location = '/'
} else {
    _(".authContainer").css("display", "block")
}