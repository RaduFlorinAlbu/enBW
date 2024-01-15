import json

from typing import Union
from django.conf import settings
from django.core.cache import cache

"""""
This has been created for getting the settings from a config file 
The use of this is to avoid hardcoding values, such as examples, default values, etc
It is not of great use for the project as it is now, but it is good for future improvements
"""""

def get_cached_configs(key: str) -> Union[dict, None]:
    """returns cached configs"""
    return cache.get(key)

def set_cached_configs(key: str, data: dict) -> None:
    """set configs to cache"""
    try:
        cache.set(key, data)
    except Exception as e:
        raise Exception(f"Error set_cached_configs {e}")

def get_config_file_json(
    file_name, fetch_from_cache=False
):
    """
    Convenience method to return parsed data from json file
    Uses cache to reduce calls to the filesystem
    """

    cached_json_data = None
    config_file_name = f"static/{file_name}"
    try:
        cached_json_data = get_cached_configs(config_file_name)
    except FileNotFoundError:
        raise FileNotFoundError("Error fetching file from cache.")

    if fetch_from_cache and cached_json_data is not None:
        return cached_json_data

    try:
        with open(config_file_name, "r") as json_file:
            json_data = json.load(json_file)
            # future caching
            if cached_json_data is None:
                set_cached_configs(config_file_name, json_data)
            return json_data
    except FileNotFoundError:     
        raise FileNotFoundError("Config file not found")

def get_setting(name: str):
    config = get_config_file_json(file_name="config.json")
    project_setting = config.get(name, None)
    if project_setting is not None:
        return project_setting
    try:
        django_setting = getattr(settings, name, None)
        return django_setting
    except KeyError:
        raise KeyError("Settings not configured")