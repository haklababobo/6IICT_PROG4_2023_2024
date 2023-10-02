from flask import Flask, jsonify

app = Flask(__name__)

aarde = {
    "Naam": "Aarde",
    "Type": "Planeet",
    "Leeftijd": "4,5 miljard jaar",
    "Diameter": "12.742 km",
    "Bevolking": "7,9 miljard (2021)",
    "Atmosfeer": ["N2 (78,08%)", "O2 (20,95%)", "CO2 (0,04%)"]
}

@app.route('/aarde', methods=['GET'])
def get_aarde():
    return jsonify(aarde)

if __name__ == '__main__':
    app.run(debug=True)

with open("aarde.json", "r") as file:
    aarde_info = json.load(file)