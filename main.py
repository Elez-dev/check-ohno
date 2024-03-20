import time
import sys
import requests
from web3 import Web3
from loguru import logger

logger.remove()
logger.add("./data/log.txt")
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")


def get_data():
    res = requests.get('https://ohno.wtf/airdrop.json')
    return res.json()


def main(address_list):
    total_point = 0
    prescale = 4500
    data = get_data()
    for address in address_list:
        # address = Web3.to_checksum_address(address)
        if address in data:
            point_quantitu = prescale * data[address]
            logger.success(f'{address}: {point_quantitu}')
            total_point += point_quantitu

    time.sleep(1)
    print()
    logger.success(f'Total points: {total_point}')


if __name__ == '__main__':
    with open("address.txt", "r") as f:
        list1 = [row.strip() for row in f]

    main(list1)
