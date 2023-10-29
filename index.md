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
            transform: scale(1.1);
            transition: transform 0.3s ease;
        }
        /* Styles for the #firstSection */
        #firstSection {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
        @keyframes colorChange {
            0% { color: black; }
            50% { color: grey; }
            100% { color: black; }
        }

        #firstText {
            animation: colorChange 2s infinite;
        }

    </style>


</head>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Click Counter</title>
    <style>
        #firstSection {
            text-align: center;
            padding: 50px;
            border: 1px solid #ccc;
            margin: 20px auto;
            width: 400px;
        }

        #button1 {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>

    <div id="firstSection">
        <h2>Click as much as you can before someone hits ctrl-R on you</h2>
        <p id="firstText">Click the button!</p>
        <button id="button1">CLICK ME!!</button>
        <p id="count">0</p>
    </div>

    <script>
        document.getElementById("button1").addEventListener("click", function() {
            document.getElementById("firstText").innerHTML = "Keep clicking it!";
            
            var numElement = document.getElementById("count");
            var currentCount = parseInt(numElement.innerHTML);
            numElement.innerHTML = currentCount + 1;
        });
    </script>

</body>
Just to demonstrate our knowledge of JS

# Sections

<html>
<head>
    <title>Dropdown Box Example</title>
</head>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cipher Selection</title>
</head>
<body>
    <label for="ciphers">Select a cipher:</label>
    <select id="ciphers">
        <option value="caesar">Caesar Cipher</option>
        <option value="RSA">RSA</option>
        <option value="hexadecimal">Hexadecimal</option>
        <option value="binary">Binary</option>
        <option value="substitution">Substitution</option>
    </select>

    <p>Selected cipher: <span id="selectedCipher"></span></p>

    <script>
        const dropdown = document.getElementById("ciphers");
        const selectedCipher = document.getElementById("selectedCipher");

        dropdown.addEventListener("change", function() {
            const selectedOption = dropdown.value;
            selectedCipher.textContent = selectedOption;

            // Depending on the selected option, interact with different backends
            switch (selectedOption) {
                case "caesar":


                    break;
                case "RSA":
                    // Code for RSA
                    break;
                case "hexadecimal":
                    // Code for hexadecimal
                    break;
                case "binary":
                    // Code for binary
                    break;
                case "substitution":
                    // Code for substitution
                    break;
                default:
                    // Handle any other cases or errors
                    break;
            }
        });
    </script>
</body>
</html>
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/skulpt/0.10.0/skulpt.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/skulpt/0.10.0/skulpt-stdlib.js"></script>
  </head>
  <body>
    <button onclick="runPythonCode()">Run Python Code</button>
    <pre id="output"></pre>
    <script>
      function runPythonCode() {
        var output = document.getElementById("output");
        var prog = 'print("Hello from Python!")'; // Your Python code here
        var myPromise = Sk.misceval.asyncToPromise(function() {
          return Sk.importMainWithBody("<stdin>", false, prog, true);
        });
        myPromise.then(function(mod) {
          console.log('Python code executed successfully.');
        }, function(err) {
          output.textContent = err.toString();
        });
      }
    </script>
  </body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>Send Data to Flask Backend</title>
</head>
<body>
    <input type="text" id="textInput" placeholder="Enter text here">
    <button onclick="sendData()">Send Data</button>
    <h3 id="caesar"></h3>

<script>
    function sendData() {
    var inputText = document.getElementById('textInput').value;
    fetch('http://localhost:8080/caesarencrypt', {
        method: 'POST', // or 'GET'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: inputText}),
    })
    .then(response => response.text())
    .then(data => {
        console.log('Success:', data);
        var txt = document.getElementById("caesar")
        txt.innerText = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
    </script>
</body>
</html>
