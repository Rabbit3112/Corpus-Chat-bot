import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import uuid

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load the JSON file
with open("C:\\Users\\Admin\\Sample Question Answers.json", 'r') as file:
    corpus = json.load(file)

# Preprocess the questions
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]

# Preprocess the entire corpus
for entry in corpus:
    entry['processed_question'] = preprocess(entry['question'])

# Vectorize the questions
questions = [" ".join(entry['processed_question']) for entry in corpus]
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def retrieve_answer(user_query):
    processed_query = preprocess(user_query)
    query_vector = vectorizer.transform([" ".join(processed_query)])
    similarities = cosine_similarity(query_vector, question_vectors).flatten()
    most_similar_index = similarities.argmax()
    if similarities[most_similar_index] > 0.1:  # Set a threshold to determine relevance
        return corpus[most_similar_index]['answer']
    else:
        return "Please contact the business directly for more information."

# Local dictionary to store sessions
session_store = {}

def store_session(session_id, user_input, response):
    if session_id not in session_store:
        session_store[session_id] = []
    session_store[session_id].append((user_input, response))

def get_session(session_id):
    return session_store.get(session_id, [])

# Streamlit UI Design
st.balloons()
st.title("Corpus Wines")


st.markdown("""
            
            Welcome to Corpus Wine Company, your premier destination for exquisite wines. Our carefully curated selection of wines is sourced from the finest vineyards, ensuring every bottle offers a unique and delightful experience. Whether you are a connoisseur or a casual enthusiast, our website is your gateway to discovering exceptional wines that cater to all tastes and occasions. 
            
            
            Visit us online to explore our extensive collection, learn about our wine offerings, and find the perfect bottle to elevate your celebrations. At Corpus Wine Company, we are committed to providing exceptional quality and unparalleled customer service, making your wine journey truly memorable.""")




st.header("Scroll down for chat bot")


st.image("D:\\Projects\\LOGO.png")
st.header(" Taste the true wine with Corpus")
st.image("C:\\Users\\Admin\\Pictures\\wine logo.jpg")
st.logo("C:\\Users\\Admin\\Pictures\\LOGO.png")
st.header('Natural and Premium Quality wines')
st.image("C:\\Users\\Admin\\Pictures\\Screenshots\\new.jpg")
st.markdown("""
            """)
st.subheader("For more information about our wine products without any hassle, just use our chatbot for instant answers")
st.header("Ask anything with Corpus Bot")



# Initialize session state for session_id if it doesn't exist
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())  # Initialize with a unique identifier

# Use session_id from session_state
session_id = st.session_state.session_id

user_input = st.text_input("Ask Here:")

if user_input:
    response = retrieve_answer(user_input)  # Backend logic to generate response
    st.write(response)
    store_session(session_id, user_input, response)
    st.write("Conversation History:")
    history = get_session(session_id)
    for query, resp in history:
        st.write(f"Q: {query}")
        st.write(f"A: {resp}")
st.image("D:\\Projects\\wine glass.png")
