_("#loginTBarOption").addEventListener("click", (e) => {
    // display menu
    const popup = _(".popup_accountOptionsPopup")
    if (popup.css("opacity") == "1") {
        popup.css("opacity", "0")
    } else {
        popup.css("opacity", "1")
    }
})