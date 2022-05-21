from flask import Blueprint, request, redirect, url_for, render_template
from db_connection import get_db_connection

blog_pages = Blueprint("blogs", __name__)

#display a blog
@blog_pages.route("/blogs/<string:blog_id>")
def display_blog(blog_id: str):
	conn = get_db_connection()
	blog = conn.execute("SELECT * FROM blogs WHERE id = (?)", (blog_id)).fetchone()
	return render_template('blog_page.html', blog = blog)

#create a blog
@blog_pages.route("/blogs/", methods = ["GET", "POST"])
def create_blog():
	if request.method == "POST":
		title = request.form.get("title")
		content = request.form.get("content")
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute("INSERT INTO blogs (title, content) VALUES (?, ?)", (title, content))
		blog_id = cur.lastrowid
		conn.commit()
		conn.close()
		return redirect(url_for(".display_blog", blog_id = blog_id))
	
	return render_template("new_blog.html")
