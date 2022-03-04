## **模型** 
![模型图](model-%E9%BB%91%E7%99%BD.png)
## **介绍** ：

1. 基于双重情感感知的可解释性谣言检测，
在模型中分别利用Bi-LSTM和attention提取谣言语义特征与评论情感特征，
再利用CNN提取提取谣言情感特征和用户评论情感特征，
最后利用两次co-attention学习两者的协同表示，
最后将所有特征连接分类
## **架构** ：
#1.emotional embedding
文件是情感嵌入的预训练模型，源代码发布在 https://github.com/armintabari/Emotional-Embedding，
源代码是在python2 的环境下，此文件中是python3的环境下可运行代码。
情感预训练模型的数据可以在源代码链接中找到。
源论文：Seyeditabari, A., Tabari, N., Gholizadeh, S., & Zadrozny, W. (2019). Emotional Embeddings: Refining Word Embeddings to Capture Emotional Content of Words. arXiv preprint arXiv:1906.00112., 
#2.model.py
文件中是所有模型的类，部分代码是引用dEFEND模型的代码
#3.train.py
训练函数，输出一般性评价标准，并给出混淆矩阵
4#.utils.py
数据处理，对数据进行截断，补全等。
#5.config.py
参数设置，主要包括文件路径，文本长度，个数，learn_rate等参数设置1. 