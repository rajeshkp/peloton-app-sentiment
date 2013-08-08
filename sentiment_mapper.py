# coding=utf8
import sys

negative = [ "bad", "worse", "worst", "suck", "not", "hate" ]
positive = [ "good", "best", "cool", "fantasitc", "great", "like" , "awesome" ]


for mline in sys.stdin:
  score = 0
  line = mline.split("\t")[0].lower()
  for w in negative:
    if w in line:
      score = score-1
  for w in positive:
    if w in line:
      score = score+1

  if score > 0 :
    print("positive\t"+str(score)+"\t"+mline.rstrip('\n'))
  elif score < 0:
    print("negative\t"+str(score)+"\t"+mline.rstrip('\n'))
  else:
    print("neutral\t"+str(score)+"\t"+mline.rstrip('\n'))

