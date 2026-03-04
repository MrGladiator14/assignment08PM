bryson@bryson-Nitro-15:~/dev/week-2/day-8/assignment08PM/partC$ python -c "
from improved_diamond_pattern import generate_diamond_pattern
 
print('Testing n = 1:')
print(repr(generate_diamond_pattern(1)))
print('Output:')
print(generate_diamond_pattern(1))
 
print('\nTesting n = 3:')
print(repr(generate_diamond_pattern(3)))
print('Output:')
print(generate_diamond_pattern(3))
 
print('\nTesting n = 5:')
print(repr(generate_diamond_pattern(5)))
print('Output:')
print(generate_diamond_pattern(5))
 
print('\nTesting n = 0:')
print(repr(generate_diamond_pattern(0)))
print('Output:')
print(generate_diamond_pattern(0))
"
Testing n = 1:
'*\n'
Output:
*


Testing n = 3:
'  *\n ***\n*****\n ***\n  *\n'
Output:
  *
 ***
*****
 ***
  *


Testing n = 5:
'    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n'
Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


Testing n = 0:
''
Output:
