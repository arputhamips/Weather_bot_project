# 🌤️ Weather Bot Project

A sophisticated weather inquiry bot that provides natural language weather information using OpenWeatherMap and Google Gemini AI. Built with test-driven development principles for reliability and maintainability.

## 🚀 Features

- **Natural Language Processing**: Ask questions like "What's the weather in Boston?" or "Will it rain tomorrow in Seattle?"
- **Current Weather Data**: Real-time temperature, humidity, pressure, wind conditions
- **Weather Forecasts**: 5-day weather predictions with 3-hour intervals
- **AI-Powered Responses**: Natural, conversational responses using Google Gemini AI
- **Global Coverage**: Weather data for cities worldwide
- **Smart Location Parsing**: Understands various location formats (city, state, country)
- **Multiple Units**: Temperature in Celsius, Fahrenheit, and Kelvin
- **Caching System**: Reduces API calls with intelligent data caching
- **Error Handling**: Robust error handling for network issues and invalid inputs

## 📋 Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key ([Get one here](https://openweathermap.org/api))
- Google Gemini API key ([Get one here](https://ai.google.dev/))

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather_bot_project.git
cd weather_bot_project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root:
```bash
OPENWEATHER_API_KEY=your_openweather_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ **Never commit your `.env` file to version control!**

### 4. Verify Installation
```bash
python -c "from src.config import load_configuration; print('Setup successful!')"
```

## 🏃‍♂️ Quick Start

### Run the Interactive Bot
```bash
cd src
python weather_bot.py
```

### Example Usage
```
🌤️  Weather Inquiry Bot
Ask me about weather conditions anywhere in the world!

You: What's the weather in Minneapolis?
Bot: The current weather in Minneapolis is 22°C (72°F) with partly cloudy skies. 
     Humidity is at 65% with light winds from the northwest at 8 km/h. 
     It's a pleasant day to be outside!

You: Weather forecast for London tomorrow
Bot: Tomorrow in London, expect cloudy conditions with temperatures reaching 
     18°C (64°F). There's a 30% chance of light rain in the afternoon, 
     so you might want to carry an umbrella just in case.
```

## 🧪 Development & Testing

This project follows **Test-Driven Development (TDD)** principles.

### Run Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test categories
python -m pytest tests/test_weather_bot.py::TestWeatherDataFunctions -v
python -m pytest tests/test_weather_bot.py::TestQueryProcessingFunctions -v

# Run with coverage report
pip install pytest-cov
python -m pytest tests/ --cov=src --cov-report=html
```

### Development Workflow
1. **Write/Run Tests**: Tests define the expected behavior
2. **Implement Function**: Code until tests pass
3. **Refactor**: Improve code while keeping tests green
4. **Repeat**: Move to next function

### Project Structure
```
weather_bot_project/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── .env                        # API keys (not in git)
├── .gitignore                  # Git ignore rules
├── src/                        # Source code
│   ├── __init__.py
│   ├── weather_bot.py          # Main bot implementation
│   ├── config.py               # Configuration management
│   └── utils.py                # Utility functions
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_weather_bot.py     # Main test file
│   ├── test_config.py          # Configuration tests
│   └── conftest.py             # Test fixtures
└── docs/                       # Documentation
    └── api_documentation.md    # API documentation
```

## 📚 API Documentation

### Core Functions

#### Weather Data Functions
- `get_coordinates(location_string)` - Convert city names to GPS coordinates
- `fetch_current_weather(lat, lon)` - Get current weather conditions
- `fetch_weather_forecast(lat, lon, days)` - Get weather forecast

#### Query Processing Functions
- `extract_location_from_query(user_input)` - Parse location from natural language
- `determine_query_type(user_input)` - Identify current vs forecast requests
- `parse_time_intent(user_input)` - Extract time-related requests

#### AI Response Functions
- `generate_natural_response(weather_data, query)` - AI-powered responses
- `create_fallback_response(weather_data)` - Backup response system

### Example API Usage
```python
from src.weather_bot import get_coordinates, fetch_current_weather

# Get coordinates for a city
lat, lon, city_name = get_coordinates("New York")

# Fetch current weather
weather_data = fetch_current_weather(lat, lon)
print(f"Temperature: {weather_data['temperature']}°C")
```

## 🤖 Technical Details

### APIs Used
- **OpenWeatherMap**: Weather data and geocoding
- **Google Gemini**: Natural language processing and response generation

### Key Technologies
- **Python 3.8+**: Core programming language
- **Requests**: HTTP API calls
- **Google Generative AI**: AI response generation
- **Pytest**: Testing framework
- **Python-dotenv**: Environment variable management

### Design Patterns
- **Test-Driven Development**: All functions have comprehensive tests
- **Separation of Concerns**: Config, utilities, and main logic separated
- **Error Handling**: Graceful degradation for API failures
- **Caching**: Optional data caching to reduce API calls

## 🔧 Configuration Options

Edit `src/config.py` to customize:

```python
class Config:
    DEFAULT_UNITS = "metric"        # metric, imperial, kelvin
    CACHE_DURATION_MINUTES = 10     # Cache duration
    MAX_FORECAST_DAYS = 5           # Maximum forecast days
```

## 🚨 Troubleshooting

### Common Issues

**ImportError: No module named 'src'**
```bash
# Make sure you're in the project root and src is in Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**API Key Errors**
- Verify your `.env` file exists and contains valid API keys
- Check that API keys are active and have proper permissions
- Ensure you haven't exceeded API rate limits

**Test Failures**
```bash
# Check if all dependencies are installed
pip install -r requirements.txt

# Run tests with verbose output to see specific failures
python -m pytest tests/ -v -s
```

**Location Not Found**
- Try different location formats: "City", "City, State", "City, Country"
- Check spelling of city names
- Some small towns may not be in the OpenWeatherMap database

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your feature first (TDD approach)
4. Implement your feature
5. Ensure all tests pass (`python -m pytest tests/ -v`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Development Guidelines
- Follow TDD: Write tests before implementation
- Maintain test coverage above 90%
- Use type hints for function signatures
- Add docstrings for all public functions
- Follow PEP 8 style guidelines

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for weather data API
- [Google AI](https://ai.google.dev/) for Gemini natural language processing
- [Pytest](https://pytest.org/) for excellent testing framework

## 📞 Support

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/weather_bot_project/issues)
- 📖 Documentation: [API Docs](docs/api_documentation.md)

## 🗺️ Roadmap

- [ ] **Phase 1**: Core weather functions (Current)
- [ ] **Phase 2**: Advanced forecasting features
- [ ] **Phase 3**: Web interface with Flask/FastAPI
- [ ] **Phase 4**: Weather alerts and notifications
- [ ] **Phase 5**: Historical weather data analysis
- [ ] **Phase 6**: Mobile app integration
- [ ] **Phase 7**: Machine learning weather predictions

---

**Built with ❤️ for robotics and autonomous systems applications**

*This weather bot can be integrated into larger autonomous systems for environmental awareness and decision-making in outdoor robotics applications.*
