

# import necessary libraries
from flask import Flask, render_template,redirect
#import scrape_mars
import pymongo
import scrape_mars



# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.Mars_db
collection = db.items



# create instance of Flask app
app = Flask(__name__)



# create route that renders index.html template
@app.route("/")
def index():
    mars = list(collection.find())
    print(type(mars[-1]))
    print(mars[-1])
    return render_template("index.html", mars=mars[-1])
     

#create route that does the scrape and stored the returned value in Mongodb    
@app.route("/scrape")
def scrape():
    data=scrape_mars.scrape()
    collection.insert_one(data)
    # mars.update({},data,upsert=True)
    return redirect("/",code=302)


    

   
if __name__ == "__main__":
    app.run(debug=True)
