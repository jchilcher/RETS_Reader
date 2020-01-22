import configparser

config = configparser.ConfigParser()
config.read('settings.cfg')

rets_credentials = dict(url=config.get('rets','url'),
                        username=config.get('rets','username'),
                        password=config.get('rets','password'))