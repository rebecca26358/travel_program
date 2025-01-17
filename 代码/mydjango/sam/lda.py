from sklearn.decomposition import LatentDirichletAllocation
import numpy


# 训练lda模型，返回文档主题矩阵
def lda_model(mat):
    print('开始训练lda模型')
    n_topic = 50
    lda = LatentDirichletAllocation(n_components=n_topic,
                                    max_iter=1000,
                                    learning_method='batch')
    docres = lda.fit_transform(mat)  # Document_word Sparse Matrix      返回文档主题矩阵

    # 困惑度
    print('困惑度为：' + lda.perplexity(mat))  # 收敛效果

    print(len(docres))  # 文档数目
    print(len(docres[0]))  # 主题数目
    print('lda模型训练结束')

    # 保存lda模型
    docres.dump('doc_topic_result.dat')

    return docres


def load_lda_doc():
    # 加载保存的文档主题矩阵
    print('加载lda文档主题矩阵')
    docres = numpy.load('mydjango/sam/doc_topic_result.dat', allow_pickle=True)  # 添加 allow_pickle=True
    return docres
