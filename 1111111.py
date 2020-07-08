#-*- coding:utf-8 -*-
#@Date   : 2018/12/22
#@Author : suyifan
#@File   : 1111111.py



input = [
    {'id':1,'level':0,'parent_id':0,'name':'PROVINCE_A'},
    {'id':2,'level':1,'parent_id':1,'name':'CITY_B'},
    {'id':3,'level':2,'parent_id':2,'name':'DISTRICT_C'},
    {'id':4,'level':3,'parent_id':3,'name':'VILLAGE_D'},
    {'id':5,'level':3,'parent_id':3,'name':'VILLAGE_E'},
    {'id':6,'level':0,'parent_id':0,'name':'PROVINCE_F'},
    {'id':7,'level':1,'parent_id':6,'name':'CITY_G'},
    {'id':8,'level':2,'parent_id':7,'name':'DISTRICT_H'},
    {'id':9,'level':3,'parent_id':8,'name':'VILLAGE_I'}#,{"level":"q"}
]


# from collections import defaultdict
# def nested_dict_factory():
#     return defaultdict(dict)
# def nested_dict_factory2():
#     return defaultdict(nested_dict_factory)
# db = defaultdict(nested_dict_factory2)


# def fun1(input):
#     list1 = []
#     ans = {}
#     for i in range(len(input)-1):
#         if input[i+1]["level"] != 0:
#             list1.append(input[i])
#         else:
#             list1.append(input[i])
#             ans = fun2(list1,ans)
#             list1 = []
#     list1.append(input[-1])
#     ans = fun2(list1,ans)
#     return ans
# def fun2(list1,ans):
#     list_3 = []
#     print(len(list1),"list1=",list1)
#     for dic in reversed(list1):
#
#         if dic["level"] == 3:
#             list_3.append(dic["name"])
#         else:
#
#             result = dict()
#             result[dic["name"]] = list_3
#             list_3 = result
#     a = {**ans,**result}
#     # print("list3",list_3)
#     return a
# print("ans=",fun1(input))


inputs = [
    {'id': 1, 'level': 0, 'parent_id': 0, 'name': 'PROVINCE_A'},
    {'id': 2, 'level': 1, 'parent_id': 1, 'name': 'CITY_B'},
    {'id': 3, 'level': 2, 'parent_id': 2, 'name': 'DISTRICT_C'},
    {'id': 4, 'level': 3, 'parent_id': 3, 'name': 'VILLAGE_D'},
    {'id': 5, 'level': 3, 'parent_id': 3, 'name': 'VILLAGE_E'},
    {'id': 6, 'level': 0, 'parent_id': 0, 'name': 'PROVINCE_F'},
    {'id': 7, 'level': 1, 'parent_id': 6, 'name': 'CITY_G'},
    {'id': 8, 'level': 2, 'parent_id': 7, 'name': 'DISTRICT_H'},
    {'id': 9, 'level': 3, 'parent_id': 8, 'name': 'VILLAGE_I'}
]


def fun1(inputs):
    inputs_dict = {}
    for item in inputs:
        inputs_dict[item['id']] = item

    def get_parent_ids(item_copy):
        parent_ids = []
        level = item_copy['level']
        while level > 0:
            parent_id = item_copy['parent_id']
            parent_ids.append(parent_id)
            item_copy = inputs_dict[parent_id]
            level = item_copy['level']

        return parent_ids[::-1]

    ans = {}
    for item in inputs:
        parent_ids = get_parent_ids(item)
        l = len(parent_ids)
        if l == 0:
            if item['name'] not in ans.keys():
                ans[item['name']] = {}
        else:
            parent_names = [inputs_dict[parent_id]['name'] for parent_id in parent_ids]
            parent_levels = [inputs_dict[parent_id]['level'] for parent_id in parent_ids]

            ans_node = ans
            for i, parent_name in enumerate(parent_names):
                if parent_name not in ans_node.keys():
                    ans_node[parent_name] = {} if parent_levels[i] < 2 else []
                ans_node = ans_node[parent_name]

            if item['level'] > 2:
                ans_node.append(item['name'])
            elif item['level'] == 2:
                ans_node[item['name']] = []
            else:
                ans_node[item['name']] = {}

    return ans


from pprint import pprint

pprint(fun1(inputs))