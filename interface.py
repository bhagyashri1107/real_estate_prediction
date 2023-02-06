from flask import Flask, render_template, jsonify, request
import config
from utils import Real_estate
from werkzeug.datastructures import MultiDict
import traceback
app = Flask(__name__)

@app.route('/')
def home():
    return render_template ("text.html")
    


@app.route('/predict_rate', methods = ["GET","POST"])
def predict_rate():
    try:
        if request.method == "POST":
            data = request.form.get

            
            No = int(data('No'))
            transaction_date = eval(data('transaction_date'))
            house_age = eval(data('house_age'))
            distance_to_the_nearest_MRT_station = eval(data('distance_to_the_nearest_MRT_station'))
            number_of_convenience_stores=eval(data('number_of_convenience_stores'))
            latitude = eval(data('latitude'))
            longitude = eval(data('longitude'))

            Real_estate_rate= Real_estate(No,transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude)
            
            rate = Real_estate_rate.get_predicted_rate()

            return  render_template("text.html",prediction= rate)
           
        else:
            data = request.args.get
            No = int(data('No'))
            transaction_date = eval(data('transaction_date'))
            house_age = eval(data('house_age'))
            distance_to_the_nearest_MRT_station = eval(data('distance_to_the_nearest_MRT_station'))
            number_of_convenience_stores=eval(data('number_of_convenience_stores'))
            latitude = eval(data('latitude'))
            longitude = eval(data('longitude'))
            
            

            Real_estate_rate= Real_estate(No,transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude)

            rate = Real_estate_rate.get_predicted_rate()

            return  render_template("text.html",prediction= rate)

    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})           


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5003,debug=False)