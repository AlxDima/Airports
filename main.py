from flask import Flask, render_template, Response
import illustrator as illustrator
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import db
import util
import sql_creator
import numpy as np
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
mydb = db.Database()
import datetime

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index.html')
def index():
    return render_template("index.html")


# FLIGHTS/
@app.route('/flights.html')
def flights():
    return render_template("flights.html")


# FLIGHTS/totalFlights
@app.route('/totalFlights.html')
def totalFlights():
    return render_template("totalFlights.html")


@app.route('/totalFlights.png')
def totalFlights_png():
    total_flights = []
    data = mydb.get(sql_creator.select_count_from("month", "flights", "month"))
    for i in range(12):
        total_flights.append(data[i][1])
    fig = illustrator.flights_per_months_total(total_flights)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# FLIGHTS/totalFlightsF
@app.route('/totalFlightsF.html')
def totalFlightsF():
    return render_template("totalFlightsF.html")


@app.route('/totalFlightsF.png')
def totalFlightsF_png():
    total_flights = []
    origins = ["EWR", "JFK", "LGA"]
    flights = [[], [], []]
    data = mydb.get(sql_creator.select_count_from("month", "flights", "month"))
    for i in range(12):
        total_flights.append(data[i][1])
    data = mydb.get(sql_creator.select_two_count_from("month", "origin", "flights", "origin", "month"))
    for i in range(len(data)):
        for origin in origins:
            if origin == data[i][1]:
                flights[origins.index(origin)].append(data[i][2])
    fig = illustrator.flights_per_months_freq(total_flights, flights)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# FLIGHTS/totalFlightsFS
@app.route('/totalFlightsFS.html')
def totalFlightsFS():
    return render_template("totalFlightsFS.html")


@app.route('/totalFlightsFS.png')
def totalFlightsFS_png():
    total_flights = []
    origins = ["EWR", "JFK", "LGA"]
    flights = [[], [], []]
    data = mydb.get(sql_creator.select_count_from("month", "flights", "month"))
    for i in range(12):
        total_flights.append(data[i][1])
    data = mydb.get(sql_creator.select_two_count_from("month", "origin", "flights", "origin", "month"))
    for i in range(len(data)):
        for origin in origins:
            if origin == data[i][1]:
                flights[origins.index(origin)].append(data[i][2])
    fig = illustrator.flights_per_months_stacked(total_flights, flights)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# FLIGHTS/totalFlightsSP
@app.route('/totalFlightsSP.html')
def totalFlightsSP():
    return render_template("totalFlightsSP.html")


@app.route('/totalFlightsSP.png')
def totalFlightsSP_png():
    total_flights = []
    origins = ["EWR", "JFK", "LGA"]
    flights = [[], [], []]
    data = mydb.get(sql_creator.select_count_from("month", "flights", "month"))
    for i in range(12):
        total_flights.append(data[i][1])
    data = mydb.get(sql_creator.select_two_count_from("month","origin","flights","origin","month"))
    for i in range(len(data)):
        for origin in origins:
            if origin == data[i][1]:
                flights[origins.index(origin)].append(data[i][2])
    fig = illustrator.flights_per_months_percentage(total_flights,flights)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# FLIGHTS/flightsTop10
@app.route('/flightsTop10.html')
def flightsTop10():
    return render_template("flightsTop10.html")


@app.route('/flightsTop10.png')
def flightsTop10Table():
    dest = []
    total_visits = []
    flights = [[], [], []]
    origins = ["'JFK'", "'EWR'", "'LGA'"]
    data = [item[0] for item in mydb.get(sql_creator.select_from("dest", "flights"))]
    unique, counts = np.unique(data, return_counts=True)
    y = np.argsort(counts)
    for i in range(1, 11):
        dest.append(unique[y[len(y)-i]])
        total_visits.append(counts[y[len(y)-i]])
    for origin in origins:
        for destination in dest:
            flights[origins.index(origin)].append(len(mydb.get(sql_creator.select_all_from_where_string_and("flights", "origin", origin, "dest", destination))))
    fig = illustrator.top_10_table(dest, total_visits, flights, origins)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# FLIGHTS/airtime
