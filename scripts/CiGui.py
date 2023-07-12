# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         CiGui.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/7/12
# @Software:        PyCharm
# ====/******/=====
import tkinter as tk
# from scripts.social_unified_creditcode.succ_utils.sucreditcode import CreditIdentifier
# -*-coding=utf-8-*-
# 生成、验证社会统一社会信用代码

# 统一社会信用代码中不使用I,O,Z,S,V
import random
import json
from pathlib import Path

SOCIAL_CREDIT_CHECK_CODE_DICT = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "P": 23,
    "Q": 24,
    "R": 25,
    "T": 26,
    "U": 27,
    "W": 28,
    "X": 29,
    "Y": 30,
}

# GB11714-1997全国组织机构代码编制规则中代码字符集
ORGANIZATION_CHECK_CODE_DICT = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35,
}


class CreditIdentifier(object):
    @staticmethod
    def get_random_address():
        with open(Path(__file__).parent / "address.json", encoding='utf-8') as reader:
            address = json.load(reader)
        nums_province = len(address)
        province = address[random.randint(0, nums_province - 1)]
        nums_city = len(province["child"])
        city = province["child"][random.randint(0, nums_city - 1)]
        areas = city["child"]
        nums_area = len(areas)
        area = areas[random.randint(0, nums_area - 1)]
        address_name = f"{province['name']}{city['name']}{area['name']}"
        address_code = area["code"]
        return {"name": address_name, "code": address_code}

    def CreateC9(self, code):
        # 第i位置上的加权因子
        weighting_factor = [3, 7, 9, 10, 5, 8, 4, 2]
        # 第9~17位为主体标识码(组织机构代码)
        organization_code = code[8:17]
        # 本体代码
        ontology_code = organization_code[:8]
        # 生成校验码
        tmp_check_code = self.gen_check_code(
            weighting_factor, ontology_code, 11, ORGANIZATION_CHECK_CODE_DICT
        )
        return code[:16] + tmp_check_code

    def gen_random_credit_code(self):
        """Generate random credit code"""

        department = "9"  # 登记管理部门代码
        agency = "123"  # 机构类别
        organization_num = str(random.randint(11111111, 99999999))

        # 行政区划代码
        address = self.get_random_address()
        credit_code = (
            f"{department}{random.choice(agency)}{address['code']}{organization_num}"
        )
        return {
            "address": address["name"],
            "code": self.get_social_credit_code(credit_code),
        }

    def get_social_credit_code(self, code):
        code = self.CreateC9(code[:16])
        # 第i位置上的加权因子
        weighting_factor = [
            1,
            3,
            9,
            27,
            19,
            26,
            16,
            17,
            20,
            29,
            25,
            13,
            8,
            24,
            10,
            30,
            28,
        ]
        # 本体代码
        ontology_code = code[:17]
        # 计算校验码
        tmp_check_code = self.gen_check_code(
            weighting_factor, ontology_code, 31, SOCIAL_CREDIT_CHECK_CODE_DICT
        )
        return code[:17] + tmp_check_code

    # 只返回一个值 字符
    def gen_check_code(self, weighting_factor, ontology_code, modulus, check_code_dict):
        total = sum(
            int(ontology_code[i]) * weighting_factor[i]
            if ontology_code[i].isdigit()
            else check_code_dict[ontology_code[i]] * weighting_factor[i]
            for i in range(len(ontology_code))
        )
        C9 = modulus - total % modulus
        C9 = 0 if C9 == 31 else C9
        C9 = list(check_code_dict.keys())[list(check_code_dict.values()).index(C9)]
        return C9

    def valid(self, code):
        return code == self.get_social_credit_code(code)


class App:
    def __init__(self):
        self.ci = CreditIdentifier()

        self.window = tk.Tk()
        self.window.title("社会统一信用代码生成器")
        self.window.iconbitmap('credit.ico')

        # 设置窗体大小
        self.window.geometry("350x80")

        # 标签和输入框
        self.label_address = tk.Label(self.window, text="地\t址：")
        self.label_address.grid(row=0, column=0, sticky=tk.W)

        self.address_entry = tk.Entry(self.window, width=40)
        self.address_entry.grid(row=0, column=1)

        self.label_code = tk.Label(self.window, text="统一社会信用代码：")
        self.label_code.grid(row=1, column=0, sticky=tk.W)

        self.code_entry = tk.Entry(self.window, width=40)
        self.code_entry.grid(row=1, column=1)

        # 生成按钮和清除按钮
        self.generate_button = tk.Button(self.window, text="生成", command=self.generate_code)
        self.generate_button.grid(row=2, column=0, columnspan=2)

        self.clear_button = tk.Button(self.window, text="清除", command=self.clear_fields)
        self.clear_button.grid(row=2, column=1, columnspan=2)

    def generate_code(self):
        random_code = self.ci.gen_random_credit_code()
        address = random_code["address"]
        code = random_code["code"]
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(tk.END, address)
        self.code_entry.delete(0, tk.END)
        self.code_entry.insert(tk.END, code)

    def clear_fields(self):
        self.address_entry.delete(0, tk.END)
        self.code_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


app = App()
app.run()
