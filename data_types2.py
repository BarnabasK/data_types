# For strings, return its length.
# For None return string 'no value'
# For booleans return the boolean
# For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
# For lists return the 3rd item, or None if it doesn't exist

def data_type(data):
    if data is None:
        return 'no value'
    if isinstance(data, str):
        return len(data)
    elif isinstance(data, bool):
        return data
    elif isinstance(data, int):
        if data < 100:
            return "less than 100"
        elif data == 100:
            return "equal to 100"
        return "more than 100"
    elif isinstance(data, list):
        return data[2] if len(data) > 2 else None

print data_type(None)        