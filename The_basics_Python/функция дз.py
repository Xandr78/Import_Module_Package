documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def people():
 
  res1 = None
  while res1 == None:
    doc_number = input("Введите номер документа: ",)
    for doc in documents:
      if doc_number == doc["number"]:
        res1 = doc["name"]
        return res1

def shelf():
  res1 = None
  while res1 == None:
    doc_number = input("Введите номер документа: ",)
    for key, value in directories.items():
      if doc_number in value:
        res1 = key
        return res1

def list():
  for doc in documents:
    return f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"'

def add():
  doc_number = input("введите номер документа: ", )
  doc_type = input("введите тип документа: ", )
  doc_name = input("введите имя владельца: ", )
  doc_direct = input("введите номер полки: ", )
  while doc_direct not in directories:
    doc_direct = input("введите номер полки повторно: ", )
  directories[doc_direct] = doc_number
 
  dict_new = {}
  dict_new["type"] = doc_type
  dict_new["number"] = doc_number
  dict_new["name"] = doc_name
  documents.append(dict_new)
  
  return documents, directories
  
def delete():
  
  res1 = None
  while res1 == None:
    d = input("введите номер удаляемого документа: ", )
    for doc in documents:
      if d == doc["number"]:
        res1 = d
        break
    
  for i, j in enumerate(documents):
    if j["number"] == d:
      documents.pop(i)
  for key, value in directories.items():
    if d in value:
     value.remove(d)
  return documents, directories

def move():
  res1 = None
  while res1 == None:  
    doc_number = input("введите номер документа: ", )
    for key, value in directories.items():
      if doc_number in value:
        res1 = doc_number
  doc_direct = ''
  while doc_direct not in directories:
    doc_direct = input("введите номер полки повторно: ", )
  
  for key, value in directories.items():
    if doc_number in value:
      value.remove(doc_number)
  directories[doc_direct].append(res1) 
  return directories

def add_shelf():
  direct_new = input("введите номер новой полки: ", )
  while direct_new in directories:
    direct_new = input("введите номер новой полки: ", )
  
  directories.update({direct_new: []})
  # directories[direct_new] = []
  return directories
  
print(people())
print(shelf())
print(list())
print(add())
print(delete())
print(move())
print(add_shelf())