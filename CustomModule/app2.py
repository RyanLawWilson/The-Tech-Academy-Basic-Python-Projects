import app

def print_app2():
    # Parenthese aroun __name__ seem optional
    name = (__name__)
    return name

# The file that is initially run is called __main__
if __name__ == "__main__":
    # The following is calling code from within this script
    print("I am running code from {}".format(print_app2()))
    
    # When calling another function that uses dunder function
    # __name__, __name__ will be the name of the file itself
    print("I am running code from {}".format(app.print_app()))
