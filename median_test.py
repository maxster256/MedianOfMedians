# median_tests.py
from median_of_medians import MedianOfMedians
import random
import time

select = MedianOfMedians()

data = []
for i in range(10000):
    data.append(random.randrange(2000))

start = time.time()
result = select.median_of_medians(data, 50)
end = time.time()

print("Result: {}, elapsed time: {} seconds".format(result, end-start))
