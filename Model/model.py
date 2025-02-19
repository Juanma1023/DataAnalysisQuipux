import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

class Pollution:
    def __init__(self,data):
        self.data = data
        self.model = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None

    def data_split(self):
        x = self.data.drop(columns = ["pm2.5", "date"])
        y = self.data["pm2.5"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(x, y, test_size = 0.2, random_state= 42)
        print('Data split for training')

    def model_train(self):
        if self.X_train is None or self.y_test is None:
            raise ValueError('data not prepared.')
        self.model = RandomForestRegressor(n_estimators=200, max_depth= 20,
                                        min_samples_split= 5, min_samples_leaf= 2, random_state= 42)
        self.model.fit(self.X_train, self.y_train)
        print('model trained')

        joblib.dump(self.model, filename ='DataAnalysisQuipux\Model\model_rfr.pkl')

    
    def model_evaluate(self):
        if self.model is None: 
            raise ValueError('model does not train')
        
        y_pred = self.model.predict(self.X_test)
        mean_abs_error = mean_absolute_error(self.y_test, y_pred)
        mean_sq_error = mean_squared_error(self.y_test, y_pred)

        print(f"evaluation: ")
        print(f"mean absolute error: {mean_abs_error}")
        print(f"mean squared error: {mean_sq_error}")

                            