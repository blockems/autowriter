from flask import Flask, render_template
from flask_login import LoginManager, login_required
from database import db  # import the db instance
import os

def create_app():
    app = Flask(__name__)

    db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SECRET_KEY'] = 'ProjectAssistant'

    # Initialize SQLAlchemy
    db.init_app(app)  # Initialize with app

    # Initialize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # specify what view handles login

    @login_manager.user_loader
    def load_user(user_id):
        from user_management.models import User
        return User.query.get(int(user_id))

    from user_management.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app, db, login_manager

app, db, login_manager = create_app()

with app.app_context():
    from user_management.models import User  # import your User model here
    db.create_all()  # create tables for our models

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/setup')
@login_required
def setup():
    return render_template('setup.html')
    
@app.route('/knowledge')
@login_required
def knowledge():
    return render_template('knowledge.html')

@app.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    app.run(debug=True)
