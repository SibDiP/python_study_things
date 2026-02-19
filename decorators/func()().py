def func_two_brackets(*args):
    print(f"Outer args={args}")
    def inner_func(*args):
        print(f"inner args={args}")
        return 
    return inner_func

print()
func_two_brackets()
print()
func_two_brackets()()
print()
print(type(func_two_brackets()))
print()
print(type(func_two_brackets()()))