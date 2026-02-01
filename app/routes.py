from flask import Blueprint, render_template, request, redirect, flash
from .models import db, Link
import secrets

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            flash("Please enter a valid URL", "error")
            return redirect("/")
        
        short_id = secrets.token_urlsafe(6)
        new_link = Link(original_url=url, short_id=short_id)
        db.session.add(new_link)
        db.session.commit()
        
        return render_template("index.html", short_url=f"{request.host_url}{short_id}")
    
    return render_template("index.html")

@main.route("/<short_id>")
def redirect_to_url(short_id):
    link = Link.query.filter_by(short_id=short_id).first_or_404()
    link.clicks += 1
    db.session.commit()
    return redirect(link.original_url)