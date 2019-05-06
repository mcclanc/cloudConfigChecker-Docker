#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os
import sqlite3

exists = os.path.isfile('./casdeployments.db')

if exists:
  print("DB Already Exists")
else:
  conn = sqlite3.connect('casdeployments.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE DEPLOYMENTS ([generated_id] INTEGER PRIMARY KEY,[DeploymentName] text, [Status] text)''')
  conn.commit()


db_connect = create_engine('sqlite:///casdeployments.db')
app = Flask(__name__)
api = Api(app)


class DEPLOYMENTS(Resource):
    def get(self, deployment_name):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select Status from DEPLOYMENTS where DeploymentName='%s'" %(deployment_name)) # This line performs query and returns json result
        row = (query.cursor.fetchone())
        if row == None:
            return {'status': 'Not Done'}, 210
        else:
            query = conn.execute("select Status from DEPLOYMENTS where DeploymentName='%s'" %(deployment_name))
            for i in query.cursor.fetchall():
                depres = (i[0])
                return {'status': depres}



class DEPLOYMENTPUSH(Resource):
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        DeploymentName= request.json['DeploymentName']
        Status = request.json['Status']
        query = conn.execute("insert into DEPLOYMENTS values(null,'{0}','{1}')".format(DeploymentName,Status))
        return {'status':'success'}, 201


api.add_resource(DEPLOYMENTS, '/deployments/<string:deployment_name>') # Route_1
api.add_resource(DEPLOYMENTPUSH, '/deploymentpush') # Route_2

if __name__ == '__main__':
     app.run(host='0.0.0.0')
