from flask import render_template , redirect , url_for , session , request , Blueprint , make_response , jsonify
from app.models.models import test , users
from flask_jwt_extended import create_access_token , decode_token , JWTManager
from app.extension import db , csrf
from app.models.models import users,tasks
from datetime import datetime
home_bp = Blueprint("home" , __name__ , template_folder='templates', static_folder="static" ,static_url_path="/static_home")

@home_bp.route("/home", methods=["POST" , "GET"])
def home():
    token = request.cookies.get("access_token")
    if token == None:
        print("here1")
        return redirect(url_for("login.login"))
    if token:
        print("here")      
        try:
            print("trying to decode token")
            print(decode_token(token))
            print("TTT")
            user_id = decode_token(token)['sub']
            print(user_id)
            user = users.query.get(user_id)
            task = tasks.query.filter_by(owner_id=user_id).all()
            if task:
                print("ppo")
                return render_template("home.html" , taskat=task)
            else:
                return  render_template("home.html" )
        except Exception as e:
            print("Decode error:", e)
            response = make_response(redirect(url_for('login.login')))
            response.delete_cookie("access_token")
            return response
@csrf.exempt       
@home_bp.route("/addtask" , methods=["POST"])
def addtask():
    token = request.cookies.get("access_token")
    if not token:
        return jsonify({'success' : False})
    try:
        user_id = decode_token(token)['sub']
        data = request.get_json()
        if not data or "Task" not in data:
            return {'success' : False}
        if tasks.query.filter_by(owner_id=user_id , task_title= data['Task']['task_title'],task_description=data["Task"]["discrtiption"],due_at= data["Task"]["deadline"]).first():
            return {'success' : False}
        print(data['Task']["task_title"])
        now = datetime.now()
        formatted_time = now.strftime("%m/%d/%Y %I:%M:%p")
        print(repr(data["Task"]["deadline"]))
#        due_date = datetime.strptime(data["Task"]["deadline"], '%Y-%m-%d %H:%M').date()
 #       print(due_date + "this is the date")
        try:
            dt = datetime.strptime(data["Task"]["deadline"], '%Y-%m-%dT%H:%M').strftime('%m/%d/%Y %I:%M %p')
            print(dt)
        except Exception as e:
            print("Exception" + e)
        task = tasks(user_id , data['Task']['task_title'] , data["Task"]["discrtiption"] ,formatted_time ,dt)
        db.session.add(task)
        db.session.commit()
        return jsonify({'success' : True , "id":task.task_id ,"due_time":dt ,"created_at":formatted_time})
    except:
        return jsonify({'success' : False})

#@csrf.exempt
@home_bp.route("/remove_task" , methods=["DELETE"])
def task_remove():
    data = request.get_json()
    token = request.cookies.get("access_token")
    print(token)
    if not token:
        return {"redirect":url_for("login.login") , "success":False} , 401
    try:
        dt = decode_token(token)

    except:    
        response = make_response("deleting cookie !")
        response.delete_cookie("access_token")
        return {"redirect":url_for("login.login") , "success":False}
    try:
        print(data["task_id"])
        del_task = tasks.query.filter_by(owner_id=dt['sub'] ,task_id=data["task_id"] ).first()
        db.session.delete(del_task)
        db.session.commit()
        return  {"redirect":None , "success":True}    
    except:
        return {"redirect":None , "success":False , "id_task":data["task_id"]}

