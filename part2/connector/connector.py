import asyncio
from contextlib import asynccontextmanager
import json
import logging

from confluent_kafka import Consumer
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

TOPIC = 'metrics'
TEST = 'test'
TIMEOUT = 1
metrics = {}
priorities = []
lock = asyncio.Lock()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info('metrics consumer started')

conf = {
    "group.id": 'metrics',
    "bootstrap.servers": "kafka-0:9092,kafka-1:9092,kafka-2:9092",
    "auto.offset.reset": "latest",
    "enable.auto.commit": "true",
    "fetch.min.bytes": 512,
}

consumer = Consumer(conf)
consumer.subscribe([TOPIC, TEST])


def gen_str(metrics: dict) -> str:
    strs = []
    for key, value in metrics.items():
        schema = f"# HELP {value['Name']} {value['Description']}\n# TYPE {value['Name']} {value['Type']}\n{value['Name']} {value['Value']} "
        strs.append(schema)
    return '\n'.join(strs)


async def read_metrics(consumer: Consumer) -> None:
    try:
        while True:
            msg = consumer.poll()

            if msg is None:
                continue
            if msg.error():
                logger.error(f'получена ошибка: {msg.error()}')
                continue

            logger.info(f'полученое сообщение: {msg.value().decode("utf-8")} из топика {msg.topic()}')

            
            if msg.topic() == TOPIC:
                async with lock:
                    global metrics
                    metrics = msg.value().decode("utf-8")
            if msg.topic() == TEST:
                async with lock:
                    global priorities
                    priorities.append(msg.value().decode("utf-8"))

            break

    except Exception as e:
        logger.error(f'поймана ошибка: {e}')

    #finally:
    #    consumer.close()


async def run_scheduler(consumer: Consumer):
    while True:
        await read_metrics(consumer)
        await asyncio.sleep(TIMEOUT)


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(
        run_scheduler(consumer)
    )

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    if priorities:
        pr_json = gen_str(json.loads(priorities.pop(0)))
        return pr_json
    metrics_dict = json.loads(metrics)
    return gen_str(metrics_dict)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
