from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://magdaz:Ksdbk8273Jhb@mottahost.ddns.net/sadzonki_madzia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PlantDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100))
    data_wysiewu = db.Column(db.Date)
    do_doniczki = db.Column(db.Boolean)
    do_gruntu = db.Column(db.Boolean)
    data_rozsadzania = db.Column(db.String(100))
    rodzaj_ziemi = db.Column(db.String(100))
    producent = db.Column(db.String(100))


@app.route('/')
def index():
    plant1 = PlantDatabase(nazwa='Pomidor', data_wysiewu='2024-02-04', do_doniczki=True, do_gruntu=True, data_rozsadzania='2022-01-01', rodzaj_ziemi='Uniwersalna ziemia ogrodnicza', producent='Świat kwiatów')
    plant2 = PlantDatabase(nazwa='ogórek', data_wysiewu='2024-02-04', do_doniczki=True, do_gruntu=True, data_rozsadzania='2022-01-01', rodzaj_ziemi='Uniwersalna ziemia ogrodnicza', producent='Świat kwiatów')
    plant3 = PlantDatabase(nazwa='Arbuz', data_wysiewu='2024-02-04', do_doniczki=True, do_gruntu=True, data_rozsadzania='2022-01-01', rodzaj_ziemi='Uniwersalna ziemia ogrodnicza', producent='Świat kwiatów')


    db.session.add(plant1)
    db.session.add(plant2)
    db.session.add(plant3)
    db.session.commit()

    plants = PlantDatabase.query.all()

    return render_template('index.html', rosliny=plants)

if __name__ == "__main__":
    app.run(debug=True)
