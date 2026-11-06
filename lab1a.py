import sys
import math


class BiquadEquation:


    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.roots = []

    def get_coef(self, index, prompt):

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

    def read_coefs(self):
        self.a = self.get_coef(1, 'Введите коэффициент А:')
        self.b = self.get_coef(2, 'Введите коэффициент B:')
        self.c = self.get_coef(3, 'Введите коэффициент C:')

    def calc_roots(self):
        D = self.b*self.b - 4*self.a*self.c
        print(f'Дискриминант: {D}')
        if D < 0.0:
            return
        t_list = []
        if D == 0.0:
            t_list.append(-self.b / (2.0*self.a))
        else:
            sqD = math.sqrt(D)
            t_list.append((-self.b + sqD) / (2.0*self.a))
            t_list.append((-self.b - sqD) / (2.0*self.a))
        for t in t_list:
            if t == 0.0:
                self.roots.append(0.0)
            elif t > 0.0:
                self.roots.append(math.sqrt(t))
                self.roots.append(-math.sqrt(t))

    def print_roots(self):
        if len(self.roots) == 0:
            print('Нет корней')
        else:
            print(f'Количество корней: {len(self.roots)}')
            for root in self.roots:
                print(root)


def main():
    eq = BiquadEquation()
    eq.read_coefs()
    eq.calc_roots()
    eq.print_roots()


if __name__ == "__main__":
    main()
