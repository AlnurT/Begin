"""Задача 6. Монетка 2
Практиканту снова дали задание найти старую металлическую монетку по заданным координатам.
Но теперь металлоискатель сканирует местность вокруг пользователя в виде круга и
при обнаружении/отсутствии металла прибор отображает на экране соответствующее сообщение.

Даны два действительных числа x и y и радиус r.
Напишите функцию, которая проверяет, лежит ли точка с координатами (x, y) внутри круга с радиусом r (включая его границу).
Координаты центра круга — (0, 0). Если точка принадлежит кругу, выведите сообщение «Монетка где-то рядом»,
иначе выведите сообщение «Монетки в области нет». """


from math import sqrt


def is_coin_in_circle(x: float, y: float, r: float) -> bool:
    coin_distance = sqrt(x ** 2 + y ** 2)
    return coin_distance <= r


def main():
    print("Введите координаты монетки:")
    x = float(input("X: "))
    y = float(input("Y: "))
    r = float(input("Введите радиус: "))

    if is_coin_in_circle(x, y, r):
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


if __name__ == "__main__":
    main()
