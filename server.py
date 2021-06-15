def flask_server():
    from flask import Flask, request, jsonify
    from flask_restful import Resource, Api
    from sqlalchemy import create_engine
    from json import dumps

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

    if __name__ == '__main__':
        app.run()

flask_server()
