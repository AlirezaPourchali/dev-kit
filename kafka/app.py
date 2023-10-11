# pip install kafka-python
from kafka import KafkaProducer

# connect a PRODUCER

producer = KafkaProducer(bootstrap_servers=['<service_name>:9092'], api_version=(2,0,1) , security_protocol="SASL_PLAINTEXT", sasl_mechanism="SCRAM-SHA-256" , sasl_plain_username="<username>(user1)" , sasl_plain_password="<password>")

# sending strings 

string = bytes("test_string" , 'utf-8')

producer.send( '<topic_name>' , string )

# close connection
producer.flush()

# 
