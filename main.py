def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        space = (length - len(string)) // 2
        return " " * space + string