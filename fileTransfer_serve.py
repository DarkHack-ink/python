import http.server
import socketserver
port = 8000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",port ),handler) as http:
  print("Server runnin on port ", port )
  http.serve_forever()
  