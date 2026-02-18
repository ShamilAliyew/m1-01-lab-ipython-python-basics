def string_to_float(text):
    try:
        return float(text)
    except ValueError:
        return None

def clean_str(text):
    return text.strip().upper()


test_inputs = ["hello", " 3.14 ", "", "abc", "  7  ", "4.5"]

float_results = [string_to_float(x) for x in test_inputs]

cleaned_results = [clean_str(x) for x in test_inputs]

print("string_to_float results:", float_results)
print("clean_str results:", cleaned_results)