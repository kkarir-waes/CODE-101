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
        parrot = "Norwegian Blue"       # <-- new, class attribute
        return f"A {self.kind} goes {self.call} and is {self.definition} It is not a {parrot}" 
       

owl = Bird('owl', 'Twit Twoo!')
print(owl.description())

#--------------------------------------------------
# 
#--------------------------------------------------


class   BlogPost:
    """ Creates an instance of BlogPost """
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def get_overview(self):
        return f"{self.title} by {self.author}"
        
    def full_info(self):
        return f"Blog post: {self.title}. Content: {self.content}. Author: {self.author}"
    
post = BlogPost("Python Classes", "Python is known as an object-oriented language...", "Code Institute")

print(post.get_overview())  # short version of info
print(post.full_info())     # long version of info
