from confluent_kafka import Producer, Consumer
import socket


conf = {'bootstrap.servers': '192.168.88.103:9092',
        'client.id': socket.gethostname()}

producer = Producer(conf)
consumer = Consumer({'bootstrap.servers': '192.168.88.103:9092', 'group.id': 'foo'})


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


def write_message(item):
    producer.produce('TutorialTopic', value=item, callback=acked)
    producer.poll(0.001)
