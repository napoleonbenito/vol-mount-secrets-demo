from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
        try:
            with open('/etc/secret/mykey', 'r') as file:
                secret = file.read().strip()
        except IOError:
            secret = 'Secret not found'

        self._send_response(f'Secret: {secret}')

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server...')
    httpd.serve_forever()