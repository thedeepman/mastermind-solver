def example_method():
    return 0

def method_with_examples(num, operation):
    if operation == 'add':
        return num + num
    elif operation == 'multiply':
        return num * num
    else:
        return Exception("Not a valid operation")