import pytest
import unittest.mock as mock
from datetime import datetime, timedelta
import json
import sys
import os

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import your weather bot functions
from weather_bot import (
    get_coordinates,
    fetch_current_weather,
    fetch_weather_forecast,
    extract_location_from_query,
    determine_query_type,
    parse_time_intent,
    convert_units,
    calculate_wind_direction,
    format_weather_data,
    initialize_gemini_client,
    generate_natural_response,
    create_fallback_response,
    validate_api_keys,
    handle_api_errors,
    format_timestamp,
    clean_location_string,
    process_user_query,
    load_configuration,
    cache_weather_data,
    get_cached_data,
    log_user_interaction
)

class TestWeatherDataFunctions:
    """Tests for core weather data retrieval functions"""
    
    def test_get_coordinates_valid_city(self):
        """Test coordinate retrieval for valid city"""
        # Mock the function since we don't have the actual implementation yet
        # Expected: get_coordinates("New York") should return (lat, lon, "New York")
        lat, lon, city = get_coordinates("New York")
        assert lat is not None
        assert lon is not None
        assert city == "New York"
        assert isinstance(lat, float)
        assert isinstance(lon, float)
    
    def test_get_coordinates_invalid_city(self):
        """Test coordinate retrieval for invalid city"""
        lat, lon, city = get_coordinates("InvalidCityName123")
        assert lat is None
        assert lon is None
        assert city is None
    
    def test_get_coordinates_empty_input(self):
        """Test coordinate retrieval with empty input"""
        lat, lon, city = get_coordinates("")
        assert lat is None
        assert lon is None
        assert city is None
    
    def test_fetch_current_weather_valid_coords(self):
        """Test current weather fetch with valid coordinates"""
        # NYC coordinates
        result = fetch_current_weather(40.7128, -74.0060)
        assert isinstance(result, dict)
        assert 'temperature' in result
        assert 'humidity' in result
        assert 'description' in result
        assert isinstance(result['temperature'], (int, float))
    
    def test_fetch_current_weather_invalid_coords(self):
        """Test current weather fetch with invalid coordinates"""
        result = fetch_current_weather(999, 999)
        assert isinstance(result, str)  # Should return error string
        assert "error" in result.lower()
    
    def test_fetch_weather_forecast_valid_coords(self):
        """Test forecast fetch with valid coordinates"""
        result = fetch_weather_forecast(40.7128, -74.0060, 3)
        assert isinstance(result, dict)
        assert 'forecast' in result or isinstance(result, list)
    
    def test_fetch_weather_forecast_default_days(self):
        """Test forecast fetch with default days parameter"""
        result = fetch_weather_forecast(40.7128, -74.0060)
        # Should default to 5 days
        assert isinstance(result, (dict, list))


class TestQueryProcessingFunctions:
    """Tests for natural language query processing"""
    
    def test_extract_location_simple_city(self):
        """Test location extraction from simple city queries"""
        assert extract_location_from_query("weather in Boston") == "Boston"
        assert extract_location_from_query("Boston weather") == "Boston"
        assert extract_location_from_query("How's the weather in Chicago?") == "Chicago"
    
    def test_extract_location_city_state(self):
        """Test location extraction with city and state"""
        assert extract_location_from_query("weather in Dallas, Texas") == "Dallas, Texas"
        assert extract_location_from_query("forecast for Miami, FL") == "Miami, FL"
    
    def test_extract_location_international(self):
        """Test location extraction for international cities"""
        assert extract_location_from_query("weather in London, UK") == "London, UK"
        assert extract_location_from_query("Tokyo forecast") == "Tokyo"
    
    def test_extract_location_no_location(self):
        """Test location extraction when no location is mentioned"""
        assert extract_location_from_query("What's the weather like?") is None
        assert extract_location_from_query("Is it raining?") is None
    
    def test_determine_query_type_current(self):
        """Test query type determination for current weather"""
        assert determine_query_type("What's the weather in NYC?") == "current"
        assert determine_query_type("Current temperature in Boston") == "current"
        assert determine_query_type("How hot is it in Phoenix?") == "current"
    
    def test_determine_query_type_forecast(self):
        """Test query type determination for forecast"""
        assert determine_query_type("Weather forecast for tomorrow") == "forecast"
        assert determine_query_type("Will it rain next week in Seattle?") == "forecast"
        assert determine_query_type("Upcoming weather in Denver") == "forecast"
    
    def test_parse_time_intent_specific_days(self):
        """Test time intent parsing for specific days"""
        assert parse_time_intent("weather tomorrow") == 1
        assert parse_time_intent("forecast for 3 days") == 3
        assert parse_time_intent("next week weather") == 7
    
    def test_parse_time_intent_no_time(self):
        """Test time intent when no specific time is mentioned"""
        assert parse_time_intent("current weather") is None
        assert parse_time_intent("what's it like outside") is None


