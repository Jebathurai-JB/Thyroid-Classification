import json
import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://jebathurai:7010333275jb@cluster0.irlqnsu.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"D:\PROJECTS\IneuronProject\Energy-Efficiency\energy_efficiency_data.csv")
DATABASE_NAME = "Ineuron_project"
COLLECTION_NAME = "Energy_Efficiency"


if __name__ == "__main__":
	df = pd.read_csv(DATA_FILE_PATH)
	print(f'rows and columns: {df.shape}')

	json_record = list(json.loads(df.T.to_json()).values())
	print(json_record[0])

	client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)