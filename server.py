from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import webbrowser

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

def comments():
    #!/usr/bin/python3
    # link: https://github.com/sreegithub19/python_rest_flask
    # http://127.0.0.1:5000/employees/5  ;  http://127.0.0.1:5000/list_of_tables
    # https://jsonbeautifier.org/?id=  - online json beautifier
    # https://www.sqlitetutorial.net/sqlite-sample-database/  - about chinook database
    # https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/  - another sample example
    a = 2+3   # this line is written to just avoid IndentationError  
comments()

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                            '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                            '{13}')".format(LastName,FirstName,Title,
                            ReportsTo, BirthDate, HireDate, Address,
                            City, State, Country, PostalCode, Phone, Fax,
                            Email))
        return {'status':'success'}

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Tracks_all(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Tracks_id(Resource):
    def get(self,track_id):
        conn = db_connect.connect()
        query = conn.execute("select * from tracks where TrackId=%d ;" %int(track_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Tracks_all(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Playlists(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from playlists;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Artists(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from artists;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Albums(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from albums;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Invoices(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from invoices;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Customers(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from customers;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class List_of_tables(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class SQLite_stat(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * from sqlite_stat1;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

def routes():
    api.add_resource(Employees, '/employees') # Route_1
    api.add_resource(Tracks, '/tracks') # Route_2
    api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
    api.add_resource(Tracks_all, '/tracks_all') #Route_4
    api.add_resource(Tracks_id, '/tracks/<track_id>')  #Route_5
    api.add_resource(Playlists, '/playlists')    #Route_6
    api.add_resource(Artists, '/artists')       #Route_7
    api.add_resource(Albums, '/albums')     #Route_8
    api.add_resource(Invoices, '/invoices')     #Route_9
    api.add_resource(Customers, '/customers')      #Route_10
    api.add_resource(List_of_tables, '/list_of_tables')  #Route_11
    api.add_resource(SQLite_stat, '/sqlite_stat1')     #Route_12
routes()

@app.route('/')
def run_code_1():
    return "<!DOCTYPE html> <html> <head> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <style> body, html { height: 100%; margin: 0; } .content { position: absolute; top: 15%; left:25%; background: rgb(0, 0, 0); /* Fallback color */ background: rgba(0, 0, 0, 0.76); /* Black background with 0.5 opacity */ color: #f1f1f1; width: 50%; padding: 20px; } .bg { /* The image used */ background-image: url(\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcRqNquWxQHJAPgugDwzXokAU_dQUXzknUTA&usqp=CAU\"); /* Full height */ height: 100%; /* Center and scale the image nicely */ background-position: center; background-repeat: no-repeat; background-size: cover; } table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } div.parent { text-align: center; } ul { display: inline-block; text-align: left; }</style>\
     </head> <body> <div class=\"bg\"></div>  <div class=\"content\"> <h1 id=\"home\" \
         style=\"text-align: center;font-weight: bold;text-decoration: underline;\">\
             WELCOME TO PYTHON REST API!</h1> \
    <h3 style=\"text-align:center;\"> Click on any of the below links</h3>\
    <div class=\"parent\"> <ul>\
         <li><a href='http://127.0.0.1:5000/employees'>Employees (8 employees)</a></li> \
        <li><a href='http://127.0.0.1:5000/employees/1'>Employee Info by Id</a></li>\
         <li><a href='http://127.0.0.1:5000/tracks'>Tracks Info from some columns</a></li>\
        <li><a href='http://127.0.0.1:5000/tracks_all'>Tracks Info from all columns (3503 tracks)</a></li>\
            \
        <li><a href='http://127.0.0.1:5000/tracks/1'>Tracks Info by Id</a></li>\
        <li><a href='http://127.0.0.1:5000/playlists'>Playlists Info (18 playlists)</a></li>\
        <li><a href='http://127.0.0.1:5000/artists'>Artists Info (275 artists)</a></li>\
        <li><a href='http://127.0.0.1:5000/albums'>Albums Info (347 albums)</a></li>\
        <li><a href='http://127.0.0.1:5000/invoices'>Invoice Info (412 invoices)</a></li>\
        <li><a href='http://127.0.0.1:5000/customers'>Customers Info (59 customers)</a></li>\
        <li><a href='http://127.0.0.1:5000/list_of_tables'>List of all tables of Chinook database (13 tables)</a></li>\
        <li><a href='http://127.0.0.1:5000/sqlite_stat1'>Sqlite stat1 (15)</a></li>\
            \
    </ul> </div> \
        </div> </body> </html>"

webbrowser.open('http://127.0.0.1:5000/')
if __name__ == '__main__':
        app.run()



