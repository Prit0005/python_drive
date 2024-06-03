#When is the finally block executed?
'''
The finally block in Python is executed when  exception is occurred or not.
It is typically used for cleanup code that needs to be executed whether an
exception occurred or not, such as closing files or releasing other resources.
'''

try:
    x = 10 / 0 
except ZeroDivisionError:
    print("Division by zero error occurred")
finally:
    print("finally occurred")
