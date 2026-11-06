import sys
import math


def ask_coef(prompt):

    print(prompt)
    try:
        return float(input())
    except ValueError:
        print('Некорректное значение')
        return ask_coef(prompt)


def get_coef(index, prompt):

    try:
        return float(sys.argv[index])
    except:
        return ask_coef(prompt)


def get_t_roots(a, b, c):

    D = b*b - 4*a*c
    print('Дискриминант: {}'.format(D))
    match D:
        case 0.0:
            return [-b / (2.0*a)]
        case _ if D > 0.0:
            sqD = math.sqrt(D)
            return [(-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a)]
        case _:
            return []


def get_x_roots(t):

    match t:
        case 0.0:
            return [0.0]
        case _ if t > 0.0:
            return [math.sqrt(t), -math.sqrt(t)]
        case _:
            return []


def get_roots(a, b, c):
    result = []
    for t in get_t_roots(a, b, c):
        result += get_x_roots(t)
    return result


def show(roots):
    match roots:
        case []:
            print('Нет корней')
        case _:
            print('Количество корней: {}'.format(len(roots)))
            print(roots)


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    show(get_roots(a, b, c))


if __name__ == "__main__":
    main()
