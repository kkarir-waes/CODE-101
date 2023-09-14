class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call}" 
       
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())      # prints the Owl description
print(owl.definition)         # prints the Class Atrribute 'definition'
print(owl.call)
print(Bird.definition)      # this is ok cos Bird has a definition
print(Bird.call)            # this is error cos Bird doesnt have an instance


#-------------------------------------
#
#-------------------------------------

class ContactInfo:
    """ Creates an instance of ContactInfo """
    about = "Contact information for customer"

    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def description(self):
        return f'{self.name}: {self.email}'


print(ContactInfo.about)
contact = ContactInfo("dave", "lister@email.com" )
print(contact.description())


