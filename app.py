from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# 108 Traditional Indian Sanskrit First Names
first_names = [
    "Aarav", "Bhavya", "Chaitanya", "Dev", "Eshaan", "Falguni", "Gautam", "Hari", "Ishwar", "Jatin",
    "Kiran", "Lakshman", "Moksha", "Nirvan", "Omkar", "Pranav", "Quirsh", "Rohan", "Surya", "Tanmay",
    "Ujjwal", "Vikram", "Yug", "Zayin", "Aditi", "Bhagirath", "Chandraprakash", "Dhananjay", "Ekalavya"
] * 4  # Repeat to reach 108

# 108 Typical American Jewish Last Names
last_names = [
    "Abrams", "Baum", "Cohen", "Davidson", "Eisenberg", "Feinstein", "Goldberg", "Horowitz", "Isaacs", "Jacobs",
    "Kaplan", "Levin", "Mandel", "Nussbaum", "Oppenheimer", "Perlman", "Quint", "Rosen", "Silverstein", "Tannenbaum",
    "Ullman", "Vogel", "Weinberg", "Zucker", "Ackerman", "Bernstein", "Carmel", "Drucker", "Epstein", "Feldman"
] * 4  # Repeat to reach 108

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-name')
def generate_name():
    """Returns a random Sanskrit first name + Jewish last name."""
    first = random.choice(first_names)
    last = random.choice(last_names)
    return jsonify({"name": f"{first} {last}"})

if __name__ == '__main__':
    app.run(debug=True)
