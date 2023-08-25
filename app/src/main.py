import fasttext
import config
from globals import *

from flask import Flask, jsonify
from flask import request
from summarizer import Summarizer
from transformers import MBartTokenizer, MBartForConditionalGeneration


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

classificator_model_ru = config.classificator_model_ru
summarize_model_ru = config.summarize_model_ru


model = fasttext.load_model(classificator_model_ru)

tokenizer_summary = MBartTokenizer.from_pretrained(summarize_model_ru)
model_summary = MBartForConditionalGeneration.from_pretrained(summarize_model_ru)


@app.route('/', methods=["GET"])
def healthcheck():
    return "healthy", 200


@app.route("/predict", methods=["POST"])
def predict_news():
    """"""
    news = request.json["news"]
    preds = model.predict(news)
    return preds[0], 200


@app.route("/summary", methods=["POST"])
def summary_news():
    """"""
    model_old_summary = Summarizer()
    text = request.json["text"]
    result = model_old_summary(text, ratio=0.3, num_sentences=1)
    return "".join(result), 200


@app.route("/summary_v2", methods=["POST"])
def summary_news():
    """"""
    print(request.json)
    text = request.json["text"]
    input_ids = tokenizer_summary(
        [text],
        max_length=SUMMARIZE_MAX_LENGTH_RU,
        padding=SUMMARIZE_PADDING_RU,
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model_summary.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=SUMMARIZE_NO_REPEAT_NGRAM_SIZE
    )[0]
    summary = tokenizer_summary.decode(output_ids, skip_special_tokens=True)

    return "".join(summary), 200
