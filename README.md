# Igachan-s-Fakelake

## dockerコンテナの立ち上げ  
- ソースコードを取得します  
`git clone https://github.com/Keisuke-Igarashi/Igachan-D-Fakelake.git`  
- dockerイメージをビルドします  
`sudo docker build --tag igachan-d-fakelake .`  
- 8000番ポートで起動します。  
`sudo docker run -d -p 8000:5000 igachan-d-fakelake `  
