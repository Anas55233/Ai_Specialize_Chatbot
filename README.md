# 🤖 AI Mentor — AI Specialized Chatbot

AI Mentor is an AI-powered educational chatbot built with **Python, Streamlit, and Google Gemini**. It is designed to help students learn and understand concepts related to **Artificial Intelligence and its major fields**.

The chatbot maintains the conversation history during the session and uses previous messages to provide context-aware responses.

## 🚀 Features

* 💬 Interactive chatbot interface
* 🤖 Powered by Google Gemini
* 🧠 AI-focused responses
* 📚 Supports topics such as:

  * Artificial Intelligence
  * Machine Learning
  * Deep Learning
  * Natural Language Processing
  * Computer Vision
* 🗨️ Maintains conversation history using Streamlit session state
* 🔐 Uses Streamlit Secrets for API key management
* ⚡ Simple and lightweight Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Gemini**
* **LangChain**
* **streamlit-chat**
* **Git & GitHub**

## 🎯 Purpose

The main purpose of this project is to create a simple **AI technical mentor** that helps students ask questions and learn AI-related concepts through an interactive conversational interface.

## 🔑 Environment Variable

The Gemini API key should be stored securely using Streamlit Secrets:

```toml
GEMINI_API_KEY = "your-api-key"
```

**Do not upload your API key or `.env`/secret files containing credentials to GitHub.**

## 📌 Future Improvements

* Add document/PDF-based question answering
* Add RAG (Retrieval-Augmented Generation)
* Add source citations
* Add user authentication
* Improve chat UI
* Add conversation export
* Deploy the application online
