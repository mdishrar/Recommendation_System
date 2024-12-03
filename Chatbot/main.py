from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

# API endpoint for fetching careers
CAREERS_API_URL = 'http://localhost:5000/careers'  # Replace with your actual API endpoint

def fetch_careers():
    """Fetch careers from the API and organize by domain"""
    try:
        response = requests.get(CAREERS_API_URL)
        if response.status_code == 200:
            all_careers = response.json()['careers']
            
            # Organize careers by domain
            CAREER_DATA = {
                'CS': [],
                'IT': [],
                'ECE': []
            }
            
            for career in all_careers:
                domain = career['domain']
                if domain in CAREER_DATA:
                    CAREER_DATA[domain].append({
                        'role': career['role'],
                        'description': career['description'],
                        'skills': career['skills'],
                        'average_salary': career['average_salary'],
                        'growth_potential': career['growth_potential']
                    })
            
            return CAREER_DATA
        else:
            print(f"Error fetching careers: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error connecting to careers API: {e}")
        return None

# Conversation flow remains the same as in the original script
CONVERSATION_STEPS = [
    {
        'id': 'welcome',
        'message': "Welcome to the Technology Career Recommendation Chatbot! What's your name?",
        'type': 'input'
    },
    {
        'id': 'field_interest',
        'message': lambda name: f"Hi {name}! Which technology field interests you most? (CS/IT/ECE)",
        'type': 'select'
    },
    {
        'id': 'skill_assessment',
        'message': lambda field: f"Great choice! What skills do you currently have in {field}?",
        'type': 'input'
    }
]

class ChatbotSession:
    def __init__(self):
        self.current_step = 0
        self.user_responses = {}
        self.conversation_history = []
        self.CAREER_DATA = fetch_careers() or {}  # Fetch careers on initialization

    def process_input(self, user_input):
        current_step = CONVERSATION_STEPS[self.current_step]

        if current_step['id'] == 'welcome':
            self.user_responses['name'] = user_input
            response = current_step['message'].replace("What's your name?", f"Hi {user_input}! Which technology field interests you most? (CS/IT/ECE)")
            self.current_step += 1
            return response

        elif current_step['id'] == 'field_interest':
            field = user_input.upper()
            if field in ['CS', 'IT', 'ECE']:
                self.user_responses['field'] = field
                response = f"Great choice! What skills do you currently have in {field}?"
                self.current_step += 1
                return response
            else:
                return "Please enter a valid field: CS, IT, or ECE"

        elif current_step['id'] == 'skill_assessment':
            # Find matching careers based on skills
            field = self.user_responses['field']
            recommendations = [
                career for career in self.CAREER_DATA.get(field, [])
                if any(skill.lower() in user_input.lower() for skill in career['skills'])
            ]

            if recommendations:
                response = f"Based on your skills, here are some recommended careers in {field}:\n\n"
                for rec in recommendations:
                    response += (
                        f"🌟 {rec['role']}\n"
                        f"Description: {rec['description']}\n"
                        f"Avg Salary: {rec['average_salary']}\n"
                        f"Growth Potential: {rec['growth_potential']}\n\n"
                    )
                return response
            else:
                return f"No direct matches found. Consider exploring entry-level roles in {field} or expanding your skill set."

# Global session storage (in a real app, use session management)
current_session = ChatbotSession()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global current_session
    user_input = request.json['message']
    
    # Process input and get response
    bot_response = current_session.process_input(user_input)
    
    return jsonify({
        'response': bot_response
    })

@app.route('/reset', methods=['POST'])
def reset():
    global current_session
    current_session = ChatbotSession()
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)