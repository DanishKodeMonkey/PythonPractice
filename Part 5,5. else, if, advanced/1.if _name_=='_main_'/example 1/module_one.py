'''
if __name__ == '__main__'
'''

'''
Why does this happen?
For starters, remember python files are also known as modules.
and if __name__ == '__main__' then:
1. The Module can be run as a standalone program
2. The Module can be imported and used by other modules

So by using the if __name__ == '__main__'
were effectively checking if the module is being run directly, or indirectly by another module.

Python interpreter sets "special variables", one of which is __name__
then python will execute the code found within __main__
'''
import module_two

print(__name__)
print(module_two.__name__)

print("-----------------------------------")

if __name__ == '__main__':
    print("Running this module directly")
else:
    print("Running other module indirectly")
