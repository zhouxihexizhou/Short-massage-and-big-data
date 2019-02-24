from time import time
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from scipy import sparse, io
from sklearn.decomposition import PCA


def dimensionality_reduction(training_data, test_data, type='pca'):
    if type == 'pca':
        t0 = time()
        pca1 = PCA(n_components=58, svd_solver='randomized', whiten=True)
        pca2 = PCA(n_components=58, svd_solver='randomized', whiten=True)
        pca1.fit(training_data)
        pca2.fit(test_data)
        print("done in %0.3fs" % (time() - t0))
        t0 = time()
        training_data_transform = sparse.csr_matrix(pca1.transform(training_data))
        test_data_transform = sparse.csr_matrix(pca2.transform(test_data))
        print("done in %0.3fs" % (time() - t0))
        #random_projections
        #feature_agglomeration
        return training_data_transform, test_data_transform



def split_data(content, label, new_content):
    training_data, test_data, training_target, test_target = train_test_split(
        content, label, test_size=0, random_state=0)
    test_data = new_content

    return training_data, test_data, training_target, test_target



def standardized_data(content, label):
    training_data, test_data, training_target, test_target = split_data(content, label)
    scalar = preprocessing.StandardScaler().fit(training_data)
    training_data_transformed = scalar.transform(training_data)
    test_data_transformed = scalar.transform(test_data)
    return training_data_transformed, test_data_transformed, training_target, test_target





