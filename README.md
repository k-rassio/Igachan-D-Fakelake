# Igachan-s-Fakelake

## dockerコンテナの立ち上げ  
### 前提条件
- dockerがインストールされている環境であること
- poetryがインストールされている環境であること

### コマンド
- poetryの設定を読み込みます  
`source ~/.profile`  
`which poetry`  
- ソースコードを取得します  
`git clone https://github.com/Keisuke-Igarashi/Igachan-D-Fakelake.git`  
- dockerイメージをビルドします  
`sudo docker build --tag igachan-d-fakelake .`  
- 8000番ポートで起動します。  
`sudo docker run -d -p 8000:5000 igachan-d-fakelake `  

## csvの拡張子について
- shift-jisでの管理とする
