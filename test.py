from DataClean.dataClean import Data
from Model.model import Pollution

# Cargar y limpiar los datos
extractor = Data("DataAnalysisQuipux\Data\data.txt")
extractor.load_data()
extractor.clean_data()
data = extractor.get_data()
null_rows = extractor.null_values_data()

# Entrenar y evaluar el modelo
predictor = Pollution(data)
predictor.split_data()
predictor.train_model()
predictor.evaluate_model()

#Realiza una copia de la base de datos con el fin de probar el modelo.
result_df = data.copy()

# Iterar sobre todas las filas del DataFrame
for i, row in result_df.iterrows():
    input_data = row.drop(["pm2.5", "date","Is" , "Ir","cbwd_NW","cbwd_SE","cbwd_cv"]).to_dict()
    predicted_value = predictor.prediction_test(input_data)
    result_df.at[i, "predicted_pm2.5"] = predicted_value  
    
# Reordenar columnas para que "predicted_pm2.5" esté junto a "pm2.5"
column_order = result_df.columns.tolist()
column_order.insert(column_order.index("pm2.5") + 1, column_order.pop(column_order.index("predicted_pm2.5")))
result_df = result_df[column_order]

# Guardar el DataFrame con las predicciones en un nuevo archivo
result_df.to_csv("result_test.csv", index=False)
