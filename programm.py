#Программа для расчета ЖБ конструкций
#Версия 0.000

from tkinter import *
from tkinter.ttk import *
from math import *

root = Tk()
root.title('РАСЧЁТ ЖБ БАЛКИ')
root.geometry('585x450')



lab6 = Label(text = 'Схема работы:')
lab6.place(x = 0, y = 0)
lab1 = Label(text = 'Класс бетона:')
lab1.place(x = 0, y = 25)
lab2 = Label(text = 'Класс арматуры:')
lab2.place(x = 0, y = 50)
lab3 = Label(text = 'Длинна балки, m:')
lab3.place(x = 0, y = 75)
lab4 = Label(text = 'Нагрузка, kH/m:')
lab4.place(x = 0, y = 100)
lab5 = Label(text = 'Момент пролёт:')
lab5.place(x = 0, y = 175)
lab7 = Label(text = 'Момент опора:')
lab7.place(x = 0, y = 150)
lab8 = Label(text = 'Ширина балки, m:')
lab8.place(x = 200, y = 75)
lab9 = Label(text = 'Высота балки, m:')
lab9.place(x = 200, y = 100)
lab10 = Label(text = 'Защитный слой, m:')
lab10.place(x = 270, y = 0)
lab11 = Label(text = 'A0pr:')
lab11.place(x = 270, y = 175)
lab12 = Label(text = 'A0op:')
lab12.place(x = 270, y = 150)
lab13 = Label(text = 'D Верх. арм., mm:')
lab13.place(x = 10, y = 225)
lab14 = Label(text = 'D Нижн. арм., mm:')
lab14.place(x = 10, y = 275)
lab15 = Label(text = 'As tr op:')
lab15.place(x = 255, y = 225)
lab16 = Label(text = 'As op:')
lab16.place(x = 410, y = 225)
lab17 = Label(text = 'Шт:')
lab17.place(x = 350, y = 250)
lab18 = Label(text = 'Шт:')
lab18.place(x = 350, y = 300)
lab19 = Label(text = 'As tr pr:')
lab19.place(x = 255, y = 275)
lab20 = Label(text = 'As pr:')
lab20.place(x = 410, y = 275)
lab21 = Label(font='Arial 15', text = '+')
lab21.place(x = 420, y = 245)
lab22 = Label(font='Arial 15', text = '+')
lab22.place(x = 420, y = 295)
lab23 = Label(text = ' -' * 71)
lab23.place(x = 0, y = 200)
lab24 = Label(font='Arial 15', text = 'ПРОГИБ, m:')
lab24.place(x = 10, y = 335)
lab25 = Label(text = 'расчетный -')
lab25.place(x = 250, y = 360)
lab26 = Label(text = 'нормативный -')
lab26.place(x = 90, y = 360)
lab27 = Label(text = '% -')
lab27.place(x = 508, y = 250)
lab28 = Label(text = '% -')
lab28.place(x = 508, y = 300)
lab29 = Label(text = ' -' * 71)
lab29.place(x = 0, y = 125)



def getRb(root):
    a = beton.get()
    global Rb, Rbser, Eb
    if a == 'B10':
        Rb = 5600
        Rbser = 5600
        Eb = 18000000
    elif a == 'B15':
        Rb = 8500
        Rbser = 8500
        Eb = 23000000
    elif a == 'B20':
        Rb = 11500
        Rbser = 11500
        Eb = 27000000
    elif a == 'B25':
        Rb = 14500
        Rbser = 14500
        Eb = 30000000
    elif a == 'B30':
        Rb = 17000
        Rbser = 17000
        Eb = 32500000
    elif a == 'B35':
        Rb = 19500
        Rbser = 19500
        Eb = 34500000
    elif a == 'B40':
        Rb = 22000
        Rbser = 22000
        Eb = 36000000
    elif a == 'B45':
        Rb = 25000
        Rbser = 25000
        Eb = 37500000
    elif a == 'B50':
        Rb = 27500
        Rbser = 27500
        Eb = 39000000
    elif a == 'B55':
        Rb = 30000
        Rbser = 30000
        Eb = 39500000
    elif a == 'B60':
        Rb = 33000
        Rbser = 33000
        Eb = 40000000

beton = Combobox(width = 5, values = [u'B10',
                                u'B15',
                                u'B20',
                                u'B25',
                                u'B30',
                                u'B35',
                                u'B40',
                                u'B45',
                                u'B50',
                                u'B55',
                                u'B60'])
