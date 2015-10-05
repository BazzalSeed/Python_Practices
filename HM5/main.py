#Main Driver


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
from RPNCalculator import*
from Stack import*
# the main function to activate the whole process            
def main():
    #while loop will go on forever
    n = 0
    while(n <=  10):
        try:
            #ask user to enter the sequence in the right format as described
            var = input('enter the thing you want to caculate'+':'+' ')
            if var == 'quit':
                return
            else:
                #call the evaluate method
                a= RPNCalculator()
                a = a.evaluate(var)
                print (a)
        #Catch the value Error
        except ValueError:
            print('INVALID')
        #Catch the Type Error
        #except TypeError:
            #print('give me a string')
        
#Call the Main function
if __name__ == '__main__':
    main()

        
