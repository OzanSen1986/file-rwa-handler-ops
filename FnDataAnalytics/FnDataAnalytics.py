from datetime import datetime, date
from uuid import UUID, uuid4
import json
import os
from typing import Literal, Any, Optional, Iterator
from pathlib import Path
import logging
from dataclasses import dataclass, field


FILE_PATH = Path('basicLogFile.csv')
ORDERS = Path('order_details.csv')

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", filename=FILE_PATH)

def current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")

@dataclass
class Customer:
    id: UUID
    name: str
    quantity: int
    price: float
    grade: int
    modify_date: str = field(default_factory=current_date)

def data_entry(path: Path, cust: Customer) -> None:
    with path.open('a') as f:
        f.write(f"{cust.id},{cust.name},{cust.quantity},{cust.price},{cust.grade},{cust.modify_date}\n")
    logging.info(f'Data added to the file: {cust.id}, {cust.name} on {cust.modify_date}')


def read_file(path: Path) -> Iterator[Customer]:
    try:
        with path.open('r') as f:
            for line in f:
                id, name, quantity, price, grade, modify_date = line.strip().split(",")
                yield Customer(id, name, int(quantity), float(price), int(grade), modify_date)
        logging.info(f"logging records added to the file: {FILE_PATH}")
    except FileNotFoundError:
        logging.warning(f'File: {FILE_PATH} not exists!')
        return iter([])


def main() -> Iterator[Customer]:

    # data_entry(ORDERS, Customer(uuid4(),'FSG-79',24, 35.99, 2))
    # data_entry(ORDERS, Customer(uuid4(), 'SCD-6342',160, 12.45, 3))
    # data_entry(ORDERS, Customer(uuid4(), 'XXDGS', 220, 14.99, 2))
    # data_entry(ORDERS, Customer(uuid4(), 'CCSS-XX', 200, 124.99, 1))
    # data_entry(ORDERS, Customer(uuid4(), 'MDS-LL56', 125, 99.99, 2))
    # data_entry(ORDERS, Customer(uuid4(), 'OMR-5642', 95, 19.99, 1))

    order_details=list(read_file(ORDERS))

    for item in order_details:
        print(f"ID 🪪  {item.id} ,Item 🍏 : {item.name}, Grade 🧪: {item.grade}")

    Grade_1_Total = sum(item.quantity for item in order_details if item.grade == 1)
    Grade_2_Total = sum(item.quantity for item in order_details if item.grade == 2)
    Grade_3_Total = sum(item.quantity for item in order_details if item.grade == 3)

    Grade_1_Total_Price = sum(item.quantity * item.price for item in order_details if item.grade == 1)
    Grade_2_Total_Price = sum(item.quantity * item.price for item in order_details if item.grade == 2)
    Grade_3_Total_Price = sum(item.quantity * item.price for item in order_details if item.grade == 3)

    Total_Product_Number = len(order_details)

    print(f'Summary Below: \n')

    print('-->')
    print(f'Grade 1 Total_Quantity: {Grade_1_Total}')
    print(f'Grade 2 Total_Quantity: {Grade_2_Total}')
    print(f'Grade 3 Total_Quantity: {Grade_3_Total}')
    print('-->')
    print(f'Grade 1 Total_Price: ${Grade_1_Total_Price:,.2f}')
    print(f'Grade 2 Total_Price: ${Grade_2_Total_Price:,.2f}')
    print(f'Grade 3 Total_Price: ${Grade_3_Total_Price:,.2f}')
    print('-->')
    print(f'Total Number of Products: {Total_Product_Number}')
    

if __name__ == "__main__":
    main()