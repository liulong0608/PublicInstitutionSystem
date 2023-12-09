"""         ==Coding: UTF-8==
**    @Project :        随机生成身份证号码
**    @fileName         generateRandomIDNumbers.py
**    @version          v0.1
**    @author           Echo
**    @Warehouse        https://gitee.com/liu-long068/
**    @EditTime         2023/10/7
"""
import random
import tkinter as tk

from utils.areaCode import gen_area


class GenerateRandomIDNumbers(object):
    """
    A class for generating random ID numbers.
    """

    CHECK_CODE = {
        "0": '1',
        "1": '0',
        "2": 'X',
        "3": '9',
        "4": '8',
        "5": '7',
        "6": '6',
        "7": '5',
        "8": '4',
        "9": '3',
        "10": '2'
    }

    def __init__(self):
        """
        Initializes a new instance of the GenerateRandomIDNumbers class.
        """
        self.area_code = gen_area()

    def gen_birthday(self):
        """
        Generates a random birthday in the format YYYYMMDD.

        Returns:
            str: The generated birthday.
        """
        birth_year = str(random.randint(1970, 2004))
        birth_month = str(random.randint(1, 12)).zfill(2)

        if birth_month in ['01', '03', '05', '07', '08', '10', '12']:
            birth_day = str(random.randint(1, 31)).zfill(2)
        elif birth_month in ['04', '06', '09', '11']:
            birth_day = str(random.randint(1, 30)).zfill(2)
        else:
            birth_day = str(random.randint(1, 28)).zfill(2)

        sequence_code = str(random.randint(1, 999)).zfill(3)
        temp_code = self.area_code + birth_year + birth_month + birth_day + sequence_code
        return temp_code

    def get_check_digit(self, id_number):
        """
        Calculates the check digit for the given ID number.

        Args:
            id_number (str): The ID number without the check digit.

        Returns:
            str: The calculated check digit.
        """
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(id_number[i])
        check_digit = self.CHECK_CODE[str(check_sum % 11)]
        return check_digit

    @property
    def generate_id(self):
        """
        Generates a random ID number.

        Returns:
            str: The generated ID number.
        """
        id_number = self.gen_birthday()
        check_digit = self.get_check_digit(id_number)
        id_number += str(check_digit)
        return id_number


if __name__ == '__main__':
    print(GenerateRandomIDNumbers().generate_id)
