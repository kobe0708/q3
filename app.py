from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
registrations = []

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    registrations.append({'name': name, 'email': email})
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/registrations')
def list_registrations():
    return render_template('list.html', registrations=registrations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
