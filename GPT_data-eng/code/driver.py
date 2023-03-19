import numpy as np
import pandas as pd
import json
import re

f = open('train_data.json', encoding='utf-8')
data = json.load(f)
length = len(data)
print(length)
print(data[111])

file = open("data2.txt", "a", encoding="utf-8")
for val in data:
    file.write(val[1]+'\n')
file.close()


