from __future__ import print_function 
import pandas as pa
import numpy as nu
import datetime as dt

def readRelevantColumns():
    aux = open("assets/relevant_cols", "r").read().split("\n")[:-1]
    cols  = [int(y) for y in aux]
    return cols

def getRelevantData(namefile, codeSession, cols):
    now = dt.datetime.now()
    strnow = str(now.strftime("%Y-%m-%d"))
    nameExportFile = "clean_data_{}.{}".format(strnow,"csv")
    
    data = pa.read_csv("data/"+namefile);
    data = data[ data["session.code"] == codeSession ] 
    data = data.iloc[:,cols]
    data.to_csv(nameExportFile)

    print( "The file with name  = {} was created at {}".format(nameExportFile, strnow) )
    print( "This file contains the clean data")


if __name__  == "__main__":   
    namefile = "data.csv"
    codeSession = "6h9k4r19"
    labelSession = "1803231630C0106"

    cols =   readRelevantColumns()
    getRelevantData(namefile, codeSession, cols)
    

    
