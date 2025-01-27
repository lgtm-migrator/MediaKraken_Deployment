import asyncio
import json

import aio_pika


# grabs the messages and processes

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process(ignore_processed=True):
        try:
            json_message = json.loads(message.body)
            print(json_message)
        except json.decoder.JSONDecodeError as e:
            print('json error:', message.body)
            await message.reject()
            return
        await message.ack()
        await asyncio.sleep(1)


async def main(loop):
    content_providers = 'themoviedb'

    # start up rabbitmq
    connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1/", loop=loop)
    # Creating a channel
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)
    # Declaring exchange
    exchange = await channel.declare_exchange(name='mkque_metadata_ex',
                                              type=aio_pika.ExchangeType.DIRECT,
                                              durable=True)
    # Declaring queue
    queue = await channel.declare_queue(name=content_providers,
                                        durable=True)
    # Binding queue
    await queue.bind(exchange=exchange, routing_key='mkque_metadata_ex')
    # Start listening
    await queue.consume(on_message)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(main(loop))

    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(connection.close())
