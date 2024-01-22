import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getGoogleURL():
       googleUrl=config.get('common info','GoogleUrl')
       return googleUrl

    @staticmethod
    def getBingURL():
       bingUrl=config.get('common info','BingUrl')
       return bingUrl

    @staticmethod
    def getYahooURL():
       yahooUrl=config.get('common info','YahooUrl')
       return yahooUrl

    @staticmethod
    def getDefaultSearchText():
       default_search_text=config.get('common info','default_search_text')
       return default_search_text

    @staticmethod
    def getGoogleEngineName():
        return config.get('SEARCH_ENGINES', 'Google')

    @staticmethod
    def getBingEngineName():
        return config.get('SEARCH_ENGINES', 'Bing')