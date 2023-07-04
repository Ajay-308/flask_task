from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

mongo_url='mongodb+srv://AJAYKUMAR:AJAY2001@blogging.zwdh3ol.mongodb.net/?retryWrites=true&w=majority'


DB_NAME = 'student'
COLLECTION_NAME = 'submission'

# Connect to MongoDB
client = MongoClient(mongo_url)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]






@app.route('/', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        college = request.form.get('college')
        Branch = request.form.get('Branch')

        submission = {"name": name, "college": college, "Branch": Branch}
        collection.insert_one(submission)

        # # Add SweetAlert script to display a success message
        return render_template('success.html')
    submissions = collection.find()
    return render_template('intern.html', submissions=submissions)


if __name__ == '__main__':
    app.run(debug=True)
