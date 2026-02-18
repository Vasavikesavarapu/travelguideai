# travelguideai
Project Overview

This project is a Streamlit-based web application that integrates with an external AI API using a secure API key. The application allows users to interact with AI features through a simple and user-friendly interface.

The project is designed for easy local development and cloud deployment using Streamlit Community Cloud.

🚀 Features

✅ User-friendly Streamlit UI

✅ Secure API Key handling

✅ Environment variable support

✅ Ready for Streamlit Cloud deployment

✅ Clean project structure

✅ Easy setup for team collaboration

🛠️ Tech Stack

Frontend & Backend: Python

Framework: Streamlit

API Integration: External AIstudio

Deployment: Streamlit Community Cloud

Version Control: GitHub

📂 Project Structure
project-folder/
│
├── app.py
├── requirements.txt
├── README.md
└── .env (optional for local development)

⚙️ Installation & Setup (Local Development)
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Add API Key (Local Method)

Create a .env file in the root folder:

API_KEY=your_api_key_here


Then install dotenv:

pip install python-dotenv


In your app.py:

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

🔐 How to Add API Key in Streamlit Deployment

When deploying to Streamlit Community Cloud, DO NOT upload .env file.

Instead:

Go to your app dashboard on Streamlit Cloud

Click on Settings

Go to Secrets

Add:

API_KEY = "your_api_key_here"


Save

Then access it in app.py like this:

import streamlit as st

api_key = st.secrets["API_KEY"]


✅ This keeps your API key secure.

▶️ Run the Application
streamlit run app.py


App will open in your browser automatically.

🌍 Deployment Steps

Push project to GitHub

Go to Streamlit Community Cloud

Click New App

Connect your GitHub repository

Select branch

Deploy

Your app will be live in a few minutes 🚀

🔒 Security Best Practices

❌ Never upload .env file to GitHub

❌ Never hardcode API keys in code

✅ Use environment variables

✅ Use Streamlit secrets in deployment

🤝 Team Collaboration Guide

For team members:

Clone repository

Add their own API key in .env

Install requirements

Run locally
