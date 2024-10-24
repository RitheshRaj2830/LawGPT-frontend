from flask import Flask, render_template

app = Flask(__name__)

# Route for the first HTML page
@app.route('/')
def page1():
    return render_template('main.html')

# Route for the second HTML page
@app.route('/chatbot')
def page2():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
