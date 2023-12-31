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


<!-- This is the Encryption Code -->
<body>
    <!-- This is the dropdown box with all the options -->
    <label for="ciphers">Select a cipher:</label>   
    <select id="ciphers">
        <option value="caesar">Caesar Cipher</option>
        <option value="RSA">RSA</option>
        <option value="hexadecimal">Hexadecimal</option>
        <option value="binary">Binary</option>
        <option value="substitution">Substitution</option>
        <option value="morse">morse</option>
    </select>
    <input type="text" id="Encryptinput" placeholder="Type The Text You want to Encrypt">
    <h3 id="encrypted"></h3>
    <button onclick="Encrypt()">ENCRYPT</button>
    <p>Selected cipher: <span id="selectedCipher"></span>
    </p>
    <script>
        function Encrypt() {
            console.log("Encrypt function called");
            const dropdown = document.getElementById("ciphers");
            const selectedCipher = document.getElementById("selectedCipher");
            // Get the input text outside the switch statement
            var inputText = document.getElementById('Encryptinput').value;
            // Depending on the selected option, interact with different backends
            const selectedOption = dropdown.value;
            selectedCipher.textContent = selectedOption;
            switch (selectedOption) {
                case "caesar": // Ceasar Encryption making connection to backend
                    console.log("Encrypt caesar function called");
                    fetch('http://localhost:8080/caesarencrypt', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: inputText }),
                    })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Success:', data);
                        var txt = document.getElementById("encrypted");
                        txt.innerText = JSON.parse(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                    break;
                case "RSA": // RSA Encryption making connection to backend
                    console.log("Encrypt RSA function called");
                    fetch('http://localhost:8080/rsaencrypt', {
                        method: 'POST',
                        timeout: 1000000,
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: inputText }),
                    })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Success:', data);
                        var txt = document.getElementById("encrypted");
                        txt.innerText = JSON.parse(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                    break;
                case "hexadecimal": // Hexadecimal Encryption making connection to backend
                    console.log("Encrypt RSA function called");
                    fetch('http://localhost:8080/hexencrypt', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: inputText }),
                    })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Success:', data);
                        var txt = document.getElementById("encrypted");
                        txt.innerText = JSON.parse(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                    break;
                case "binary": // Binary Encryption making connection to backend
                    console.log("Encrypt RSA function called");
                    fetch('http://localhost:8080/binaryencrypt', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: inputText }),
                    })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Success:', data);
                        var txt = document.getElementById("encrypted");
                        txt.innerText =JSON.parse(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                    break;
                case "substitution":
                    console.log("Encrypt RSA function called");
                    fetch('http://localhost:8080/subencrypt', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: inputText }),
                    })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Success:', data);
                        var txt = document.getElementById("encrypted");
                        txt.innerText = JSON.parse(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                    break;
                case "morse":
                    console.log("Encrypt RSA function called");
                    fetch('http://localhost:8080/morseencrypt', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: inputText }),
                    })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Success:', data);
                        var txt = document.getElementById("encrypted");
                        txt.innerText = JSON.parse(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                    break;
                default:
                    // Handle any other cases or errors
                    break;
            }
        }
    </script>
</body>




</html> 


 <!-- Testing out the Ceasar Cipher connection to the backend -->
<html>
<head>
    <title>Classify the Cipher being used</title>
</head>
<body>
    <input type="text" id="textInput" placeholder="Enter text here">
    <button onclick="sendData()">Decrypt</button>
    <h3 id="Decryptor"></h3>

<script>
    function sendData() {
    var inputText = document.getElementById('textInput').value;
    fetch('http://localhost:8080/decryption', {
        method: 'POST', // or 'GET'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: inputText}),
        })
    .then(response => response.text())
    .then(data => {
        console.log('Success:', data);
        var txt = document.getElementById("Decryptor")
        txt.innerText = data;
        })
    .catch(error => {
        console.error('Error:', error);
        });
    }
</script>




</body>
</html>
