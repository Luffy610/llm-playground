# 🧠 CrewAI WebSocket API

A FastAPI-based backend that exposes a WebSocket endpoint to run a CrewAI-powered report generator in real time. Send a topic via WebSocket and receive a generated report instantly.

## 🚀 Features

- WebSocket endpoint for real-time interaction
- Dynamic topic input for report generation
- Simple integration with any frontend (HTML/JS, React, etc.)


## ⚡ Quick Start

1. **Install dependencies:**
    ```bash
    pip install fastapi uvicorn
    ```

2. **Run the API server:**
    ```bash
    uvicorn crewai_with_websocket.api.main:app --reload
    ```

3. **Test the WebSocket:**
    - Connect to `ws://localhost:8000/ws/run-crew`
    - Send a topic string (e.g., `AI LLMs`)
    - Receive a JSON response with the generated report

## 🧪 Example Frontend

You can use a simple HTML/JS client to test the WebSocket endpoint. Save the following as `test.html` and open it in your browser:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Crew WebSocket Test</title>
</head>
<body>
    <h2>Crew WebSocket Test</h2>
    <label for="topic">Topic:</label>
    <input type="text" id="topic" value="AI LLMs">
    <button id="connectBtn">Connect</button>
    <button id="sendBtn" disabled>Send Topic</button>
    <pre id="output"></pre>

    <script>
        let ws;

        document.getElementById('connectBtn').onclick = function() {
            ws = new WebSocket('ws://localhost:8000/ws/run-crew');
            ws.onopen = function() {
                document.getElementById('output').textContent = 'Connected\n';
                document.getElementById('sendBtn').disabled = false;
            };
            ws.onmessage = function(event) {
                document.getElementById('output').textContent += 'Response: ' + event.data + '\n';
            };
            ws.onclose = function() {
                document.getElementById('output').textContent += 'Disconnected\n';
                document.getElementById('sendBtn').disabled = true;
            };
            ws.onerror = function(e) {
                document.getElementById('output').textContent += 'Error\n';
            };
        };

        document.getElementById('sendBtn').onclick = function() {
            const topic = document.getElementById('topic').value;
            ws.send(topic);
            document.getElementById('output').textContent += 'Sent: ' + topic + '\n';
        };
    </script>
</body>
</html>