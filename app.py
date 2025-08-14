from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from External LLM Docker App!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    return jsonify({"input": text, "prediction": text[::-1]})  # Example: reverse string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
