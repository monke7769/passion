---
layout: home
search_exclude: true
---
The Passion Project
- Hayden Chen
- Shuban Pal
- Tarun Jaikumar
- Deva Sasikumar

<div id="firstSection">
    <h1>Click as much as you can before someone hits ctrl-R on you</h1>
    <p id="firstText">Click the button!</p>
    <button id="button1">CLICK ME!!</button>
    <p id="count">0</p>
</div>

<script>
function clickedButton() {
    var firsthref = document.getElementById("firstText")
    firstText.innerHTML = "Keep clicking it!"
    var num = document.getElementById("count")
    num.innerHTML = String(parseInt(num.innerHTML)+1)
}
var thebutton = document.getElementById("button1")
thebutton.onclick = clickedButton // on click, call the above function
</script>

Just to demonstrate our knowledge of JS

# Sections