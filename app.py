from chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    p=["The","current","time"]
    s=str(chatbot.get_response(userText))
    k=s.split()
    if k[:3]==p:
        return 'I am sorry, but I do not understand. I am still learning.'
    else:
        return s
if __name__ == "__main__":
    app.run() 
