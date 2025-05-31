from flask import render_template , redirect , url_for , session , request , Blueprint , make_response , jsonify
from app.models.models import test , users
from flask_jwt_extended import create_access_token , decode_token , JWTManager
from app.extension import db , csrf
from app.models.models import users,tasks
from datetime import datetime
# blue print
home_bp = Blueprint("home" , __name__ , template_folder='templates', static_folder="static" ,static_url_path="/static_home")

@home_bp.route("/home", methods=["POST" , "GET"])
def home():
    token = request.cookies.get("access_token")
    # checking if is there a token?
    if token == None:
       
        return redirect(url_for("login.login"))
    if token:
  
        # checking if token is valid    
        try:
            
            decode_token(token)
        
            user_id = decode_token(token)['sub']
          
            user = users.query.get(user_id)
            #taking all tasks from the db
            task = tasks.query.filter_by(owner_id=user_id).all()
            # render the page
            if task:
               
                return render_template("home.html" , taskat=task)
            else:
                return  render_template("home.html" )
        except Exception as e:
            print("Decode error:", e)
            # if there is error decoding the token remove it from cookies & redirect to the login page
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
    
        now = datetime.now()
        formatted_time = now.strftime("%m/%d/%Y %I:%M:%p")
      
        try:
            dt = datetime.strptime(data["Task"]["deadline"], '%Y-%m-%dT%H:%M').strftime('%m/%d/%Y %I:%M %p')
           
        except Exception as e:
            print("Exception" + e)
        task = tasks(user_id , data['Task']['task_title'] , data["Task"]["discrtiption"] ,formatted_time ,dt)
        db.session.add(task)
        db.session.commit()
        return jsonify({'success' : True , "id":task.task_id ,"due_time":dt ,"created_at":formatted_time})
    except:
        return jsonify({'success' : False})


@home_bp.route("/remove_task" , methods=["DELETE"])
def task_remove():
    data = request.get_json()
    token = request.cookies.get("access_token")
    
    # if there is no token
    if not token:
        return {"redirect":url_for("login.login") , "success":False} , 401
     # checking if token is valid
    try:
        dt = decode_token(token)

    except:    
        response = make_response("deleting cookie !")
        response.delete_cookie("access_token")
        return {"redirect":url_for("login.login") , "success":False}
    try:
        print(data["task_id"])
        #deleteing the task from the db after checking whos the owner 
        del_task = tasks.query.filter_by(owner_id=dt['sub'] ,task_id=data["task_id"] ).first()
        db.session.delete(del_task)
        db.session.commit()
        return  {"redirect":None , "success":True}    
    except:
        return {"redirect":None , "success":False , "id_task":data["task_id"]}

