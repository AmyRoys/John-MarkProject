from web_application import db

class Metrics(db.Model):
    __tablename__ = 'device_metrics'
    
    device_id = db.Column(db.String(255), primary_key=True)  # Matches character varying(255)
    cpu_usage = db.Column(db.Float)  # Remove nullable=False to align with schema
    memory_usage = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)  # Matches timestamp without time zone
    metric_name = db.Column(db.String(50))  # Matches character varying(50)
    metric_value = db.Column(db.String(50))
