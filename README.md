# News Predictions

Flask application with models for classification and summarization of news in Russian.

## Description

The application contains two handlers with calls to the text classification model (/predict) and the summarization model (/summary_v2)

- /predict: Uses trained `fasttext` model for classification
- /summary: We use a [model]((https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)) pre-trained on the dataset of russian news `mbart_ru_sum_gazeta`

The application is used to operate another application - a telegram [bot](https://t.me/news_filtering_bot) and placed in a [separate repository](https://github.com/aspnmrv/telegram_bot_news)

## About the code:

This project is a modular bot, made using Python 3 and the following:

- [FastText](https://fasttext.cc/docs/en/python-module.html)
- Pre-trained model [mbart_ru_sun_gazeta](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)


## Setting up

Before all, clone this repository.

You need to have a trained fasttext classification model and filling congig.yml file:

```
CLASSIFICATOR_MODEL_RU: "fasstext_model.bin"
SUMMARIZE_MODEL_RU: "IlyaGusev/mbart_ru_sum_gazeta"
```

### Using Docker

Simply, run the following command:
```
docker-compose up --build -d
```

### Without Docker

Run main file news_predictions/app/src/wsgi.py => python3 main.py

## Authors

Contributors names and contact info

ex. Artem Ponomarev
ex. [@aspnmrv](https://t.me/aspnmrv)
