# coding=utf8
import sys

negative = [ "bad", "worse", "worst", "suck", "not", "hate" ]
positive = [ "good", "best", "cool", "fantasitc", "great", "like" , "awesome" ]


for line in sys.stdin:
  score = 0
  line = line.lower()
  for w in negative:
    if w in line:
      score = score-1
  for w in positive:
    if w in line:
      score = score+1

  if score > 0 :
    print("positive\t"+str(1))
  elif score < 0:
    print("negative\t"+str(1))
  else:
    print("neutral\t"+str(1))

