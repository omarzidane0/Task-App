from flask import render_template , redirect , url_for , session , request , Blueprint , make_response ,jsonify
from app.extension import db
from app.models.models import users
from flask_wtf import CSRFProtect 
from app.extension import csrf
from flask_jwt_extended import create_access_token , decode_token , JWTManager
from app.extension import jwt
from app.utils.jwt_utils import createtoken , decodetoken

login_bp = Blueprint("login" , __name__ , template_folder='templates' , static_folder="static" , static_url_path="/static_login" )

@login_bp.route("/login" , methods=["POST","GET"])
def login():
    token = request.cookies.get("access_token")
    if not token:
        if request.method =="POST":
            username = request.form.get("username")
            password = request.form.get("password")
    
            if username == "" or password =="":
                return render_template("login.html" , errors="please fill all the fields")
            if users.query.filter_by(user_name=username).first() and username == users.query.filter_by(user_name=username).first().user_name:
                if password == users.query.filter_by(user_name=username).first().password:
                    token = createtoken(users.query.filter_by(user_name=username).first().user_id)
                    response = make_response(redirect(url_for("home.home")))
                    response.set_cookie("access_token" ,token ,secure=False, httponly=True )
                    print("تم إنشاء التوكن وإرساله بالكوكيز")
                    return response
                else:
                    return render_template("login.html" , errors="Wrong password")
            else:
                return render_template("login.html" , errors="Wrong UserName")
        return render_template("login.html")
    else:
        try:
            print("trying to decode token")
            print(decode_token(token))
            print("decoded succsess")
            return redirect(url_for("home.home"))      
        except Exception as e:
            print("Decode error:", e)
            response = make_response(redirect(url_for('login.login')))
            response.delete_cookie("access_token")
            return response
       
@login_bp.route("/logout" , methods=["POST"])
def logout():
        token = request.cookies.get("access_token")
        if not token:
            return {"success" : False}
        response = make_response(jsonify({"success": True}))
        response.delete_cookie("access_token")
       # response.set_cookie('access_token', '', expires=0, httponly=True , secure=True, samesite='Lax')
        return response
         