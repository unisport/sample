import web

urls = (
    '/hello_kitty', 'bad_kitty'
)

app = web.application(urls, globals())

class bad_kitty:
    def GET(self):
        web.header('Content-Type', 'text/html')
        return 'Hello, Kitty'


if __name__ == '__main__':
    app.run()
