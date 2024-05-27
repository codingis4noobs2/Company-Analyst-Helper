import os
import time
from exa_py import Exa
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Set page configuration
st.set_page_config(
    page_title="Company Analyst Helper",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
    initial_sidebar_state="auto"
)

load_dotenv()

# Retrieve API keys
EXA_API_KEY = st.secrets["EXA_API_KEY"]
try:
  genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
  st.error(f"Error: {e}")
# System message for the GenerativeModel
SYSTEM_MESSAGE = """You are a helpful assistant writing a research report about a company. 
Summarize the users input into multiple paragraphs. 
Be extremely concise, professional, and factual as possible. 
The first paragraph should be an introduction and summary of the company. 
The second paragraph should include pros and cons of the company. 
Things like what are they doing well, things they are doing poorly or struggling with. 
And ideally, suggestions to make the company better."""
model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=SYSTEM_MESSAGE)
exa = Exa(api_key=EXA_API_KEY)

# Sidebar
with st.sidebar:
    st.header("Tech Stack")
    st.markdown("""
    - Streamlit
    - Exa AI
    - Google Gemini
    """)

st.header("Welcome to the Interactive Company Analyst Helper!")
st.subheader("Are you looking to uncover your competitors' strengths and weaknesses? You've come to the right place.")

# Initialize session state for inputs
if 'input_url' not in st.session_state:
    st.session_state.input_url = ''
if 'competitor' not in st.session_state:
    st.session_state.competitor = ''

try:
    st.session_state.input_url = st.text_input("Your company URL", st.session_state.input_url)
    submit = st.button("Submit URL")

    if submit and st.session_state.input_url:
        search_response = exa.find_similar_and_contents(
            st.session_state.input_url,
            highlights={"num_sentences": 2},
            num_results=10
        )
        companies = search_response.results
        st.session_state.urls = [c.url for c in companies]
        
        with st.expander("Competitors Found"):
            for c in companies:
                st.write(c.title + ': ' + c.url)
    
    if 'urls' in st.session_state and st.session_state.urls:
        st.session_state.competitor = st.selectbox("Select Competitor", st.session_state.urls)
        final_submit = st.button("Finalize")

        if final_submit and st.session_state.competitor:
            all_contents = ""
            search_response = exa.search_and_contents(
                st.session_state.competitor,
                type="keyword",
                num_results=3
            )
            research_response = search_response.results
            for r in research_response:
                all_contents += r.text

            response = model.generate_content(all_contents)
            st.write(response.text)
except Exception as e:
    st.write("Exa was unable to process the URL, please try a different URL.")
    st.write(f"Error: {e}")
