"""
 Example:

"""

""" Import common python packages """
import sys
import os
import numpy as np      # Mathematical package
import pandas as pd     # Time serie package
import matplotlib.pyplot as plt # Plotting package
sys.path.insert(0, '../src/')   # To be able to import packages from parent directory 
sys.path.insert(0, '../src/Methods')

print ("\n")
print("******************************************************************************************")
print("This script computes...")
print("******************************************************************************************")

""" Import wanted module with every parent packages """


""" Import Utils modules """



""" Define input signals in pd.dataFrame format """



"""OR"""
""" Import signals from a .csv file """



""" Define class attributes of the wanted method """


""" Instanciate the class with its attributes """
print("\n")

try : 
    c=
except TypeError, err :
    print("TypeError in constructor : \n" + str(err))
    sys.exit(-1)
except ValueError, err :
    print("ValueError in constructor : \n" + str(err))
    sys.exit(-1)
except Exception, e :
    print("Exception in constructor : \n" + str(e))
    sys.exit(-1)

print("An instance the class is now created with the following parameters:\n" +
      
	  )


""" Compute the method and get the result """
print("\n")
print("Computing...")

try : 
    res= c.compute([x, y])
except TypeError, err :
    print("TypeError in computation : \n" + str(err))
    sys.exit(-1)
except ValueError, err :
    print("ValueError in computation : \n" + str(err))
    sys.exit(-1)
except Exception, e :
    print("Exception in computation : \n" + str(e))
    sys.exit(-1)

""" Display result """
print("\n")
print("**************************************** \n")
print('Complete result :')
print("****************************************\n")




raw_input("Push ENTER key to exit.")

