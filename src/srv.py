import os
import socketserver
from http.server import SimpleHTTPRequestHandler
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.resolve()

PORT = int(os.getenv("PORT", 8000))
print(f"PORT={PORT}")


class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        path = self.extract_path()
        urls = {
            '': self.get_form
        }
        handler = urls[path]
        handler()
#
    def extract_path(self):
        path = self.path.split("/")[0]
        print(path)
        return path

    def get_form(self):
        msg = self.get_content("pages/index.html")
        print(msg)
        self.response_200(msg)

    def response_200(self, msg):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if isinstance(msg, str):
            msg = msg.encode()
        self.wfile.write(msg)

    @staticmethod
    def get_content(path):
        file = PROJECT_DIR/ path
        with open(file, "r", encoding="utf-8") as fp:
            content = fp.read()
        return content

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it works")

    httpd.serve_forever()


