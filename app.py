from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Gaming Website!"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle form submission here
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # You can add logic to handle the form data, such as saving it to a database
        # For now, let's just print the values and redirect to a success page
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}")

        return redirect(url_for('home'))  # Redirect to home after signup
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission here
        username = request.form['username']
        password = request.form['password']

        # Add your authentication logic here
        print(f"Username: {username}")
        print(f"Password: {password}")

        return redirect(url_for('home'))  # Redirect to home after login
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)