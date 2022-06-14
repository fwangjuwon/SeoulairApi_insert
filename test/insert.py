from dao import insert_all
from download import *

list = info(count())

for row in list:
    insert_all(**row)
