Sum = [50, 1200, 200, 50, 80, 456, 150, 841, 1850, 210, 217, 470, 95, 15, 20, 30, 140, 128, 50, 65, 75, 335, 35, 229, 567, 303, 65, 195, 50, 60, 60, 60, 60, 96]

# Мода - значение встречающееся чаще других значений. 
# Полимодальное распределение - несколько значений имеют одинаковое максимальное значение в списке.


def mode(Sum):
    unik = set(Sum)
    score = 0
    for i in unik:
        s = Sum.count(i)
        if s > score:
            score = s
            f = {i:s}
        elif s == score:
            f[i] = s
    m = [x for x in f.keys()]
    
    return f'Мода(-ы):{m} Частота:{[score]}'



# Средне-арифметичское значение - это значение получаемое когда сумму всех элементов разделить на их кол-во.
# Усеченное средне-арифметическое - значение 
def avarege(Sum):
    sorted = sorted(Sum)
    avarege = sum()/len(Sum)
    return avarege


 
# Медиана - значение расположенное по середине отсортированного списка чисел.

def median(Sum):
    sort = sorted(Sum)
    if len(sort) % 2 == 0:
        return (sort[len(sort)//2 - 1] + sort[len(sort)//2]) / 2
    else:
        return sort[len(sort)//2]
        


# Размах - разница между самым большим и малеьнким значениями в списке.

def range_(Sum):
    x = abs(min(Sum)-max(Sum))
    return x



# Отклонение - эта разница между конкретным значение из списка и средним значением этого списка.
# Дисперсия - среднее значение отклания которая получилась в результате сложения всех квадратов откланений и делением это суммы на колл-во отклонений.

def dispersion(Sum):
    deviation = []
    avarege = sum(Sum)/len(Sum)
    for i in Sum:
        deviation.append(avarege - i)
    dispersion_deviation = []
    for b in deviation:
        dispersion_deviation.append(b**2)
    return sum(dispersion_deviation)/len(dispersion_deviation)



# Среднеквадратическое отклонение - это дисперсия взятая под корень. 

def ccc(Sum):
    deviation = []
    avarege = sum(Sum)/len(Sum)
    for i in Sum:
        deviation.append(avarege - i)
    dispersion_deviation = []
    for b in deviation:
        dispersion_deviation.append(b**2)
    return (sum(dispersion_deviation)/len(dispersion_deviation)) ** (1/2)

print(ccc([1, 2, 3, 4, 5]))
