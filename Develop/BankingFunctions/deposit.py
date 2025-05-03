"""This function handles the deposit process for the user."""

# TODO: Build out the handle_deposit function
# TODO: Pass in the checking account and savings account objects.
def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    # TODO: Prompt the user to select an account and make a deposit.
    # TODO: If the user chooses to quit, return from the function.
    choice = input("Enter 1 for checking, 2 for savings, q to quit: ")
    if choice == "q":
        return
    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        if choice in ["1", "2"]:
            try:
                # TODO: Prompt the user to enter the amount to deposit and convert it to a float.
                amount = float(input("How much would you like to deposit? $"))
            # Use the ValueError as an exception.
            except ValueError:
                # TODO: Print an error message if the user enters an invalid amount.

                # TODO: Call the handle_deposit function recursively for an invalid amount.

                # TODO: Ensure the function returns after the recursive call.
                print("Invalid amount. Please enter a valid number.")
                handle_deposit(checking, savings)
                return


            # TODO: Add an if/else conditional statement to check the account choice,
            if choice == "1":
                checking.deposit(amount)
                print(f"Here is your checking balance: ${checking.get_balance():,.2f}")
                # TODO: Call the withdraw method on the appropriate account.
                # TODO: Add a print statement to display the updated balance after the deposit
                # TODO: Format the balance to two decimal places and thousands.
            else:
                savings.deposit(amount)
                print(f"Here is your savings balance: ${savings.get_balance():,.2f}")
                # TODO: Call the deposit methods on the appropriate account.
                # TODO: Add a print statement to display the updated balance after the deposit
                # TODO: Format the balance to two decimal places and thousands.
        else:
            raise ValueError("Invalid choice. Please enter 1, 2, or q.")
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
