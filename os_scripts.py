import os
print('\n')
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

current_dir = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(current_dir, 'tmp'))
