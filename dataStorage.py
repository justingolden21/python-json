import json

# a simple json manager in python 3
# requires a data.json file with at least "{}"

# adds or modifies the item's data
# newitem is created if necessary
def addItem(itemName, itemData):
  with open("data.json", "r+") as datafile:
    data = json.load(datafile)

    data[itemName] = itemData

    datafile.seek(0)
    json.dump(data, datafile)
    datafile.truncate()

def updateItem(itemName, itemData):
  addItem(itemName, itemData)

# replaces item's data with empty string
def deleteItem(itemName):
  addItem(itemName, '')

# given an array of strings of names of items to delete
def deleteMany(itemNames):
  for itemName in itemNames:
    deleteItem(itemName)

# returns string or empty string
def getItem(itemName):
  with open("data.json", "r") as datafile:
    data = json.load(datafile)
    try:
      return data[itemName]
    except:
      return ''

# makes new item with old item's data
# old item's data is empty string
def renameItem(oldItemName, newItemName):
  addItem(newItemName, getItem(oldItemName) )
  deleteItem(oldItemName)

# clears all data
def deleteAll():
  with open("data.json", "r+") as datafile:
    data = json.load(datafile)

    data = {}

    datafile.seek(0)
    json.dump(data, datafile)
    datafile.truncate()

# returns dict
def getAll():
  with open("data.json", "r") as datafile:
    return json.load(datafile)
  
