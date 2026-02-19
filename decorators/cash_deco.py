import time
from functools import lru_cache

@lru_cache()
def my_long_calc():
    time.sleep(3)
    return 42

print(my_long_calc())
print(my_long_calc())
print(my_long_calc())

