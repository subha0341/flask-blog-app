from flask import Flask, render_template
from blogs import blog_pages
from db_connection import get_db_connection

#application object creation
application = Flask(__name__)
application.register_blueprint(blog_pages)

@application.route("/")
def index():
	conn = get_db_connection()
	blogs = conn.execute("SELECT * FROM blogs").fetchall()
	conn.close()
	return render_template('index.html', blogs = blogs)

if(__name__ == "__main__"):
	application.run()