class TestDataProcessingFunctions:
    """Tests for data processing and conversion functions"""
    
    def test_convert_units_freezing(self):
        """Test temperature conversion at freezing point"""
        celsius, fahrenheit, kelvin = convert_units(0)
        assert celsius == 0
        assert fahrenheit == 32
        assert kelvin == 273.15
    
    def test_convert_units_room_temp(self):
        """Test temperature conversion at room temperature"""
        celsius, fahrenheit, kelvin = convert_units(20)
        assert celsius == 20
        assert fahrenheit == 68
        assert kelvin == 293.15
    
    def test_convert_units_negative(self):
        """Test temperature conversion with negative celsius"""
        celsius, fahrenheit, kelvin = convert_units(-10)
        assert celsius == -10
        assert fahrenheit == 14
        assert kelvin == 263.15
    
    def test_calculate_wind_direction_cardinal(self):
        """Test wind direction calculation for cardinal directions"""
        assert calculate_wind_direction(0) == "N"
        assert calculate_wind_direction(90) == "E"
        assert calculate_wind_direction(180) == "S"
        assert calculate_wind_direction(270) == "W"
    
    def test_calculate_wind_direction_intercardinal(self):
        """Test wind direction calculation for intercardinal directions"""
        assert calculate_wind_direction(45) == "NE"
        assert calculate_wind_direction(135) == "SE"
        assert calculate_wind_direction(225) == "SW"
        assert calculate_wind_direction(315) == "NW"
    
    def test_calculate_wind_direction_edge_cases(self):
        """Test wind direction calculation for edge cases"""
        assert calculate_wind_direction(360) == "N"
        assert calculate_wind_direction(-45) == "NW"  # Should handle negative
    
    def test_format_weather_data_structure(self):
        """Test weather data formatting maintains required structure"""
        mock_raw_data = {
            'main': {'temp': 20, 'humidity': 60, 'pressure': 1013},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 5, 'deg': 180}
        }
        result = format_weather_data(mock_raw_data)
        assert isinstance(result, dict)
        assert 'temperature' in result
        assert 'humidity' in result
        assert 'description' in result
    
    def test_format_weather_data_missing_fields(self):
        """Test weather data formatting with missing fields"""
        mock_raw_data = {'main': {'temp': 15}}
        result = format_weather_data(mock_raw_data)
        assert isinstance(result, dict)
        assert 'temperature' in result


class TestAIResponseFunctions:
    """Tests for AI response generation functions"""
    
    @mock.patch('google.generativeai.configure')
    def test_initialize_gemini_client_valid_key(self, mock_configure):
        """Test Gemini client initialization with valid key"""
        mock_configure.return_value = None
        result = initialize_gemini_client("valid_api_key")
        assert result is not None
        mock_configure.assert_called_once_with(api_key="valid_api_key")
    
    def test_initialize_gemini_client_invalid_key(self):
        """Test Gemini client initialization with invalid key"""
        result = initialize_gemini_client("")
        assert result is None
    
    def test_generate_natural_response_valid_data(self):
        """Test natural response generation with valid data"""
        mock_weather = {
            'location': 'Boston',
            'temperature': 22,
            'description': 'sunny'
        }
        result = generate_natural_response(mock_weather, "How's the weather in Boston?")
        assert isinstance(result, str)
        assert len(result) > 0
        assert 'Boston' in result or 'boston' in result.lower()
    
    def test_create_fallback_response_current_weather(self):
        """Test fallback response for current weather"""
        mock_weather = {
            'location': 'New York',
            'temperature': 18,
            'description': 'cloudy',
            'humidity': 65
        }
        result = create_fallback_response(mock_weather)
        assert isinstance(result, str)
        assert 'New York' in result
        assert '18' in result or 'eighteen' in result.lower()
    
    def test_create_fallback_response_forecast(self):
        """Test fallback response for forecast data"""
        mock_forecast = {
            'location': 'Seattle',
            'forecast': [
                {'temperature': 16, 'description': 'rainy'},
                {'temperature': 19, 'description': 'partly cloudy'}
            ]
        }
        result = create_fallback_response(mock_forecast)
        assert isinstance(result, str)
        assert 'Seattle' in result


