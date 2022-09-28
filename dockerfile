# syntax=docker/dockerfile:1

# pythonイメージを取得
FROM python:3.10-slim-buster

# コンテナの作業ディレクトリ
WORKDIR /Igachan-D-Fakelake

# アプリ資材のコピー
COPY . .

# poetryを使用可能にするためのビルド時実行コマンド

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

# poetryの設定ファイルの内容をrequirements.txt化
RUN poetry export -f requirements.txt > requirements.txt

# poetryの設定ファイルの通りのライブラリをインストール
RUN pip install -r requirements.txt

# 環境変数の設定
ENV FLASK_APP ./app/hello
ENV FLASK_ENV produciton

# コンテナの実行
CMD ["flask", "run", "--host=0.0.0.0"]