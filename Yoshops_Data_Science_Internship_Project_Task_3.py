def shipping_address_differs_billing_address():
    # Import necessary libraries
    import pandas as pd
    import ydata_profiling

    # Read the input data file
    df = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    df_copy = df.copy()

    # Filter the data based on the input value
    df_filtered = df_copy[df_copy['Shipping Street Address'] != df_copy['Billing Street Address']]

    # Generate a profile report of the filtered data
    profile = ydata_profiling.ProfileReport(df_filtered)

    # Save the profile report as a PDF file
    report_path = 'shipping_address_differs_billing_address.pdf'
    profile.to_file(report_path)

    # Generate an Excel sheet of the filtered data
    excel_path = 'shipping_address_differs_billing_address.xlsx'
    df_filtered.to_excel(excel_path, index=False)

    # Generate an CSV sheet of the filtered data
    csv_path = 'shipping_address_differs_billing_address.csv'
    df_filtered.to_csv(csv_path, index=False)

    # Print the number of orders where the shipping address differs from the billing address
    print(f"Number of orders where the shipping address differs from the billing address: {df_filtered.shape[0]}")


def multiple_orders_same_item():
    import pandas as pd
    import ydata_profiling

    # Read the input data file
    df = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    df_copy = df.copy()

    # Filter the data to include only orders with multiple items
    df_filtered = df_copy.groupby(['Order #', 'LineItem Name']).filter(lambda x: len(x) > 1)

    # Generate a profile report of the filtered data
    profile = ydata_profiling.ProfileReport(df_filtered)

    # Save the profile report as a PDF file
    report_path = 'multiple_orders_same_item.pdf'
    profile.to_file(report_path)

    # Generate a excel file of the filtered data
    excel_path = 'multiple_orders_same_item.xlsx'
    df_filtered.to_excel(excel_path, index=False)

    # Generate a CSV file of the filtered data
    csv_path = 'multiple_orders_same_item.csv'
    df_filtered.to_csv(csv_path, index=False)

    # Print the number of orders with multiple items of the same type
    print(f"Number of orders with multiple items of the same type: {df_filtered.shape[0]}")


def unusally_large_orders():
    # Import necessary libraries
    import pandas as pd
    import ydata_profiling

    # Read the input data file
    df = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    df_copy = df.copy()

    # Define the threshold value for unusually large orders
    threshold = '10000.00'

    # Filter the data based on the threshold value
    df_filtered = df_copy[df_copy['Total'] > threshold]

    # Generate a profile report of the filtered data
    profile = ydata_profiling.ProfileReport(df_filtered)

    # Save the profile report as a PDF file
    report_path = 'unusually_large_orders.pdf'
    profile.to_file(report_path)

    # Generate a CSV file of the filtered data
    csv_path = 'unusually_large_orders.csv'
    df_filtered.to_csv(csv_path, index=False)

    # Generate a excel file of the filtered data
    excel_path = 'unusually_large_orders.xlsx'
    df_filtered.to_excel(excel_path, index=False)

    # Print the number of unusually large orders
    print(f"Number of unusually large orders: {df_filtered.shape[0]}")


def multiple_order_same_address_different_payment_method():
    # Import necessary libraries
    import pandas as pd
    import ydata_profiling

    # Read the input data file
    df = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    df_copy = df.copy()

    # Filter the data based on the input value
    df_filtered = df_copy.groupby(['Shipping Street Address']).filter(lambda x: x['Payment Method'].nunique() > 1)

    # Generate a profile report of the filtered data
    profile = ydata_profiling.ProfileReport(df_filtered)

    # Save the profile report as a PDF file
    report_path = 'multiple_orders_same_address_diff_payment_method.pdf'
    profile.to_file(report_path)

    # Generate an Excel file of the filtered data
    excel_path = 'multiple_orders_same_address_diff_payment_method.xlsx'
    df_filtered.to_excel(excel_path, index=False)

    # Generate a CSV file of the filtered data
    csv_path = 'multiple_orders_same_address_diff_payment_method.csv'
    df_filtered.to_csv(csv_path, index=False)

    # Print the number of orders with multiple payment methods to the same address
    print(f"Number of orders with multiple payment methods to the same address: {df_filtered.shape[0]}")


def unexpected_international_orders():
    import pandas as pd
    import ydata_profiling

    # Read the input data file
    df = pd.read_csv("orders_2020_2021_DataSet_Updated.csv")
    df_copy = df.copy()

    # Filter the data based on the input value
    df_filtered = df_copy[(df_copy['Shipping Country'] != 'IND')]

    # Generate a profile report of the filtered data
    profile = ydata_profiling.ProfileReport(df_filtered)

    # Save the profile report as a PDF file
    report_path = 'unexpected_international_orders.pdf'
    profile.to_file(report_path)

    # Generate a CSV file of the filtered data
    csv_path = 'unexpected_international_orders.csv'
    df_filtered.to_csv(csv_path, index=False)

    # Generate an Excel file of the filtered data
    excel_path = 'unexpected_international_orders.xlsx'
    df_filtered.to_excel(excel_path, index=False)

    # Print the number of unexpected international orders
    print(f"Number of unexpected international orders: {df_filtered.shape[0]}")


def yoshops_data_science_intern_task_3():
    print("Welcome to Yoshops.com.")
    print("\n\nPlease select any one of the option:- ")
    print("\n\n Enter 1 to see the shipping address differs from the billing address.")
    print("\n\n Enter 2 to see multiple orders of the same item.")
    print("\n\n Enter 3 to see unusually large orders.")
    print("\n\n Enter 4 to see multiple orders to the same address with different payment method.")
    print("\n\n Enter 5 to see unexpected international orders.")
    choice = int(input("\n\nEnter only the numeric option(1,2,3,..,5) here : "))
    print("\n\nYou have selected option ", choice)

    def yoshops_sales_order_eda(choice):
        if choice == 1:
            return shipping_address_differs_billing_address()
        elif choice == 2:
            return multiple_orders_same_item()
        elif choice == 3:
            return unusally_large_orders()
        elif choice == 4:
            return multiple_order_same_address_different_payment_method()
        elif choice == 5:
            return unexpected_international_orders()
        else:
            print("\n\nYou have entered a false choice. Please go through the available options and try again")

    yoshops_sales_order_eda(choice)
yoshops_data_science_intern_task_3()
input('Enter 0 to exit: ')