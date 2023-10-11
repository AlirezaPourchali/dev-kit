# pip install kafka-python
from kafka import KafkaProducer

# connect a PRODUCER

producer = KafkaProducer(bootstrap_servers=['<service_name>:9092'], api_version=(2,0,1) , security_protocol="SASL_PLAINTEXT", sasl_mechanism="SCRAM-SHA-256" , sasl_plain_username="<username>(user1)" , sasl_plain_password="<password>")

# sending strings 

string = bytes("test_string" , 'utf-8')

producer.send( '<topic_name>' , string )

# close connection
producer.flush()


# connect a CONSUMER and print messages
# set 'group_id' and 'auto_offset_reset' to 'earliest' if you want to continue from where the consumer left off before

from kafka import KafkaConsumer 

consumer = KafkaConsumer('<topic_name>' , group_id='<something>'  ,bootstrap_servers=['<service_name>:9092'], api_version=(2,0,1) , security_protocol='SASL_PLAINTEXT', sasl_mechanism='SCRAM-SHA-256' , sasl_plain_username='<username>(user1)' , sasl_plain_password='<password>' , auto_offset_reset='earliest' ) 

# NOTE: this loop(for) will hang forever until an error is occurred

for i in consumer:
    print(i.value.decode('utf-8'))

# download with wget ( messages are links )

import wget
for i in consumer:
    link = i.value.decode('utf-8')
    name = "test_download"
    wget.download(link , out=f"/tmp/{name}")


