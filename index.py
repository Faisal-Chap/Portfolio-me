# lets create our portfolio flask app

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Project  # import db and Project model



import os
app = Flask(__name__)


# Use a consistent database path in the instance folder

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with app
db.init_app(app)
# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    featured_projects = Project.query.filter_by(is_featured=True).all()
    return render_template('index.html', projects=featured_projects)


@app.route('/projects')
def all_projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/like/<int:id>', methods=['POST'])
def like_project(id):
    project = Project.query.get_or_404(id)
    project.likes += 1
    db.session.commit()
    return redirect(url_for('index'))


app = app

if __name__ == "__main__":
    app.run()

