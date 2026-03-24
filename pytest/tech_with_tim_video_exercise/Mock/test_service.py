import pytest
from service import UserService, APIClient

def test_get_username_with_mock(mocker):
	mock_api_client = mocker.Mock(spec=APIClient) # создаём мок API клиента

	mock_api_client.get_user_data.return_value = {"id": 1, "name": "Alice"}
	
	service = UserService(mock_api_client) # Inject mock API client
	
	result = service.get_username(1) # Вызов метода опирающегося на mock
	
	# Assertions
	assert result == "ALICE" # проверка выполнена ли обработка данных корректно
	mock_api_client.get_user_data.assert_called_once_with(1) # проверка корректности вызова API.