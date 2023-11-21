
### Weather Class

The `Weather` class is designed to fetch weather information from the OpenWeatherMap API for a specific city. It includes functionalities to make API requests, handle caching to reduce the number of API calls, and retrieve various weather-related data such as coordinates, temperature, wind information, current weather, and sunrise/sunset times.

#### Constructor

```python
def __init__(self, city: str, api: str = "00cd4be2b420a9aac2dceca8849fac6f") -> None:
    """
    Initializes a Weather instance.

    Parameters:
        city (str): The name of the city for which weather information is to be fetched.
        api (str, optional): The API key for accessing the OpenWeatherMap API. Defaults to a sample key.
    """
```

#### Attributes

- `apikey` (str): The API key for accessing the OpenWeatherMap API.
- `city` (str): The name of the city for which weather information is fetched.
- `city_url` (str): The URL for the OpenWeatherMap API endpoint for the specified city.

#### Methods

##### `make_request()`

```python
def make_request(self):
    """
    Makes a request to the OpenWeatherMap API and retrieves the weather information. 
    Also checks whether cache is present for that city or not.

    Returns:
        dict or None: A dictionary containing weather information if successful, None otherwise.
    """
```

This method checks if there is valid cached data for the city. If cached data is present and still valid, it returns the cached data; otherwise, it makes a request to the API, updates the cache, and returns the API response.

##### `load_cache_file()`

```python
def load_cache_file(self):
    """
    Checks whether the cached data is available or not.

    Returns:
        json or None: A json file containing all the information about the weather.
    """
```

This method checks if a cached file exists for the city and loads the cached data if available.

##### `save_cached_data(data)`

```python
def save_cached_data(self, data):
    """
    Saves the information for a city in a json file. <city_name>_cache.json is the file name.

    Returns:
        Nothing: It saves the file so there's no need to return anything.
    """
```

This method saves the weather data for the city in a JSON file for future use.

##### `is_cached_valid(cached_data)`

```python
def is_cached_valid(self, cached_data):
    """
    Checks whether the cached data is valid or not. Default time interval is 30 minutes, 
    you can change it according to your need.

    Returns:
        True or False: True if the cached data is valid, False otherwise.
    """
```

This method checks if the cached data for the city is still valid based on a default expiration time (30 minutes). You can modify the expiration time as needed.

##### `coordinates()`

```python
def coordinates(self):
    """
    Retrieves the coordinates (longitude, latitude) of the city.

    Returns:
        tuple or None: A tuple containing longitude and latitude if successful, None otherwise.
    """
```

This method retrieves and returns the longitude and latitude coordinates of the city.

##### `temperature()`

```python
def temperature(self):
    """
    Retrieves the temperature (Current, Feels, Min, Max, Humidity) of the city.

    Returns:
        dict or None: A dictionary containing all of the above information in the same order.
    """
```

This method retrieves and returns various temperature-related information for the city, including current temperature, feels-like temperature, minimum and maximum temperatures, and humidity.

##### `wind()`

```python
def wind(self):
    """
    Retrieves the wind (speed, deg) information of the city.

    Returns:
        tuple or None: A tuple containing speed of the wind and the degree from where it's coming.
    """
```

This method retrieves and returns information about the wind speed and direction for the city.

##### `weather()`

```python
def weather(self):
    """
    Retrieves current weather (main, description) information of the city.

    Returns:
        tuple or None: A tuple containing information about the current weather of the city.
    """
```

This method retrieves and returns information about the current weather conditions, including the main weather category and a description.

##### `sun()`

```python
def sun(self):
    """
    Retrieves information regarding the sunset and sunrise according to UTC format.

    Returns:
        tuple or None: A tuple containing time of sunrise and sunset in UTC format.
    """
```

This method retrieves and returns information about the sunrise and sunset times in UTC format for the city.

### Example Usage

```python
# Create a Weather instance for a specific city
weather_instance = Weather("New York", api="your_openweathermap_api_key")

# Retrieve various weather information
coordinates = weather_instance.coordinates()
temperature_info = weather_instance.temperature()
wind_info = weather_instance.wind()
current_weather = weather_instance.weather()
sun_info = weather_instance.sun()
```

Note: Replace `"your_openweathermap_api_key"` with your actual OpenWeatherMap API key.