beton.set(u'B30')
beton.place(x = 110, y = 25)





def getKm(root):
    a = shema.get()
    global Kpr, Kop
    if a == 'Заделка-Заделка':
        Kpr = 24
        Kop = 12
    elif a == 'Заделка-Шарнир':
        Kpr = 16
        Kop = 8
    elif a == 'Шарнир-Шарнир':
        Kpr = 8
        Kop = 0
    elif a == 'Консоль':
        Kpr = 0
        Kop = 2

shema = Combobox(width = 18, values = ['Заделка-Заделка',
                                'Заделка-Шарнир',
                                'Шарнир-Шарнир',
                                'Консоль'])
shema.set('Заделка-Шарнир')
shema.place(x = 110, y = 0)





def getRs(root):
    a = arm.get()
    global Rs, Es
    Es = 200000000
    if a == 'A240 (A-I)':
        Rs = 215000
    elif a == 'A300 (A-II)':
        Rs = 270000
    elif a == 'A400 (A-III, A400C)':
        Rs = 355000
    elif a == 'A500 (A500C)':
        Rs = 435000
    elif a == 'B500 (Bp-I, B500C)':
        Rs = 415000
       
arm = Combobox(width = 18, values = ['A240 (A-I)',
                                           'A300 (A-II)',
                                           'A400 (A-III, A400C)',
                                           'A500 (A500C)',
                                           'B500 (Bp-I, B500C)'])
arm.set('A400 (A-III, A400C)')
arm.place(x = 110, y = 50)







Varm = Combobox(width = 2, values = ['6',
                              '8',
                              '12',
                              '16',
                              '22'])
Varm.set('16')
Varm.place(x = 130, y = 225)

def getVarm(root):
    a = Varm.get()
    global VarmS
    if a == '6':
        VarmS = (6**2 * 3.14)/400
    elif a == '8':
        VarmS = (8**2 * 3.14)/400
    elif a == '12':
        VarmS = (12**2 * 3.14)/400
    elif a == '16':
        VarmS = (16**2 * 3.14)/400
    elif a == '22':
        VarmS = (22**2 * 3.14)/400





Narm = Combobox(width = 2, values = ['6',
                              '8',
                              '12',
                              '16',
                              '22'])
Narm.set('12')
Narm.place(x = 130, y = 275)

def getNarm(root):
    a = Narm.get()
    global NarmS
    if a == '6':
        NarmS = (6**2 * 3.14)/400
    elif a == '8':
        NarmS = (8**2 * 3.14)/400
    elif a == '12':
        NarmS = (12**2 * 3.14)/400
    elif a == '16':
        NarmS = (16**2 * 3.14)/400
    elif a == '22':
        NarmS = (22**2 * 3.14)/400





def getD(root):
    global AsD, MD, Lf, F, f
    if AsN == 0:
        AsD = AsV
    else:
        AsD = AsN
    if Mpr == 0:
        MD = Mop
    else:
        MD = Mpr
    Ebred = Rb / 0.0028
    As1 = Es / Ebred
    Ms = AsD / 10000 / B / h0
    Xm = h0 * (sqrt((Ms**2 * As1**2) + (2 * Ms * As1)) - Ms * As1)
    Z = h0 - 1 / 3 * Xm
    Dsp = Es * AsD / 10000 * Z * (h0 - Xm)

    A0H = MD / B / h0**2 / Rbser
    Ma = AsD / 10000 / B / h0 * Es / Eb
    EE = 1 / (1.8 + (1 + 5 * A0H) / 10 / Ma)
    z = h0 * (1 - EE / 2)
    Dsnip = h0 * z / (1 * 10000 / Es / AsD + 0.9 / EE / B / h0 / Eb / 0.15)
    
    DD = (Dsp + Dsnip) / 2

    A1 = shema.get()
    if A1 == 'Заделка-Заделка':
        f = q * L**4 / 384 / DD
        Lf = 200
    elif A1 == 'Заделка-Шарнир':
        f = q * L**4 / 185 / DD
        Lf = 200
    elif A1 == 'Шарнир-Шарнир':
        f = 5 * q * L**4 / 384 / DD
        Lf = 200
    elif A1 == 'Консоль':
        f = q * L**4 / 8 / DD
        Lf = 150

    F = L / Lf
    text20.delete(1.0, END)
    text20.insert(1.0, F)
    text21.delete(1.0, END)
    text21.insert(1.0, f)
    
    logfile(root)
    


