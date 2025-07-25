from flask import Flask, request, jsonify
from vertexai.generative_models import GenerativeModel
import vertexai

# Initialize Flask app
app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")
model = GenerativeModel("gemini-pro")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.json.get("prompt", "")
        if not user_input:
            return jsonify({"error": "No prompt provided"}), 400
        
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
