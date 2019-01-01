import dataStorage

options = ('add', 'update', 'delete', 'get', 'rename', 'delete all', 'get all', 'help', 'quit')

user_input = ' '



def getOption():
  while(True):
    user_input = input('What would you like to do? ')
    user_input = ' '.join(user_input.split() ).strip().lower()

    if user_input not in options:
      print(user_input, 'not found.')
    else:
      return user_input

def doAdd():
  user_input = input('Enter the item name and data seperated by a comma, or "back" to go back:')
  if(',' in user_input):
    item_name = user_input.split(',')[0]
    item_data = ','.join(user_input.split(',')[1:])
    dataStorage.addItem(item_name, item_data)
    print('Added item', item_name, 'with value', item_data)
  else:
    handleBack(user_input, doAdd)

def doUpdate():
  user_input = input('Enter the item name and data seperated by a comma, or "back" to go back:')
  if(',' in user_input):
    item_name = user_input.split(',')[0]
    item_data = ','.join(user_input.split(',')[1:])
    dataStorage.updateItem(item_name, item_data)
    print('Updated item', item_name, 'with value', item_data)
  else:
    handleBack(user_input, doUpdate)

def doDelete():
  user_input = input('Enter the name of the item to delete, or "back" to go back:')
  if(len(user_input)>0):
    item_name = user_input
    dataStorage.deleteItem(item_name)
    print('Deleted item', item_name)
  else:
    handleBack(user_input, doDelete)

def doGet():
  user_input = input('Enter the name of the item you\'d like to get, or "back" to go back:')
  if(len(user_input)>0):
    item_name = user_input
    item_data = dataStorage.getItem(item_name)
    print('Got data for item', item_name, '\n ', item_data)
  else:
    handleBack(user_input, doGet)

def doDeleteAll():
  user_input = input('Are you sure? Enter "y" to confirm, or "back" to go back:')
  if(user_input=='y'):
    dataStorage.deleteAll()
    print('Deleted all items')
  else:
    handleBack(user_input, doDeleteAll)

def doGetAll():
  data = dataStorage.getAll()
  for item in data:
    if(data[item]!=''):
      print(item, ':', data[item])

def doRename():
  user_input = input('Enter the old item name and new item name seperated by a comma, or "back" to go back:')
  if(',' in user_input):
    old_item_name = user_input.split(',')[0]
    new_item_name = user_input.split(',')[1]
      
    dataStorage.renameItem(old_item_name, new_item_name)
    print('Renamed item', old_item_name, 'to', new_item_name)
  else:
    handleBack(user_input, doRename)

def handleBack(user_input, callback):
  user_input = ' '.join(user_input.split() ).strip().lower()
  if(user_input=='back'):
    handleInput(False)
  else:
    print('Invalid input.')
    callback()

def showHelp():
  print('Valid options are:',', '.join(options) )

def handleInput(ask):

  user_input = getOption()

  if(user_input=='add'):
    doAdd()
  elif(user_input=='update'):
    doUpdate()
  elif(user_input=='delete'):
    doDelete()
  elif(user_input=='get'):
    doGet()
  elif(user_input=='rename'):
    doRename()
  elif(user_input=='delete all'):
    doDeleteAll()
  elif(user_input=='get all'):
    doGetAll()
  elif(user_input=='help'):
    showHelp()
  elif(user_input=='quit'):
    return

  if(ask):
    yes_no = input('Anything else you\'d like to do? (y/n) ')
    yes_no = yes_no.replace(' ','').lower()
    if(yes_no=='yes' or yes_no=='y'):
      handleInput(True)
  

showHelp()
handleInput(True)

