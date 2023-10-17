class JustNotCoolError(Exception):
    pass

x = 2
try: #add a try block to catch errors (and prevent program from simply crashing)
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x/0 )
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else: #occurs if there are no errors
    print('No errors!')
finally: # will occur regardless if there are errors or not
    print("I'm going to print with or without an error.")