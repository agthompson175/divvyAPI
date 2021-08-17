from flask import Blueprint, jsonify, request
from .models import Data
from datetime import datetime as dt

main = Blueprint('main', __name__)

@main.route('/')
def landing():
    return "hello world, <br> please enter / calculate with your parameters example: <br>/calculate?starts=2013-06-28&ends=2013-06-30&from_station_id=85" 

@main.route('/calculate', methods=['GET'])
def calculate():
    starts = dt.strptime(request.args.get('starts'), '%Y-%m-%d')
    ends = dt.strptime(request.args.get('ends'), '%Y-%m-%d')
    from_station_id = request.args.get('from_station_id')
    
    if from_station_id:
        from_station_name = Data.query.filter(
            Data.from_station_id == from_station_id).first().from_station_name
        valid_rows = Data.query.filter(Data.from_station_id == from_station_id, Data.start >= starts, Data.end <= ends).all()
    else:
        valid_rows = Data.query.filter(Data.start >= starts, Data.end <= ends).all()
    avg_duration = sum(record.trip_duration for record in valid_rows) / len(valid_rows)

    if from_station_id:
        return jsonify({
            'averageDuration': avg_duration,
            'fromStationId': from_station_id,
            'fromStationName': from_station_name
        })
    else:
        return jsonify({
            'averageDuration': avg_duration
        })
