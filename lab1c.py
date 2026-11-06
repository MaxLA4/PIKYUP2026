import sys
import math


def get_coef(index, prompt):
    try:
        return float(sys.argv[index])
    except:
        pass

    while True:
        print(prompt)
        try:
            return float(input())
        except ValueError:
            print('Некорректное значение')


def get_roots(a, b, c):

    result = []
    D = b*b - 4*a*c
    print('Дискриминант: {}'.format(D))
    if D < 0.0:
        return result

    t_list = []
    if D == 0.0:
        t_list.append(-b / (2.0*a))
    else:
        sqD = math.sqrt(D)
        t_list.append((-b + sqD) / (2.0*a))
        t_list.append((-b - sqD) / (2.0*a))
    # Из каждого t получаем x
    for t in t_list:
        if t == 0.0:
            result.append(0.0)
        elif t > 0.0:
            result.append(math.sqrt(t))
            result.append(-math.sqrt(t))
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    else:
        print('Количество корней: {}'.format(len_roots))
        for root in roots:
            print(root)


if __name__ == "__main__":
    main()
