first_name = input(' qual é seu primeiro nome? ')
last_name = input(' qual é seu segundo nome? ')

output1= 'Ola, ' + (first_name + ' ' + last_name)
output2= 'Ola, {} {}'.format(first_name, last_name)
output3= 'Ola, {0} {1}'.format(first_name, last_name)
print(output1)
print(output2)
print(output3)