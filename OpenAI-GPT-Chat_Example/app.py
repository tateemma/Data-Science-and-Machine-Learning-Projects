import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        human = request.form["human"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(human),
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(human):
    return """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
        Human: Hello, who are you?
        AI: I am an AI created by OpenAI. How can I help you today?
        Human: {}
        AI:""".format(human)
