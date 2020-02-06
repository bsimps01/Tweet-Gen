from random import randint
from histogram import histogram
#filename = open("/Users/benjamin5311/dev/MakeSchool/CS1-2/Tweet-Gen/EAP.text", "r")
#histogram = filename.readlines()

def sample_by_frequency(histogram):
  random_index = randint(0, sum(histogram.values()) - 1)
  start = 0 
  for word,count in histogram.items():
    end = start + count
    if random_index in range(start,end):
        return word
    else:
        start = end
        
#print(sample_by_frequency(histogram))