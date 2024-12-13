def function_with_uncommon_error(x, y):
    if x == 0:
        return 0  # This is correct for division by zero
    result = y / x
    return result

# Uncommon scenario: Exception occurs when the user passes incorrect input
# or when data is not of the expected type
try:
    result = function_with_uncommon_error(0, 10)
    print(f"Result: {result}")
except TypeError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

#Another uncommon error: forgetting to handle exceptions properly
def another_function(data):
    try:
      result = len(data) / data[0]
    except (IndexError, TypeError) as e:
      return "Error Occurred"    
    return result

print(another_function([0])) # leads to ZeroDivisionError
print(another_function([]))   # leads to IndexError
print(another_function([1,2,3]))# returns 1.5