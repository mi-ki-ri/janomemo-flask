from flask import Flask
from flask import request
from flask import render_template
from janome.charfilter import UnicodeNormalizeCharFilter

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter

app = Flask(__name__)
t = Tokenizer("user_dic.csv", udic_type="simpledic", udic_enc="utf8")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/post', methods=['POST'])
def hello():
    post_text = request.form['text']
    tags = []
    syurui="名詞"

    cf = [UnicodeNormalizeCharFilter()]#前処理フィルタ
    tf = [CompoundNounFilter(),POSKeepFilter([syurui])]
    a = Analyzer(char_filters=cf,token_filters=tf)#解析器生成

    for token in a.analyze(post_text):
        print(token)
        if token.part_of_speech.split(',')[1] == "固有名詞" or token.part_of_speech.split(',')[1] == "一般":
            tags.append(token.surface)

        

    ret_text = ""
    for tag in list(set(tags)):
        if len(tags) >= 2:
          ret_text += f'"{tag}",'

    ret_text = f"keywords: [{ret_text[:-1]}]"
    return ret_text
