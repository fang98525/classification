import pandas
import collections
train=pandas.read_excel("train.xlsx")

#去掉指定无用符好
puncts = [' ',"","\n",]
def clean_text(x):
    x=x.strip()
    for punct in puncts:
        x=x.replace(punct,'')
    return x






# print(train["title"][70])
train["title"].fillna("",inplace=True)
# print(train["title"][70])

train["sentence"]=train["title"]+"。"+train["diseaseName"]+","+train["conditionDesc"]
a=train["sentence"].isnull()
for i in train["sentence"]:
    i.replace("。","")

print(a)
a=collections.Counter(a)
print(a)
print(len(train["sentence"]))
print(train["sentence"].values)
train["sentence"].to_excel("分析训练集.xlsx")


