import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------------------
# PAGE SETTINGS
# ------------------------------------
st.set_page_config(
    page_title="Smart Farmer NLP Chatbot",
    page_icon="🌾",
    layout="centered"
)

# ------------------------------------
# LANGUAGE SELECTION
# ------------------------------------
language = st.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"]
)

# ------------------------------------
# LOAD FAQ FILES
# ------------------------------------
if language == "English":
    faq = pd.read_csv("faq_english.csv")
    title = "🌾 Smart Farmer NLP Chatbot"
    prompt_text = "Ask your farming question..."

elif language == "Hindi":
    faq = pd.read_csv("faq_hindi.csv")
    title = "🌾 स्मार्ट किसान चैटबॉट"
    prompt_text = "अपना कृषि प्रश्न पूछें..."

else:
    faq = pd.read_csv("faq_telugu.csv")
    title = "🌾 స్మార్ట్ రైతు చాట్‌బాట్"
    prompt_text = "మీ వ్యవసాయ ప్రశ్నను అడగండి..."

# ------------------------------------
# EXTRACT QUESTIONS & ANSWERS
# ------------------------------------
questions = faq["Question"].astype(str).tolist()
answers = faq["Answer"].astype(str).tolist()

# ------------------------------------
# TF-IDF MODEL
# ------------------------------------
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words=None
)

question_vectors = vectorizer.fit_transform(
    questions
)

# ------------------------------------
# CHATBOT FUNCTION
# ------------------------------------
def get_response(user_input):

    user_vector = vectorizer.transform(
        [user_input]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    # Lower threshold for better matching
    if best_score >= 0.05:
        return answers[best_match_index]

    # Fallback Responses
    if language == "English":
        return "I do not have an exact answer for that question. Please ask a farming related question."

    elif language == "Hindi":
        return "मेरे पास इस प्रश्न का सटीक उत्तर नहीं है। कृपया कृषि से संबंधित प्रश्न पूछें।"

    else:
        return "ఈ ప్రశ్నకు నా వద్ద ఖచ్చితమైన సమాధానం లేదు. దయచేసి వ్యవసాయానికి సంబంధించిన ప్రశ్న అడగండి."

# ------------------------------------
# TITLE
# ------------------------------------
st.title(title)

st.markdown("---")

# ------------------------------------
# CHAT HISTORY
# ------------------------------------
history_key = f"chat_{language}"

if history_key not in st.session_state:
    st.session_state[history_key] = []

for msg in st.session_state[history_key]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------------------------
# USER INPUT
# ------------------------------------
prompt = st.chat_input(prompt_text)

if prompt:

    st.session_state[history_key].append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = get_response(prompt)

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state[history_key].append(
        {
            "role": "assistant",
            "content": response
        }
    )