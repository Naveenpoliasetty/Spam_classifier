import streamlit as st
import pickle
import string
import sklearn
import nltk
import string

import nltk

nltk.data.path.append("/path/to/nltk_data")

nltk.download('punkt', download_dir="/path/to/nltk_data")

nltk.download('stopwords', download_dir="/path/to/nltk_data")
from  nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
count = 0
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
 
    return " ".join(y)

 
 
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
 
 
st.title("Email Spam Classifier")
result = None
input_sms = st.text_input("Enter the message")
if st.button('Predict'):
    transform_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transform_sms])
    result = model.predict(vector_input)[0]
if result is not None:
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
else:
    st.warning("Prediction result is empty. Please make sure to run the prediction first.")
