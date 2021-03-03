import os
import socketserver
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from typing import Dict
from urllib.parse import parse_qs
import smtplib

PROJECT_DIR = Path(__file__).parent.parent.resolve()

PORT = int(os.getenv("PORT", 8001))
print(f"PORT={PORT}")


class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        path = self.extract_path()
        urls = {
            '/form': self.get_form,
            '/static/css/main.css': self.get_css,
            '/static/img/bg.jpg': self.get_img,
            '/post': self.post
        }
        handler = urls[path]
        handler()

    def get_css(self):
        msg = self.get_content("static/css/main.css")
        self.response_200(msg, 'text/css')

    def get_img(self):
        msg = self.get_image("static/img/bg.jpg")
        self.response_200(msg, 'image/jpg')

    def extract_path(self):
        path = self.path.split("?")[0]
        print(path)
        return path

    def get_form(self):
        msg = self.get_content("templatestemplates/index.html")
        print(msg)
        self.response_200(msg, 'text/html')

    def response_200(self, msg, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        if isinstance(msg, str):
            msg = msg.encode()
        self.wfile.write(msg)

    @staticmethod
    def get_content(path):
        file = PROJECT_DIR / path
        with open(file, "r", encoding="utf-8") as fp:
            content = fp.read()
        return content

    @staticmethod
    def get_image(path):
        file = PROJECT_DIR / path
        with open(file, 'rb') as fp:
            image = fp.read()
        return image

    def post(self):
        # smtp_object = smtplib.SMTP('smtp@gmail.com', 587)
        # smtp_object.starttls()
        # smtp_object.login('evzhenko1106@gmail.com', 'EADSbMFFD6GwBdM')
        # smtp_object.sendmail("spacexxx47@gmail.com", "evzhenko1106@gmail.com", "Дороу спасибо за заказ")
        # smtp_object.quit()
        a = 1
        b = 2
        content = self.parse_user_sessions()
        print(content)

    def parse_user_sessions(self) -> Dict[str, str]:
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        payload = data.decode()
        qs = parse_qs(payload)
        user_data = {}
        for key, values in qs.items():
            if not values:
                continue
            user_data[key] = values[0]
        return user_data



with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it works")

    httpd.serve_forever()
