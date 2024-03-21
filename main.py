import time
import sys
import json
from loguru import logger

logger.remove()
logger.add("./data/log.txt")
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")


def main(address_list):
    total_point = 0
    prescale = 4500
    data = json.load(open('addr.json', 'r'))
    for address in address_list:
        if address.lower() in data:
            point_quantitu = prescale * data[address.lower()]
            logger.success(f'{address}: {point_quantitu}')
            total_point += point_quantitu

    time.sleep(1)
    print()
    logger.success(f'Total points: {total_point}')


if __name__ == '__main__':
    with open("address.txt", "r") as f:
        list1 = [row.strip() for row in f]

    main(list1)
