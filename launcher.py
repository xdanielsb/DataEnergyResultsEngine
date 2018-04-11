import pandas as pa
import numpy as nu
import datetime as dt

#Execute with python3

MONTHS =  {1: "January", 
           2: "February", 
           3: "March", 
           4: "April", 
           5: "May" , 
           6: "June",
           7: "July",
           8: "August",
           9: "September",
           10: "October", 
           11: "November", 
           12: "December"}

TYPES = {"D": "Descriptive (D)",
         "C": "Control (C)", 
         "DTI": "Descriptive Tailored Injuctive (DTI) "}

def readRelevantColumns():
  aux = open("./assets/relevant_cols", "r").read().split("\n")[:-1]
  cols  = [int(y) for y in aux]
  return cols

COLS =   readRelevantColumns()

def getHeadersDataFrame(df):
  headers = list(df)
  categories = set()
  subcategories = {}
  
  for header in headers:
      aux = header.split(".")
      if (len(aux) > 1):
          categories.add(aux[0])
          if aux[0] in subcategories:
            subcategories[aux[0]].append(header[len(aux[0]):]) 
          else:
            subcategories[aux[0]] = []

  return categories, subcategories


def labelParser(label):
  reallabel = label
  year, month, day = label[:2], label[2:4], label[4:6]
  hour, minu = label[6:8], label[8:10]
  ttype = label[10:11]
  if ttype == "D" and label[11] == "T":
      ttype = "DTI"
      label = label[2:]
  idx =  label[11:13]
  num_participants = label[13:16]
  month = MONTHS[int(month)]  
  ttype = TYPES[ttype]
  date = "20{}-{}-{} at {}:{} ".format(year, month, day, hour, minu)
  return [date, ttype, num_participants, idx, reallabel]

def getLabels(data):
  ulabels = set()
  flabels = []
  session_labels = data["session.label"].tolist()
  for label in session_labels:
    if str(label) != "nan":
      ulabels.add(label)
  for label in ulabels:
      flabels.append(labelParser(label))
  return flabels

def getSpecificData(path, labelid):
  data = pa.read_csv(path)
  data = data[ data["session.label"] == labelid ]
  data = data.iloc[:,COLS]
  headers = list(data)
  values = data.values.tolist()
  return headers, values

def getRelevantData(path):
  #Read the data
  data = pa.read_csv(path)
  flabels = getLabels(data)
  #Get the time and create
  now = dt.datetime.now()
  strnow = str(now.strftime("%Y-%m-%d"))
  nameExportFile = "./clean/clean_data_{}.{}".format(strnow,"csv")
  
  #Filter the data
  
  #data = data[ data["session.code"] == codeSession ] 
  data = data.iloc[:,COLS]

  data.to_csv(nameExportFile)

  print( "The file with name  = {} was created at {}".format(nameExportFile, strnow) )
  print( "This file contains the clean data")


def getSessionInfo(path, labelid):
  data = pa.read_csv(path)
  data = data[ data["session.label"] == labelid ] 
  _, subcategories = getHeadersDataFrame(data)
  aim = "session"
  headers_session = []
  values_session = []
  for sub in subcategories[aim]:
    headers_session.append(sub[1:].split(".")[-1])
    values_session.append(data[aim+sub].iloc[0] )  
  return headers_session, values_session

if __name__  == "__main__":   
    path = "data/data.csv"
    labelid = "1803291630D0106"
    h, v  = getSessionInfo(path, labelid)
    print(h)
    print(v)
    
    

