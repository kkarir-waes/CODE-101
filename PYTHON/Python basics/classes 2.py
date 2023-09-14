class Bird:
   """
   Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
  
   def bird_call(self):
       print(self.call.upper())



# creat Bird objects
owl = Bird('Owl', 'Twit Twoo!')
print(owl.call)
print(owl.description())


crow = Bird('Crow', 'Caaaw!')
print(crow.description())

# change the call attribute
owl.call = 'screech'
print(owl.description())

# delete owl's call attribute
del owl.call

print(crow.description())   # this is ok, Note () after description
print(owl.description())    # run time error as 'call' deleted

#-----------------------------------
#-
#-----------------------------------
class User():
    """
    Creates an instance of User
    """
    def __init__(self, username, email, subscribed):
        self.username = username
        self.email = email
        self.subscribed = subscribed
    
    def description(self):
        """
        Describes the instance of User
        """
        return f"user: {self.username}, email: {self.email}, subscribed: {self.subscribed}"


# 
user_one = User("arnold", "arnold@email.com", True)

print(user_one.email)
user_one.email = "murphy@email.com"
print(user_one.description())   # note ()



