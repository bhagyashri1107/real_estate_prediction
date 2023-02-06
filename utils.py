import pickle
import json
import config
import numpy as np
from werkzeug.datastructures import MultiDict
import warnings
warnings.filterwarnings('ignore')


class Real_estate():

    def __init__(self, No,transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude) :
        self.No = No
        self.transaction_date= transaction_date
        self.house_age = house_age
        self.distance_to_the_nearest_MRT_station = distance_to_the_nearest_MRT_station
        self.number_of_convenience_stores= number_of_convenience_stores
        self.latitude=latitude
        self.longitude= longitude
        

    def __load_model(self):
        
        with open(r'artifacts/linear_reg.pkl', 'rb') as f:
            self.model = pickle.load(f)
           

        # Load Project Data 
        with open(r'artifacts/project_data.json','r') as f:
            self.project_data = json.load( f)
            



    def get_predicted_rate(self): 
        self.__load_model()
        test_array = np.zeros((1,self.model.n_features_in_))
        test_array[0][0] = self.No
        test_array[0][1] = self.transaction_date
        test_array[0][2] = self.house_age
        test_array[0][3] = self.distance_to_the_nearest_MRT_station
        test_array[0][4] = self.number_of_convenience_stores
        test_array[0][5] = self.latitude
        test_array[0][6] = self.longitude
       


        # print("Test Array is :",test_array)

        predicted_rate = np.around(self.model.predict(test_array)[0],3)
        # print("Home Rate :", predicted_rate)
        return predicted_rate

if __name__ == '__main__':
    cls =Real_estate(1,2023.98,23.22,23.41,12.2,12.3,87.54)
    prediction = cls.get_predicted_rate()
    print(prediction)
    
