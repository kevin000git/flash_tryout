from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return ("welkom op mijn opdracht pagina van hoofdstuk 11")




if __name__ == '__main__':
    app.run(port=5000, debug=True)
    

