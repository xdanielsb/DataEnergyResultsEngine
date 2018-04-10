import pandas as pa
import numpy as nu
import datetime as dt

#Execute with python3

def readRelevantColumns():
  aux = open("./assets/relevant_cols", "r").read().split("\n")[:-1]
  cols  = [int(y) for y in aux]
  return cols

def getHeadersDataFrame(df):
  headers = list(df)
  columns = set()
  for header in headers:
      aux = header.split(".")
      if (len(aux) > 0):
          columns.add(aux[0])

  return columns

def getRelevantData(path, cols):
  #Read the data
  data = pa.read_csv(path)
  print(getHeadersDataFrame(data))
    
  #Get the time and create
  now = dt.datetime.now()
  strnow = str(now.strftime("%Y-%m-%d"))
  nameExportFile = "./clean/clean_data_{}.{}".format(strnow,"csv")
  
  #Filter the data
  #data = data[ data["session.code"] == codeSession ] 
  data = data.iloc[:,cols]

  data.to_csv(nameExportFile)

  print( "The file with name  = {} was created at {}".format(nameExportFile, strnow) )
  print( "This file contains the clean data")


if __name__  == "__main__":   
    path = "data/data.csv"
    cols =   readRelevantColumns()
    getRelevantData(path , cols)
    

    
