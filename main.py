import openai
import requests
from decouple import config
from flask import Flask, render_template, request, jsonify

from common import bodys

app = Flask(__name__)

openai.api_key = config("OPENAI_API_KEY_FOUR")
openai.Model.list()

message = bodys.example


# def get_completion(prompt):
#     print(prompt)
#     query = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#
#     response = query.choices[0].text
#     return response


def get_other(prompt):
    print(prompt)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config('OPENAI_API_KEY')}"
    }
    response = requests.post(url='https://api.openai.com/v1/chat/completions',
                             json=message,
                             headers=headers)
    print(response.json())
    return jsonify({'response': response.json()})


# @app.route("/", methods=['POST', 'GET'])
# def query_view():
#     if request.method == 'POST':
#         print('step1')
#         prompt = request.form['prompt']
#         response = get_completion(prompt)
#         print(response)
#
#         return jsonify({'response': response})
#     return render_template('index.html')


@app.route("/second/", methods=['POST', 'GET'])
def second_query_view():
    if request.method == 'POST':
        print('step2')
        prompt = request.form['prompt']
        response = get_other(prompt)
        print(response)

        return jsonify({'response': response})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
