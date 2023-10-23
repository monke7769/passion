---
layout: home
search_exclude: true
---
<head>
    <title>Flask Button Example</title>
    <link rel="stylesheet" href="assets/style/css/style.css">
    <style>
        /* Styles for the body */
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        /* Styles for h2 elements */
        h2 {
            color: #333366;
            margin-bottom: 20px;
        }
        /* Styles for p elements */
        p {
            color: #666666;
        }
        /* Styles for buttons */
        button {
            background-color: #4CAF50; /* Green */
            color: white;
            padding: 15px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        /* Styles for the #firstSection */
        #firstSection {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
    </style>
</head>

<body>
    <div class="passion">
        ## Passion
        - Hayden Chen
        - Shuban Pal
        - Tarun Jaikumar
        - Deva Sasikumar
    </div>
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
    <div id="firstSection">
        <h2>Click as much as you can before someone hits ctrl-R on you</h2>
        <p id="firstText">Click the button!</p>
        <button id="button1">CLICK ME!!</button>
        <p id="count">0</p>
    </div>
    <script>
        function clickedButton() {
            var firstText = document.getElementById("firstText");
            firstText.innerHTML = "Keep clicking it!";
            var num = document.getElementById("count");
            num.innerHTML = String(parseInt(num.innerHTML)+1);
        }
        var thebutton = document.getElementById("button1");
        thebutton.onclick = clickedButton; // on click, call the above function
    </script>

</body>

Just to demonstrate our knowledge of JS

# Sections
