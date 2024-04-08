# API de Notícias - Grupo 4 
Projeto do Grupo 4 para extração da News API para o módulo 4 de Extração de dados de Engenharia de dados do Santander Coders.



O objetivo dessa projeto é criar uma API que extrai dados de nóticias através da News API [https://newsapi.org/](https://newsapi.org/), e a partir disso transformar esses dados para consumo final.

Esse projeto é composto pelos seguintes arquivos:

- **extract_data.ipynb** - presente arquivo que contém todos os códigos reunidos.
- **app.py** - script com Flask API que gera o ambiente para consumo dos dados.
- **data/**
  - **api_extract.csv** - arquivo com as notícias extraídas da News API;
  - **articles_relevance.csv** - arquivo com relevância dos artigos;
  - **keyword_counts.csv** - arquivo com a quantidade de vezes que cada palavra-chave aparece;
  - **news_data.csv** - arquivo de dados de notícias;
  - **news_per_date.csv** - arquivo com a quantidade de notícias por ano, mês e dia de publicação;
  - **news_per_source_author.csv** - arquivo com a quantidade de notícias por fonte e autor.


Para a criação desse trabalho foi preciso desenvolver alguns critérios para a extração. Onde foram escolhidas três palavras-chave para filtrar as notícias, sendo elas **"DNA sequencing", "gene therapy" e "genetic diseases"**. E com o script de extração feito, as notícias extraídas são armazenadas em formato raw em um csv, para posteriormente ocorrer uma transformação dos dados e consequentemente a disponibilidade para consumo.

A extração ocorre a cada 1 hora onde apenas notícias novas são adicionadas ao arquivo e, se alguma notícia já estiver armazenada, ela não é adicionada novamente, evitando duplicação.