@app.route('/airtime.html')
def airtime():
    return render_template("airtime.html")


@app.route('/airtime.png')
def airtime_png():
    origins = ["EWR", "JFK", "LGA"]
    mean_air_time = []
    for origin in origins:
        data = mydb.get_item_0(sql_creator.select_from_where_string("air_time", "flights", "origin", origin))
        mins = [(item // 100)*60 + (item % 100) for item in data]
        am = np.mean(mins)
        print(am)
        h = int(am//60)
        m = int((am-h*60)//1)
        s = int((int((am-h*60-m)*100)*60)/100)
        mean_air_time.append(datetime.time(h,m,s))
    print(mean_air_time)
    fig = illustrator.manufac_200(origins, mean_air_time)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# FLIGHTS/delays
@app.route('/delays.html')
def delays():
    return render_template("delays.html")


@app.route('/delays.png')
def delays_png():
    origins = ["EWR", "JFK", "LGA"]
    arr_delay = []
    dep_delay = []
    
    delays = [[]]
    for origin in origins:
        print(origin)
        data = mydb.get_item_0(sql_creator.select_from_where_string("arr_delay", "flights", "origin", origin))
        arr_delay.append(util.avg_time(data))
        data = mydb.get_item_0(sql_creator.select_from_where_string("dep_delay", "flights", "origin", origin))
        dep_delay.append(util.avg_time(data))
    delays.append(arr_delay)
    delays.append(dep_delay)
    print(arr_delay)
    print(dep_delay)
    fig = illustrator.table3(arr_delay, dep_delay)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



# TEMPERATURE/
@app.route('/temperature.html')
def temperature():
    return render_template("temperature.html")


# TEMPERATURE/temperature3x
@app.route('/temperature3x.html')
def temperature3x():
    return render_template("temperature3x.html")


@app.route('/temperature3x.png')
def temperature3x_png():
   # get temp at JFK
    JFK_temps = [util.F_to_C(item)for item in mydb.get_item_0(sql_creator.select_from_where_string("temp", "weather", "origin", "JFK" ))]
    mess_JFK = len(JFK_temps)
    # get JFK measurements timestamps
    dates_JFK = util.datetime_format(mydb.get_item_0(sql_creator.select_from_where_string("time_hour", "weather", "origin", "JFK" )))
    # get temp at EWR
    EWR_temps = [util.F_to_C(item)for item in mydb.get_item_0(sql_creator.select_from_where_string("temp", "weather", "origin", "EWR" ))]
    mess_EWR = len(EWR_temps)
    # get EWR measurements timestamps
    dates_EWR = util.datetime_format(mydb.get_item_0(sql_creator.select_from_where_string("time_hour", "weather", "origin", "EWR" )))
    # get temp at LGA
    LGA_temps = [util.F_to_C(item)for item in mydb.get_item_0(sql_creator.select_from_where_string("temp", "weather", "origin", "LGA" ))]
    mess_LGA = len(LGA_temps)
    # get LGA measurements timestamps
    dates_LGA = util.datetime_format(mydb.get_item_0(sql_creator.select_from_where_string("time_hour", "weather", "origin", "LGA" )))
    fig = illustrator.temperature_orig(dates_JFK, dates_EWR, dates_LGA, JFK_temps, EWR_temps, LGA_temps, mess_EWR, mess_JFK, mess_LGA)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# TEMPERATURE/temperatureJFK
@app.route('/temperatureJFK.html')
def temperatureJFK():
    return render_template("temperatureJFK.html")


@app.route('/temperatureJFK.png')
def temperatureJFK_png():
    JFK_temps = [util.F_to_C(item)for item in mydb.get_item_0(sql_creator.select_from_where_string("temp", "weather", "origin", "JFK" ))]
    dates_JFK = util.datetime_format(mydb.get_item_0(sql_creator.select_from_where_string("time_hour", "weather", "origin", "JFK" )))
    fig = illustrator.all_JFK_temp(JFK_temps, dates_JFK)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# TEMPERATURE/temperaturedailyMeanJFK
@app.route('/temperaturedailyMeanJFK.html')
def temperaturedailyMeanJFK():
    return render_template("temperatureDailyMeanJFK.html")


@app.route('/daily_temps_JFK.png')
def daily_temps_JFK_plot():
    temps = [util.F_to_C(item[0]) for item in mydb.get(sql_creator.select_avg_from_group_by_2("temp", "weather", "origin", "'JFK'", "month", "day"))]
    date = mydb.get(sql_creator.select_2_distinct_from("month", "day", "weather"))
    dates = util.datetime_format([datetime.datetime(year=int(2013), month=int(item[0]), day=int(item[1])) for item in date])
    fig = illustrator.daily_temps_JFK(temps, dates)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# TEMPERATURE/temperatureDailyMean3x
@app.route('/temperatureDailyMean3x.html')
def temperatureDailyMean3x():
    return render_template("temperatureDailyMean3x.html")


@app.route('/temperatureDailyMean3x.png')
def temperatureDailyMean3x_plot():
    JFK_temps = [util.F_to_C(item[0]) for item in mydb.get(sql_creator.select_avg_from_group_by_2("temp", "weather", "origin", "'JFK'", "month", "day"))]
    EWR_temps = [util.F_to_C(item[0]) for item in mydb.get(sql_creator.select_avg_from_group_by_2("temp", "weather", "origin", "'EWR'", "month", "day"))]
    LGA_temps = [util.F_to_C(item[0]) for item in mydb.get(sql_creator.select_avg_from_group_by_2("temp", "weather", "origin", "'LGA'", "month", "day"))]
    date = mydb.get(sql_creator.select_2_distinct_from("month", "day", "weather"))
    days = util.datetime_format([datetime.datetime(year=int(2013), month=int(item[0]), day=int(item[1])) for item in date])
    fig = illustrator.daily_temps_plot(JFK_temps, EWR_temps, LGA_temps, days)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# MANUFACTURERS/
@app.route('/manufac.html')
def manufac():
    return render_template("manufac.html")


# MANUFACTURERS/200 MORE
@app.route('/manufac200planes.html')
def manufac200planes():
    return render_template("manufac200planes.html")


@app.route('/manufac200.png')
def manufac200():
    temp = mydb.get_item_0(sql_creator.select_from("manufacturer", "planes"))
    manufacturers, no_of_planes = util.unique_elem_from_2dim_arr(temp)
    big_manufacturers = []
    big_no_of_planes = []
    for i in range(len(no_of_planes)):
        if(no_of_planes[i] > 200):
            big_manufacturers.append(manufacturers[i])
            big_no_of_planes.append(no_of_planes[i])
    fig = illustrator.manufac_200(big_manufacturers, big_no_of_planes)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# MANUFACTURERS/FLIGHTS 200 MORE
@app.route('/manufac200planesFlights.html')
def manufac200planesFlights():
    return render_template("manufac200planesFlights.html")


@app.route('/manufac200flights.png')
def manufac200flights():
    temp = mydb.get_item_0(sql_creator.select_from("manufacturer", "planes"))
    manufacturers, no_of_planes = util.unique_elem_from_2dim_arr(temp)
    big_manufacturers = []
    no_of_flights = []
    for i in range(len(no_of_planes)):
        if(no_of_planes[i] > 200):
            big_manufacturers.append(manufacturers[i])
    for i in range (len(big_manufacturers)):
            temp = mydb.get_item_0(sql_creator.select_tailnum(big_manufacturers[i]))
            no_of_flights.append(sum(temp))    
    
    fig = illustrator.manufac_200(big_manufacturers, no_of_flights)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# MANUFACTURERS/AIRBUS
@app.route('/manufacAIRbus.html')
def manufacAIRbus():
    return render_template("manufacAIRbus.html")

@app.route('/manufacAIRBUS.png')
def manufacAIRBUS():
    sql = """ SELECT  model, COUNT(model)  FROM planes WHERE manufacturer='AIRBUS' GROUP BY model""" 
    temp = mydb.get(sql)
    models = [item[0] for item in temp]
    no_of_models = [item[1] for item in temp]
    fig = illustrator.airbus_mod(models, no_of_models)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
