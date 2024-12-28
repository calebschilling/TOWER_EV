import configparser


def get_config(config_section, config_variable):
    
    config = configparser.ConfigParser()
    config.read('private/config.ini')

    config_entry = config[config_section][config_variable]
    # open_weather_api = config['OPEN_WEATHER']['open_weather_api']
    print(f"Getting the following config: [{config_section}] \nfrom {config_variable}: {config_entry}\n")

    return config_entry

