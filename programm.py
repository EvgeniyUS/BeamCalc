# Программа для расчета ЖБ конструкций
# Версия 0.000

from tkinter import *
from tkinter.ttk import *
from math import *
import datetime

root = Tk()
root.title('Расчёт ЖБ конструкций при распределённой нагрузке')
root.geometry('585x450')

#tL = StringVar()


def uni_lab(tL, xL, yL, tF='Arial 10', tFG='', tW=0):
    LName = Label(text=tL, font=tF, foreground=tFG, width=tW)
    LName.place(x=xL, y=yL)


uni_lab('Схема работы:', 0, 0)
uni_lab('Класс бетона:', 0, 25)
uni_lab('Класс арматуры:', 0, 50)
uni_lab('Длинна балки, m', 0, 75)
uni_lab('Нагрузка, kH/m', 0, 100)
uni_lab('Момент пролёт:', 0, 175)
uni_lab('Момент опора:', 0, 150)
uni_lab('Ширина балки, m', 200, 75)
uni_lab('Высота балки, m', 200, 100)
uni_lab('Защитный слой, m', 270, 0)
uni_lab('A0pr=', 270, 175)
uni_lab('A0op=', 270, 150)
uni_lab('D Верх. арм., mm', 10, 225)
uni_lab('D Нижн. арм., mm', 10, 275)
uni_lab('As tr op=', 254, 225)
uni_lab('As op=', 406, 225)
uni_lab('As tr pr=', 254, 275)
uni_lab('As pr=', 406, 275)
uni_lab('+', 420, 245, 'Arial 15')
uni_lab('+', 420, 295, 'Arial 15')
uni_lab(' -' * 71, 0, 200)
uni_lab('ПРОГИБ:', 10, 335, 'Arial 15')
uni_lab('расчетный -', 290, 360)
uni_lab('нормативный -', 90, 360)
uni_lab(' -' * 71, 0, 125)


beton_class = ('B10', 'B15', 'B20', 'B25', 'B30',
               'B35', 'B40', 'B45', 'B50', 'B55', 'B60')
rb_data = (5600,
          8500,
          11500,
          14500,
          17000,
          19500,
          22000,
          25000,
          27500,
          30000,
          33000)
eb_data = (18000000,
          23000000,
          27000000,
          30000000,
          32500000,
          34500000,
          36000000,
          37500000,
          39000000,
          39500000,
          40000000)
rb_dict = dict(zip(beton_class, rb_data))
eb_dict = dict(zip(beton_class, eb_data))


def get_rb(root):
    a = beton_combo.get()
    global Rb, Rbser, Eb
    Rb = rb_dict[a]
    Rbser = rb_dict[a]
    Eb = eb_dict[a]

beton_combo = Combobox(width=5, values=beton_class)
beton_combo.set('B30')
beton_combo.place(x=110, y=25)


schema_data = ('Заделка-Заделка',
               'Заделка-Шарнир',
               'Шарнир-Шарнир',
               'Консоль')
kpr_data = (24, 16, 8, 0)
kop_data = (12, 8, 0, 2)
kpr_dict = dict(zip(schema_data, kpr_data))
kop_dict = dict(zip(schema_data, kop_data))

def get_km(root):
    a = schema.get()
    global Kpr, Kop
    Kpr = kpr_dict[a]
    Kop = kop_dict[a]

schema = Combobox(width=18, values=schema_data)
schema.set('Заделка-Шарнир')
schema.place(x=110, y=0)


arm_type = ('A240 (A-I)',
             'A300 (A-II)',
             'A400 (A-III, A400C)',
             'A500 (A500C)',
             'B500 (Bp-I, B500C)')
rs_data = (215000, 270000, 355000, 435000, 415000)
rs_dict = dict(zip(arm_type, rs_data))

def get_rs(root):
    a = arm_combo.get()
    global Rs, Es
    Es = 200000000
    Rs = rs_dict[a]

arm_combo = Combobox(width=18, values=arm_type)
arm_combo.set('A400 (A-III, A400C)')
arm_combo.place(x=110, y=50)

arm_data = ('6', '8', '12', '16', '22')

