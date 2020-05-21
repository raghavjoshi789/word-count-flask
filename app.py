import os
import requests
import operator
import re
import nltk
from nltk.corpus import stopwords
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
#from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


from models import *
nltk.data.path.append('./nltk_data/')  # set the path
stops = stopwords.words('english')

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        try:
            headers = headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
            url = request.form['url']
            r = requests.get(url,headers=headers)
        except Exception as e:
            errors.append(
                f"Unable to get URL, Please make sure it's valid and try again.{type(e)}"
            )
            return render_template('index.html',errors=errors)

        if r:
            f = open('output.py','w')

            raw = BeautifulSoup(r.text, 'html.parser').get_text()
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            # remove punctuation, count raw words
            nonPunct = re.compile('.*[A-Za-z].*')
            raw_words = [w.lower() for w in text if nonPunct.match(w)]
            raw_word_count = Counter(raw_words)
            # stop words
            no_stop_words = [w for w in raw_words if w not in stops]
            no_stop_words_count = Counter(no_stop_words)
            # save the results
            results = sorted(
                no_stop_words_count.items(),
                key=operator.itemgetter(1),
                reverse=True
            )
            try:
                result = Result(
                    url=url,
                    result_all=raw_word_count,
                    result_no_stop_words=no_stop_words_count
                )
                db.session.add(result)
                db.session.commit()
            except Exception as e:
                errors.append(f"Unable to add item to database.{e}")
    return render_template('index.html',errors=errors,results=results)

if __name__ == "__main__":
    app.run()
