import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

class Pollution:
    def __init__(self,data):
        self.data = data
        self.model = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None

    def split_data(self):
        x = self.data.drop(columns = ["pm2.5", "date","Is" , "Ir","cbwd_NW","cbwd_SE","cbwd_cv"])
        y = self.data["pm2.5"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(x, y, test_size = 0.15, random_state= 42)
        print('Data split for training')

    def train_model(self):
        if self.X_train is None or self.y_test is None:
            raise ValueError('data not prepared.')
        self.model = GradientBoostingRegressor(n_estimators=500, max_depth= 10,
                                        min_samples_split= 5, min_samples_leaf= 2, random_state= 42)
        self.model.fit(self.X_train, self.y_train)
        print('model trained')

        joblib.dump(self.model, filename ='DataAnalysisQuipux\Model\model_rfr.pkl')

    
    def evaluate_model(self):
        if self.model is None: 
            raise ValueError('model does not train')
        
        y_pred = self.model.predict(self.X_test)
        mean_abs_error = mean_absolute_error(self.y_test, y_pred)
        mean_sq_error = mean_squared_error(self.y_test, y_pred)

        print(f"Evaluation: \nMean Absolute Error: {mean_abs_error} \nMean Squared Error: {mean_sq_error}")


                            