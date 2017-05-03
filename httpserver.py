from http.server import BaseHTTPRequestHandler,HTTPServer
import cgi

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        print(postvars)
        self.send_response(200)
        self.end_headers()

server = HTTPServer(('localhost', 6666), Handler)
server.serve_forever()