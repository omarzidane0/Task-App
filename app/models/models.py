from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extension import db


class users(db.Model):
    user_id = db.Column("user_id" , db.Integer , primary_key=True)
    user_name = db.Column("user_Fname" , db.String(80) , unique=True, nullable=False )
    password = db.Column("password" , db.String(300) , nullable=False)
    def __init__(self , user_name , password):
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return f"User ID : {self.user_id} User_name : {self.user_name}"
class tasks(db.Model):
    owner_id = db.Column("owner_id" , db.Integer)
    task_id = db.Column("task_id" , db.Integer , primary_key=True)
    task_title = db.Column("task_title" , db.String(300), nullable=False)
    task_description = db.Column("taksk_description" , db.String(6000))
    created_at = db.Column("created_at" , db.String(20), nullable=False)
    due_at = db.Column("due_at" , db.String(20), nullable=False)
    def __init__(self , owner_id , task_title , task_description , created_at , due_at):
        self.owner_id = owner_id
        self.task_title = task_title
        self.task_description = task_description
        self.created_at = created_at
        self.due_at = due_at
    def __repr__(self):
        return f"Owner_Id :  {self.owner_id} \nTaskTitle : {self.task_title}\nTaskDescription : {self.task_description}\nCreated_At : {self.created_at}\nDue_At : {self.due_at}"
     
def test():
    user1 = users( "omar" , "Oz0799178174@")
    db.session.add(user1)
    db.session.commit()
        