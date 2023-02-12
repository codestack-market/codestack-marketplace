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

  var loading = false;
  _("#searchMarket").addEventListener("keydown", (e) => {
    if (loading) return e.preventDefault();
    if (e.keyCode === 13) {
      if (_("#searchMarket").value.replaceAll(" ", "") == "") return;
      loading = true;
      _(".openMarketButton").innerHTML = "<img src='/static/assets/loader-spinning.gif' height='25px' width='35px' style='vertical-align: middle'> Searching..."
      _(".openMarketButton").attribute("disabled", "true")
      setTimeout(() => window.location = '/marketplace/search?q=' + _("#searchMarket").value, getRand(500, 1100))
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
    if (loading) return e.preventDefault();
    if (!_("#searchMarket").value.replaceAll(" ", "") == "") {
      loading = true
      _(".openMarketButton").attribute("disabled", "true")
      _(".openMarketButton").innerHTML = "<img src='/static/assets/loader-spinning.gif' height='25px' width='35px' style='vertical-align: middle'> Searching..."
      setTimeout(() => window.location = '/marketplace/search?q=' + _("#searchMarket").value, getRand(500, 1100))
      } else {
      window.location = '/marketplace'
    }
  })
  /*
  postData('/logout', "logout")
    .then((data) => {
      console.log(data);
    });*/