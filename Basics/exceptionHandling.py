
def getInfo():
    var1 = input("\nPlease provide the first number: ")
    var2 = input("\nPlease provide the second number: ")
    return var1, var2


def compute():
    invalidInput = True
    
    while invalidInput:
        var1,var2 = getInfo()
        
        try:
            var3 = int(var1) + int(var2)
            
            invalidInput = False
        # Shows this if the error is a ValueError
        except ValueError as e:
            print("{}:\n\nYou did not provide a numberic value!".format(e))
        # Shows this if the error is anything else
        except:
            print("\n\nWhatever you did, it didn't work...")

        # After the exceptions are caught, do this.
        # finally:
           #  print("Moving on...")
           
    print("{} + {} = {}".format(var1, var2, var3))



if __name__ == "__main__":
    compute()    
