# get_name — функция. Принимает номер документа и выводит имя человека, которому он принадлежит. Если такого документа не существует вывести “Документ не найден”.
# get_directory — функция. Принимает номер документа и выводит номер полки, на которой он находится. Если такой документ не найден на полках вывести “Полки с таким документом не найдено”.
# add — функция, которая добавит новый документ в каталог и перечень полок.

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

def get_name(doc_number):
    # your code
  res1 = None
  
  for doc in documents:
    if doc_number in doc["number"]:
      res1 = doc["name"]
      
    # else:
    #   res1 = "Документ не найден"
  if res1 != None:
    return res1 
  else:
    return "Документ не найден"
    
def get_directory(doc_number):
    # your code
  res2 = None
  for key, value in directories.items():
    if doc_number in value:
      res2 = key
  if res2 != None:
    return res2
  else:
    return "Полки с таким документом не найдено"
  # return documents, directories 
def add(document_type, number, name, shelf_number):
    # your code
  
  dict_add = {}
  dict_add["type"] = document_type
  dict_add["number"] = number
  dict_add["name"] = name
  
  documents.append(dict_add)
  directories[str(shelf_number)] = number
  # for key in directories.keys():
  #   if key == shelf_number:
  #     directories[key] = number
      
  return number
  
if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))