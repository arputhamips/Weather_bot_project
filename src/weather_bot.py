"""
Weather Bot Main Implementation

Start implementing your functions here. Import from config and utils as needed.
"""

import requests
import re
from datetime import datetime
from typing import Tuple, Dict, Optional, List, Union
import google.generativeai as genai

from config import Config, load_configuration
from utils import handle_api_errors, format_timestamp, clean_location_string

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
    # 1. Clean the location string using utils.clean_location_string()
    # 2. Make API call to OpenWeatherMap geocoding API
    # 3. Parse response and return coordinates
    # 4. Handle errors gracefully
    
    # For now, return None to make tests fail (TDD approach)
    return None, None, None

# TODO: Add all your other function stubs here...

def fetch_current_weather(lat: float, lon: float) -> Union[Dict, str]:
    """Fetch current weather for given coordinates"""
    pass

def fetch_weather_forecast(lat: float, lon: float, days: int = 5) -> Union[Dict, str]:
    """Fetch weather forecast for given coordinates"""
    pass

def extract_location_from_query(user_input: str) -> Optional[str]:
    """Extract location from natural language query"""
    pass

def determine_query_type(user_input: str) -> str:
    """Determine if query is for current weather or forecast"""
    pass

def parse_time_intent(user_input: str) -> Optional[int]:
    """Parse time-related intent from query"""
    pass

def convert_units(temp_celsius: float) -> Tuple[float, float, float]:
    """Convert temperature between units"""
    pass

def calculate_wind_direction(degrees: int) -> str:
    """Convert wind degrees to cardinal direction"""
    pass

def format_weather_data(raw_weather_dict: Dict) -> Dict:
    """Format raw API response to standardized structure"""
    pass

def initialize_gemini_client(api_key: str):
    """Initialize Gemini AI client"""
    pass

def generate_natural_response(weather_data: Dict, original_query: str) -> str:
    """Generate natural language response using Gemini"""
    pass

def create_fallback_response(weather_data: Dict) -> str:
    """Create basic response when AI is unavailable"""
    pass

def validate_api_keys(openweather_key: str, gemini_key: str) -> bool:
    """Validate API keys"""
    pass

def process_user_query(user_input: str) -> str:
    """Main function to process user queries"""
    pass

def cache_weather_data(location: str, weather_data: Dict, cache_duration: int = 10):
    """Cache weather data"""
    pass

def get_cached_data(location: str) -> Optional[Dict]:
    """Retrieve cached weather data"""
    pass

def log_user_interaction(query: str, response: str, timestamp: datetime):
    """Log user interactions"""
    pass

def run_interactive_session():
    """Run the interactive weather bot session"""
    pass

if __name__ == "__main__":
    run_interactive_session()
