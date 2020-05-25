import pickle

f = open("game.pkl", 'rb')


print(pickle.load(f))   # first in first out  FIFO 先进先出
print(pickle.load(f))

