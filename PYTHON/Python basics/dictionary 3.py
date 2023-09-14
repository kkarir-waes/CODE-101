
# multiple items in dictionary

payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
     'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}

print(payroll)

print('Emp1 name', payroll['emp1']['name'])
print('Emp1 salary',payroll['emp1'].get('salary'))
print('Emp1 wage',payroll['emp1'].get('Wage'))
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}
print('updated ',payroll)
del payroll['emp3']

for id, info in payroll.items():
    print(f'\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')

