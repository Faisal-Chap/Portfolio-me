# Faisal Chap Portfolio Website

👋 Hi! This is my personal portfolio website built with Python and Flask to showcase my projects, skills, and connect with others.

---

## 🚀 Features

- **Home page** with dynamic Featured Projects loaded from a database  
- **Projects section** showing project cards with images, descriptions, GitHub links, and like buttons  
- **Tech stack section** presenting my core skills in a clean, modern layout  
- **About Me section** with a profile image and a short bio  
- **Contact section** with email and social media links  
- Responsive design using Tailwind CSS  
- Database handled with Flask-SQLAlchemy  
- Jinja2 templating for dynamic HTML rendering  
- Git integration for version control and deployment readiness  

---

## 🛠️ Technologies Used

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- Jinja2  
- Tailwind CSS  
- SQLite (default DB, easily replaceable)  

---

## 💾 Installation & Setup

1. **Clone the repo**
   git clone https://github.com/yourusername/faisal-chap-portfolio.git
   cd faisal-chap-portfolio


2.  **Create and activate a virtual environment**
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows


3.  **Install dependencies**
pip install -r requirements.txt

4.  **Initialize the database and seed projects**
python seed_projects.py

5.  **Run the Flask app**
flask run


## 🎯 Usage
Add new projects by updating the database model via SQLAlchemy or modifying the seed script

Customize the bio, profile image, and contact links in templates

Extend functionality by adding new sections or integrating APIs



## 🤝 Contributing
Feel free to open issues or submit pull requests to improve the project. Your contributions are welcome!

## 📫 Contact Me
Email: zia639329@gmail.com

LinkedIn: https://www.linkedin.com/in/faisal-zia-dev/

GitHub: https://github.com/Faisal-Chap

Twitter: https://x.com/faisalziachap

##  ⚖️ License
This project is open source under the MIT License.
