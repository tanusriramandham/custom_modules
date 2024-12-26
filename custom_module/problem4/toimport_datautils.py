from data_utils import cal_mean,cal_median,cal_mode
import random
random_numbers=[random.randrange(0,1000) for i in range(10)]
print(random_numbers)

def cal_statistics(random_numbers):
    print(cal_mean(random_numbers))
    print(cal_median(random_numbers))
    print(cal_mode(random_numbers))


cal_statistics(random_numbers)