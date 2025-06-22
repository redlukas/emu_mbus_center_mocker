import http.server
import socketserver
import os

PORT = 5000
RESPONSES_FOLDER = "./devices"
VALID_IDS = {
    3: "emu_allrounder_v16_17val.json",
    4: "emu_professional_v16_31val.json",
    6: "emu_professional_v25_24val.json",
    7: "gwf_water_2val.json"
}

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"path is: {self.path}")
        if self.path == "/":
            html_content = "<p>emu_logo_128px</p>"
            encoded = html_content.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
        if self.path.startswith("/app/api/id/"):
            try:
                number = int(self.path.split("/")[-1].replace(".json", ""))
                print(f"accessing id {number}")
                if number in VALID_IDS.keys():
                    print("valid")
                    file_path = os.path.join(RESPONSES_FOLDER, VALID_IDS[number])
                    print(f"path is {file_path}")
                    if os.path.exists(file_path):
                        print("exists")
                        with open(file_path, "rb") as f:
                            data = f.read()
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.send_header("Content-Length", str(len(data)))
                        self.end_headers()
                        self.wfile.write(data)
                        return
                else:
                    print("ID does not exist")
                    self.connection.close()
                    return
            except Exception as e:
                print("Generic exception", e)
                pass



        self.send_error(404)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Mock server running on port {PORT}")
    httpd.serve_forever()
