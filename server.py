from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define server address and port
HOST = '127.0.0.1'
PORT = 8000

# Create an HTTP server
with HTTPServer((HOST, PORT), SimpleHTTPRequestHandler) as server:
    print(f"Serving HTTP on {HOST} port {PORT}...")
    # Serve until process is killed
    server.serve_forever()
