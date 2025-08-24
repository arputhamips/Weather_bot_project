"""
Weather Bot Main Implementation

Start implementing your functions here. Import from config and utils as needed.
"""

import requests
import re
from datetime import datetime
from typing import Tuple, Dict, Optional, List, Union
import google.generativeai as genai

from .config import Config, load_configuration
from .utils import handle_api_errors, format_timestamp, clean_location_string

# Example function to get you started:
def get_coordinates(location_string: str) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    """
    Get latitude, longitude, and formatted city name for a location
    
    Args:
        location_string: City name or "City, Country" format
        
    Returns:
        Tuple of (latitude, longitude, formatted_city_name) or (None, None, None)
    """
    if not location_string or not location_string.strip():
        return None, None, None
    
    # TODO: Implement this function
    # 1. Clean the location string
    # 2. Make API call to OpenWeatherMap geocoding
    # 3. Parse response and return coordinates
    pass

# Add all your other functions here...
# def fetch_current_weather(lat: float, lon: float) -> Union[Dict, str]:
# def fetch_weather_forecast(lat: float, lon: float, days: int = 5) -> Union[Dict, str]:
# etc...