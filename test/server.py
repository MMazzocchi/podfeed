from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread

class Handler(SimpleHTTPRequestHandler):
  def log_request(code="-", size="-"):
    pass

class Server:
  def __init__(self, port):
    server_address = ('', port)
    self.httpd = HTTPServer(server_address, Handler)

  def run(self):
    self.httpd.serve_forever()

  def stop(self):
    self.httpd.shutdown()

class ServerThread(Thread):
  def __init__(self, port):
    self.server = Server(port)
    self.thread = Thread(target=lambda: self.server.run())
    self.thread.start()

  def stop(self):
    self.server.stop()
    self.thread.join()
