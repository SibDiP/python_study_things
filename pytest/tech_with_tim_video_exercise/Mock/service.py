import requests

class APIClient:
	"""Псевдо API клиент"""
	def get_user_data(self, user_id):
		response = requests.get(f"https://api.example.com/users/{user_id}")
		if response.status_code == 200:
			return response.json()
		raise ValueError("API request failed")
		
class UserService:
    """Использует APIClient для получения данных пользователя и их обработки"""
    def __init__(self, api_client):
        self.api_client = api_client # Dependency injection
        
    def get_username(self, user_id):
        """Скачивает данные пользователя и возвращает имя прописными буквами"""
        user_data = self.api_client.get_user_data(user_id) # Исправил опечатку (было users_data)
        return user_data["name"].upper() 
