from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prijzen')
def prijzen():
    items = [
        {
            "product": 'vanille-ijs 1 liter',
            "prijs": '€ 2,00'
        },
        {
            "product": 'chocolade-ijs 1 liter',
            "prijs": '€ 2,00'
        },
        {
            "product": 'aardbeien-ijs 1 liter',
            "prijs": '€ 2,00'
        },
        {
            "product": 'sundae (met slagroom en saus)',
            "prijs": '€ 3,50'
        },
        {
            "product": 'milkshake (vanille, chocolade of aardbei)',
            "prijs": '€ 3,00'
        },
        {
            "product": 'ijsje (1 bolletje)',
            "prijs": '€ 1,00'
        }
    ]
    return render_template('prijzen.html', items=items)

@app.route('/recepten')
def recepten():
    items = [
        {
            "recept": "tiramisu di nona",
            "img": "tiramisu.png"
        },
        {
            "recept": "ijstaart",
            "img": "ijstaart.png"
        }
    ]
    return render_template('recepten.html', items=items)

@app.route('/contact')
def contact():
    items = [
        {
            "type": "Adres",
            "info": "Bellesteynlaan 19, 2241WG Wassenaar"
        },
        {
            "type": "Telefoon",
            "info": "+31 6 21899466"
        },
        {
            "type": "Email",
            "info": "info@ijssalon.nl"
        }
    ]
    return render_template('contact.html', items=items)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    