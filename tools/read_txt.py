import yaml
import os
from config import BASE_URL


def read_txt(filename):
    with open(BASE_URL + os.sep + "data" + os.sep + filename, "r", encoding="utf-8")as f:
        arr = []
        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))
        return arr[1::]

#
# if __name__ == '__main__':
#     print(read_yaml("mp_login.txt"))
