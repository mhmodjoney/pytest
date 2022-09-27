
from turtle import update
from urllib import request
from flask import Flask
from flask_restful import Api, Resource
import time
import facebook as fb
from hcopy import coment_after_cheak, get_comment
import requests
import json


x11=True

app = Flask(__name__)
api= Api(app)

class stop(Resource):
    def get(self):
        global  x11
        x11=not x11
        return{"data":"stoped...."}

class run(Resource):
    def get(self):
        while (x11):
        # print(url)
            get_comment()
            commentID=[]
            coment_after_cheak()
            time.sleep(3)
        return{"data":"running....."}



api.add_resource(run,"/run")
api.add_resource(stop,"/stop")



if __name__=="__main__":
    app.run(debug=True)