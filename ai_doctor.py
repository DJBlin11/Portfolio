import telebot
import openai
from promptify import Prompter

TELEGRAM_TOKEN = '...'
OPENAI_API_KEY = '...'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

doctor_prompt = Prompter(

    system = """You are an expert physician with years of experience in the most renowned clinic. 
    You are compassionate, attentive, and always prioritize the well-being of your patients. Your answers are always polite and positive""",
    
    user = """I'm your patient. 
    Based on my symptoms and health issues, please recommend a personalized treatment plan 
    or lifestyle changes that may help.."""
)

@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_message = "Hello! I am your virtual doctor. Please tell me about your health issues and symptoms."
    bot.send_message(message.chat.id, welcome_message)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = generate_response(message.text)
    bot.send_message(message.chat.id, response)

def generate_response(user_input):
    prompt = doctor_prompt.render(user=user_input)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].text.strip()



if __name__ == '__main__':
    bot.polling(none_stop=True)


