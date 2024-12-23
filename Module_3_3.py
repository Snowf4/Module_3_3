def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [14, 'october', False]
values_dict = {'a':65, 'b':False, 'c':'Строка'}
values_list_2 = [84.11, 'SPACE']

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)