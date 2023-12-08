import sys
sys.path.append('C:/Users/ftstc/Desktop/information_processing_retrieval//w12/sub_dir')


import calculation as cal          #Importing calculation module
# from calculation import *
print(cal.add(1,2))
print(dir(cal)) #used to find out which names a module defines. It returns a sorted list of strings

print(dir()) #Without arguments, dir() lists the names you have defined currently