def ArmProc(root):
    ArmProcV = AsV / ((AA / 2 * B * 10000) / 100)
    ArmProcN = AsN / ((AA / 2 * B * 10000) / 100)
    text22.delete(1.0, END)
    text22.insert(1.0, ArmProcV)
    text23.delete(1.0, END)
    text23.insert(1.0, ArmProcN)


def getAs(root):
    global AsV, AsN, SHTUKop, SHTUKpr
    a = int(text18.get(1.0, END))
    SHTUKop = ceil(AstrV / VarmS) + a
    text16.delete(1.0, END)
    text16.insert(1.0, SHTUKop - a)

    AsV = SHTUKop * VarmS
    text14.delete(1.0, END)
    text14.insert(1.0, AsV)

    
    b = int(text19.get(1.0, END))
    SHTUKpr = ceil(AstrN / NarmS) + b
    text17.delete(1.0, END)
    text17.insert(1.0, SHTUKpr - b)

    AsN = SHTUKpr * NarmS
    text15.delete(1.0, END)
    text15.insert(1.0, AsN)

    getD(root)

    ArmProc(root)




def getAstr(root):
    global AstrV, AstrN
    
    if nop == 0:
        AstrV = 0
        text12.delete(1.0, END)
        text12.insert(1.0, AstrV)
    else:
        AstrV = (Mop * 10000) / (Rs * nop * h0)
        text12.delete(1.0, END)
        text12.insert(1.0, AstrV)

    if npr == 0:
        AstrN = 0
        text13.delete(1.0, END)
        text13.insert(1.0, AstrN)
    else:
        AstrN = (Mpr * 10000) / (Rs * npr * h0)
        text13.delete(1.0, END)
        text13.insert(1.0, AstrN)
    getAs(root)




def getA0(root):
    global h0, B, AA, c
    B = float(text5.get(1.0, END))
    AA = float(text6.get(1.0, END))
    c = float(text7.get(1.0, END))
    h0 = AA - c
    global A0pr, A0op
    A0pr = Mpr / (Rb * B * (h0**2))
    A0op = Mop / (Rb * B * (h0**2))
    text8.delete(1.0, END)
    text8.insert(1.0, round(A0pr, 5))
    text9.delete(1.0, END)
    text9.insert(1.0, round(A0op, 5))
    getNu(root)





def getNu(root):
#    0.5 * Epr**2 - Epr + A0pr = 0    ----   квадратное уравнение
    global npr, nop
    if A0pr < 0.01:
        npr = 0
    elif A0pr > 0.455:
        npr = 0
    else:        
        Epr = (1 - sqrt(1 - (4 * 0.5 * A0pr))) / (2 * 0.5)
        npr = 1 - 0.5 * Epr
    text10.delete(1.0, END)
    text10.insert(1.0, npr)

    if A0op < 0.01:
        nop = 0
    elif A0op > 0.455:
        nop = 0
    else:  
        Eop = (1 - sqrt(1 - (4 * 0.5 * A0op))) / (2 * 0.5)
        nop = 1 - 0.5 * Eop
    text11.delete(1.0, END)
    text11.insert(1.0, nop)
    getAstr(root)





def START(root):
    getKm(root)
    getRb(root)
    getRs(root)
    getVarm(root)
    getNarm(root)
    global L, q
    L = float(text1.get(1.0, END))
    q = float(text2.get(1.0, END))
    global Mpr
    if Kpr > 0:
        Mpr = (q * L**2) / Kpr
        text3.delete(1.0, END)
        text3.insert(1.0, round(Mpr, 2))
    elif Kpr == 0:
        Mpr = 0
        text3.delete(1.0, END)
        text3.insert(1.0, Mpr)
    if Kop > 0:
        global Mop
        Mop = (q * L**2) / Kop
        text4.delete(1.0, END)
        text4.insert(1.0, round(Mop, 2))
    elif Kop == 0:
        Mop = 0
        text4.delete(1.0, END)
        text4.insert(1.0, Mop)
    getA0(root)





button1 = Button(text="Ресчёт")
button1.place(x = 250, y = 400)
button1.bind("<Button-1>", START)






text1 = Text(height=1,
             width=10,
             font='Arial 10')
