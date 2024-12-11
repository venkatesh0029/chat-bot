# AI Chatbot

A conversational chatbot that can understand natural language queries and provide coherent responses using NLP techniques. This project uses the DialoGPT model from Microsoft for natural language understanding and generation.

## Features

- Natural language understanding and generation
- Real-time chat interface
- FastAPI backend with efficient response generation
- Modern and responsive UI
- Support for continuous conversation

## Technical Stack

- Backend: Python with FastAPI
- NLP: Transformers (DialoGPT model)
- Frontend: HTML, CSS, JavaScript
- Dependencies: PyTorch, Transformers, FastAPI

## Setup Instructions

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8000/static/index.html
   ```

## Usage

1. Type your message in the input field
2. Press Enter or click the Send button
3. Wait for the AI to generate a response
4. Continue the conversation naturally

## Model Information

The chatbot uses the DialoGPT-small model by default. You can modify the model size in `main.py` by changing the model name to:
- `microsoft/DialoGPT-medium` for better quality responses (slower)
- `microsoft/DialoGPT-large` for best quality responses (much slower)

## Customization

You can customize the following aspects:
- Model parameters in `main.py` (temperature, top_k, top_p)
- UI appearance in `static/style.css`
- Chat behavior in `static/script.js`
