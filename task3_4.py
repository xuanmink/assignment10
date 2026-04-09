from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/prime_number/<int:num>')
def prime(num):
    is_prime = True
    if num <= 1:
        is_prime = False
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return jsonify({"Number": num, "isPrime": is_prime})

@app.route('/airport/<code>')
def airport(code):
    f = open("airports.json", "r", encoding="utf-8")
    data = json.load(f)
    f.close()
    if code in data:
        return jsonify({"icao": code, "name": data[code]["name"], "city": data[code]["city"], "country": data[code]["country"]})
    return jsonify({"message": "Not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)