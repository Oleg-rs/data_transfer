from random import randint


def generator():
    itog = []
    bbbb = randint(1, 9999)
    if bbbb < 10:
        bbbb = "000" + str(bbbb)
    elif bbbb < 100:
        bbbb = "00" + str(bbbb)
    elif bbbb < 1000:
        bbbb = "0" + str(bbbb)
    else:
        bbbb = str(bbbb)
    itog.append(bbbb)
    id = randint(1, 99)
    if id < 10:
        id = "0" + str(id)
    else:
        id = str(id)
    itog.append(id)

    score = []

    hh = randint(0, 24)
    if hh == 0:
        hh = "00"
    elif hh < 10:
        hh = "0" + str(hh)
    else:
        hh = str(hh)
    score.append(hh)

    mm = randint(0, 60)
    if mm == 0:
        mm = "00"
    elif mm < 10:
        mm = "0" + str(mm)
    else:
        mm = str(mm)
    score.append(mm)

    ss = randint(0, 60)
    if ss == 0:
        ss = "00"
    elif ss < 10:
        ss = "0" + str(ss)
    else:
        ss = str(ss)
    score.append(ss)
    my_time = ":".join(score)
    score_2 = []
    score_2.append(my_time)

    zhq = randint(0, 999)
    if zhq == 0:
        zhq = "000"
    if int(zhq) < int(10):
        zhq = "00" + str(zhq)
    elif zhq < 100:
        zhq = "0" + str(zhq)
    else:
        zhq = str(zhq)
    score_2.append(zhq)
    vr = ".".join(score_2)
    itog.append(vr)

    numm = randint(0, 99)
    if numm == 0:
        numm = "00"
    elif numm < 10:
        numm = "0" + str(numm)
    else:
        numm = str(numm)
    itog.append(numm)
    # fin = str(*itog)
    fin = " ".join(itog)

    return fin


def chek(arg):
    a = arg.split()
    if int(a[3]) != 0:
        return False
    else:
        stroka = f"\rспортсмен, нагрудный номер {a[0]} прошёл отсечку {a[1]} в {a[2]}"
        return stroka



# BBBBxNNxHH: MM:SS.zhqxGGCR
# Где
# BBBB - номер участника
# x - пробельный символ
# NN - id канала
# HH - Часы
# MM - минуты
# SS - секунды
# zhq - десятые сотые тысячные
# GG - номер группы
# CR - «возврат каретки»

# 0002 C1 01: 13:02.877 00[CR]
