
## Reference
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 

## Logging

python標準に用意されているハンドラ
- [便利なハンドラ](https://docs.python.org/ja/3/howto/logging.html#useful-handlers)

flaskのLogging

- [Logging - Flask](https://flask.palletsprojects.com/en/2.0.x/logging/)
- [いまさらながら Flask についてまとめる 〜Logging〜](https://www.subarunari.com/entry/2017/10/07/014911)


## Loki

- [Configuration](https://grafana.com/docs/loki/latest/configuration/)


## Promtail

Promtailを使ってGrafana Lokiにログを送信する

- [Get Logs into Grafana Loki](https://grafana.com/docs/loki/latest/getting-started/get-logs-into-loki/)

- [Label](https://grafana.com/docs/loki/next/fundamentals/labels/)


## LocalStack

S3バケット作成

```
aws s3 mb s3://sample-bucket --endpoint-url=http://localhost:4566
```
