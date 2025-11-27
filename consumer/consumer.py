import pika
import time
import json
from bson import ObjectId
from database import books_collection

RABBIT_URL = "amqp://guest:guest@rabbitmq:5672/"


def connect():
    while True:
        try:
            params = pika.URLParameters(RABBIT_URL)
            connection = pika.BlockingConnection(params)
            print("[Consumer] Conectado ao RabbitMQ!")
            return connection
        except Exception as e:
            print(f"[Consumer] Falha ao conectar. Tentando novamente em 5s... ({e})")
            time.sleep(5)

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    book_id = message.get("book_id")

    print(f"[Consumer] Mensagem recebida: {message}")

    valid = False

    try:
        obj = ObjectId(book_id)
        found = books_collection.find_one({"_id": obj})
        valid = found is not None
    except:
        valid = False

    response = { "valid": valid }

    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        ),
        body=json.dumps(response)
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)



def start():
    while True:
        connection = connect()
        channel = connection.channel()

        channel.queue_declare(queue="validate_book_queue")

        channel.basic_consume(
            queue="validate_book_queue",
            on_message_callback=callback,
        )

        print("[Consumer] Aguardando mensagens...")
        
        try:
            channel.start_consuming()
        except Exception as e:
            print(f"[Consumer] Erro no consuming. Reiniciando... ({e})")
            time.sleep(3)

if __name__ == "__main__":
    start()
