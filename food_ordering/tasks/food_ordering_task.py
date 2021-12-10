
from __future__ import absolute_import, unicode_literals

import kombu
from celery import shared_task, bootsteps
from food_ordering.celery import app
from food_ordering.services.subscriber_process import ProcessService


@shared_task
def publish_message(message):
    with app.producer_pool.acquire(block=True) as producer:
        producer.publish(
            message,
            exchange='exchange',
            routing_key='secret_key',
        )


class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):

        with app.pool.acquire(block=True) as conn:
            exchange = kombu.Exchange(
                name='exchange',
                type='direct',
                durable=True,
                channel=conn,
            )
            exchange.declare()

            queue = kombu.Queue(
                name='myqueue',
                exchange=exchange,
                routing_key='secret_key',
                channel=conn,
                message_ttl=600,
                queue_arguments={
                    'x-queue-type': 'classic'
                },
                durable=True
            )
            queue.declare()
        return [kombu.Consumer(channel,
                               queues=[queue],
                               callbacks=[self.handle_message],
                               accept=['json'])]

    def handle_message(self, body, message):
        res = ProcessService.process_order(body)
        if res:
            print('Order with id: %s is completed' % str(body['obj_id']))
            print('Received message: %s' % body)
        else:
            print('Order with id: %s is NOT completed' % str(body['obj_id']))
            print('Received message: %s' % body)
        message.ack()


app.steps['consumer'].add(MyConsumerStep)
