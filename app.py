from flask import Flask, render_template
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    # Render the index.html template
    return render_template('index.html')

# Run the application in debug mode if this script is executed directly
if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)  # Set debug=True for development