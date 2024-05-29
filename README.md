# CSP First Trimester Passion-Project

Hayden Chen, Shuban Pal, Tarun Jaikumar, Deva Sasikumar

### Cipher Hijinks

This project aims to expose different ciphers and encryption methods for text strings to people who have had little to no experience with cryptography. There are two main components:
  - The learning modules formulated in a Wiki fashion, where users can read through the various types of ciphers and their encryption/decryption
  - Cipher Encryption and Decryption Functionality. This component was made possible through Flask API, with user input text being processed by the backend server. https://github.com/monke7769/passion-backend.git

#### Key Features 

The ciphers included in this project:
 - Caesar cipher
 - Substitution cipher
 - Binary
 - Hexadecimal
 - Morse Code
 - RSA

- Search functionality: the learning modules are searchable via the search feature at /search.
- Interactive module/wiki pages enabling users to test their knowledge of the ciphers with short quizzes at the end. Users are informed on the page via JavaScript whether they answered correctly or not
- Encryption is done via .py files stored on the backed. The user can select which cipher they want to use to encrypt an input message, and a POST method is made to the appropraite
- Decryption is done similarly on the frontend, but the user is not required to know which cipher the input message was encrypted with. After a POST method is sent to the decrypt URL, the server can detect which cipher was used in encryption via AI tools and decrypt the message accordingly.

#### AI/Machine Learning tools 

The backend server runs Keras (neural network), Scikit-learn, numpy and classification algorithms to enable analysis of which cipher was used to encrypt the user's message.

Model Loading and Prediction:
- Model Serialization: Saving a trained model to a file (JSON for structure, HDF5 for weights) and loading it for inference.
- Prediction: Using the trained model to predict the class of new input data.

Text Feature Extraction:
- Vectorization: Converting text data into numerical format (token counts) suitable for machine learning models.

Classification:
- Sparse Categorical Crossentropy: A loss function used for classification tasks where the output is a single class among many.

Machine Learning Workflow:
- Data Transformation: Preprocessing input text data to match the format used during model training.
- Inference: Running the model on new data to make predictions.

### For developers and users

Run **make** to build the website page on http://127.0.0.1:4100/Passion-Project/. The Makefile will then convert all the .ipynb notebook files into the wiki pages. The frontpage (index.html) contains the encrypt and decrypt features but does not have links to the rest of the site (for aesthetic purposes). To access them, go to http://127.0.0.1:4100/Passion-Project/search and search for the pages on the rest of the site.

Run **python main.py** to start the backend Flask server at http:127.0.0.1:8080. main.py contains all the code handling POST requests to backend urls, including calling functions from other python files to encrypt the input. These other files are located within the main directory, including hex.py, caesar.py, etc. The file aiprediction.py trains the machine to detect which cipher was used for encryption.

Be sure to install all the packages in requirements.txt before running!
