import pandas as pd
import os

class Data:
    def __init__(self, file_path):
        """
        Clase para la carga, limpieza y preprocesamiento de datos.
        Parámetros:
        file_path (str): Ruta del archivo con los datos.
        """
        self.file_path = file_path
        self.df = None
        self.null_values = None
    
    def load_data(self):
        """
        Carga los datos desde un archivo en formato CSV y los almacena en un DataFrame.
        Lanza un error si el archivo no se encuentra en la ruta especificada.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("File %s not found" % self.file_path)
        self.df = pd.read_csv(self.file_path)
        print("Data loaded")

    def clean_data(self):
        """
        Realiza la limpieza y preprocesamiento de los datos:
        1. Crea una columna "date" a partir de las columnas "year", "month", "day" y "hour".
        2. Almacena los valores nulos en "pm2.5" antes de la imputación.
        3. Elimina las columnas de fecha originales para evitar redundancia.
        4. Interpola los valores nulos de "pm2.5" utilizando un método lineal.
        5. Convierte la variable categórica "cbwd" en variables dummy.
        """
        self.df["date"] = pd.to_datetime(self.df[["year","month","day","hour"]])
        self.null_values = self.df[self.df["pm2.5"].isnull()].copy()
        self.df.drop(columns=["year","month","day","hour"], inplace= True)
        self.df["pm2.5"] = self.df["pm2.5"].interpolate(method="linear",limit_direction="both")
        self.df = pd.get_dummies(self.df, columns=["cbwd"], drop_first= True)
        print("Data cleaned")
        print(self.df)

    def get_data(self):
        """
        Devuelve el DataFrame con los datos procesados.
        Lanza un error si los datos no han sido cargados previamente.
        """
        if self.df is None:
            raise ValueError("Data not loaded")
        return self.df
    
    def null_values_data(self):
        """
        Devuelve un DataFrame con los registros que contenían valores nulos en "pm2.5" antes de la interpolación.
        """
        return self.null_values