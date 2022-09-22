# import statements


# functions go here

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank, please enter your name")

# checks fro an integer between two values
def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        #ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error
        except ValueError:
            print(error)



# Main Routine
name = ""
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

while name != "xxx" and ticket_count <= MAX_TICKETS:
    print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    # Get details...
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    ticket_count += 1

    if ticket_count == MAX_TICKETS:
        print("You have sold all the available tickets!")
    else:
        print("You have sold {} tickets. There are {} places still available".format(ticecount, MAX_TICKETS - count))
    # main routine goes here
    age = int_check("Age: ", 12, 130)


# End of tickets loop

# Calculate profit etc..
if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} places still available".format(count, MAX_TICKETS - count))


# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# Get name (can't be blank)
name = not_blank("Name: ")

# Get age (between 12 and 130)
age = int_check("Age: ")

# Check that age is valid...

    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5


    ticket_count +=1
    ticket_sales += ticket_price


#Calculate the ticket price
ticket_profit = ticket_sales - (5 * ticket_count)

# Loop to ask for snacks

# Calculate snack price

# ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file
