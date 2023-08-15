import json
with open('servicios.json') as misEmpleados:
    data = json.load(misEmpleados)

    for usuario in data['usuarios']:
        print('Full name: ', usuario['full_name'])
        print('email: ', usuario['email'])
        print('Id number: ', usuario['id_number'])
        print('Total packagers per user: ', usuario['total_packagers_per_user'])
        print('Total price: ', usuario['total_price'])
        print('')