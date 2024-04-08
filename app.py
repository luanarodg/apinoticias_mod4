from flask import Flask, jsonify, request, render_template
import pandas as pd
import random

app = Flask(__name__)

df_news = pd.read_csv("data/api_extract.csv")
df_news_per_source_author = pd.read_csv("data/news_per_source_author.csv")
df_keyword_counts = pd.read_csv("data/keyword_counts.csv")


# Home
@app.route("/", methods=["GET"])
def homepage():
    return render_template('index.html')


# Retornar todas as notícias
@app.route("/api/news", methods=["GET"])
def get_all_news():
    return jsonify(df_news.to_dict(orient='records'))


# Retornar notícia por id
@app.route('/api/news/<int:id>', methods=['GET'])
def get_news_by_id(id):
    news = df_news.loc[df_news['id'] == id]
    if len(news) == 0:
        return "Notícia não encontrada", 404
    return jsonify(news.to_dict(orient='records')[0])


# Receber outras notícias que não foram mapeadas pela API original
@app.route('/api/news', methods=['POST'])
def add_new_news():
    global df_news
    new_news = request.json  
    df_news = pd.concat([df_news, pd.DataFrame([new_news])], ignore_index=True) 
    df_news.to_csv("data/api_extract.csv", index=False) 
    return jsonify({'message': 'Notícia adicionada com sucesso'}), 201


# Retornar a quantidade de notícias por ano, mês e dia de publicação do item 4.1
@app.route('/api/news/count_by_date', methods=['GET'])
def get_news_count_by_date():
    news_count_by_date = df_news.groupby(['publishedAt']).size().reset_index(name='news_count')
    return jsonify(news_count_by_date.to_dict(orient='records'))


# Retornar a quantidade de notícias por fonte e autor do item 4.2
@app.route('/api/news/count_by_source_author', methods=['GET'])
def get_news_count_by_source_author():
    return jsonify(df_news_per_source_author.to_dict(orient='records'))


# Retornar a quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação  do item 4.3
@app.route('/api/news/count_by_keyword', methods=['GET'])
def get_news_count_by_keyword():
    return jsonify(df_keyword_counts.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
