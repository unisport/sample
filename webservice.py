import web

urls = (
    '/products', 'products'
)

app = web.application(urls, globals())

class products:
    def GET(self):
        web.header('Content-Type', 'text/html')
        return 'Hello, Kitty'


if __name__ == '__main__':
    app.run()
