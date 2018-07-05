#!/bin/env python
import random
import string
import datetime
from calendar import monthrange

def create_random_alpha_key(key_len, key_case=None):
    key_list = [random.choice(string.ascii_letters + string.digits) for i in range(key_len)]
    if key_case is None:
        return "".join(key_list)
    if key_case is string.ascii_lowercase:
        return ("".join(key_list)).lower()
    if key_case is string.ascii_uppercase:
        return ("".join(key_list)).upper()


def create_random_num_key(key_len):
    key_list = [random.choice(string.digits) for i in range(key_len)]
    return "".join(key_list)


def get_random_value_from_list(key_list):
    rand_idx = random.randint(0, len(key_list) - 1)
    return key_list[rand_idx]

def generate_random_date_hhmiss(hours=None, minutes=None, seconds=None):
    if hours is None:
        hours = str(random.randint(0, 23)).zfill(2)
    if minutes is None:
        minutes = str(random.randint(0, 59)).zfill(2)
    if seconds is None:
        seconds = str(random.randint(0, 59)).zfill(2)
    return hours + minutes + seconds


def generate_random_date_yyyymmdd(day=None,month=None,year=None):
    if year is None:
        year = random.randint(1900,datetime.datetime.now().year)
    if month is None:
        month = random.randint(1,12)
    if day is None:
        day = random.randint(1,monthrange(year,month)[1])

    return str(year) + str(month).zfill(2) + str(day).zfill(2)

offer_names=['BP_GIGA', 'READYROAM_A', 'READYROAM_B', 'EASY_MOBILE_L', 'EASY_MOBILE_S', 
          'EASY_MOBILE_M', 'EASY_MOBILE_XL', 'SILVER_COMBO_1', 'SILVER_COMBO_2', 'YOUTH_COMBO_1', 
          'YOUTH_COMBO_2', 'YOUTH_COMBO_3', 'YOUTH_COMBO_6', 'COMBO_1', 'COMBO_2', 
          'COMBO_3', 'COMBO_6', 'COMBO_12', 'SIMONLY_5G', 'SIMONLY_3G']

Event_Type=['INEAISOAP_addSuibscriptionRequest', 'INEAISOAP_removeSubscriberRequest']

file = open('notifData.txt', 'w')

subscriber_id = 456700000
hourly_count = 80

for day in range(19,27):
    for hour in range(0,24):
        if not hour:
            hourly_count = random.randint(75,85) 
        elif hour <= 11:
            hourly_count = hourly_count+1  
        else:
            hourly_count = hourly_count-1

        print(day, hour, hourly_count)

        for rec_num in range(hourly_count):
            minute = random.randint(0,59)
            seconds = random.randint(0,59)
            subscriber_id += 1

            if rec_num < (hourly_count * 0.6):
                channel = 'SMS'
                destination = subscriber_id

                if rec_num < (hourly_count * 0.6 * 0.8):
                    type = 'postpaid'
                else:
                    type = 'prepaid'
            elif rec_num < (hourly_count * 0.9):
                channel = 'EMAIL'
                destination = str(subscriber_id) + '@example.com'

                if rec_num < (hourly_count * 0.3 * 0.8):
                    type = 'postpaid'
                else:
                    type = 'prepaid'
            else:
                channel = 'GCM'
                destination = 'app'

                if rec_num < (hourly_count * 0.1 * 0.8):
                    type = 'postpaid'
                else:
                    type = 'prepaid'

            if rec_num < hourly_count//2:
                offerId = offer_names[rec_num % 4]
            else:
                offerId = offer_names[minute//3]

            if random.randint(1,10) == 1:
                notif_type = 'OFFER_EXPIRE_REMINDER'
            else:
                notif_type = 'THR_NOTIF'
            
            date = '201806' + str(day) + str(hour).zfill(2) + str(minute).zfill(2) + str(seconds).zfill(2)

            file.write(channel + '|' + str(date) + '|140212990605056_1529936186|' + str(subscriber_id) + '|' + str(subscriber_id) + '|' + 
                  type + '||' + str(destination) + '|' + notif_type + '|' + offerId + '|986756458100025152614080010|||||||\n')

print('finished')
file.close()