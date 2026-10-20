from flask import Flask, request, jsonify, render_template, Response
import requests
import json

# Initialize Flask App
app = Flask(__name__)

# 1. Main Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# 2. Fast Streaming Chat Route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    payload = {
        "model": "llama3.2:1b",  # Fast lightweight model
        "messages": [
            {"role": "system", "content": "You are Study Buddy, an expert, concise AI learning assistant."},
            {"role": "user", "content": user_message}
        ],
        "stream": True,  # Enables streaming responses live
        "options": {
            "num_predict": 250,  # Keeps answers concise for high speed
            "temperature": 0.7
        }
    }

    def generate():
        try:
            # Stream response directly from local Ollama service
            res = requests.post('http://localhost:11434/api/chat', json=payload, stream=True, timeout=60)
            for line in res.iter_lines():
                if line:
                    body = json.loads(line.decode('utf-8'))
                    content = body.get('message', {}).get('content', '')
                    yield content
        except Exception as e:
            yield f"\n[Error connecting to backend model: {str(e)}]"

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)