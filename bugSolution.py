def function_with_uncommon_error(x, y):
    if x == 0 or type(x) is not int or type(y) is not int:
        return "Invalid Input: x must be non-zero integer and y must be an integer"
    result = y / x
    return result

# Improved exception handling and input validation
try:
    result = function_with_uncommon_error(0, 10)
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {e}")

#Another uncommon error: forgetting to handle exceptions properly
def another_function(data):
    if not data:
        return "Error: Empty input list"
    try:
      result = len(data) / data[0]
    except (IndexError, TypeError,ZeroDivisionError) as e:
      return "Error Occurred"
    return result

print(another_function([0])) # leads to Error Occurred
print(another_function([]))   # leads to Error: Empty input list
print(another_function([1,2,3]))# returns 1.5