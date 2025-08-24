"""
Pytest configuration and shared fixtures
"""

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_openweather_response():
    """Mock OpenWeatherMap API response"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'main': {
            'temp': 22.5,
            'humidity': 60,
            'pressure': 1013
        },
        'weather': [{'description': 'partly cloudy'}],
        'wind': {'speed': 5.2, 'deg': 180},
        'name': 'Test City'
    }
    return mock_response

@pytest.fixture
def sample_weather_data():
    """Sample weather data for testing"""
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