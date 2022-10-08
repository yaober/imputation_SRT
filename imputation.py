import stlearn as st
import numpy as np
from scipy.sparse import csr_matrix
adata_h5 = st.Read10X(path=r'./', count_file='151676'+'_filtered_feature_bc_matrix.h5' )
#<class 'scipy.sparse._csr.csr_matrix'> to numpy
data = adata_h5.X.toarray().astype(np.float64) #csr to dense
#data = np.array([[0,0,1],[0,1,1],[0,2,1]])
print("XXXXXXXXXXXXXXXXx")
cnt_zero =  (np.count_nonzero(data))/(data.shape[0] * data.shape[1])
print("data: \n", data,"\n", data.shape)
print("cnt_zero: ", cnt_zero)
data_bool = np.where(data != 0., 1., 0.)
data_sum_percol = data_bool.sum(axis=0)
print("data_sum_percol: ", data_sum_percol)
data_sum_percol[data_sum_percol == 0] = 999.
data_mean = data.sum(axis = 0) / data_sum_percol
print("data_mean: ", data_mean)
data_bool_reverse = ~(data_bool.astype(np.bool_))
result = data_mean * data_bool_reverse.astype(np.float64)
result = data + result
k = csr_matrix(result, dtype=np.float64)
adata_h5.X = k

#check
print("###############check###################")
r_cnt_zero = result.shape[0] * result.shape[1] - np.count_nonzero(result)
print("result: \n", result,"\n", result.shape)
print("r_cnt_zero: ", r_cnt_zero)
r_mean = result.mean(axis = 0)

assert((r_mean - data_mean).sum() < 1e-10)
s = k.toarray().astype(np.float64)

assert((s!=result).sum()==0)



