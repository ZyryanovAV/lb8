#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

if __name__ == '__main__':
    class_in_school = {'1a': 25, "2a": 30, '3a': 27, '3b': 20, '4a': 24}

    class_in_school['1a'] = 17
    class_in_school['4b'] = 56
    del class_in_school['3b']
    print(class_in_school)

    f = sum(class_in_school.values())
    print(f)