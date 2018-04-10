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
  categories = set()
  subcategories = {}
  
  for header in headers:
      print(header)
      aux = header.split(".")
      if (len(aux) > 1):
          categories.add(aux[0])
          if aux[0] in subcategories:
            subcategories[aux[0]].append(header[len(aux[0]):]) 
          else:
            subcategories[aux[0]] = []

  return categories, subcategories


def getLabels(data):
  ulabels = set()
  session_labels = data["session.label"].tolist()
  for label in session_labels:
    if str(label) != "nan":
      ulabels.add(label)
  return ulabels

def getRelevantData(path, cols):
  #Read the data
  data = pa.read_csv(path)
  print(getLabels(data))
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
    

    
