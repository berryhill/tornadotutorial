import tornado.ioloop
import tornado.web
import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	self.render('index.html')

class SecondHandler(tornado.web.RequestHandler):
    def get(self):
	self.render('world.html')

settings = dict(
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
	static_path=os.path.join(os.path.dirname(__file__), "static"),
	debug=True
)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/hello", MainHandler),
    (r"/world", SecondHandler)
],**settings)

if __name__ == "__main__":
    print 'Server Running...'
    print 'Press ctrl + c to close'
    application.listen(4444)
    tornado.ioloop.IOLoop.instance().start()
