from flask import Flask, render_template
from data.load_db import insert_all_data_from_api_to_db_if_empty
from blue_prints.users_bp import users_bp
from blue_prints.posts_bp import posts_bp

app = Flask(__name__)
insert_all_data_from_api_to_db_if_empty()
app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)

@app.route('/')
def home_page():
    return render_template('home_page.html')

if __name__ == '__main__':
    app.run()
