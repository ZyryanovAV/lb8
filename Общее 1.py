#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
# числа.

if __name__ == '__main__':
    school = {1: 'One', 2: 'Two', 3: 'Three'}

    new_school = {}
    for key, value in school.items():
        new_school[value] = key
    print(new_school)
