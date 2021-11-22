# janomemo

1. `python3 -m venv venv`
1. `. /venv/bin/activate`
1. `pip install -r requirements.txt`
1. `export FLASK_APP=app.py`
1. `flask run`
1. フォームに入力して送信
1. キーワード列を得る


```sh
nkf -w jawiki-latest-all-titles-in-ns0 | grep -v '[!-/:-@≠\[-`{-~]' | grep -v '^[0-9]' | egrep -v '^[ぁ-ん]{2}' | grep -v 'の一覧' | grep -v '曖昧さ回避' | awk '{ print length($1),$1; }' | grep -v '1[[:space:]]' | sed -r 's/.*[[:space:]](.*)/\1,名詞,\1/g' > user_dic.csv

```