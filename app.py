from dataset import Database
import mysql.connector
from flask import Flask, request, make_response

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="***********",
    database="movies"
)

mycursor = db.cursor()

@app.route("/getallmovies/<filter>", methods=['GET'])
def getmovies(filter):
    if request.method == 'GET' and filter == "none":
        mycursor.execute("SELECT * FROM Movie")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        return str(myresult)
    elif request.method == 'GET' and filter == "release":
        mycursor.execute("SELECT * FROM Movie ORDER BY release_year desc")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        return str(myresult)
    elif request.method == "GET" and filter == "name":
        mycursor.execute("SELECT * FROM Movie ORDER BY name ASC")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        return str(myresult)

@app.route("/getmovie/<id>", methods=["GET"])
def getmoviefromid(id):
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Movie WHERE id=" + str(id))
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        return str(myresult) 

@app.route("/getmoviename/<id>", methods=["GET"])
def getmovienamefromid(id):
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Movie WHERE id=" + str(id))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
            return str(myresult[0][1]) 

@app.route("/getmoviereleaseyear/<id>", methods=["GET"])
def getMovieReleaseYearFromId(id):
    if request.method == "GET":
        mycursor.execute("SELECT * FROM Movie WHERE id=" + str(id))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
            return str(myresult[0][2])

@app.route("/deletemovie/<movieId>", methods=['DELETE'])
def deleteMovie(movieId):
    if request.method == "DELETE":
        sql = "DELETE FROM Movie WHERE id=" + movieId
        mycursor.execute(sql)
        db.commit()
        return "Successfully deleted movie!"

@app.route("/addmovie/<name>/<release_year>", methods=['POST'])
def addMovie(name, release_year):
    if request.method == "POST":
        sql = "INSERT INTO Movie (name, release_year) VALUES (%s, %s)"
        val = (name, release_year)
        mycursor.execute(sql, val)
        db.commit()
        return "Movie Added successfully!"

if __name__ == '__main__':
    app.run(debug=True)