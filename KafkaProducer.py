import random
import time
from confluent_kafka import Producer
import json

# Set up the Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092', # Your Kafka server address
}

# Create the producer with the above configuration
producer = Producer(conf)

# Device IDs
device_ids = [f'device_{i}' for i in range(10)] # 10 unique devices

# Latitude and Longitude range (This example is roughly centered on Toronto, Canada)
lat_range = (43.70, 43.75)
long_range = (-79.42, -79.37)

# Speed range (in km/h)
speed_range = (0, 120)

while True:
    data_point = {
        'device_id': random.choice(device_ids),
        'timestamp': time.time(), # Current time in seconds since the Unix Epoch
        'latitude': random.uniform(*lat_range),
        'longitude': random.uniform(*long_range),
        'speed': random.uniform(*speed_range),
    }
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_point)

    # Produce and send the data to the Kafka topic
    producer.produce('your_kafka_topic', json_data)

    # Wait for any outstanding messages to be delivered and delivery reports to be acknowledged.
    producer.flush()

    time.sleep(1) # Pause for a second before generating the next data point
