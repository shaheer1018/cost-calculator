from IPython.display import display
from src.helper_functions import calculate_miscellenous_expenses
from src.helper_functions import save_animal_price_raw
from src.helper_functions import create_members_table
import pandas as pd

def main():
    #-------------------------------------------------------------
    #               Calculate total expenses
    #-------------------------------------------------------------
    expense1 = float(input('Labour cost (animal purchasing): '))
    expense2 = float(input('Labour cost loading animals: '))  
    expense3 = float(input('Market animal tax: '))
    expense4 = float(input('Transportation of animals (fare): '))
    expense5 = float(input('Miscellaneous expenses market: '))
    expense6 = float(input('Labour cost unloading animals: '))
    expense7 = float(input('Gaurd charges: '))
    expense8 = float(input('Total expenses of animal food: '))
    expense9 = float(input('Labour cost butcher: '))
    expense10 = float(input('Shoping bags for meat cost: '))
    expense11 = float(input('Expenses for tent etc.: '))
    expense12 = float(input('Labour for workers: '))
    expense13 = float(input('Expenses for lunch etc.: '))
    income = float(input('Enter income: '))
    total_expenses = calculate_miscellenous_expenses(expense1, expense2, expense3, expense4, expense5, 
                                                     expense6, expense7, expense8, expense9, expense10, 
                                                     expense11, expense12, expense13)
    print('Total expenses: ', total_expenses)
    net_expenses = total_expenses - income
    print('Net expenses: ', net_expenses)
    #-------------------------------------------------------------
    #                 Total number of animals
    #-------------------------------------------------------------
    total_animals = int(input('Enter total number of animals: '))
    print('Total animals: ', total_animals)

    #-------------------------------------------------------------
    #                Total expenses per animal
    #-------------------------------------------------------------
    net_expenses_per_animal = net_expenses / total_animals
    print('Total expenses per animal', net_expenses_per_animal)


    #-------------------------------------------------------------
    #                Save animal price raw
    #-------------------------------------------------------------
    animal_price_raw_dict = save_animal_price_raw(total_animals)
    print('Animal price raw dictionary')
    print(animal_price_raw_dict)


    #-------------------------------------------------------------
    #                 Total cost per animal
    #-------------------------------------------------------------
    # Create a new dictionary with each value updated
    total_cost_per_animal_dict = {key: value + net_expenses_per_animal for key, value in animal_price_raw_dict.items()}
    print('Total cost per animal dict')
    print(total_cost_per_animal_dict)

    # calculate actual cost per share for all the animals
    cost_per_share_animal_dict = {}
    for animal in total_cost_per_animal_dict.keys():
        print(animal)
        print(total_cost_per_animal_dict[animal])
        cost_per_share = total_cost_per_animal_dict[animal] / 7
        print('Cost per share')
        print(cost_per_share)
        cost_per_share_animal_dict['cost_per_share_' + animal] = cost_per_share

    print(cost_per_share_animal_dict)


    #-------------------------------------------------------------
    #           Create members table for each animal
    #-------------------------------------------------------------
    animal_num = 1
    df_members = create_members_table(animal_num)
    display(df_members)



if __name__ == '__main__':
    main()