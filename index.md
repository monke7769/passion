---
layout: home
search_exclude: true
---
## Passion
- Hayden Chen
- Shuban Pal
- Tarun Jaikumar
- Deva Sasikumar

<head>
    <title>Flask Button Example</title>
</head>
<body>
    <button id="submitButton">Submit Text</button>
    <div id="result"></div>

<script>
    document.getElementById('submitButton').addEventListener('click', function() {
        var text = "Example text to submit";  // You can replace this with the actual text you want to submit

        // Send a POST request to the Flask endpoint
        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = data.message;
        });
    });
</script>
</body>

<div id="firstSection">
    <h2>Click as much as you can before someone hits ctrl-R on you</h2>
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