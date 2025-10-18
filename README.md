## Streamlit Chatbot with LangGraph & OpenAI

This is a simple chatbot application built using Streamlit for the frontend and LangGraph + OpenAI for the conversational backend. The chatbot maintains conversation history and leverages LangGraph to handle message state and flow.

# Features
- Interactive chat interface using Streamlit
- Conversation state preserved across turns
- Backend built with LangGraph for message orchestration
- Powered by OpenAI language models (via langchain_openai)
- In-memory conversation checkpointing
- Simple and extendable architecture

# Project Structure
.
├── chatbot_backend.py   # Backend logic using LangGraph + OpenAI
├── chatbot_frontend.py  # Streamlit frontend (main app)
├── .env                 # Environment variables (API keys)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

# Requirements

Before running the application, make sure you have:
- Python 3.9 or above
- An OpenAI API Key
- Streamlit installed

# Installation

1. Clone the repository
2. Create a virtual environment (optional but recommended)
3. Install dependencies
     pip install -r requirements.txt
5. Add your API key
    - Create a .env file
    - OPENAI_API_KEY=your_openai_api_key_here
  
# Run the application
streamlit run chatbot_frontend.py
The app will open in your browser at http://localhost:8501.

<img width="914" height="728" alt="Screenshot 2025-10-18 at 12 47 58 PM" src="https://github.com/user-attachments/assets/838a7bd0-c85c-406b-95b1-777fe714bc7e" />


 

