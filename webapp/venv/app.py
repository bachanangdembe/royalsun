from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        lat = request.form.get("latitude")
        lng = request.form.get("longitude")

        u = User(name=name, email=email, latitude=lat, longitude=lng)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for("list_users"))

    return render_template("form.html")

@app.route("/list")
def list_users():
    users = User.query.all()
    return render_template("list.html", users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
