
# Function to get a valid Date
def get_valid_date(date_message):
    
    date = ""
    valid_date = False

    while valid_date == False:
        date = input(f"Please enter {date_message} date dd/mm/yyyy : ")

        day, month, year = date.split('/')
        
        # check for all digits only
        if day.isdigit() and month.isdigit() and year.isdigit:                        # check for digits
            if day >= '01' and day <= '31':                 # day from 01 to 31
                  if month >= '01' and month <= '12':       # month 01 - 12:
                      if year >= '1900' and year <= '2050': # year 
                          valid_date = True

    return date
    # end of function ---------------------------------



# Function to get 'yes' or 'no' reply
def get_yes_or_no():
    
    yes_or_no = ""
    valid_reply = False

    while valid_reply == False:
        yes_or_no = input("Please enter Y/N or y/n : ")

        if yes_or_no.lower() == 'y' or yes_or_no.lower() == 'n':
            valid_reply = True

    return yes_or_no
    # end of function -------------------------------------------------------




# Get married status - M(arried) or S(ingle) ----------------------------
def get_status():

    married_status = ""
    valid_reply = False
    while valid_reply == False:
        married_status = input("Please enter married status - M /S or m/s : ")

        if married_status.lower() == 'm' or married_status.lower() == 's':
            valid_reply = True

    return married_status
    # end of function ---------------------------------------------------
    


# ========= MAIN PROGRAM =================

user_reply = get_yes_or_no()
print("You replied with ", user_reply)

married_single = get_status()
print("You replied with ", married_single)


start_date = get_valid_date("start")
print("Start Date : ", start_date)

leaving_date = get_valid_date("leaving")
print("Leaving Date : ", leaving_date)

