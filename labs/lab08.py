# Nome 
# Data DD-MM-AAAA
# Endereco
# telefone (XX)XXXXX-XXXX

total_clients = None
clients = []

last_name_patterns = ['de', 'da', 'das', 'do', 'dos', 'e']

def format_name(name):
    formated_name = ' '
    name = ([item.lower() if item.lower() in last_name_patterns else item.capitalize() for item in name])
    return formated_name.join(name)

def format_birthday(birthday):
    # DD/MM/AAAA, DDMMAAAA e DD-MM-AAAA
    birthday = (birthday.replace('/', '').replace('-', ''))
    birthday = f"{birthday[0]}{birthday[1]}-{birthday[2]}{birthday[3]}-{birthday[4]}{birthday[5]}{birthday[6]}{birthday[7]}"
    return birthday

def format_address(address):
    address_number = address.replace('-', ',')
    address_number = address_number.split(',')
    address_number[0] = format_name(address_number[0].split(' '))
    address_number[0] = address_number[0].rstrip()
    address_number[1] = address_number[1].lstrip()
    address_number = f"{address_number[0]}, {address_number[1]}"
    return address_number

def format_phone(phone_number):
    phone_number = phone_number.replace('(', '').replace(')', '').replace('-', '')
    phone_number = f"({phone_number[0]}{phone_number[1]}){phone_number[2]}{phone_number[3]}{phone_number[4]}{phone_number[5]}{phone_number[6]}-{phone_number[7]}{phone_number[8]}{phone_number[9]}{phone_number[10]}"
    return phone_number

def format_item(item: dict):
    item['name'] = format_name(item.get('name').split(' '))
    item['birthday'] = format_birthday(item.get('birthday'))
    item['address'] = format_address(item.get('address'))
    item['phone_number'] = format_phone(item.get('phone_number'))
    return item

while True:
    if not total_clients:
        n = input()
        total_clients = n

    name = input('')
    birthday = input('')
    address = input('')
    phone = input('')

    formated_item = format_item({
        "name": name,
        "birthday": birthday,
        "address": address,
        "phone_number": phone
    })
    clients.append(formated_item)

    if len(clients) == int(total_clients):
        for item in clients:
            for value in item.values():
                print(value)
        break

    continue