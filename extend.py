# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv

import sys,random
from ezr import the, DATA, csv, dot, NUM, SYM

def show(lst):
  return print(*[f"{word:6}" for word in lst], sep="\t")

def myfun(train):
  d    = DATA().adds(csv(train))
  x    = len(d.cols.x)
  nums = sum(isinstance(col, NUM) for col in d.cols.all)
  syms = sum(isinstance(col, SYM) for col in d.cols.all)
  size = len(d.rows)
  dim  = "small" if x <= 5 else ("med" if x < 12 else "hi")
  size = "small" if size< 500 else ("med" if size<5000 else "hi")
  return [dim, size, x,len(d.cols.y), nums, syms, len(d.rows), train[17:]]

random.seed(the.seed) #  not needed here, but good practice to always take care of seeds
show(["dim", "size","xcols","ycols","num","sym","rows","file"])
show(["------"] * 8)
[show(myfun(arg)) for arg in sys.argv if arg[-4:] == ".csv"]
