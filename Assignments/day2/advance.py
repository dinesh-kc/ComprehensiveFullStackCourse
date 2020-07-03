
name = input ('Enter  name:')
phone_no = input('Enter Phone No:')
first_name = name.split()[0]


username = f'{first_name}_{phone_no[-4::]}'
password = f'{phone_no[:4]}_{first_name[:2].upper()}'
print(f'username- {username} && password- {password}')
