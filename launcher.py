from __future__ import print_function 
import pandas as pa
import numpy as nu
import datetime as dt

def readRelevantColumns():
    aux = open("assets/relevant_cols", "r").read().split("\n")[:-1]
    cols  = [int(y) for y in aux]
    return cols

def getRelevantData(namefile, cols):
    #Get the time and create
    now = dt.datetime.now()
    strnow = str(now.strftime("%Y-%m-%d"))
    nameExportFile = "clean_data_{}.{}".format(strnow,"csv")
    
    #Read the data
    data = pa.read_csv("data/"+namefile);
    
    #Filter the data
    #data = data[ data["session.code"] == codeSession ] 
    data = data.iloc[:,cols]


    data.to_csv(nameExportFile)

    print( "The file with name  = {} was created at {}".format(nameExportFile, strnow) )
    print( "This file contains the clean data")


if __name__  == "__main__":   
    namefile = "data.csv"
    cols =   readRelevantColumns()
    getRelevantData(namefile , cols)
    

    
