import pandas as pd
from config import Config
import collections
from sklearn import  model_selection
# from nlpcda import Similarword
config = Config()

# #补齐法使每一类的个数等于最多的那一类
# translator= Similarword(create_num=3, change_rate=0.2)

# train= pd.read_excel(config.base_dir + 'train.xlsx')
# print(train)
# print("*"*25)
# a=train["label"].sort_values()
# counter=collections.Counter(a)
# print("每种类别的样本个数分别为：",counter.values())
# print("需要补充的样本个数为：",[1086-i for i in counter.values()])
# print("*"*25)
# train=train.sort_values(by="label")
# train["sentence"]=train["diseaseName"]+","+train["conditionDesc"]
# train=train.loc[:,["id","sentence","label"]]

# #增强部分
# text_change=[]
# print(train["sentence"][:10])
# for text in train["sentence"][:] :
#     print(text)
#     rs1 = translator.replace(text)
#     print(rs1)
#     for i in rs1:
#         text_change.append(i)
# text=pd.DataFrame(text_change)
# text["label"]=train["label"]
# text.to_excel(config.base_dir + 'text_change.xlsx', encoding='utf-8')







# 将enforce的 数据还原到模型需要的格式

train=pd.read_excel(config.base_dir + 'train_enforce.xlsx', encoding='utf-8')
train=train.sort_values(by="id")
print(train)
print(train.info())
train['num_label'] = train['label']
train=train.loc[:,["id","sentence","num_label"]]
train.to_excel(config.base_dir + 'train_enforce1.xlsx', encoding='utf-8')

#对数据集进行划分
# train=pd.read_excel(config.base_dir + 'train_enforce1.xlsx', encoding='utf-8')
# train_new=train[:1500]+train[2500:]
# train_dev=train[1500:2500]
# train_new.to_excel(config.base_dir + 'train1.xlsx', encoding='utf-8')
# train_dev.to_excel(config.base_dir + 'dev1.xlsx', encoding='utf-8')
