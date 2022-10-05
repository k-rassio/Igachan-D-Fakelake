# Igachan-s-Fakelake
## ローカルでの立ち上げ
- ソースコードを取得します  
`git clone https://github.com/Keisuke-Igarashi/Igachan-D-Fakelake.git`  
- 環境変数を設定します
```
export FLASK_APP=hello
export FLASK_ENV=development
cd app/
flask run --host=0.0.0.0
```

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
- 文字コードutf8での管理とする

## 集めたデータについて
- データ収集サイト（情報源）
  - BuzzFeed(https://www.buzzfeed.com/jp/badge/factcheckjp)
  - InFact(https://infact.press/category/factcheck/)

- 情報源として選定した理由
  - 信憑性のある根拠を用いるか、独自の調査を行い、しっかりと真相を究明しているため。
    - 根拠に信憑性がある理由として、政府のサイトや論文記事、専門家へのインタビュー等が用いられていたため。
  - 根拠が説明できない場合には、「根拠不明」としてフェイクニュースであることは明示していないため。
  - 載っている情報が多彩なため。
    -　政治のニュースが主で、経済、健康、日常等様々なジャンルの記載がある。
  - 引用の仕方、 載っている情報等、詳細は各社のガイドラインを参照してください。
    - https://www.buzzfeed.com/jp/shani/the-buzzfeed-editorial-standards-and-ethics-guide-1
    - https://infact.press/factcheck-policy/
 
    
  


