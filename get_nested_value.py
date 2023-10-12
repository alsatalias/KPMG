def get_nested_value(data, key):
    if '/' in key:
        result = data
        keys = key.split('/')
        for i in keys:
            print(i)
            if isinstance(result, dict) and i in result:
                result = result[i]
                print(result)

            else:
               return None
        return result
    else:
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    return v
                if isinstance(v, (dict, list)):
                    result = get_nested_value(v, key)
                    if result is not None:
                        return result
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    result = get_nested_value(item, key)
                    if result is not None:
                        return result

# Inputs:
data = {"a": {"b": {"c": "d"}}}

key_to_find = "a/b/c"

result = get_nested_value(data, key_to_find)

if result is not None:
    print(f"The value for key'{key_to_find}' is: {result}")
else:
    print(f"Key '{key_to_find}' not found in the nested object.")