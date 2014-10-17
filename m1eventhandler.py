#!/usr/bin/env python


import SocketServer
from threading import Thread
import push
import arduino

class service(SocketServer.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print "Client connected with ", self.client_address
        while len(data):
            data = self.request.recv(1024)
            data = ' '.join(data.strip().split()).strip()
            print data
            if data:
                notifier = push.pusher()
                notifier.push(data, data)
                try:
                    ard = arduino.arduinocoms()
                    ard.blink()
                except:
                    pass

        print "Client exited"
        self.request.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

server = ThreadedTCPServer(('',1234), service)
server.serve_forever()
