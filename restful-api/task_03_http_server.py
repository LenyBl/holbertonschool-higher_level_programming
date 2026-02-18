#!/usr/bin/python3
"""
Module: task_03_http_server
Description: A simple HTTP server that responds to specific GET requests.
"""

import http.server
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
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(
                json.dumps(data).encode("utf-8")
            )

        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            status = {"status": "OK"}

            self.wfile.write(
                json.dumps(status).encode("utf-8")
            )

        elif self.path == "/info":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description":
                    "A simple API built with http.server"
            }

            self.wfile.write(
                json.dumps(info).encode("utf-8")
            )

        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
