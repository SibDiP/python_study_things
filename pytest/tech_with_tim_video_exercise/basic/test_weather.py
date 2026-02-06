from weather import get_weather

def test_get_weather():
    assert get_weather(21) == "Hot"
    assert get_weather(19) == "Cold"
    assert get_weather(0) == "Cold"
    assert get_weather(-1) == "Cold"