v_arm_combo = Combobox(width=2, values=arm_data)
v_arm_combo.set('16')
v_arm_combo.place(x=130, y=225)

def get_v_arm(root):
    a = int(v_arm_combo.get())
    global VarmS
    VarmS = (a ** 2 * pi) / 400


n_arm_combo = Combobox(width=2, values=arm_data)
n_arm_combo.set('12')
n_arm_combo.place(x=130, y=275)

def get_n_arm(root):
    a = int(n_arm_combo.get())
    global NarmS
    NarmS = (a ** 2 * 3.14) / 400

def get_d(root):
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
    Xm = h0 * (sqrt((Ms ** 2 * As1 ** 2) + (2 * Ms * As1)) - Ms * As1)
    Z = h0 - 1 / 3 * Xm
    Dsp = Es * AsD / 10000 * Z * (h0 - Xm)

    A0H = MD / B / h0 ** 2 / Rbser
    Ma = AsD / 10000 / B / h0 * Es / Eb
    EE = 1 / (1.8 + (1 + 5 * A0H) / 10 / Ma)
    z = h0 * (1 - EE / 2)
    Dsnip = h0 * z / (1 * 10000 / Es / AsD + 0.9 / EE / B / h0 / Eb / 0.15)

    DD = (Dsp + Dsnip) / 2

    A1 = schema.get()
    if A1 == 'Заделка-Заделка':
        f = q * L ** 4 / 384 / DD
        Lf = 200
    elif A1 == 'Заделка-Шарнир':
        f = q * L ** 4 / 185 / DD
        Lf = 200
    elif A1 == 'Шарнир-Шарнир':
        f = 5 * q * L ** 4 / 384 / DD
        Lf = 200
    elif A1 == 'Консоль':
        f = q * L ** 4 / 8 / DD
        Lf = 150

    F = L / Lf
    if F<=f:
        f_color='red'
    else:
        f_color='green'
    uni_lab(str(round(F, 3))+' m', 180, 350, 'Arial 18', tW=7)
    uni_lab(str(round(f, 3))+' m', 370, 350, 'Arial 18', f_color, tW=7)

    log_file(root)


def arm_proc(root):
    ArmProcV = AsV / ((AA / 2 * B * 10000) / 100)
    ArmProcN = AsN / ((AA / 2 * B * 10000) / 100)
    uni_lab(str(round(ArmProcV, 2))+'%', 503, 250, tW=6)
    uni_lab(str(round(ArmProcN, 2))+'%', 503, 300, tW=6)


def get_as(root):
    global AsV, AsN, ShtukOp, ShtukPr
    a = int(text18.get())
    ShtukOp = ceil(AstrV / VarmS) + a
    uni_lab(str(ShtukOp-a)+'шт.', 340, 245, 'Arial 15', 'green', tW=7)

    AsV = ShtukOp * VarmS
    uni_lab(str(round(AsV, 3)), 450, 225, tW=7)

    b = int(text19.get())
    ShtukPr = ceil(AstrN / NarmS) + b
    uni_lab(str(ShtukPr-b)+'шт.', 340, 295, 'Arial 15', 'green', tW=7)

    AsN = ShtukPr * NarmS
    uni_lab(str(round(AsN, 3)), 450, 275, tW=7)

    get_d(root)

    arm_proc(root)


def get_astr(root):
    global AstrV, AstrN
    if nop == 0:
        AstrV = 0
        uni_lab(str(round(AstrV, 3)), 310, 225, tW=7)
    else:
        AstrV = (Mop * 10000) / (Rs * nop * h0)
        uni_lab(str(round(AstrV, 3)), 310, 225, tW=7)

    if npr == 0:
        AstrN = 0
        uni_lab(str(round(AstrN, 3)), 310, 275, tW=7)
    else:
        AstrN = (Mpr * 10000) / (Rs * npr * h0)
        uni_lab(str(round(AstrN, 3)), 310, 275, tW=7)

    get_as(root)


