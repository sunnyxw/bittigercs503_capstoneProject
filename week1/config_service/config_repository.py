import json

class ConfigRepository():
    def __init__(self):
        self.config_service_config_path = 'config_service_config.json'
        self.backend_server_config_path = 'backend_server_config.json'
        self.news_recommendation_service_config_path = 'news_recommendation_service_config.json'
        self.click_log_processor_config_path = "click_log_processor_config.json"
        self.news_pipeline_config_path = "news_pipeline_config.json"

    def _readJson(self, path):
        with open(path) as json_data:
            return json.load(json_data)

    def configServerConfig(self):
        return self._readJson(self.config_service_config_path)

    def backendServerConfig(self):
        return self._readJson(self.backend_server_config_path)

    def newsRecommendationServiceConfig(self):
        return self._readJson(self.news_recommendation_service_config_path)

    def clickLogProcessorConfig(self):
        return self._readJson(self.click_log_processor_config_path)

    def newsPipelineConfig(self):
        return self._readJson(self.news_pipeline_config_path)
    


