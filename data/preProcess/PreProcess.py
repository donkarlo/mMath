from sklearn.preprocessing import StandardScaler
import numpy as np
class PreProcess:
    @staticmethod
    def getNpNormalizedNpData(npData: np.ndarray) -> np.ndarray:
        # Scale data to have zero mean and unit variance
        scaler = StandardScaler()
        scaler.fit(npData)
        npData = scaler.transform(npData)

        return npData