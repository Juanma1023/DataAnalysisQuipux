import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

class Pollution:
    def __init__(self,data):
        """
        Clase para modelar la polucion.
        Parámetros:
        data (DataFrame): DataFrame con los datos de entrenamiento.
        """
        self.data = data
        self.model = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None

    def split_data(self):
        """
        Divide los datos en conjuntos de entrenamiento y prueba.
        Se eliminan las columnas irrelevantes antes de la división.
        """
        x = self.data.drop(columns = ["pm2.5", "date","Is" , "Ir","cbwd_NW","cbwd_SE","cbwd_cv"])
        y = self.data["pm2.5"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(x, y, test_size = 0.15, random_state= 42)
        print("Data split for training")

    def train_model(self):
        """
        Entrena el modelo Gradient Boosting Regressor.
        """
        if self.X_train is None or self.y_test is None:
            raise ValueError("data not prepared.")
        self.model = GradientBoostingRegressor(n_estimators=500, max_depth= 10,
                                        min_samples_split= 5, min_samples_leaf= 2, random_state= 42)
        self.model.fit(self.X_train, self.y_train)
        print("model trained")

    def evaluate_model(self):
        """
        Evalúa el modelo con datos de prueba y calcula métricas de error.
        """
        if self.model is None: 
            raise ValueError("model does not train")
        
        y_pred = self.model.predict(self.X_test)
        mean_abs_error = mean_absolute_error(self.y_test, y_pred)
        mean_sq_error = mean_squared_error(self.y_test, y_pred)

        print(f"Evaluation: \nMean Absolute Error: {mean_abs_error} \nMean Squared Error: {mean_sq_error}")

    def prediction_test(self, new_data):
        """
        Realiza una predicción con nuevos datos de entrada.
        Retorna el Valor predicho de "pm2.5".
        """
        new_data = pd.DataFrame([new_data])
        predictions = self.model.predict(new_data)[0]
        return predictions