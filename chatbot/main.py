from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random
import re

class ChatbotResponse:
    # Greeting patterns and responses
    greetings = {
        "hello": ["Hello! How can I help you today?", "Hi there! What's on your mind?", "Hey! Nice to meet you!"],
        "hi": ["Hi! How are you doing?", "Hello! How can I assist you?", "Hey there! What can I help you with?"],
        "hey": ["Hey! What's up?", "Hello! Ready to chat?", "Hi there! How can I help?"],
        "good morning": ["Good morning! How are you today?", "Morning! Hope you're having a great day!", "Good morning! What can I do for you?"],
        "good afternoon": ["Good afternoon! How can I help?", "Hi there! Having a good afternoon?", "Good afternoon! What's on your mind?"],
        "good evening": ["Good evening! How can I assist you?", "Evening! What can I help you with?", "Good evening! How are you?"]
    }

    # Topic-based responses
    topics = {
        "weather": ["The weather can really affect our mood, can't it?", "Do you enjoy this kind of weather?", "What's your favorite type of weather?"],
        "music": ["Music is a universal language! What genres do you enjoy?", "Do you play any instruments?", "Who are your favorite artists?"],
        "movies": ["Movies are a great way to escape! What's your favorite genre?", "Have you watched any good movies lately?", "What's your all-time favorite film?"],
        "food": ["Food is always an interesting topic! What cuisine do you prefer?", "Do you enjoy cooking?", "What's your favorite dish?"],
        "work": ["Work can be quite challenging sometimes. How's your work going?", "What do you like most about your job?", "What field do you work in?"],
        "hobby": ["Hobbies are important for balance in life! What do you enjoy doing?", "That's an interesting hobby! How did you get started?", "Do you have any other hobbies?"]
    }

    # Question patterns and responses
    question_patterns = {
        "what": ["That's an interesting question about {}", "Let me help you understand {}", "Good question about {}"],
        "how": ["I'll explain how {} works", "Let me break down how {}", "Here's my understanding of how {}"],
        "why": ["The reason for {} is interesting", "Let me explain why {}", "There are several reasons why {}"],
        "when": ["Regarding when {}", "The timing of {} depends on several factors", "Let's talk about when {}"],
        "where": ["The location of {} is important", "Let me tell you about where {}", "When it comes to where {}"],
        "who": ["Let me tell you about who {}", "The person {} is interesting", "When it comes to who {}"]
    }

    # General responses for various situations
    general_responses = [
        "That's an interesting perspective! Could you tell me more about it?",
        "I understand what you're saying. How does that make you feel?",
        "That's fascinating! What made you think about this?",
        "I'd love to hear more about your thoughts on this.",
        "That's a unique point of view! How did you come to that conclusion?",
        "Could you elaborate on that? I'm quite interested.",
        "What aspects of this topic interest you the most?",
        "That's quite thought-provoking! What else do you think about it?",
        "I appreciate you sharing that. What other insights do you have?",
        "That's an interesting way to look at it. What led you to this understanding?"
    ]

    @staticmethod
    def get_response(message):
        message = message.lower().strip()

        # Check for greetings
        for greeting, responses in ChatbotResponse.greetings.items():
            if greeting in message:
                return random.choice(responses)

        # Check for questions
        question_words = ["what", "how", "why", "when", "where", "who"]
        if any(message.startswith(word) for word in question_words) or "?" in message:
            # Extract the main topic from the question
            topic = message.split()[1] if len(message.split()) > 1 else "that"
            for word, patterns in ChatbotResponse.question_patterns.items():
                if message.startswith(word):
                    return random.choice(patterns).format(topic)

        # Check for topics
        for topic, responses in ChatbotResponse.topics.items():
            if topic in message:
                return random.choice(responses)

        # If no specific pattern is matched, return a general response
        return random.choice(ChatbotResponse.general_responses)

class ChatbotHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()
        
    def do_GET(self):
        if self.path == '/':
            with open('static/index.html', 'rb') as file:
                content = file.read()
            self._set_headers()
            self.wfile.write(content)
        elif self.path.startswith('/static/'):
            try:
                with open(self.path[1:], 'rb') as file:
                    content = file.read()
                self._set_headers('text/css' if self.path.endswith('.css') else 'text/javascript')
                self.wfile.write(content)
            except:
                self.send_error(404, 'File not found')

    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Generate response using the ChatbotResponse class
            response = ChatbotResponse.get_response(data['message'])
            
            # Send response
            self._set_headers('application/json')
            self.wfile.write(json.dumps({'response': response}).encode())

def run(server_class=HTTPServer, handler_class=ChatbotHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting chatbot server on port {port}...')
    print(f'Open your browser and go to http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
