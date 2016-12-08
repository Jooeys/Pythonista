一、使用说明
    
***
1.情况：由于目前spark直接生成的json是每行一个对象，类似以下的json数据格式
    [
  {
    "cardno": 100000026235,
    "trdate": "2015-12-25",
    "otime": "16:13:33",
    "dtime": "16:21:10",
    "osite": 16,
    "dsite": 15,
    "tfc": 1
  }]

***

2.需求：转换成Json column arrays 数组格式 [{},{}]如下
{'cardno': [100006734923], 'trdate': ['2015-12-25'], 'dtime': ['17:56:45'], 'dsite': [40], 'osite': [41], 'otime': ['17:50:11'], 'tfc': [1]}

***

3.Python代码实现：
import sys
import json

with open(r'D:/data.json', 'r') as f:
    data = json.load(f)
	# test =  {
	#     "cardno": 100006734923,
	#     "trdate": "2015-12-25",
	#     "otime": "17:50:11",
	#     "dtime": "17:56:45",
	#     "osite": 41,
	#     "dsite": 40,
	#     "tfc": 1
 #  	}
	result = {"cardno": [], "trdate":[], "otime":[],"dtime":[],"osite":[],"dsite":[],"tfc":[]}
for test in data:
	for a in test.keys():
		result[a].append(test[a]);
print(result)
 
输入本地文件路径转换。
