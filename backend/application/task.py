from sympy import re
from application.workers import celery
from datetime import datetime
import csv
import time


@celery.task()
def generate_csv(input):
    with open(
        "/Downloads/Mad2_Project/TrackerInfo.csv",
        "w",
        encoding="utf8",
        newline="",
    ) as output_file:
        output = csv.DictWriter(output_file, fieldnames=input[0].keys(), restval="")
        output.writeheader()
        output.writerows(input)
    return "CSV Generated"
