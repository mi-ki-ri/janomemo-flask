from flask import Flask
from flask import request
from flask import render_template

from janome.tokenizer import Tokenizer


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/post', methods=['POST'])
def hello():
    t = Tokenizer()
    post_text = request.form['text']
    tags = []
    for token in t.tokenize(f"{post_text}"):
      print(token)
      if token.part_of_speech.split(',')[0] == "名詞" and (token.part_of_speech.split(",")[1] == "一般" or token.part_of_speech.split(",")[1] == "固有名詞" ):
        tags.append(token.surface)

    ret_text = ""
    for tag in list(set(tags)):
      ret_text += f'"{tag}",'

    ret_text = f"keywords: [{ret_text[:-1]}]"
    return ret_text
