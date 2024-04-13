from src.helper_functions import calculate_miscellenous_expenses
from src.helper_functions import save_animal_price_raw
from src.helper_functions import create_members_table
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime




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


    st.markdown(f"**Total expenses:** {total_expenses}")
    net_expenses = (total_expenses - income)
    st.markdown(f"**Net expenses:** {net_expenses}")

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

    # Convert the DataFrame to CSV format
    df_net_expenses_csv = df_net_expenses.to_csv(index=False)

    # Add a download button to allow the user to download the CSV file
    st.download_button(label="Download table as CSV", data=df_net_expenses_csv, file_name="net_expenses.csv")

    


    #-------------------------------------------------------------
    #                  Cost per share
    #-------------------------------------------------------------
    st.title("Cost per share")
    
    # Step 1: Get the number of rows from the user
    num_rows = st.number_input("Enter the total number of animals: ", min_value=3, step=1)
    
    # Step 2: Initialize an empty DataFrame with the specified number of rows and 5 columns
    if num_rows > 0:
        # Define the data types for each column
        dtypes = {
            "Animal Number": float,  # Use float to allow NaN values
            "Animal Price": float,
            "Expenses Per Animal": float,
            "Total Cost Per Animal": float,
            "Cost Per Share": float,
        }
        
        # Create the DataFrame with the specified data types
        df_cost_per_share = pd.DataFrame(index=range(num_rows), columns=dtypes.keys())
        df_cost_per_share = df_cost_per_share.astype(dtypes)  # Apply the specified data types to the DataFrame
        
        # Step 3: Populate the table based on user input
        for i in range(num_rows):
            # User input for each row
            col1 = st.number_input(f"Enter value for Animal Number, Row {i + 1}:", key=f"col1_{i}")
            col2 = st.number_input(f"Enter value for Animal Price, Row {i + 1}:", key=f"col2_{i}")
            col3 = st.number_input(f"Enter value for Expenses Per Animal, Row {i + 1}:", key=f"col3_{i}")
            
            # Fill in the DataFrame with the user inputs for columns 1, 2, and 3
            df_cost_per_share.loc[i, "Animal Number"] = col1 if col1 != 0 else np.nan  # Allow NaN values in Animal Number column
            df_cost_per_share.loc[i, "Animal Price"] = col2
            df_cost_per_share.loc[i, "Expenses Per Animal"] = col3
            
            # Step 4: Calculate Column 4 as the sum of Column 2 and Column 3
            df_cost_per_share.loc[i, "Total Cost Per Animal"] = df_cost_per_share.loc[i, "Animal Price"] + df_cost_per_share.loc[i, "Expenses Per Animal"]
            
            # Step 5: Calculate Column 5 as Column 4 divided by 7
            df_cost_per_share.loc[i, "Cost Per Share"] = df_cost_per_share.loc[i, "Total Cost Per Animal"] / 7
        
        # Step 6: Display the final DataFrame as a table
        st.table(df_cost_per_share)

        # Convert the DataFrame to CSV format
        df_cost_per_share_csv = df_cost_per_share.to_csv(index=False)

        # Add a download button to allow the user to download the CSV file
        st.download_button(label="Download table as CSV", data=df_cost_per_share_csv, file_name="cost_per_share.csv")


    #-------------------------------------------------------------
    #                 Total number of animals
    #-------------------------------------------------------------
    total_animals = len(df_cost_per_share)
    st.markdown(f"**Total animals:** {total_animals}")


    #-------------------------------------------------------------
    #                Total expenses per animal
    #-------------------------------------------------------------
    net_expenses_per_animal = net_expenses / total_animals
    st.markdown(f"**Net expenses per animal:** {net_expenses_per_animal}")



    #-------------------------------------------------------------
    #                Animal price raw
    #-------------------------------------------------------------
    st.title("Animal price raw")
    
    # Get the number of rows from the user
    num_rows_animal_price_raw = st.number_input("Enter the number of animals: ", min_value=3, step=1)
    
    # Initialize an empty DataFrame with the specified number of rows and 2 columns
    if num_rows > 0:
        # Define the data types for each column
        dtypes = {
            "Animal Number": float,  # Use float to allow NaN values
            "Animal Price": float}
        
        # Create the DataFrame with the specified data types
        df_animal_price_raw = pd.DataFrame(index=range(num_rows_animal_price_raw), columns=dtypes.keys())
        df_animal_price_raw = df_animal_price_raw.astype(dtypes)  # Apply the specified data types to the DataFrame
        
        # Step 3: Populate the table based on user input
        for i in range(num_rows_animal_price_raw):
            # User input for each row
            col1 = st.number_input(f"Enter value for Animal Number, Row {i + 1}:", key=f"animal_number_raw_col_{i}")
            col2 = st.number_input(f"Enter value for Animal Price, Row {i + 1}:", key=f"animal_price_raw_col_{i}")
            
            # Fill in the DataFrame with the user inputs for columns 1, 2, and 3
            df_animal_price_raw.loc[i, "Animal Number"] = col1 if col1 != 0 else np.nan  # Allow NaN values in Animal Number column
            df_animal_price_raw.loc[i, "Animal Price"] = col2
            
        
        # Display the final DataFrame as a table
        st.table(df_animal_price_raw)

        # Convert the DataFrame to CSV format
        df_animal_price_raw_csv = df_animal_price_raw.to_csv(index=False)

        # Add a download button to allow the user to download the CSV file
        st.download_button(label="Download table as CSV", data=df_animal_price_raw_csv, file_name="animal_price_raw.csv")

    #-------------------------------------------------------------
    #                 Total cost per animal
    #-------------------------------------------------------------
    st.title("Individual animal price total")
    
    # Copy the original DataFrame to create a new DataFrame
    df_total_cost_per_animal = df_animal_price_raw.copy()
    
    # update the total price of each animal
    df_total_cost_per_animal['Animal Price Total'] = df_total_cost_per_animal['Animal Price'] + net_expenses_per_animal

    # Display the new DataFrame as a table
    # st.subheader("Individual animal price total")
    st.table(df_total_cost_per_animal)


    #-------------------------------------------------------------
    #                 Create members tables
    #-------------------------------------------------------------
    st.title("Create Members Information Tables")
    
    # Prompt the user for the number of tables they want to create
    num_tables = st.number_input("For how many animals do you want to create tables?", min_value=1, step=1, key="num_tables")
    members_tables_list = []


    # Create the specified number of tables
    for table_index in range(int(num_tables)):
        # Add a subheader to distinguish each table
        st.subheader(f"Table for Animal {table_index + 1}")
        
        # Create the table using the function, passing the table index
        members_table = create_members_table(table_index)
        members_tables_list.append(members_table)
        # Display the table using Streamlit
        st.table(members_table)
        
        # Optionally, provide a download button for each table as CSV
        csv = members_table.to_csv(index=False)
        st.download_button(
            label=f"Download Table for animal {table_index + 1} as CSV",
            data=csv,
            file_name=f"members_table_animal_{table_index + 1}.csv")
    
    print(len(members_tables_list))
    print(members_tables_list[0])

    
if __name__ == '__main__':
    main()














