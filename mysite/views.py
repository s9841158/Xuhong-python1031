from django.shortcuts import render
from django.http import HttpResponse
import random

def index(requst):
    especially_no = random.randint(1, 42)  ##第1個變數
    numbers = list() ##第二個變數
    for i in range(6):
        numbers.append(random.randint(1, 42))
    return render(requst,'index.html', locals()) ##locals區域 把上面的資料打包