text1.insert(1.0, 4)
text1.place(x = 110, y = 75)

text2 = Text(height=1,
             width=10,
             font='Arial 10')
text2.insert(1.0, 125)
text2.place(x = 110, y = 100)

text3 = Text(height=1,
             width=10,
             font='Arial 10')
text3.insert(1.0, 'kH*m')
text3.place(x = 110, y = 175)

text4 = Text(height=1,
             width=10,
             font='Arial 10')
text4.insert(1.0, 'kH*m')
text4.place(x = 110, y = 150)

text5 = Text(height=1,
             width=10,
             font='Arial 10')
text5.insert(1.0, 1)
text5.place(x = 310, y = 75)

text6 = Text(height=1,
             width=10,
             font='Arial 10')
text6.insert(1.0, 0.3)
text6.place(x = 310, y = 100)

text7 = Text(height=1,
             width=5,
             font='Arial 10')
text7.insert(1.0, 0.03)
text7.place(x = 390, y = 0)

text8 = Text(height=1,
             width=10,
             font='Arial 10')
text8.insert(1.0, 'A0 pr')
text8.place(x = 310, y = 175)

text9 = Text(height=1,
             width=10,
             font='Arial 10')
text9.insert(1.0, 'A0 op')
text9.place(x = 310, y = 150)

text10 = Text(height=1,
             width=10,
             font='Arial 10')
text10.insert(1.0, 'n pr')
text10.place(x = 390, y = 175)

text11 = Text(height=1,
             width=10,
             font='Arial 10')
text11.insert(1.0, 'n op')
text11.place(x = 390, y = 150)

text12 = Text(height=1,
             width=10,
             font='Arial 10')
text12.insert(1.0, 'Верх расч.')
text12.place(x = 310, y = 225)

text13 = Text(height=1,
             width=10,
             font='Arial 10')
text13.insert(1.0, 'Низ треб.')
text13.place(x = 310, y = 275)

text14 = Text(height=1,
             width=10,
             font='Arial 10')
text14.insert(1.0, 'Верх факт.')
text14.place(x = 450, y = 225)

text15 = Text(height=1,
             width=10,
             font='Arial 10')
text15.insert(1.0, 'Низ факт.')
text15.place(x = 450, y = 275)

text16 = Text(height=1,
             width=3,
             font='Arial 12')
text16.insert(1.0, 0)
text16.place(x = 374, y = 248)

text17 = Text(height=1,
             width=3,
             font='Arial 12')
text17.insert(1.0, 0)
text17.place(x = 374, y = 298)

text18 = Text(height=1,
             width=3,
             font='Arial 10')
text18.insert(1.0, 0)
text18.place(x = 450, y = 250)

text19 = Text(height=1,
             width=3,
             font='Arial 10')
text19.insert(1.0, 0)
text19.place(x = 450, y = 300)

text20 = Text(height=1,
             width=5,
             font='Arial 14')
text20.place(x = 180, y = 350)

text21 = Text(height=1,
             width=5,
             font='Arial 14')
text21.place(x = 323, y = 350)

text22 = Text(height=1,
             width=5,
             font='Arial 10')
text22.place(x = 530, y = 250)

text23 = Text(height=1,
             width=5,
             font='Arial 10')
text23.place(x = 530, y = 300)



import datetime
def logfile(root):
    CT = datetime.datetime.now()
    loging=open('log.txt', 'a')
    loging.write('\n'+'-'*40+'\n'+
                 'Запись от: '+str(CT)+'\n'+
                 '  Данные расчёта:\n'+
                 str(shema.get())+'\n'+
                 'Класс бетона: '+str(beton.get())+'\n'+
                 'Класс арматуры: '+str(arm.get())+'\n'+
                 'L = '+str(L)+'\n'+
                 'q = '+str(q)+'\n'+
                 'b = '+str(B)+'\n'+
                 'h0 = '+str(h0)+'\n'+
                 'Верх. арм. D'+str(Varm.get())+' '+str(SHTUKop)+'+'+text18.get(1.0)+' шт.\n'+
                 'Нижн. арм. D'+str(Narm.get())+' '+str(SHTUKpr)+'+'+text19.get(1.0)+' шт.\n'+
                 '  ПРОГИБы: \n'+
                 '    нормативный '+str(F)+' m.\n'+
                 '    расчетный '+str(round(f, 3))+' m.\n'
                 )
    loging.close()





root.mainloop()
