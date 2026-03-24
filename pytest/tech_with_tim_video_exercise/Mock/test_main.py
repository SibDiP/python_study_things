import pytest
from main import get_wather

def test_get_weather(mocker): # pip install pytest-mock
	# Mock requests.get. Подменяем.
	mock_get = mocker.patch("main.requests.get") 
	
	# Set return values
	mock_get.return_value.status_code = 200
	mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}
	
	# Call function
	result = get_wather("Dubai")
	
	# Assertations
	assert result == {"temperature": 25, "condition": "Sunny"}
	mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
	# вариант проверки количества вызовов
	assert mock_get.call_count == 1  # Проверяем, что было именно 1 вызова