import boto3
import json

class GraphUtils:

    @classmethod
    def makeGraphItems(cls, items):
        units = []
        for item in items:
            units.append({'Option':item['Option']['S'], 'Total': int(item['Total']['N'])})

        return units


