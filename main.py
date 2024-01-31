
# Import necessary modules
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    """Renders the home page."""
    # Render the index.html template
    return render_template('index.html')

# Define the route for the lessons page
@app.route('/lessons')
def lessons():
    """Renders the lessons page."""
    # Render the lessons.html template
    return render_template('lessons.html')

# Define the route for the quiz page
@app.route('/quiz')
def quiz():
    """Renders the quiz page."""
    # Render the quiz.html template
    return render_template('quiz.html')

# Define the route for the about page
@app.route('/about')
def about():
    """Renders the about page."""
    # Render the about.html template
    return render_template('about.html')

# Define the route for the contact page
@app.route('/contact')
def contact():
    """Renders the contact page."""
    # Render the contact.html template
    return render_template('contact.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
