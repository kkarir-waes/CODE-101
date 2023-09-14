# OOP - paramter passing  #
#-------------------------#

# class method for accepting a user's menu selection
class Get_selection:
    ''' Get the user's menu selection '''
    
    def get_opt():
        menu_opt = input("Enter your choice : " )

        ''' you probably want to do some validation here '''

        # return the user's selection
        return menu_opt




# - Main processing ----------------------------- #

user_opt = Get_selection.get_opt()

print(user_opt)
