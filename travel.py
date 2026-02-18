import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
#load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="TravelGuideAI", page_icon="🌍")

st.title("🌍 TravelGuideAI")
st.write("AI-powered travel itinerary generator using Gemini 2.5 Flash")

destination = st.text_input("Enter Destination")
days = st.number_input("Number of Days", min_value=1, max_value=30, value=3)
nights = st.number_input("Number of Nights", min_value=0, max_value=30, value=2)
interests = st.text_input("Enter Interests (comma separated e.g., food, adventure, history)")

if st.button("Generate Itinerary"):

    if not destination or not interests:
        st.warning("Please fill all fields.")

    elif nights >= days:
        st.warning("Nights should be less than days.")

    else:
        with st.spinner("Generating your travel plan..."):

            prompt = f"""
            Create a detailed {days}-day and {nights}-night travel itinerary for {destination}.
            User interests: {interests}.
            Include:
            - Day-wise plan
            - Morning, Afternoon, Evening activities
            - Hotel stay suggestions for {nights} nights
            - Food recommendations
            - Travel tips
            Make it well formatted.
            """

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success("Itinerary Generated Successfully!")
                st.markdown(response.text)

            except Exception as e:
                st.error("Error occurred:")
                st.code(str(e))

