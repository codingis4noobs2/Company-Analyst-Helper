# Company-Analyst-Helper
A Streamlit app leveraging neural search and AI to analyze competitors, providing insights into their strengths and weaknesses for strategic decision-making.

## Demo
https://github.com/codingis4noobs2/Company-Analyst-Helper/assets/87560178/ef808496-6889-4b51-a6a9-75732496a4ca

## How to Use
The Company Analyst Helper app helps you uncover your competitors' strengths and weaknesses using advanced neural search technology. Simply input your company's URL, and the app will identify similar companies and analyze their pros and cons to provide actionable insights.

## Local Installation Steps
1. Fork the repo
2. Clone it on your machine
   ```bash
   git clone https://github.com/{your-github-username}/Company-Analyst-Helper.git
   cd Company-Analyst-Helper
   ```
3. Create and Activate a Virtual Environment (Optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Get Gemini api key from [here](https://aistudio.google.com/app/apikey), exa-ai api key from [here](https://exa.ai/)
6. Set Up Environment Variables, Create a .env file in the project root directory and add your API keys
   ```bash
   EXA_API_KEY=your_exa_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```
7. Run the streamlit application
   ```bash
   streamlit run app.py --server.port 8000
   ```
8. Visit localhost:8000 to use the application.

