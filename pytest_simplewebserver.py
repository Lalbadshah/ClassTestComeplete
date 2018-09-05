#!/usr/bin/python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
cwd = os.getcwd()

client_ip=''
client_port=''
Server_Root= cwd

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip,client_port = self.client_address
        if  self.requestline.find('EXIT')!=-1:
            print('SERVER Exiting CLient IP: '+str(client_ip)+'Client port: '+str(client_port))
            self.send_response(200)
            self.wfile.write(bytes("Server Shut Down", "utf-8"))

            self.close_connection = True
            exit()
        try:
            #print(self.path)
            file = open(Server_Root+ self.path, 'r')
            self.send_response(200)
            self.wfile.write(bytes("Timestamp "+time.asctime()+"    path: %s    File Contents: " % self.path, "utf-8"))
            self.wfile.write(bytes("%s" % file.read() , "utf-8"))
        except:
            self.send_response(200)
            self.wfile.write(bytes("File not found","utf-8"))






def run(server_class=HTTPServer, handler_class=S, port=80,):
    server_address = ('' , port)
    httpd = server_class(server_address, handler_class)
    print('SERVER READY')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 3:
        Server_Root= str(argv[2])
        run(port=int(argv[1]))

    else:
        run()