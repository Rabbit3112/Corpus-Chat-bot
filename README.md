# Corpus-Chat-bot.

To run the Corpus Wine Company chatbot, please follow these steps:



step 1 : Clone the Repository:

git clone <https://github.com/Rabbit3112/Corpus-Chat-bot.git>

Now open the cloned directory and open your VS-Code or any other tool to run the code





step 2:  Install Dependencies:

Ensure you have Python 3.7+ installed. 

Install the required libraries using pip by running 'requirements.txt' :

    Json 
    Nltk
    Sklearn 
    Streamlit 

Run code in Terminal: 

pip install -r requirements.txt







Step 3 : Download NLTK Resources:

If you haven't downloaded NLTK resources previously, run the following script to download the necessary resources:

import nltk
nltk.download('punkt')
nltk.download('stopwords')






step 4: Prepare the Corpus:

Ensure the corpus file  "Sample Question Answers.json"  is located at C:\\Users\\Admin\\. 
Modify the path in the code if your file is located elsewhere.







Step 5: Run the Streamlit Application:

Start the Streamlit application using the command:

streamlit run app.py
Access the Application:
Open a web browser and go to http://localhost:8501 to access the chatbot interface.
