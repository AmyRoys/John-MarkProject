from collector_agent.pc_collector import collect_metrics
from collector_agent.uploader_queue import insert_metrics_to_db
from web_application import create_app

app = create_app()

def run_collector():
    """
    Collect metrics and insert them into the database.
    """
    device_id = "Device_1"
    metrics = collect_metrics(device_id)
    print(f"Collected Metrics: {metrics}")
    insert_metrics_to_db(metrics)
    print("Metrics inserted into the database!")

if __name__ == "__main__":
    # Run metrics collection logic
    run_collector()

    # Start the Flask web application
    app.run(host="0.0.0.0", port=5000)


