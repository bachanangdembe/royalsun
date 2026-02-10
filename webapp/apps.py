from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

latest_location = {
    "lat": None,
    "lng": None
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    latest_location["lat"] = data.get("lat")
    latest_location["lng"] = data.get("lng")
    return jsonify({"status": "ok"})

@app.route("/get_location")
def get_location():
    return jsonify(latest_location)

if __name__ == "__main__":
    app.run(debug=True)
