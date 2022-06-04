import random
from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple
from pympler import asizeof
import humanize

# 1000 instances of dataclass
@dataclass
class Sizetest_dataclass():
    x: int
    y: int
    z: int

dataclasses_1000 = []
for i in range(1000):
    dataclasses_1000.append(Sizetest_dataclass(
            x = random.randint(1000, 10000), 
            y = random.randint(1000, 10000),
            z = random.randint(1000, 10000)
    ))

# 1000 instances of namedtuple:
Sizetest_namedtuple = namedtuple('Sizetest_namedtuple', ['x', 'y', 'z'])

namedtuples_1000 = []
for i in range(1000):
    namedtuples_1000.append(Sizetest_namedtuple(
            x = random.randint(1000, 10000), 
            y = random.randint(1000, 10000),
            z = random.randint(1000, 10000)
    ))

# 1000 instances of NamedTuple:
class Sizetest_NT(NamedTuple):
    x: int
    y: int
    z: int

nt_typing_1000 = []
for i in range(1000):
    nt_typing_1000.append(Sizetest_NT(
            x = random.randint(10000, 100000), 
            y = random.randint(10000, 100000),
            z = random.randint(10000, 100000)
    ))
    
print(f'dataclasses size: {humanize.naturalsize(asizeof.asizeof(dataclasses_1000))}')
print(f'namedtuples size: {humanize.naturalsize(asizeof.asizeof(namedtuples_1000))}')
print(f'NamedTuples size: {humanize.naturalsize(asizeof.asizeof(nt_typing_1000))}')
