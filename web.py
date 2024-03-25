from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Top Software Companies In Revenue With Table</title>
</head>
<body align="center">
<img src="/static/images.png" height="200" width="800">
<table border="2" cellspacing="5" cellpadding="5" width="40" height="50">
<caption>Saveetha staff Details</caption>
<tr bgcolor="pink">
<th>S.NO</th>
<th>Staff ID</th>
<th>staff </th>
</tr>

<tr bgcolor="gold">
<td bgcolor="pink">1</td>
<td>SEC25</td>
<td>Sivaraj</td>
</tr>

<tr bgcolor="gold">
<td bgcolor="pink">2</td>
<td>SEC84</td>
<td>Naveen</td>
</tr>

<tr bgcolor="gold">
<td bgcolor="pink">3</td>
<td>SEC95</td>
<td>Somanathan</td>
</tr>

<tr bgcolor="gold">
<td bgcolor="pink">4</td>
<td>SEC145</td>
<td>Bhavadharani</td>
</tr>

<tr bgcolor="gold">
<td bgcolor="pink">5</td>
<td>SEC225</td>
<td>Swetha</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()