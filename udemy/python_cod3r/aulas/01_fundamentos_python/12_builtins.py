# Builtins (Built-in)

"""
Builtins são basicamente funções (métodos) nativas da linguagem e as quais chamamos com o intuito de executarmos mais rapidamente 
certas ações. Por exemplo usamos a função 'print()' para imprimir em nosso terminal alguma informação, veremos mais funções abaixo.
"""

# type()
"""
A função 'type()' como o próprio nome já diz serve para apresentar o tipo de um dado
"""

type(1) # me retonará um inteiro '<class "int">'

# __builtins__()
"""
Magic methods são métodos que começam e terminam com 2(dois) sinais de underscore, também são comumente conhecidas como
Dunder Methods, no qual a palavra 'Dunder' faz referência a 'Double Under (Undescores)' e são usados muitas vezes
para realizam de sobrecarga de operadores, que basicamente é uma maneira de estender a linguagem para que você possa
fazer somas, multiplicações, conversões entre outras operações entre os objetos que você criou
"""

__builtins__.type("Olá mundo!") # retornará um string (str) '<class "str">'

__builtins__.print(10 / 3) # retornará o resultado da operação como sendo 3.3333...

# Escopo Global
"""
São métodos de escopo global àqueles que trazem o que podemos chamar de explicações e/ou esclarecimentos sobre
uma função builtin ou produto de uma função da sua aplicação 
"""

__builtins__.help(__builtins__.dir)
"""
Como resultado teremos algo assim:

'Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.'
"""

dir(__builtins__)

"""
Teremos como resulto o seguinte:

'[
    'ArithmeticError', 
    'AssertionError', 
    'AttributeError', 
    'BaseException', 
    'BaseExceptionGroup', 
    'BlockingIOError', 
    'BrokenPipeError', 
    'BufferError', 
    'BytesWarning', 
    'ChildProcessError', 
    'ConnectionAbortedError', 
    'ConnectionError', 
    'ConnectionRefusedError', 
    'ConnectionResetError', 
    'DeprecationWarning', 
    'EOFError', 
    'Ellipsis', 
    'EncodingWarning', 
    'EnvironmentError', 
    'Exception', 
    'ExceptionGroup', 
    'False', 
    'FileExistsError', 
    'FileNotFoundError', 
    'FloatingPointError', 
    'FutureWarning', 
    'GeneratorExit', 
    'IOError', 
    'ImportError', 
    'ImportWarning', 
    'IndentationError', 
    'IndexError', 
    'InterruptedError', 
    'IsADirectoryError', 
    'KeyError', 
    'KeyboardInterrupt', 
    'LookupError', 
    'MemoryError', 
    'ModuleNotFoundError', 
    'NameError', 
    'None', 
    'NotADirectoryError', 
    'NotImplemented', 
    'NotImplementedError', 
    'OSError', 
    'OverflowError', 
    'PendingDeprecationWarning', 
    'PermissionError', 
    'ProcessLookupError', 
    'RecursionError', 
    'ReferenceError', 
    'ResourceWarning', 
    'RuntimeError', 
    'RuntimeWarning', 
    'StopAsyncIteration', 
    'StopIteration', 
    'SyntaxError', 
    'SyntaxWarning', 
    'SystemError', 
    'SystemExit', 
    'TabError', 
    'TimeoutError', 
    'True', 
    'TypeError', 
    'UnboundLocalError', 
    'UnicodeDecodeError', 
    'UnicodeEncodeError', 
    'UnicodeError', 
    'UnicodeTranslateError', 
    'UnicodeWarning', 
    'UserWarning', 
    'ValueError', 
    'Warning', 
    'ZeroDivisionError', 
    '_', 
    '__build_class__', 
    '__debug__', 
    '__doc__', 
    '__import__', 
    '__loader__', 
    '__name__', 
    '__package__', 
    '__spec__', 
    'abs', 
    'aiter', 
    'all', 
    'anext', 
    'any', 
    'ascii', 
    'bin', 
    'bool', 
    'breakpoint', 
    'bytearray', 
    'bytes', 
    'callable', 
    'chr', 
    'classmethod', 
    'compile', 
    'complex', 
    'copyright', 
    'credits', 
    'delattr', 
    'dict', 
    'dir', 
    'divmod', 
    'enumerate', 
    'eval', 
    'exec', 
    'exit', 
    'filter', 
    'float', 
    'format', 
    'frozenset', 
    'getattr', 
    'globals', 
    'hasattr', 
    'hash', 
    'help', 
    'hex', 
    'id', 
    'input', 
    'int', 
    'isinstance', 
    'issubclass', 
    'iter', 
    'len', 
    'license', 
    'list', 
    'locals', 
    'map', 
    'max', 
    'memoryview', 
    'min', 
    'next', 
    'object', 
    'oct', 
    'open', 
    'ord', 
    'pow', 
    'print', 
    'property', 
    'quit', 
    'range', 
    'repr', 
    'reversed', 
    'round', 
    'set', 
    'setattr', 
    'slice', 
    'sorted', 
    'staticmethod', 
    'str', 
    'sum', 
    'super', 
    'tuple', 
    'type', 
    'vars', 
    'zip'
]'
"""
