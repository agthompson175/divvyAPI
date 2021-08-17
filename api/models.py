from . import db


class Data(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String(50))
    trip_duration = db.Column(db.Integer)
    
