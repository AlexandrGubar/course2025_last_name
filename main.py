def process_string(s):
    return "".join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(s))