class TestUtilityFunctions:
    """Tests for utility and helper functions"""
    
    @mock.patch('requests.get')
    def test_validate_api_keys_valid(self, mock_get):
        """Test API key validation with valid keys"""
        mock_get.return_value.status_code = 200
        result = validate_api_keys("valid_openweather_key", "valid_gemini_key")
        assert result is True
    
    @mock.patch('requests.get')
    def test_validate_api_keys_invalid_openweather(self, mock_get):
        """Test API key validation with invalid OpenWeather key"""
        mock_get.return_value.status_code = 401
        result = validate_api_keys("invalid_key", "valid_gemini_key")
        assert result is False
    
    def test_handle_api_errors_success(self):
        """Test API error handling for successful response"""
        mock_response = mock.Mock()
        mock_response.status_code = 200
        result = handle_api_errors(mock_response)
        assert result is None  # No error
    
    def test_handle_api_errors_client_error(self):
        """Test API error handling for client errors"""
        mock_response = mock.Mock()
        mock_response.status_code = 404
        mock_response.text = "Not found"
        result = handle_api_errors(mock_response)
        assert isinstance(result, dict)
        assert 'error' in result
    
    def test_format_timestamp_unix(self):
        """Test timestamp formatting from Unix time"""
        unix_timestamp = 1640995200  # 2022-01-01 00:00:00 UTC
        result = format_timestamp(unix_timestamp)
        assert isinstance(result, str)
        assert '2022' in result
    
    def test_format_timestamp_current(self):
        """Test timestamp formatting for current time"""
        current_time = int(datetime.now().timestamp())
        result = format_timestamp(current_time)
        assert isinstance(result, str)
        assert str(datetime.now().year) in result
    
    def test_clean_location_string_basic(self):
        """Test location string cleaning for basic cases"""
        assert clean_location_string("  New York  ") == "New York"
        assert clean_location_string("Chicago,") == "Chicago"
        assert clean_location_string("Los Angeles?") == "Los Angeles"
    
    def test_clean_location_string_complex(self):
        """Test location string cleaning for complex cases"""
        assert clean_location_string("  San Francisco, CA !!! ") == "San Francisco, CA"
        assert clean_location_string("Boston.....") == "Boston"


class TestMainApplicationFunctions:
    """Tests for main application orchestration functions"""
    
    def test_process_user_query_simple_current(self):
        """Test processing simple current weather query"""
        result = process_user_query("What's the weather in Miami?")
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_process_user_query_forecast(self):
        """Test processing forecast query"""
        result = process_user_query("Weather forecast for Austin tomorrow")
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_process_user_query_no_location(self):
        """Test processing query without location"""
        result = process_user_query("What's the weather?")
        assert isinstance(result, str)
        assert 'location' in result.lower() or 'specify' in result.lower()
    
    def test_load_configuration_default(self):
        """Test configuration loading with default values"""
        config = load_configuration()
        assert isinstance(config, dict)
        assert 'openweather_key' in config
        assert 'gemini_key' in config
    
    @mock.patch.dict('os.environ', {'OPENWEATHER_API_KEY': 'test_key'})
    def test_load_configuration_env_vars(self):
        """Test configuration loading from environment variables"""
        config = load_configuration()
        assert config['openweather_key'] == 'test_key'


class TestCachingFunctions:
    """Tests for optional caching functionality"""
    
    def test_cache_weather_data_storage(self):
        """Test weather data caching storage"""
        mock_data = {'temperature': 20, 'humidity': 60}
        cache_weather_data("Boston", mock_data, 10)
        # Should not raise an exception
    
    def test_get_cached_data_hit(self):
        """Test cache retrieval when data exists"""
        mock_data = {'temperature': 25, 'humidity': 55}
        cache_weather_data("Seattle", mock_data, 10)
        result = get_cached_data("Seattle")
        # Should return cached data or None if cache is empty/expired
        assert result is None or isinstance(result, dict)
    
    def test_get_cached_data_miss(self):
        """Test cache retrieval when data doesn't exist"""
        result = get_cached_data("NonExistentCity")
        assert result is None
    
    def test_log_user_interaction(self):
        """Test user interaction logging"""
        timestamp = datetime.now()
        log_user_interaction("test query", "test response", timestamp)
        # Should not raise an exception


# Test fixtures and utilities
@pytest.fixture
def sample_weather_data():
    """Fixture providing sample weather data for tests"""
    return {
        'location': 'Test City',
        'temperature': 22.5,
        'humidity': 60,
        'pressure': 1013,
        'description': 'partly cloudy',
        'wind_speed': 5.2,
        'wind_direction': 180,
        'timestamp': '2024-01-01 12:00:00'
    }

@pytest.fixture
def sample_forecast_data():
    """Fixture providing sample forecast data for tests"""
    return {
        'location': 'Test City',
        'forecast': [
            {'datetime': '2024-01-01 15:00', 'temperature': 20, 'description': 'sunny'},
            {'datetime': '2024-01-01 18:00', 'temperature': 18, 'description': 'clear'},
            {'datetime': '2024-01-02 09:00', 'temperature': 16, 'description': 'cloudy'}
        ]
    }

if __name__ == "__main__":
    # Run tests with: python -m pytest weather_bot_tests.py -v
    # Or run specific test class: python -m pytest weather_bot_tests.py::TestWeatherDataFunctions -v
    print("To run these tests:")
    print("1. Install pytest: pip install pytest")
    print("2. Save this file as 'test_weather_bot.py'")
    print("3. Run: python -m pytest test_weather_bot.py -v")
    print("4. Run specific tests: python -m pytest test_weather_bot.py::TestWeatherDataFunctions -v")