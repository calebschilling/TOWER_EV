from get_config import get_config


open_weather_api = get_config("OPEN_WEATHER", "open_weather_api")
print(open_weather_api)