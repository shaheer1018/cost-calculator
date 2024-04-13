import pandas as pd
#------------------------------------------------------------------------
#                   Calculate miscellenous expenses
#------------------------------------------------------------------------
def calculate_miscellenous_expenses(*args):
    total_expenses = sum([*args])
    return total_expenses

#------------------------------------------------------------------------
#                       Animal price raw
#------------------------------------------------------------------------
def save_animal_price_raw(total_animals):
    animal_price_raw_dict = {}

    for i in range(1, total_animals + 1):
        price_of_animal  = int(input('Enter price of animal ' + str(i) + ': '))
        animal_price_raw_dict['animal_' + str(i)] = price_of_animal

    return animal_price_raw_dict


#-----------------------------------------------------------------------
#                     Create members tables     
#-----------------------------------------------------------------------
def create_members_table(animal_num):

    rows_list = []

    for i in range(1, 8):
        member_name = input(f'Enter name of member {i}: ')
        member_phone = input(f'Enter phone no. of member {i}: ')
        member_address = input(f'Enter address of member {i}: ')
        member_animal_num = input(f'Enter animal number: ')
        member_animal_total_expense = input(f'Enter total expenses of the animal {i}: ')
        member_received_amount = input(f'Enter received amount from member {i}: ')

        temp_difference = (float(member_received_amount) - float(member_animal_total_expense))
        
        if temp_difference > 0:
            receivable_amount = 0   
            refundable_amount = (float(member_received_amount) - float(member_animal_total_expense))

        elif temp_difference < 0:
            receivable_amount = (float(member_received_amount) - float(member_animal_total_expense))  
            refundable_amount = 0
        else:
            receivable_amount = 0 
            refundable_amount = 0

        rows_list.append({'Member name': member_name, 'Member phone': member_phone, 'Member address': member_address,
                          'Member_animal_num': member_animal_num, 'Cost per share': 0,
                          'Received amount': 0, 'Refundable': refundable_amount, 'Receivable': receivable_amount})

    df_members_sheet = pd.DataFrame(rows_list)


    return df_members_sheet

