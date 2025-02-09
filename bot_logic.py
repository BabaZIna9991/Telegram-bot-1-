import random

def gen_pass():
    simvoli = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    dlina = 10
    parol = ""
    for i in range(dlina):
        j = random.choice(simvoli)
        parol += j 
    return parol
