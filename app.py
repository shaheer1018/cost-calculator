from src.helper_functions import calculate_miscellenous_expenses
from src.helper_functions import save_animal_price_raw
from src.helper_functions import create_members_table
import streamlit as st
import pandas as pd





def main():
    #-------------------------------------------------------------
    #               Calculate net expenses
    #-------------------------------------------------------------
    # Add a title to the app
    st.title("Calculate Net Expenses")

    expense1 = st.number_input('Labour cost (animal purchasing): ', min_value=0, max_value=99999999)
    expense2 = st.number_input('Labour cost loading animals: ', min_value=0, max_value=99999999)
    expense3 = st.number_input('Market animal tax: ', min_value=0, max_value=99999999)
    expense4 = st.number_input('Transportation of animals (fare): ', min_value=0, max_value=99999999)
    expense5 = st.number_input('Miscellaneous expenses market: ', min_value=0, max_value=99999999)
    expense6 = st.number_input('Labour cost unloading animals: ', min_value=0, max_value=99999999)
    expense7 = st.number_input('Gaurd charges: ', min_value=0, max_value=99999999)
    expense8 = st.number_input('Total expenses of animal food: ', min_value=0, max_value=99999999)
    expense9 = st.number_input('Labour cost butcher: ', min_value=0, max_value=99999999)
    expense10 = st.number_input('Shoping bags for meat cost: ', min_value=0, max_value=99999999)
    expense11 = st.number_input('Expenses for tent etc.: ', min_value=0, max_value=99999999)
    expense12 = st.number_input('Labour for workers: ', min_value=0, max_value=99999999)
    expense13 = st.number_input('Expenses for lunch etc.: ', min_value=0, max_value=99999999)
    income = st.number_input('Income: ', min_value=0, max_value=99999999)
    total_expenses = calculate_miscellenous_expenses(expense1, expense2, expense3, expense4, expense5, 
                                                     expense6, expense7, expense8, expense9, expense10, 
                                                     expense11, expense12, expense13)
    

    # Add a button to submit the input
    if st.button("Submit"):

        print('Total expenses: ', total_expenses)
        net_expenses = (total_expenses - income)
        print('Net expenses: ', net_expenses)

        # Create a new DataFrame with the user input
        new_row = {'Labour cost (animal purchasing)': expense1, 'Labour cost loading animals': expense2,
                   'Market animal tax': expense3, 'Transportation of animals (fare)': expense4,
                   'Miscellaneous expenses market': expense5, 'Labour cost unloading animals:': expense6,
                   'Gaurd charges': expense7, 'Total expenses of animal food': expense8,
                   'Labour cost butcher': expense9, 'Shoping bags for meat cost:': expense10, 
                   'Expenses for tent etc.': expense11, 'Labour for workers': expense12, 
                   'Expenses for lunch etc.': expense13, 'Income': income, 'Total expenses': total_expenses,
                   'Net expenses': net_expenses}
        df_net_expenses = pd.DataFrame([new_row])

        # Display the updated DataFrame as a table
        st.table(df_net_expenses)

    


    #-------------------------------------------------------------
    #                  Cost per share
    #-------------------------------------------------------------

    # Define the column names
    columns = ['Animal Number', 'Animal Price', 'Expenses Per Animal', 'Total Cost Per Animal', 'Cost Per Share']

    # Prompt the user to enter the number of initial rows
    initial_rows = st.number_input("Enter the number of initial rows:", min_value=0, value=2, step=1)

    # Initialize the DataFrame with the specified number of initial rows and the given columns
    # Use appropriate data types for Columns 2, 3, and 4 (float) and Column 1 and 5 (str)
    df_cost_per_share = pd.DataFrame(
                                    {
                                        'Animal Number': [0] * int(initial_rows),
                                        'Animal Price': [0] * int(initial_rows),
                                        'Expenses Per Animal': [0] * int(initial_rows),
                                        'Total Cost Per Animal': [0] * int(initial_rows),
                                        'Cost Per Share': [0] * int(initial_rows)
                                    }
                                )

    # Function to display input fields for each row and calculate Column 4
    def display_input_fields(df):
        # Iterate through the rows of the DataFrame
        for idx, row in df.iterrows():
            # Create unique keys based on the row index for each widget
            col1_key = f'col1_{idx}'
            col2_key = f'col2_{idx}'
            col3_key = f'col3_{idx}'
            # col5_key = f'col5_{idx}'

            # Display input fields for each column (except Column 4) in the row using unique keys
            col1 = st.number_input(f"{columns[0]} (Row {idx + 1}):", value=float(row[columns[0]]), key=col1_key)
            col2 = st.number_input(f"{columns[1]} (Row {idx + 1}):", value=float(row[columns[1]]), key=col2_key)
            col3 = st.number_input(f"{columns[2]} (Row {idx + 1}):", value=float(row[columns[2]]), key=col3_key)
            # Calculate Column 4 as the sum of Columns 2 and 3
            col4 = col2 + col3
            # Calculate Column 5 
            col5 = col4/7
            
            # Update the DataFrame with the input values for Columns 1, 2, 3, and calculated value for Column 4, 5
            df.loc[idx] = [col1, col2, col3, col4, col5]

    # Display input fields for the DataFrame
    display_input_fields(df_cost_per_share)

    # Button to add a new row
    if st.button("Add Row"):
        # Append an empty row to the DataFrame
        new_row = pd.Series([0, 0, 0, 0, 0], index=columns)
        df = df.append(new_row, ignore_index=True)
        # Redisplay input fields for the updated DataFrame
        display_input_fields(df)

    # Display the DataFrame as a table
    st.write("Your Data Table:")
    st.table(df)


if __name__ == '__main__':
    main()














# Create input widgets
name = st.text_input("Enter your name:")

city = st.text_input("Enter your city:")

