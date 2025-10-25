def add(a :int, b :int) -> int:
   """
   >>> add(1, 2)
   4
   """
   return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()