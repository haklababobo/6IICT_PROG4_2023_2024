from flask import Flask, request, jsonify

app = Flask(__name__)

# TODO-lijst
todo = [
    "Boodschappen",
    "cadeau kopen",
    "Doktersafspraak maken"
]

# Endpoint om een specifieke taak op te halen op basis van de index
@app.route('/toon_todo', methods=['GET'])
def toon_todo():
    index = request.args.get('index')
    try:
        index = int(index)
        if 0 <= index < len(todo):
            return jsonify({"todo": todo[index]})
        else:
            return jsonify({"todo": "Kan deze todo niet vinden"})
    except ValueError:
        return jsonify({"todo": "Ongeldige index"})

if __name__ == '__main__':
    app.run(debug=True)
