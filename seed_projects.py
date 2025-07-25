from app import app, db
from models import Project

with app.app_context():
    db.create_all()
    projects = [
        Project(
            title=" Code & Decode",
            description="Encodes and decodes messages using a custom secret language logic.",
            image_url="🔐",
            github_link="https://github.com/Faisal-Chap/python-projects-code-decode"
        ),
        Project(
            title=" Email My FESCO Bill",
            description="Automates electricity bill retrieval and sends it via email monthly using Selenium.",
            image_url="📧",
            github_link="https://github.com/Faisal-Chap/Email_My_FESCO_Bill"
        ),
        Project(
            title=" wapda.digital",
            description="WhatsApp-based bill alert platform with user signup & automation.",
            image_url="📱",
            github_link="https://github.com/Faisal-Chap/wapda-digital"
        ),
        Project(
            title=" Pixela Activity Tracker",
            description="Command-line tool for tracking daily activities via the Pixela API.",
            image_url="📊",
            github_link="http://github.com/Faisal-Chap/Habit_Tracker"
        ),
        Project(
            title=" ISS Overhead Notifier",
            description="Email alerts when ISS passes overhead at night. Uses sunrise/sunset logic.",
            image_url="🛰️",
            github_link="https://github.com/Faisal-Chap/Is-ISS-Overhead"
        ),
        Project(
            title=" NLP Workout Tracker",
            description="Tracks ISS with NLP integration and notifies user — night visibility considered.",
            image_url="💪",
            github_link="https://github.com/Faisal-Chap/NLP-workout-Tracking",
            is_featured=True
        ),
        Project(
            title=" Weather Forecast Notification",
            description="Sends SMS notifications for upcoming rain using OpenWeather + Twilio API.",
            image_url="🌧️",
            github_link="https://github.com/Faisal-Chap/RainAalert_via_Text"
        ),
        Project(
            title=" Stock Price Alert",
            description="Tracks Tesla stock price & sends news updates on major changes via SMS.",
            image_url="📉",
            github_link="https://github.com/Faisal-Chap/Stock_Price_Alerter",
            is_featured=True
        ),
        Project(
            title=" Password Manager",
            description="Tkinter GUI app to store, generate, and retrieve secure passwords in JSON.",
            image_url="🔑",
            github_link="https://github.com/Faisal-Chap/Password-Manager"
        ),
        Project(
            title=" Pomodoro Timer",
            description="A Tkinter-based visual Pomodoro Timer to boost productivity with breaks.",
            image_url="⏱️",
            github_link="https://github.com/Faisal-Chap/Pomodoro-Timer",
            is_featured=True
        ),
        Project(
            title=" Text to Morse Code Converter",
            description="Converts English text to Morse code using dictionaries and loops.",
            image_url="🔡",
            github_link="https://github.com/Faisal-Chap/Text-to-Morse-Code-Converter"
        ),
        Project(
            title=" Portfolio Website",
            description="My portfolio with all featured & notable projects listed and showcased.",
            image_url="🌍",
            github_link="https://github.com/Faisal-Chap/dev-portfolio"
        ),
        Project(
            title=" House Price Predictor (ML)",
            description="Multivariable regression to predict house prices. Includes log transformation & feature analysis.",
            image_url="🏠",
            github_link="https://github.com/Faisal-Chap/House_Price_Prediction_ML-Model",
            is_featured=True
        ),
        Project(
            title=" Semmelweis Handwashing Analysis",
            description="Historical data analysis on maternal mortality & handwashing impact using t-tests & visualizations.",
            image_url="🧼",
            github_link="https://github.com/Faisal-Chap/Maternal-Mortality-Analysis"
        ),
        Project(
            title=" Nobel Prize Data Analysis",
            description="Explore over 100 years of Nobel Prize trends using Python & visualization libraries.",
            image_url="🏅",
            github_link="https://github.com/Faisal-Chap/Nobel-Prize-Data-Analysis"
        ),
        Project(
            title=" Movie Revenue Prediction",
            description="Can big budgets predict box office success? ML-based analysis of movie datasets.",
            image_url="🎬",
            github_link="https://github.com/Faisal-Chap/Movie-Revenue-Prediction-Using-the-scikit-learn"
        ),
        Project(
            title=" Google Play Store EDA",
            description="In-depth interactive EDA of Android app performance using Plotly & Pandas.",
            image_url="📱",
            github_link="https://github.com/Faisal-Chap/Google-Play-Store-Data-Analysis",
            is_featured=True
        ),
        Project(
            title=" Google Trends vs Reality",
            description="Time series analysis connecting Google Trends with stock & economic data.",
            image_url="📊",
            github_link="https://github.com/Faisal-Chap/Google-Trends-Analysis"
        ),
        Project(
            title=" Image Manipulation with NumPy",
            description="Medical AI-inspired image processing using NumPy — part of #100DaysOfAI.",
            image_url="🧠",
            github_link="https://github.com/Faisal-Chap/Intermediate-NumPy---Image-Manipulation"
        ),
        Project(
            title=" LEGO Data Analysis",
            description="Explore LEGO dataset insights using Python and Pandas. #100DaysOfData challenge.",
            image_url="🧱",
            github_link="https://github.com/Faisal-Chap/LEGO-Data-Analysis-project",
            is_featured=True
        ),
        Project(
            title=" Programming Language Popularity",
            description="Trend analysis of language popularity using Stack Overflow data from 2008–2023.",
            image_url="📈",
            github_link="https://github.com/Faisal-Chap/Programming-Language-Popularity-Analysis-2008-2023-",
            is_featured=True
        ),
        Project(
            title=" University Major Salaries",
            description="Analyzes earnings by major using PayScale survey data. EDA & career insights.",
            image_url="🎓",
            github_link="https://github.com/Faisal-Chap/PayScale-Data-Analysis---Major-Salaries",
            is_featured=True
        ),
        Project(
            title=" TikTok Auto Like Bot",
            description="Selenium-based TikTok automation tool to like videos automatically.",
            image_url="🤖",
            github_link="https://github.com/Faisal-Chap/Tiktok_Like_Bot"
        ),
        Project(
            title=" Silence Remover for Audio",
            description="Automatically removes silent segments from audio files. Podcast/editor ready.",
            image_url="🔇",
            github_link="https://github.com/Faisal-Chap/Auto-Silence-Remover---for-Audio-Files",
            is_featured=True
        ),
        Project(
            title=" Rock-Paper-Scissors",
            description="Simple CLI game of Rock, Paper, Scissors against the computer.",
            image_url="✊",
            github_link="https://github.com/Faisal-Chap/Rock-Paper-Scissors-Game",
            is_featured=True
        ),
        Project(
            title=" Hangman Game",
            description="Command-line classic Hangman game with ASCII feedback and guessing logic.",
            image_url="🪓",
            github_link="https://github.com/Faisal-Chap/Hang-Man-Game-In-Python",
            is_featured=True
        ),
        Project(
            title=" Text Encoder & Decoder",
            description="CLI program for letter shifting text encoding & decoding with ASCII flair.",
            image_url="📝",
            github_link="https://github.com/Faisal-Chap/Text-Encoder-Decoder---Python-Script"
        ),
        Project(
            title=" TikTok Followers Comparison Game",
            description="Game where user guesses which TikTok influencer has more followers.",
            image_url="📊",
            github_link="https://github.com/Faisal-Chap/TikTok-Followers-Comparison-Game"
        ),
        Project(
            title=" Turtle Race Game",
            description="Place bets and watch turtles race using Python's turtle module.",
            image_url="🐢",
            github_link="https://github.com/Faisal-Chap/Turtle-race-Challenge---Python"
        ),
        Project(
            title=" Snake Game",
            description="Classic snake game built with Python turtle graphics. Eat to grow!",
            image_url="🐍",
            github_link="https://github.com/Faisal-Chap/Snake-Game---Python-Code",
            is_featured=True
        ),
        Project(
            title=" Mail Merge Automation",
            description="Auto-generates personalized letters from templates and name lists.",
            image_url="📨",
            github_link="https://github.com/Faisal-Chap/Mail-Merger---Python-Script"
        ),
        Project(
            title=" Ping Pong Game",
            description="2-player Ping Pong game with keyboard controls built using turtle module.",
            image_url="🏓",
            github_link="https://github.com/Faisal-Chap/Ping-Pong-Game---Python-Script",
            is_featured=True
        ),
        Project(
            title=" US States Guessing Game",
            description="Guess all 50 US states with turtle graphics and coordinate mapping.",
            image_url="🗺️",
            github_link="https://github.com/Faisal-Chap/US-states-Guessing-Game---TkInter"
        ),
        Project(
            title=" Squirrel Fur Color Analysis",
            description="Analyzes Central Park squirrel fur color dataset and outputs counts to CSV.",
            image_url="🐿️",
            github_link="https://github.com/Faisal-Chap/Squirrel-Fur-Color---Data-Analysis"
        ),
    ]

    db.session.bulk_save_objects(projects)
    db.session.commit()
    print("✅ Projects added!")
