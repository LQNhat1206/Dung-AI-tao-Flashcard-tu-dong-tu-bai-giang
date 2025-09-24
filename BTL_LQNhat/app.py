from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret-key-demo"   # đổi key thực tế cho bảo mật
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

# ===== Model User =====
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# ===== Trang login/register =====
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("flashcards"))
    return render_template("login.html")

# ===== Đăng ký =====
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "Tên đăng nhập đã tồn tại"}), 400

    hashed = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Đăng ký thành công"})

# ===== Đăng nhập =====
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Sai tài khoản hoặc mật khẩu"}), 401

    session["user_id"] = user.id
    return jsonify({"message": "Đăng nhập thành công"})

# ===== Đăng xuất =====
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# ===== Trang flashcards =====
@app.route("/flashcards")
def flashcards():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("flashcards.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
