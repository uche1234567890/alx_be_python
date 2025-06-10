def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        try:
            result = num / denom
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."


# Example usage
result = safe_divide(73, 5)

if isinstance(result, float):
    print(f"The result of the division is {result}")
else:
    print(result)
