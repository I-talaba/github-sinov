"""Son topish funksiyasi"""

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi? ")
    taxminlar = 0

    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))

        if taxmin < tasodifiy_son:
            print("Xato!Men o'ylagan son bundan kattaroq.Yana xarakat qiling: ")
        elif taxmin > tasodifiy_son:
            print("Xato!Men o'ylagan son bundan kichikroq.Yana xarakat qiling: ")
        else:
            print(f"Tabriklaymiz! Siz {taxminlar} ta taxmin bilan topdingiz.")
            break
    return taxminlar

# sontop()


def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman!\n>>> ")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
           taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz:to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+),yoki kichikroq (-)".lower())

        if javob == '-':
            yuqori = taxmin -1
        elif javob == '+':
            quyi = taxmin + 1

        else:
            print(f"Men {taxminlar} ta taxmin bilan topdim!")
            break

    return taxminlar

# sontop_pc()


def play(x=10):

    yana = True
    while yana:

        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men Men {taxminlar_user} ta taxmin bilan topdim va yuttim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_pc} ta taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ymaysizmi? Ha(1)ni bosing, Yo'q(0)ni bosing."))
play(50)