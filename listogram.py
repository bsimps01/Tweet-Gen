from histogram import histogram

def get_index(word, listogram):
  index = 0
  for inner_list in listogram:
    if inner_list[0] == word:
      return index
    else:
      index += 1
    
  return "nope didn't find it"
  
def listogram(lines):
    listogram = []
    
    for word in lines:
      word = word.rstrip()
      result = get_index(word, listogram) 
      if result == "nope didn't find it": # first time seeing the word
        listogram.append([word, 1])
      else:
        listogram[result][1] += 1
    return listogram
    
    
lines = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/Tweet-Gen/EAP.text", "r").readlines()
print(listogram(lines))