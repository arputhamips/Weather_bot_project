import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration management for Weather Bot"""
    
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # API URLs
    OPENWEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5"
    OPENWEATHER_GEO_URL = "http://api.openweathermap.org/geo/1.0"
    
    # Default settings
    DEFAULT_UNITS = "metric"
    CACHE_DURATION_MINUTES = 10
    MAX_FORECAST_DAYS = 5

def load_configuration():
    """Load and validate configuration"""
    config = {
        'openweather_key': Config.OPENWEATHER_API_KEY,
        'gemini_key': Config.GEMINI_API_KEY,
        'openweather_base_url': Config.OPENWEATHER_BASE_URL,
        'openweather_geo_url': Config.OPENWEATHER_GEO_URL
    }
    
    # Validate required keys
    if not config['openweather_key']:
        raise ValueError("OPENWEATHER_API_KEY not found in environment variables")
    if not config['gemini_key']:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    return config