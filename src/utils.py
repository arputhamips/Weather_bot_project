"""
Utility functions for Weather Bot
"""

import re
from datetime import datetime
from typing import Dict, Optional, Any

def handle_api_errors(response) -> Optional[Dict[str, Any]]:
    """Handle API response errors"""
    if response.status_code == 200:
        return None
    
    error_info = {
        'error': True,
        'status_code': response.status_code,
        'message': response.text
    }
    return error_info

def format_timestamp(unix_timestamp: int) -> str:
    """Convert Unix timestamp to readable format"""
    dt = datetime.fromtimestamp(unix_timestamp)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def clean_location_string(raw_location: str) -> str:
    """Clean and standardize location string"""
    if not raw_location:
        return ""
    
    # Remove extra whitespace and punctuation
    cleaned = re.sub(r'[.!?]+$', '', raw_location.strip())
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    return cleaned