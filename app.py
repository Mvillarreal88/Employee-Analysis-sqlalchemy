import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement


# Calculate the date one year from the last date in data set.
one_year_recent = dt.date(2017,8,23) - dt.timedelta(days=365)

#temperature information for the most active station
most_active = 'USC00519281'


# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Weather API!"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the data and precipitation scores
    precip_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_recent).all()

    session.close()

    # Convert list of tuples into a dictionary
    precip_dict = dict(precip_scores)

    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)


    # Perform a query to retrieve the unique stations
    stations = session.query(Measurement.station).distinct().all()


    session.close()

    # Convert list of tuples into normal list
    stations_list = list(stations)

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    station_active = session.query(Measurement.date,  Measurement.tobs,Measurement.prcp).filter(Measurement.date >= one_year_recent).filter(Measurement.station==most_active).order_by(Measurement.date).all()

    session.close()

    # Create list
    station_info = []
    for date, prcp, tobs in station_active:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["prcp"] = prcp
        tobs_dict["tobs"] = tobs
        
        station_info.append(tobs_dict)


    return jsonify(station_info)

# Start and end date

@app.route("/api/v1.0/<start>/<end>")
def Start_end_date(start, end):

    # Session link
    session = Session(engine)

    # Query
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>= start).filter(Measurement.date<= end).all()


    session.close()

    # Create list for results
    start_end_list = []
    for min, avg, max in results:
        start_end_date_dict = {}
        start_end_date_dict["min_temp"] = min
        start_end_date_dict["max_temp"] = max
        start_end_date_dict["avg_temp"] = avg

        start_end_list.append(start_end_date_dict) 

    return jsonify(start_end_list)

##############################################  

if __name__ == '__main__':
    app.run(debug=True)
