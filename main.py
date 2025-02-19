from DataClean.dataClean import Data
from Model.model import Pollution

def main():
    data_extract = Data("DataAnalysisQuipux\Data\data.txt")
    data_extract.load_data()
    data_extract.clean_data()
    data = data_extract.get_data()

    prediction = Pollution(data)
    prediction.split_data()
    prediction.train_model()
    prediction.evaluate_model()

if __name__ == "__main__":
    main()
