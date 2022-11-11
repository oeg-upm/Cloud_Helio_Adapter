from configparser import ConfigParser

class Config_Manager:
    def __init__(self):
        self.__class__.adapter_host = None
        self.__class__.adapter_port = None
        self.__class__.helio_host = None

    def save_config(self):
        config = ConfigParser()
        if config.read('./config.ini'):
            if not config.has_section('helio'):
                print("Missing 'helio' mandatory section in 'config.ini'.")
                exit()
            else:
                if not config.has_option('helio', 'host'):
                    print("Missing 'host' option in 'helio' section in 'config.ini'.")
                    exit()
            if not config.has_section('adapter'):
                print("Missing 'helio' mandatory section in 'config.ini'.")
                exit()
            else:
                if not config.has_option('adapter', 'host'):
                    print("Missing 'host' option in 'adapter' section in 'config.ini'.")
                    exit()
                if not config.has_option('adapter', 'port'):
                    print("Missing 'port' option in 'adapter' section in 'config.ini'.")
                    exit()
        
            self.adapter_host = config.get('adapter', 'host')
            self.adapter_port = config.getint('adapter', 'port')
            self.helio_host = config.get('helio', 'host')
        else:
            print("Missing 'config.ini' file.")