def get_a0(root):
    global h0, B, AA, c, A0pr, A0op
    B = float(text5.get())
    AA = float(text6.get())
    c = float(text7.get())
    h0 = AA - c
    A0pr = Mpr / (Rb * B * (h0 ** 2))
    A0op = Mop / (Rb * B * (h0 ** 2))
    uni_lab(str(round(A0pr, 3)), 310, 175, tW=7)
    uni_lab(str(round(A0op, 3)), 310, 150, tW=7)
    
    get_nu(root)


def get_nu(root):
    '''0.5 * Epr**2 - Epr + A0pr = 0   ----   квадратное уравнение'''
    global npr, nop
    if A0pr < 0.01:
        npr = 0
    elif A0pr > 0.455:
        npr = 0
    else:
        Epr = (1 - sqrt(1 - (4 * 0.5 * A0pr))) / (2 * 0.5)
        npr = 1 - 0.5 * Epr
    uni_lab('npr= '+str(round(npr, 3)), 390, 175, tW=10)

    if A0op < 0.01:
        nop = 0
    elif A0op > 0.455:
        nop = 0
    else:
        Eop = (1 - sqrt(1 - (4 * 0.5 * A0op))) / (2 * 0.5)
        nop = 1 - 0.5 * Eop
    uni_lab('nop= '+str(round(nop, 3)), 390, 150, tW=10)
    
    get_astr(root)


def start(root):
    get_km(root)
    get_rb(root)
    get_rs(root)
    get_v_arm(root)
    get_n_arm(root)
    global L, q, Mpr, Mop
    L = float(text1.get())
    q = float(text2.get())
    if Kpr > 0:
        Mpr = (q * L ** 2) / Kpr
        uni_lab(str(round(Mpr, 2))+'  kH*m', 110, 175, tW=15)
    elif Kpr == 0:
        Mpr = 0
        uni_lab(str(round(Mpr, 2))+'  kH*m', 110, 175, tW=15)
    if Kop > 0:
        Mop = (q * L ** 2) / Kop
        uni_lab(str(round(Mop, 2))+'  kH*m', 110, 150, tW=15)
    elif Kop == 0:
        Mop = 0
        uni_lab(str(round(Mop, 2))+'  kH*m', 110, 150,tW=15)
    get_a0(root)


start_button = Button(text="Ресчёт")
start_button.place(x=250, y=400)
start_button.bind("<Button-1>", start)

root.bind('<Return>', start)
root.bind('<KP_Enter>', start)


text1 = Entry(width=10)
text1.insert(0, 4)
text1.place(x=110, y=75)

text2 = Entry(width=10)
text2.insert(0, 125)
text2.place(x=110, y=100)

text5 = Entry(width=10)
text5.insert(0, 1)
text5.place(x=310, y=75)

text6 = Entry(width=10)
text6.insert(0, 0.3)
text6.place(x=310, y=100)

text7 = Entry(width=5)
text7.insert(0, 0.03)
text7.place(x=390, y=0)


text18 = Entry(width=3)
text18.insert(0, 0)
text18.place(x=450, y=250)

text19 = Entry(width=3)
text19.insert(0, 0)
text19.place(x=450, y=300)



def log_file(root):
    CT = datetime.datetime.now()
    loging = open('log.txt', 'a')
    loging.write('\n' + '-' * 40 + '\n' +
                 'Запись от: ' + str(CT) + '\n' +
                 '  Данные расчёта:\n' +
                 str(schema.get()) + '\n' +
                 'Класс бетона: ' + str(beton_combo.get()) + '\n' +
                 'Класс арматуры: ' + str(arm_combo.get()) + '\n' +
                 'L = ' + str(L) + ' m\n' +
                 'q = ' + str(q) + ' kH/m\n' +
                 'b = ' + str(B) + ' m\n' +
                 'h0 = ' + str(h0) + ' m\n' +
                 'Верх. арм. D' + str(v_arm_combo.get()) + ' ' + str(ShtukOp) + 'шт.\n' +
                 'Нижн. арм. D' + str(n_arm_combo.get()) + ' ' + str(ShtukPr) + 'шт.\n' +
                 '  ПРОГИБы: \n' +
                 '    нормативный ' + str(F) + ' m\n' +
                 '    расчетный ' + str(round(f, 3)) + ' m\n'
                 )
    loging.close()


root.mainloop()
