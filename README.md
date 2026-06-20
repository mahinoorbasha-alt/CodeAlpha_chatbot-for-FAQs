🌾 Smart Farmer NLP Chatbot

📌 Project Overview

Smart Farmer NLP Chatbot is a multilingual agriculture-focused chatbot developed using Python, Streamlit, TF-IDF Vectorization, and Cosine Similarity. The chatbot is designed to assist farmers by answering frequently asked questions related to farming, crop management, irrigation, fertilizers, government schemes, crop prices, and other agricultural topics.

The project uses Natural Language Processing (NLP) techniques to understand user queries and provide the most relevant response from a predefined knowledge base. Unlike traditional keyword-based systems, the chatbot uses TF-IDF and Cosine Similarity to match similar questions and deliver accurate answers.

This project was developed as part of the CodeAlpha Internship Program.

---

🎯 Objectives

- Build an intelligent FAQ chatbot for farmers.
- Implement Natural Language Processing techniques.
- Provide multilingual support for better accessibility.
- Improve user interaction through a chat-based interface.
- Deliver farming-related information quickly and efficiently.

---

✨ Features

🌐 Multilingual Support

The chatbot supports multiple languages:

- English
- Hindi
- Telugu

Users can select their preferred language from a dropdown menu.

🤖 NLP-Based Question Matching

The chatbot uses:

- TF-IDF Vectorization
- Cosine Similarity

to identify the most relevant answer even when the user's question is not exactly the same as the stored FAQ question.

💬 Interactive Chat Interface

Built using Streamlit's chat components:

- User-friendly interface
- Real-time conversation
- Chat history support
- Clean and responsive design

🌾 Agriculture Knowledge Base

The chatbot can answer questions related to:

- Farmer Registration
- Login and Account Access
- Crop Prices
- Organic Farming
- Crop Rotation
- Irrigation Methods
- Fertilizers
- Pesticides
- Soil Testing
- Crop Insurance
- Government Schemes
- Sustainable Agriculture
- Harvesting Techniques
- Crop Storage

---

🛠️ Technologies Used

Technology| Purpose
Python| Core Programming Language
Streamlit| Web Application Framework
Pandas| Data Handling
Scikit-learn| NLP and Machine Learning
TF-IDF Vectorizer| Text Feature Extraction
Cosine Similarity| Question Matching

---

🧠 Working Principle

Step 1: User Enters a Question

Example:

How do I register as a farmer?

Step 2: Text Processing

The chatbot processes the user's question using NLP techniques.

Step 3: TF-IDF Vectorization

The question is converted into numerical vectors using TF-IDF.

Step 4: Similarity Calculation

Cosine Similarity compares the user's question with all stored FAQ questions.

Step 5: Best Match Selection

The chatbot identifies the most relevant question.

Step 6: Response Generation

The corresponding answer is displayed to the user.

---

📂 Project Structure

Smart-Farmer-NLP-Chatbot
│
├── app.py
├── faq_english.csv
├── faq_hindi.csv
├── faq_telugu.csv
├── requirements.txt
└── README.md

---

🚀 Installation

Clone Repository

git clone YOUR_GITHUB_REPOSITORY_LINK

Navigate to Project Folder

cd Smart-Farmer-NLP-Chatbot

Install Dependencies

pip install streamlit pandas scikit-learn

---

▶️ Running the Application

Run the following command:

streamlit run app.py

The application will automatically open in your browser.

---

📸 Sample Questions

English

- What is organic farming?
- How do I register?
- What is irrigation?
- How do I check crop prices?
- What government schemes are available?

Hindi

- जैविक खेती क्या है?
- लॉगिन कैसे करें?
- फसल की कीमत कैसे देखें?

Telugu

- సేంద్రీయ వ్యవసాయం అంటే ఏమిటి?
- లాగిన్ ఎలా అవ్వాలి?
- పంట ధరలు ఎలా చూడాలి?

---

📈 Future Enhancements

- Voice-Based Interaction
- Live Weather Information
- Crop Disease Detection
- AI-Powered Recommendations
- Integration with Government Agriculture Portals
- Mobile Application Development
- Support for Additional Languages

---

🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit Application Development
- Data Handling with Pandas
- Building Interactive Chatbots
- Multilingual User Interfaces

---

🏆 Project Highlights

✅ NLP-Based Chatbot

✅ Multilingual Support

✅ Streamlit Chat Interface

✅ TF-IDF & Cosine Similarity

✅ Farmer-Centric Knowledge Base

✅ Interactive and User-Friendly Design

---

👨‍💻 Developed By

Meharunnisa Noorbasha

CodeAlpha Internship Project

Task 2 – FAQ Chatbot using NLP

---

📄 License

This project is developed for educational and internship purposes under the CodeAlpha Internship Program.
