#Explain Exception handling? What is an Error in Python?
'''
->In python, an error is a problem in the program that cause it to fail.
->Error hase two type:
-Syntax Errors:
 this is eccure in the syntax of the code.
 Example:
 if true
     print("hello world")
 -this example : is missing so this is called syntax error.
-Exceptions:
 this error eccure during execution time.
 Example:
 result = 10 / 0
 - this example eccure error  zerodivisionerror beacuse division by zero is not
 allowed
******************************************************************
->Exception handling is mechanism in pyhton to handle error and exceptional
  condition in controlled way.
->Structure of exception handling:
-try:
 This block contains the code that might throw an exception.
-exception:
 This block catches and handles the exception if it occurs in the try block
-else block:
 this block executes if the code in the try block does not raise an exception.
-finally block:
 this block code contaion code that will run no mettor what.
 


'''
