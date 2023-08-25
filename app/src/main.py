import os
import fasttext

from typing import List
from collections import Counter
from flask import Flask, jsonify
from flask import request
from summarizer import Summarizer


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

model = fasttext.load_model("fasstext_90_recall_last.bin")


@app.route('/', methods=["GET"])
def healthcheck():
    return "healthy", 200


@app.route("/predict", methods=["POST"])
def predict_news():
    """"""
    print(request.json)
    news = request.json["news"]
    preds = model.predict(news)
    print(preds)
    return preds[0], 200


@app.route("/summary", methods=["POST"])
def summary_news():
    """"""
    print(request.json)
    model = Summarizer()
    text = request.json["text"]
    result = model(text, ratio=0.3, num_sentences=1)
    return "".join(result), 200
