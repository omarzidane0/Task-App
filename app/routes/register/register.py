from flask import Flask , render_template , redirect , url_for , session, request , Blueprint ,jsonify
from app.extension import db
from app.models.models import users , test
from flask_wtf import CSRFProtect 
from app.extension import csrf
from flask_jwt_extended import decode_token
from app.extension import jwt

register_bp = Blueprint("register" , __name__ , template_folder='templates' , static_folder="static" , static_url_path="/static_register")


@register_bp.route("/register" , methods=["POST" , "GET"])
def register():
    token = request.cookies.get("access_token")
    if not token:
        if request.method =="POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if username == "" or password == "":
                return render_template("register.html" , errors="please fill all the fields")
            user = users.query.filter_by(user_name=username).first()
            if user and username == user.user_name:
                return render_template("register.html", errors="User Name Is Already Exist")
            try:
                user = users(username , password)
                db.session.add(user)
                db.session.commit()
            except Exception as e:
            
                return render_template("register.html", errors="Error connecting to server , Please Try Again later")
            return redirect(url_for("login.login"))
        return render_template("register.html")
    else:
        try:
            decode_token(token)
            return redirect(url_for("home.home"))
        except:
            return redirect(url_for("login.login"))

#ajax route
@csrf.exempt
@register_bp.route('/check_username', methods=['POST'])
def check_username():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'No username provided'}), 400
    
    user = data['username']
    existing_user = users.query.filter_by(user_name=user).first()

    if existing_user:
        return jsonify({'exists': True, 'message': 'Username already taken'})
    else:
        return jsonify({'exists': False})