import pandas as pd
import matplotlib.pyplot as plt
from config import Config

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


def cal_text_len(row):
    row_len = len(row)
    if row_len < 64:
        return '0-64'
    elif row_len < 128:
        return '64-128'
    elif row_len < 256:
        return '128-256'

    # else:
    #     return '512++'


config = Config()
config.base_dir="/data1/home/fzq/projects/nlpclassification/data/mdecinedata/"

train_df = pd.read_excel( '/data1/home/fzq/projects/nlpclassification/data/mdecinedata/train.xlsx')
# print(train_df.head())
train_df["text"]=train_df["diseaseName"]+","+train_df["conditionDesc"]
print(train_df["text"].head())
train_df['text_len'] = train_df['text'].apply(cal_text_len)


x_y_list = dict(train_df['text_len'].value_counts())
print((x_y_list))
# for  i in range(len(train_df["text"])):

x_name = ['0-64', '64-128', '128-256' ]
y = [x_y_list[i] for i in x_name]

print(sum(y))
# 画出条形图
#  color=['b','r','g','y','c','m','y','k','c','g','g']
plt.bar(x_name, y, color=['b', 'r', 'g', 'y', 'c', 'm'])
plt.xlabel('长度')
plt.ylabel('数量/条')
plt.title('原始数据文本长度数量分布图')
plt.savefig(config.base_dir + "cls_source.jpeg", figsize=(1024, 768), dpi=600)
plt.show()

plt.pie(x=y,  # 绘图数据
        labels=x_name,  # 添加教育水平标签
        autopct='%.1f%%'  # 设置百分比的格式，这里保留一位小数
        )
plt.title('原始数据文本长度分布占比图')
plt.savefig(config.base_dir + "cls_source_pie.jpeg", figsize=(1024, 768), dpi=600)
plt.show()
