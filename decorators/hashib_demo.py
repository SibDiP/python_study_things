import hashlib

def trace_hash(arg_str):
    print(f"1. Строка:   '{arg_str}'")
    data = arg_str.encode()
    print(f"2. Байты:    {data} ({len(data)}б)")
    
    md5_obj = hashlib.md5(data)
    print(f"3. MD5 obj:  {type(md5_obj)}")
    
    full_hex = md5_obj.hexdigest()
    print(f"4. Полный:   '{full_hex}' ({len(full_hex)} символов)")
    
    short_key = full_hex[:16]
    print(f"5. Короткий: '{short_key}' ({len(short_key)} символов)")
    print()

trace_hash("uppercase:bilbo")
trace_hash("uppercase:frodo")
