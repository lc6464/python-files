import web
from urllib.parse import unquote

urls = (
    '/' , 'hello'
)

class hello:
    def POST(self):     #使用POST接收JSON数据
        d={}
        data=web.data().decode()
        for i in data.split('&'):
            d[i.split('=')[0]]=unquote(i.split('=')[1])
        print(d, d['text'], type(d['text']))
        return {'sign':web.ctx.env['HTTP_SIGN'],'timestamp':web.ctx.env['HTTP_TIMESTAMP']}
    def GET(self):
        return 'post!'

if __name__=='__main__':
    app = web.application(urls, globals())
    app.run()
