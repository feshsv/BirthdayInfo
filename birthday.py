from tkinter import *
from tkinter import ttk
from datetime import datetime
import calendar

now = datetime.now()
year = []
month = []
day = []

# создаю главное окно с определённым размером без возможности менять его машью
root = Tk()
root.title('Расчёт дня недели возраста и времени прошедшего с даты рождения')
root.minsize(655, 290)  # можно задать root.geometry('640x480') опеределённый разм. с возможностью изменения
root.maxsize(655, 290)
root.iconbitmap(default='windowico.ico')  # ставлю иконку в угол окна

# надпись на поле главного окна
window_text = Label(root, text='Узнай о дне твоего рождения по дате', font='Arial 22', fg='pale violet red')
window_text.grid(row=0, column=0, columnspan=10)

# задаю выпадающий список с годом рождения
window_yeart = Label(root, text='Год рождения')

for one in range(100):
    year.append(now.year - one)
window_year = ttk.Combobox(root, width=20, height=20)
window_year['values'] = year

# тут упаковываю выпадающий список года рождения
window_yeart.grid(row=3, column=0, sticky=E, pady=30)  # N - верх, S - низ, W - лево, E - право
window_year.grid(row=3, column=1, pady=30)

# задаю выпадающий список с месяцем рождения
window_montht = Label(root, text='Месяц рождения')

for two in range(12):
    month.append(two + 1)
window_month = ttk.Combobox(root, width=10, height=12)
window_month['values'] = month

# тут упаковываю выпадающий список месяца рождения
window_montht.grid(row=3, column=3, sticky=E, pady=30)
window_month.grid(row=3, column=4, pady=30)

# задаю выпадающий список с днём рождения
window_dayt = Label(root, text='День рождения')

for three in range(31):
    day.append(three + 1)

window_day = ttk.Combobox(root, width=10, height=20)
window_day['values'] = day

# тут упаковываю выпадающий список месяца рождения
window_dayt.grid(row=3, column=6, sticky=E, pady=30)
window_day.grid(row=3, column=7, pady=30)

# кнопка проверить др
button = Button(root, text='Проверить')
button.grid(row=5, column=0, pady=10, padx=10)

# кнопка узнать когда др в пятницу и субботу
button1 = Button(root, text='Когда др в Пт и Сб?')
button1.grid(row=5, column=7, pady=10)

# сам функционал окна (backend)
weekdays = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']


