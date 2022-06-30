import numpy as np


class Distance:
    @staticmethod
    def getGaussianKullbackLieblerDistance(m0, S0, m1, S1)->float:
        # store inv diag covariance of S1 and diff between means
        N = m0.shape[0]
        iS1 = np.linalg.inv(S1)
        diff = m1 - m0

        # kl is made of three terms
        tr_term = np.trace(iS1 @ S0)
        det_term = np.log(np.linalg.det(S1) / np.linalg.det(S0))  # np.sum(np.log(S1)) - np.sum(np.log(S0))
        quad_term = diff.T @ np.linalg.inv(S1) @ diff  # np.sum( (diff*diff) * iS1, axis=1)
        # print(tr_term,det_term,quad_term)
        return .5 * (tr_term + det_term + quad_term - N)