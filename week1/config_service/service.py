import pyjsonrpc
from config_repository import ConfigRepository

config = ConfigRepository().configServerConfig()

SERVER_HOST = config.get("SERVER_HOST")
SERVER_PORT = config.get("SERVER_PORT")

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    # """ Test Method """
    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print "add is called with %d and %d" % (a, b)
        return a+b

    @pyjsonrpc.rpcmethod
    def backendServerConfig(self):
        return ConfigRepository().backendServerConfig()

    @pyjsonrpc.rpcmethod
    def newsRecommendationServiceConfig(self):
        return ConfigRepository().newsRecommendationServiceConfig()

    @pyjsonrpc.rpcmethod
    def clickLogProcessorConfig(self):
        return ConfigRepository().clickLogProcessorConfig()

    def newsPipelineConfig(self):
        return ConfigRepository().newsPipelineConfig()

# Threading Http Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print "Start HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

http_server.serve_forever()

