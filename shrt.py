#!/usr/bin/python
def shrt(url):
    try:
        import requests
        import json
        from re import match
    except ImportError, e:
        raise Exception('Required module missing: %s' % e.args[0])

    r = requests.post('https://www.googleapis.com/urlshortener/v1/url',
                      data=json.dumps({"longUrl": url}),
                      headers={'content-type': 'application/json'})

    content = json.loads(r.content)
    if r.status_code == 200:
      return content['id']
    else:
      return "%s: %s" % (content['code'], content['message'])
      
if __name__ == '__main__':
    from sys import argv
    print shrt(argv[1])