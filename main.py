from DataClean.dataClean import Data
from Model.model import Pollution

data_extract = Data("DataAnalysisQuipux\Data\data.txt")
data_extract.data_load()
data_extract.data_clean()
data = data_extract.data_get()

prediction = Pollution(data)
prediction.data_split()
prediction.model_train()
prediction.model_evaluate()
