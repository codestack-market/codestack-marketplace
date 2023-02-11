_("#loginTBarOption").addEventListener("click", (e) => {
    // display menu
    if (!(_("#loginTBarOption").innerHTML.includes('Sign in'))) {
        const popup = _(".popup_accountOptionsPopup")
        if (popup.css("opacity") == "1") {
            popup.css("opacity", "0")
        } else {
            popup.css("opacity", "1")
        }
    }
})

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain'
      },
      body: data
    });
    return response
  }

  _("#searchMarket").addEventListener("keydown", (e) => {
    if (e.keyCode === 13) {
      if (_("#searchMarket").value.replaceAll(" ", "") == "") return;
      window.location = '/marketplace/search?q=' + _("#searchMarket").value;
    } else {
      setTimeout(() => {
        if (_("#searchMarket").value.replaceAll(" ", "") == "") {
          _(".openMarketButton").innerHTML = "Marketplace"
        } else {
          _(".openMarketButton").innerHTML = "Search"
        }
      }, 100)
    }
  })

  _(".openMarketButton").addEventListener("click", (e) => {
    if (!_("#searchMarket").value.replaceAll(" ", "") == "") {
      window.location = '/marketplace/search?q=' + _("#searchMarket").value;
    } else {
      window.location = '/marketplace'
    }
  })
  /*
  postData('/logout', "logout")
    .then((data) => {
      console.log(data);
    });*/