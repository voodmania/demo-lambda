import os
import json

from logger import logger
from connection import Connection

INSERT = 'INSERT INTO demo ("campo_1", "campo_2", "campo_3") VALUES (%s, %s, %s);'

conn = Connection(os.environ)


def handler(event, context):  # pylint: disable=W0613
    "AWS Lambda processing entry point"

    status, output = 400, {}
    logger.info('handler() event: %s', event)

    campo_1 = event.get('campo_1', '')
    campo_2 = event.get('campo_2', '')
    campo_3 = event.get('campo_3', '')

    if campo_1 and campo_2 and campo_3:
        if conn.execute(INSERT, (campo_1, campo_2, campo_3)):
            status = 200
            output['campo_1'] = campo_1
            output['campo_2'] = campo_2
            output['campo_3'] = campo_3
        else:
            output['error'] = 'Error processing request'
    else:
        output['error'] = 'Missing params'

    return {
        'statusCode': status,
        'body': json.dumps(output),
    }
