# 导包
import json


# class Read_json:
#     # 记录查询了几次
#     count = 0
#
#     def __init__(self, filename, mode, new_file=False):
#         self.filename = filename
#         self.mode = mode
#         self.new_file = new_file
#
#     def read_json(self):
#         """
#
#         :return:
#         """
#         filepath = "../data/" + self.filename
#         # 打开文件并调用 load方法
#         with open(filepath, "r", encoding="utf-8") as f:
#             data1 = json.load(f)
#         arrs = []
#         for data in data1.values():
#             arrs.append((data.get("name"),
#                          data.get("person")))
#         if self.mode == "add":
#             return arrs
#         elif self.mode == "edit":
#             return arrs[0][0] + "修改"
#         elif self.new_file:
#             Read_json.count = 0
#             return arrs[Read_json.count]
#         else:
#             Read_json.count += 1
#             return arrs[Read_json.count - 1]

class Read_json:
    # 记录查询了几次
    count = 0
    old_file = ''

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def read_json(self):
        """

        :return:
        """
        filepath = "../data/" + self.filename
        # 打开文件并调用 load方法
        with open(filepath, "r", encoding="utf-8") as f:
            data1 = json.load(f)
        arrs = []
        for data in data1.values():
            arrs.append((data.get("name"),
                         data.get("person")))
        if self.mode == "add":
            return arrs
        elif self.mode == "edit":
            return arrs[0][0] + "修改"
        else:
            if self.filename == Read_json.old_file:
                Read_json.count += 1
                return arrs[Read_json.count]
            else:
                Read_json.old_file = self.filename
                Read_json.count = 0
                return arrs[Read_json.count]

a = Read_json("xslr.json", 'add')
print(a.read_json())
b = Read_json("xslr.json", 'edit')
print(b.read_json())
c = Read_json("xslr.json", 'xx')
print(c.read_json())
d = Read_json("xslr.json", 'xx')
print(d.read_json())
f = Read_json("xslr1.json", 'xx')
print(f.read_json())
