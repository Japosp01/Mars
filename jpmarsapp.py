from flask import Flask, render_template
# Import scraper
import jpmarsscrape

#  pymongo library, some sort of flask to mongo. Why, nobody knows.
import pymongo

# flask instant.
app = Flask(__name__)

# connection
conn = 'mongodb://mars_mission'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Route
@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template("index2.html", mars=mars)

# Scrape 
@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = jpmarsscrape.scrape()
    mars.update({}, mars_data)
    return "Ray Bradbury would be proud!"

if __name__ == "__main__":
    app.run(debug=True) 