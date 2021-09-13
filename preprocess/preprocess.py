import pandas as pd
from config import Config
from sklearn import  model_selection

config = Config()

train_df = pd.read_excel(config.base_dir + 'train.xlsx')
dev_df = pd.read_excel(config.base_dir + 'test.xlsx')
print(dev_df.info())
train_df["title"].fillna("",inplace=True)
dev_df["title"].fillna("",inplace=True)
# print(train_df.index)
# print(train_df.describe())
# print(train_df["label"].head(100))


# def cal_text_len(row):
#     row_len = len(row)
#     if row_len < 256:
#         return 256
#     elif row_len < 384:
#         return 384
#     elif row_len < 512:
#         return 512
#     else:
#         return 1024
def cal_text_len(row):
    row_len = len(row)
    if row_len < 64:
        return '0-64'
    elif row_len < 128:
        return '64-128'
    elif row_len < 256:
        return '128-256'

train_df["sentence"]=train_df["diseaseName"]+","+train_df["conditionDesc"]
dev_df["sentence"]=dev_df["conditionDesc"]
# print(train_df["text"].head())
# print(train_df["text"].values)
# for i in range(len(train_df["sentence"])):
#     print(train_df["sentence"][i])
#     train_df["sentence"][i].replace("。","")

# train_df['text_len'] = train_df['text']
# dev_df['text_len'] = dev_df['text']

# dev_df['sentence'] =dev_df["diseaseName"]+","+dev_df["conditionDesc"]
# dev_df["sentence"]=dev_df["diseaseName"]+","+dev_df["conditionDesc"]
dev_df["num_label"]=[x for x in range(1412)]


# print(train_df['text_len'].value_counts())
# print(dev_df['text_len'].value_counts())
print('-------------------')


def merge_text(text):
    if len(text) < 512:
        return text
    else:
        return text[:128] + text[-382:]

#  取文本段前128与后382作为整体的文本

#
# train_df['text_len'] = train_df['sentence'].apply(cal_text_len)
# dev_df['text_len'] = dev_df['sentence'].apply(cal_text_len)
#
# print(train_df['text_len'].value_counts())
# print(dev_df['text_len'].value_counts())

label_list = config.label_list


def make_label(label):
    return label_list.index(label)

# train_df['sentence'] = train_df['text']
train_df['num_label'] = train_df['label']
# dev_df['num_label'] = dev_df['label']
print(train_df['num_label'].unique())
print(train_df.info())
print(train_df["sentence"].isnull())

#对训练集进行划分
train_new=train_df.loc[:7000,["id","sentence","num_label"]]
print(train_new["num_label"].head(10))
# print(train_new.info())
train_dev=train_df.loc[7001:,["id","sentence","num_label"]]
# train_dev["sentence"]=train_df.loc[7001:,["conditionDesc"]]
dev_df=dev_df.loc[:,["sentence","num_label"]]
# print(train_dev.info())
train_new.to_excel(config.base_dir + 'train1.xlsx', encoding='utf-8')
train_dev.to_excel(config.base_dir + 'dev1.xlsx', encoding='utf-8')
dev_df.to_excel(config.base_dir+"test1.xlsx")


# print(train_df['num_label'].unique())

