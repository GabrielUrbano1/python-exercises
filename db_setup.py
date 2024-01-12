import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Specify a writable directory for data storage
data_directory = "/Users/gabrielurbano/Desktop/python-exercises/data"

# Create the data directory if it doesn't exist
os.makedirs(data_directory, exist_ok=True)

@app.route('/')
def show_form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    
    # Save the data locally
    with open(os.path.join(data_directory, 'data.txt'), 'a') as file:
        file.write(f"Name: {name}, Email: {email}\n")
    
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)