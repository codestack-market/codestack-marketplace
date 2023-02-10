if (document.URL.includes("?edit=")) {
    const mode = document.URL.split("?edit=")[1];
    console.log(mode);
    _("#edit-" + mode).show();
} else {
    _(".container").show();
}