from database.db_connector import get_db_connection

def insert_metrics_to_db(metrics):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO device_metrics (device_id, metric_name, metric_value, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (metrics["device_id"], "cpu_usage", metrics["cpu_usage"], metrics["timestamp"]))
        
        cursor.execute("""
            INSERT INTO device_metrics (device_id, metric_name, metric_value, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (metrics["device_id"], "memory_usage", metrics["memory_usage"], metrics["timestamp"]))
        
        conn.commit()
    except Exception as e:
        print(f"Error inserting metrics: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
