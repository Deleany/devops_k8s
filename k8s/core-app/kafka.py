from confluent_kafka import Producer, Consumer, KafkaError, KafkaException
import socket
import sys

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


def read_message():
    try:
        consumer.subscribe(['TutorialTopic'])
        msg_count = 0
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                consumer.commit(asynchronous=False)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()
