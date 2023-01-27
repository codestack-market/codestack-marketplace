if (!document.URL.includes("?id=")) {
    window.location = '/'
} else {
    _(".authContainer").css("display", "block")
}

async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }
  
  postData('/confirmEmailAuth', { id: document.URL.split("?id=")[1] })
    .then((data) => {
      console.dir(data);
    });