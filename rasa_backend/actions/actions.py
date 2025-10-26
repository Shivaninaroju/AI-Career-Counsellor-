# actions.py
import random
from typing import List, Dict, Any, Text

# Same career and knowledge mapping as before
GENERAL_KNOWLEDGE = {
    "hello": ["Hi there! How can I help you today?", "Hello! Ready to explore your career options?"],
    "hi": ["Hello! What are your interests?", "Hi! Tell me what you love doing."],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "Feeling ready to help you find a career!"],
    "what is ai": ["AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines."],
    "what is ml": ["ML is Machine Learning, a subset of AI that allows machines to learn from data."],
    "thank you": ["You're welcome!", "Happy to help!"]
}

CAREER_MAPPING = {
    "ai": ["Data Scientist", "ML Engineer", "AI Researcher"],
    "ml": ["Data Scientist", "ML Engineer", "AI Researcher"],
    "web": ["Web Developer", "Full Stack Developer", "UI/UX Designer"],
    "frontend": ["Frontend Developer", "UI/UX Designer"],
    "backend": ["Backend Developer", "Full Stack Developer"],
    "data": ["Data Analyst", "Business Analyst", "BI Developer"],
    "analytics": ["Data Analyst", "Business Analyst"],
    "singing": ["Music Producer", "Sound Engineer", "Composer"],
    "videogames": ["Game Developer", "Game Designer", "3D Artist"],
    "writing": ["Content Writer", "Copywriter", "Editor"],
    "art": ["Graphic Designer", "Illustrator", "Animator"],
    "design": ["Graphic Designer", "UI/UX Designer", "Animator"],
    "marketing": ["Digital Marketer", "SEO Specialist", "Content Strategist"],
    "business": ["Business Analyst", "Project Manager", "Consultant"],
    "finance": ["Financial Analyst", "Accountant", "Investment Banker"],
    "healthcare": ["Nurse", "Medical Technician", "Healthcare Administrator"],
    "biology": ["Biologist", "Lab Technician", "Research Scientist"],
    "chemistry": ["Chemist", "Pharmacist", "Lab Technician"],
    "cloud computing": ["Cloud Engineer", "DevOps Engineer", "Cloud Architect"],
    "cybersecurity": ["Cybersecurity Analyst", "Security Engineer", "Penetration Tester"],
    "photography": ["Photographer", "Photo Editor", "Visual Content Creator"]
    }

class ActionSmartChat:
    def name(self) -> Text:
        return "action_smart_chat"

    def run(self, dispatcher, tracker, domain: Dict[Text, Any] = {}) -> None:
        user_msg = tracker.latest_message.get('text', '').lower()

        # Career suggestions
        for keyword, careers in CAREER_MAPPING.items():
            if keyword in user_msg:
                career_suggestions = ", ".join(careers)
                dispatcher.utter_message(
                    text=f"Based on your interest in {keyword.upper()}, you can consider careers like: {career_suggestions}."
                )
                return []

        # General knowledge
        for key, responses in GENERAL_KNOWLEDGE.items():
            if key in user_msg:
                dispatcher.utter_message(text=random.choice(responses))
                return []

        # Fallback
        fallback_responses = [
            "That's interesting! Can you tell me more about your interests?",
            "Hmm, I need more info to suggest a career. What are your hobbies or skills?",
            "I'm learning every day! Can you rephrase your question?"
        ]
        dispatcher.utter_message(text=random.choice(fallback_responses))
        return []
