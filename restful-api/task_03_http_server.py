#!/usr/bin/python3

'''
    quickdoc
'''

import http.server as HS
import socketserver
import json


PORT = 8000

class WebRequestHandler(HS.BaseHTTPRequestHandler):
    '''
        quick doc
    '''

    def send_text(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_GET(self):
        '''
            quick doc
        '''
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"name": "John", "age": 30, "city": "New York"}).encode("utf-8"))
        elif self.path == "/status":
            self.send_text()
            self.wfile.write("OK".encode("utf-8"))
        elif self.path == '/':
            self.send_text()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"version": "1.0", "description": "A simple API built with http.server"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    Handler = WebRequestHandler

    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()
