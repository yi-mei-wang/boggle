import timeit

CODE = """filename = '/Users/mei/work/teaching/python-sep-19/day-3/recursion/boggle/dictionary.txt'
lines = [line.rstrip('\\n') for line in open(filename)]
"""


print(timeit.timeit(stmt=CODE,
                    number=2))
