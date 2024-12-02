from flask import Blueprint, render_template
from web_application.models import Metrics
from web_application import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def display_metrics():
    metrics = Metrics.query.order_by(Metrics.timestamp.desc()).all()
    return render_template('metrics.html', metrics=metrics)
