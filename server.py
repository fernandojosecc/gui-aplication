from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHandler)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
