# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 14:15
# @Author  : chile
# @Email   : realchilewang@foxmail.com
# @File    : config.py
# @Software: PyCharm


class Config(object):
    def __init__(self):
        self.base_dir = '/data1/home/fzq/projects/nlpclassification/data/mdecinedata/'  # 数据路径
        self.save_model = self.base_dir + 'Savemodel/'  # 模型路径
        self.result_file = 'result/'
        self.label_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.warmup_proportion = 0.05     #原始0.05
        self.use_bert = True
        self.pretrainning_model = 'roberta'
        self.embed_dense = 512

        self.decay_rate = 0.5  # 学习率衰减参数

        self.train_epoch = 15 # 训练迭代次数

        self.learning_rate = 1e-4 # 下接结构学习率  原始是1e-4
        self.embed_learning_rate = 5e-5  # 预训练模型学习率

        if self.pretrainning_model == 'roberta':
            model = '/data1/home/fzq/projects/nlpclassification/data/model/RoBERTa_zh_L12_PyTorch/'  # 中文roberta-base
        elif self.pretrainning_model == 'nezha':
            model = '/data1/home/fzq/projects/nlpclassification/data/model/nezha-cn-base/nezha-cn-base/'  # 中文nezha-base
        else:
            raise KeyError('albert nezha roberta bert bert_wwm is need')
        self.cls_num = 10
        self.sequence_length = 512
        self.batch_size =10

        self.model_path = model
        self.gpuid=[1,2]  # 修改后使用数组的形式即可 [0],[0,2,3]等
        self.bert_file = model + 'pytorch_model.bin'
        self.bert_config_file = model + 'config.json'
        self.vocab_file = model + 'vocab.txt'

        self.use_origin_bert = 'weight'  # 'ori':使用原生bert, 'dym':使用动态融合bert,'weight':初始化12*1向量
        self.is_avg_pool = 'mean'  # dym, max, mean, cls
        self.model_type = 'bilistm'  # bilstm; bigru

        self.rnn_num = 2
        self.flooding = 0
        self.embed_name = 'bert.embeddings.word_embeddings.weight'  # 词
        self.restore_file = None
        self.gradient_accumulation_steps = 1
        # 模型预测路径
        self.checkpoint_path = "/data1/home/fzq/projects/nlpclassification/data/mdecinedata/Savemodel/runs_[2, 3]/1631393203/model_0.9776_0.9776_0.9776_9464.bin"
        # self.checkpoint_path = "/data1/home/fzq/projects/nlpclassification/data/Savemodel/runs_0/1624199990/model_dist.bin"

        """
        实验记录
        """