def output(event):
    outtext.delete('1.0', END)  # отчищаю поле при каждом нажатии на кнопку
    birthday = window_day.get()
    birthmounth = window_month.get()
    birthyear = window_year.get()

    needformat = [int(birthyear), int(birthmounth), int(birthday)]
    try:
        daysinmonth = calendar.monthrange(needformat[0], needformat[1])  # в первом аргументе день недели с которого
        # начался месяц во втором сколько дней в месяце
    except calendar.IllegalMonthError:
        daysinmonth = needformat[1]
    try:
        dayofweek = calendar.weekday(needformat[0], needformat[1], needformat[2])  # какой день недели был в эту дату
    except ValueError:
        dayofweek = 'Слишком длинный выдался год'
    try:
        thisyear = calendar.weekday(now.year, needformat[1], needformat[2])
    except ValueError:
        thisyear = ''
        counter = 0
        while thisyear == '':
            counter += 1
            if needformat[1] == 2:
                try:
                    thisyear = calendar.weekday(now.year + counter, needformat[1], needformat[2])
                except:
                    pass
                if type(thisyear) == int:
                    if thisyear > 0:
                        thisyear = 'Не будет в этом году дня рождения. Будет только в ' + str(now.year + counter)
                if needformat[2] > 29:
                    thisyear = 'просто чтоб из цикла выйти'
            else:
                thisyear = 'просто чтоб из цикла выйти'

    def wrightday(wright):
        wright = str(wright)
        try:
            if wright[-1] == '1':
                return 'день'
            elif wright[-1] == '0' or int(wright[-2:]) >= 5:
                return 'дней'
            else:
                return 'дня'
        except Exception:
            return 'дней'

    def wasmonth(month):
        month = str(month)
        try:
            if month[-1] == '1':
                return 'месяц'
            elif month[-1] == '0' or int(month[-2:]) >= 5:
                return 'месяцев'
            else:
                return 'месяца'
        except Exception:
            return 'месяц'

    def wasyear(year):
        if year[-1] == '.':
            year = '0' + year[0]
        try:
            if year[-1] == '1':
                return 'год'
            elif year[-1] == '0' or int(year[-1]) >= 5:
                return 'лет'
            else:
                return 'года'
        except Exception:
            return 'года'

    def vo(day):
        if day == 'вторник':
            return 'во'
        else:
            return 'в'

    def years(yearswas):
        if yearswas[-1] == '.':
            return yearswas[0]
        else:
            return yearswas

    def was(day):
        if day == 31:
            return 'был'
        else:
            return 'было'

    def days_diff(date1, date2):
        date1 = date1
        date2 = datetime(date2[0], date2[1], date2[2])
        out = date2 - date1
        return abs(out.days)

    def diff_month(d1, d2):
        d2 = datetime(d2[0], d2[1], d2[2])
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    def outvision():
        if now.year < needformat[0] and needformat[1] <= 12 and needformat[2] <= daysinmonth[1]:
            endvers = 'Рассчёт возможен только по дате из прошлого. Ты указал ' + str(needformat[0]) + \
                      ' год. А ведь он ещё \nне наступил, поэтому могу сказать только то, что в ' + \
                      str(needformat[0]) + ' году твой день рождения будет ' + str(vo(weekdays[dayofweek])) + ' ' + \
                      str(weekdays[dayofweek])
            return endvers
        elif needformat[1] > 12:
            endvers = 'В году всего 12 месяцев. Ты давай без этого вот. Укажи нормальный месяц.'
            return endvers
        elif needformat[2] > daysinmonth[1]:
            endvers = 'В указанном месяце всего ' + str(daysinmonth[1]) + \
                      ' дней. Ты давай без этого вот. Укажи нормальный день.'
            return endvers
        elif type(thisyear) == str:
            endvers = 'Ты родился ' + str(vo(weekdays[dayofweek])) + ' ' + str(weekdays[dayofweek]) + \
                      ', в этом месяце ' + str(was(daysinmonth[1])) + ' ' + str(daysinmonth[1]) + ' ' + \
                      str(wrightday(daysinmonth[1])) + '. \nС тех пор минуло:' + '\n' + \
                      str(days_diff(now, needformat)) + ' ' + str(wrightday(days_diff(now, needformat))) + '\n' + \
                      str(diff_month(now, needformat)) + ' ' + str(wasmonth(diff_month(now, needformat))) + '\n' + \
                      str(years(str((diff_month(now, needformat)) / 12)[0:2])) + ' ' + \
                      str(wasyear(str((diff_month(now, needformat)) / 12)[0:2])) + '\n' + \
                      '\n' + thisyear + '.'
            return endvers
        else:
            endvers = 'Ты родился ' + str(vo(weekdays[dayofweek])) + ' ' + str(weekdays[dayofweek]) + \
                      ', в этом месяце ' + str(was(daysinmonth[1])) + ' ' + str(daysinmonth[1]) + ' ' + \
                      str(wrightday(daysinmonth[1])) + '. \nС тех пор минуло:' + '\n' + \
                      str(days_diff(now, needformat)) + ' ' + str(wrightday(days_diff(now, needformat))) + '\n' + \
                      str(diff_month(now, needformat)) + ' ' + str(wasmonth(diff_month(now, needformat))) + '\n' + \
                      str(years(str((diff_month(now, needformat)) / 12)[0:2])) + ' ' + \
                      str(wasyear(str((diff_month(now, needformat)) / 12)[0:2])) + '\n' + \
                      '\nв этом году твой день рождения в ' + str(weekdays[thisyear])
        return endvers
    outtext.insert(INSERT, outvision())


def output1(eventpt):
    outtext.delete('1.0', END)  # отчищаю поле при каждом нажатии на кнопку
    birthday = window_day.get()
    birthmounth = window_month.get()
    birthyear = window_year.get()
    needformat = [int(birthyear), int(birthmounth), int(birthday)]

    def outvisionpt():
        counter = 0
        text = ''
        try:
            daysinmonth = calendar.monthrange(needformat[0], needformat[1])  # в первом аргументе день недели с
            # которого начался месяц, во втором сколько дней в месяце
        except calendar.IllegalMonthError:
            daysinmonth = needformat[2]

        if needformat[1] > 12:
            text = 'В году всего 12 месяцев. Ты давай без этого вот. Укажи нормальный месяц.'
        elif needformat[2] > daysinmonth[1]:
            text = 'В указанном месяце всего ' + str(daysinmonth[1]) + \
                   ' дней. Ты давай без этого вот. Укажи нормальный день.'
        if text == '':
            while counter < 80:
                try:
                    birthday_in_pt = calendar.weekday(now.year+counter, needformat[1], needformat[2])
                    if birthday_in_pt == 4 or birthday_in_pt == 5:
                        text += str(now.year+counter) + '\n'
                        counter += 1
                    else:
                        counter += 1
                except ValueError:
                    counter += 1
        return text
    outtext.insert(INSERT, outvisionpt())


# клик левой кнопки мыши по кнопке проверить
button.bind("<Button-1>", output)

# клик левой кнопки мыши по кнопке др в пт и сб
button1.bind("<Button-1>", output1)

# определяю тип окна для вывода результата и его место в основном окне
outtext = Text(width=80, height=7)
outtext.grid(row=4, column=0, pady=5, padx=5, columnspan=10)

# создаю и закрепляю виджет прокрутки к текстовому полю в котором будет отображаться результат обработки
vscrollbar = Scrollbar(orient='vert', command=outtext.yview)
outtext['yscrollcommand'] = vscrollbar.set
vscrollbar.grid(row=4, column=0, pady=5, padx=5, columnspan=10, sticky=N+S+E)

root.mainloop()
