import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def _get_html(self):
        """
        Метод получения html разметки из файла index.html
        """
        html_file = "index.html"

        try:
            with open(html_file, "r", encoding="utf-8") as file:
                html_content = file.read()
                return html_content

        except FileNotFoundError:
            print(f"Файл '{html_file}' не найден.")
            return None


    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        page_content = self._get_html()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8")) # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")