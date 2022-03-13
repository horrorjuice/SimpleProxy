from flask import Flask, Response
from requests import get
import re

app = Flask(__name__)
SITE_NAME = 'https://news.ycombinator.com/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  resp = get(f'{SITE_NAME}{path}').content.decode('utf8')
  words = re.findall('''[^\w><"=:\/'#-](\w{6})[^\w><"=:\/'#-]''', resp)
  for i in words:
    resp = resp.replace(i, i + '™')
  return Response(resp)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8001)



