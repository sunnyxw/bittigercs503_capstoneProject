import pyjsonrpc

class ConfigService():
    def __init__(self):
        config_service_URL = "http://localhost:4000/"
        self.client = pyjsonrpc.HttpClient(url=config_service_URL)
        
    def testMethod(self, a, b):
        return self.client.call("add", a, b)

    def backendServerConfig(self):
        return self.client.call("backendServerConfig")

