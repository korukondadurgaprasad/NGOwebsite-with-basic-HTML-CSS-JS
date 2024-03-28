from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home .html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/join')
def join():
    return render_template('joinwithus.html')


if __name__ == '__main__':
    app.run(debug=True)