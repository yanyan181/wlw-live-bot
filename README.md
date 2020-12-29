# wlw-live-bot

## 動作環境
python 3.8.0
ubuntu 20.04

## 初期設定
### python
```
$ pip install -r requirements.txt
```
### 環境変数(ローカルで動かす場合)
```
$ export youtube_api_key=[youtubeの鍵に書き換え]
$ export consumer_key=[twitterAPIで払い出した鍵]
$ export consumer_secret=[twitterAPIで払い出した鍵]
$ export access_token=[twitterアカウントに対してoauthで払い出したトークン]
$ export access_token_secret=[こっちはトークンの秘密鍵]
$ export interval=15 # 実行時間の分数を指定
```