import operations
import pyjsonrpc
import sys

from config_service_client import ConfigService


config = ConfigService().backendServerConfig()

SERVER_HOST = config.get("SERVER_HOST")
SERVER_PORT = config.get("SERVER_PORT")


class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """ Test Method """
    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print "add is called with %d and %d" % (a, b)
        return a+b

    """ Get news summaries for a user """
    @pyjsonrpc.rpcmethod
    def getNewsSummariesForUser(self, user_id, page_num):
        return operations.getNewsSummariesForUser(user_id, page_num)

    """ Log user news clicks """
    @pyjsonrpc.rpcmethod
    def logNewsClickForUser(self, user_id, news_id):
        return operations.logNewsClickForUser(user_id, news_id)
        
# Threading Http Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print "Start HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

http_server.serve_forever()