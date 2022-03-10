from sklearn.preprocessing import StandardScaler
import numpy as np
class RowsNormalizer:
    @staticmethod
    def getNpNormalizedNpRows(npRows: np.ndarray) -> np.ndarray:
        # Scale data to have zero mean and unit variance
        scaler = StandardScaler()
        scaler.fit(npRows)
        npRows = scaler.transform(npRows)

        return npRows