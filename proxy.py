import http.server
import socketserver
from http.server import SimpleHTTPRequestHandler
from urllib import request, parse

class ProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Replace "https://www.google.com" with the desired target URL
        target_url = "https://www.youtube.com"

        # Extract path and query parameters from the request URL
        parsed_url = parse.urlparse(self.path)
        target_path = parsed_url.path
        target_query = parsed_url.query

        # Construct the target URL with path and query parameters
        target_full_url = target_url + target_path + ("?" + target_query if target_query else "")

        try:
            response = request.urlopen(target_full_url)
            if response.geturl() != target_full_url:
                # If there is a redirect, send a redirect response
                self.send_response(302)
                self.send_header('Location', response.geturl())
                self.end_headers()
            else:
                # If no redirect, forward the response content
                content = response.read()
                self.send_response(response.status)
                for header, value in response.getheaders():
                    self.send_header(header, value)
                self.end_headers()
                self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Proxy error: {str(e)}")

PORT = 8080

with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
