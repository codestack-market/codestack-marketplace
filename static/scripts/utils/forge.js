var url = window.location;
try {
  function _(query, all) {
    if (all) {
      if (query.startsWith("#") || query.startsWith(".")) {
        return document.querySelectorAll(query);
      }
      return false;
    }
    else if (!all || all == null) {
      if (query.startsWith("#") || query.startsWith(".")) {
        return document.querySelector(query);
      }
      else {
        return false;
      }
    }
  }

  function getRand(min, max) {
    return Math.random() * (max - min) + min;
  }

  function reload() {
    window.location = ''
  }

  function getLocal(item) {
    return localStorage.getItem(item)
  }

  function setLocal(item, nvalue) {
    localStorage.setItem(item, nvalue)
  }

  function postMessage(message) {
    window.parent.postMessage(message, '*');
  }

  function playAudio(file) {
    var audio = new Audio(file);
    audio.play()
  }

  function getRandArray(aray) {
    return aray[Math.floor(Math.random() * aray.length)];
  }

  function scrollBottom(ele) {
    const scrollToBottom = (node) => {
      node.scrollTop = node.scrollHeight;
    }
    scrollToBottom(ele)
  }

  function alphabetPosition(text) {
    var result = "";
    for (var i = 0; i < parseInt(text.length); i++) {
      var code = text.toUpperCase().charCodeAt(i)
      if (code > 64 && code < 91) result += (code - 64) + " ";
    }

    return result.slice(0, result.length - 1);
  }

  String.prototype.isUpper = function() {
    if (!isNaN(this * 1)) {
      return false;
    }
    else {
      if (this == this.toUpperCase()) {
        return true;
      }
      if (this == this.toLowerCase()) {
        return false;
      }
    }
  }


  Object.prototype.iHtml = function(query) {
    if (query == null) {
      return this.innerHTML
    }
    else {
      this.innerHTML = query;
      return true;
    }
  }

  Object.prototype.css = function(get, n) {
    if (get == null && n == null) {
      return "Arguments required"
    }
    if (get != null && n == null) {
      return this.style.getPropertyValue(get)
    }
    if (get != null && n != null) {
      this.style.setProperty(get, n)
      return true;
    }
  }

  Object.prototype.iText = function(query) {
    if (query == null) {
      return this.innerText
    }
    else {
      this.innerText = query;
      return true;
    }
  }

  Object.prototype.val = function(query) {
    if (query == null) {
      return this.value
    }
    else {
      this.value = query;
      return true;
    }
  }

  Object.prototype.remove = function() {
    this.remove()
    return true;
  }

  Object.prototype.hide = function() {
    this.style.display = "none"
  }

  Object.prototype.show = function() {
    this.style.display = "block"
  }

  Object.prototype.isShown = function() {
    if (this.style.display == "block") {
      return true;
    }
    else if (this.style.display == "none") {
      return false;
    }
  }

  Object.prototype.isChecked = function() {
    if (this.checked == true) {
      return true;
    }
    else if (this.checked == false) {
      return false;
    }
  }

  Object.prototype.attribute = function(get, n) {
    if (get == null && n == null) {
      return "Arguments required"
    }
    if (get != null && n == null) {
      return this.getAttribute(get)
    }
    if (get != null && n != null) {
      this.setAttribute(get, n)
      return true;
    }
  }

  Object.prototype.removeAll = function() {
    this.forEach(ele => {
      ele.remove()
    })
    return true;
  }

  Object.prototype.ap = function(ele) {
    this.append(ele)
  }

  Object.prototype.apc = function(ele) {
    this.appendChild(ele)
  }

  String.prototype.isEmpty = function() {
    if (this.replaceAll(/\s/g, "") == "") {
      return true;
    }
    else {
      return false;
    }
  }

  String.prototype.removeLast = function(num) {
    return this.substring(0, this.length - num)
  }

  String.prototype.isUrl = function() {
    if (this.includes("http://") || this.includes("https://")) {
      if (this.includes(".")) {
        return true;
      }
      else {
        return false;
      }
    }
    else {
      return false;
    }
  }

  Object.prototype.scrollBottom = function() {
    const scrollToBottom = (node) => {
      node.scrollTop = node.scrollHeight;
    }
    scrollToBottom(this)
  }

  var alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

  String.prototype.encrypt = function(key) {
    var s = this.toString()
    var final = ""
    for (var i = 0; i < parseInt(s.length); i++) {
      var kn = key.charAt(i);
      if (s.charAt(i) == " ") {
        final = final + " "
        continue
      }
      var item = alphabetPosition(s.charAt(i))
      var knn = parseInt(item) + parseInt(kn);
      if (knn < 0 || knn > 25) {
        final = final + s.charAt(i).toUpperCase();
        continue
      }
      var new_char = alphabet[knn]
      final = final + new_char;
    }
    return final;
  }

  String.prototype.decrypt = function(key) {
    var s = this.toString()
    var final = ""
    for (var i = 0; i < parseInt(s.length); i++) {
      if (s.charAt(i) == " ") {
        final = final + " "
        continue
      }
      if (s.charAt(i).isUpper()) {
        console.log(".")
        final = final + s.charAt(i).toLowerCase()
        continue
      }
      var kn = key.charAt(i);
      var item = alphabetPosition(s.charAt(i))
      var knn = parseInt(item) - parseInt(kn);
      knn = knn - 2;
      if (knn < 0) {
        final = final + s.charAt(i)
        continue
      }
      var new_char = alphabet[knn]
      final = final + new_char;
    }
    return final;
  }

  Object.prototype.isActive = function() {
    if (this == document.activeElement) return true;
    else if (this != document.activeElement) return false;
  }

  String.prototype.sanitize = function() {
    return this
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  String.prototype.ascii = function() {
    let charCodes = [];
    for (let i = 0; i < this.toString().length; i++) {
      charCodes.push(this.charCodeAt(i));
    }
    return charCodes;
  }

  String.prototype.asciiStr = function() {
    return String.fromCharCode(...this.split(","));
  }

  // var encrypt = "how are you doing today my friend".encrypt("132761837419283857291928386919293")
  //var decrypt = encrypt.decrypt("132761837419283857291928386919293")
  //_("#text").iText(decrypt)
}
catch (err) {
  alert(err)
}