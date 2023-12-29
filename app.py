import streamlit as st
import pandas as pd
import joblib

model_review = joblib.load('hotel_review_sentiment_classification.pkl')
# model_rating = joblib.load('hotel_rating_classification.pkl')

def classify_review_sentiment(text):
    input_text = pd.DataFrame(text,index=[0])
    classification_result = model_review.predict(input_text)[0]
    return classification_result


# def classify_rating(text):
#     input_text = pd.DataFrame(text,index=[0])
#     classification_result = model_rating.predict(input_text)[0]
#     return classification_result


# Streamlit UI
st.markdown(
    """
    <div style="font-family: Times New Roman; font-size:50px;">
        Hotel Reviews Sentiment and Ratings Classification
    </div>
    """,
    unsafe_allow_html=True
)
# User input form
st.sidebar.header('Hey there, Welcome to Hotel Reviews Classifications: ')
user_review = st.sidebar.text_area('Enter Your Reviews','Please type here.....')


# User input features
user_input = {
    'Review': user_review    
}

# Classification
if st.sidebar.button('Check Sentiment of Reviews'):
    classification_result = classify_review_sentiment(user_input)
    if classification_result == 0:
        classification_result = 'Negative'
    elif classification_result == 1:
        classification_result = 'Neutral'
    elif classification_result == 2:
        classification_result = 'Positive'
    else:
        classification_result = '404 - Not Found'

    st.success(f'Hey there, The Sentiment for your Review is:  { classification_result } ')

# if st.sidebar.button('Check Ratings of Reviews'):
#     classification_result = classify_rating(user_input)
#     st.success(f'Hey there, The Rating for your Review would be:  { classification_result } ')

# Adding "Developed by P322" at the bottom right
st.markdown(
    """
    <div style="position: fixed; bottom: 15px; right: 20px; text-align: left; font-size:15px; font-family: Courier new">
        Developed by <span style="font-family: Times New Roman; font-size:25px; style="color:#ff4b4b" >Group-1 (P322)</span>
    </div>
    """,
    unsafe_allow_html=True
)