

# import necessary libraries
from flask import Flask, render_template,redirect
import mars
import pymongo



# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.Mars_db
collection = db.items


# create instance of Flask app
app = Flask(__name__)
mongo=pymongo(app)


# create route that renders index.html template
@app.route("/")
def Mars():
     
    return "Hello"
    
@app.route("/scrape")
def scrape():
    dict=mongo.db.dict
    data=mars.scrape()
    dict.update({},data,upsert=True)
    return redirect("/",code=302)
    
    


    #  # write a statement that finds all the items in the db and sets it to a variable
    # mars_info= list(collection.find())
    # print(mars_info)

    # # render an index.html template and pass it the data you retrieved from the database
    # return render_template("index.html", mars_info=mars_info)


if __name__ == "__main__":
    app.run(debug=True)
