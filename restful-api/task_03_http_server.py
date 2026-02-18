#!/usr/bin/python3
"""
Module: task_03_http_server
Description: A simple HTTP server that responds to specific GET requests.
"""
import http.server
from http.server import HTTPServer
import json
from http import HTTPStatus


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A request handler class that handles GET requests for specific paths.
    """

    def do_GET(self):
        """Handle GET requests for specific paths."""

        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York",
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {
                "status": "OK",
                "message": "Server is running",
            }
            json_status = json.dumps(status)
            self.wfile.write(json_status.encode("utf-8"))

        elif self.path == "/info":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple HTTP server example",
            }
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode("utf-8"))

        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")


def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("\nServer stopped.")


if __name__ == "__main__":
    run()
