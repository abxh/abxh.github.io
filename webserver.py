#!/usr/bin/env python3

import http.server
import socketserver
import webbrowser

PORT = 8003
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    webbrowser.open(f"http://localhost:{PORT}/", new=0, autoraise=True)
    httpd.serve_forever()
