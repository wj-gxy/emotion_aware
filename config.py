import argparse
import inspect
import torch


class Config:
    word2vec_file = 'embedding/numberbatch-en.txt'
    emotion_file = 'embedding/counter_fitted_vector_space-0.txt'
    train_file = 'dataset/twitter15-2/train.json'
    valid_file = 'dataset/twitter15-2/valid.json'
    test_file = 'dataset/twitter15-2/test.json'
    saved_model = 'model/best_model.pt'
    device = torch.device("cuda:0")
    # device = torch.device("cpu")
    train_epochs = 200
    batch_size = 32
    learning_rate = 0.001
    learning_rate_decay = 0.99
    l2_regularization = 0.001
    content_count = 1  # max count of content
    content_length = 32  # max count of content words
    comment_count = 12  # max count of user comments
    review_length = 32  # max count of review words
    lowest_review_count = 5  # Minimum number of comments for users to keep
    PAD_WORD = '<UNK>'
    require_improvment = 1000

    fm_hidden = 10  # Hidden dim of Factorization Machine

    class_list = ['false', 'true']  # 推特15,16的2分类

    def __init__(self):
        attributes = inspect.getmembers(self, lambda a: not inspect.isfunction(a))
        attributes = list(filter(lambda x: not x[0].startswith('__'), attributes))

        parser = argparse.ArgumentParser()
        for key, val in attributes:
            parser.add_argument('--' + key, dest=key, type=type(val), default=val)
        for key, val in parser.parse_args().__dict__.items():
            self.__setattr__(key, val)
