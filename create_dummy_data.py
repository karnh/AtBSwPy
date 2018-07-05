import random
import os

# Offer List
offers = ['BP_GIGA', 'READYROAM_A', 'READYROAM_B', 'EASY_MOBILE_L', 'EASY_MOBILE_S', 
          'EASY_MOBILE_M', 'EASY_MOBILE_XL', 'SILVER_COMBO_1', 'SILVER_COMBO_2', 'YOUTH_COMBO_1', 
          'YOUTH_COMBO_2', 'YOUTH_COMBO_3', 'YOUTH_COMBO_6', 'COMBO_1', 'COMBO_2', 
          'COMBO_3', 'COMBO_6', 'COMBO_12', 'SIMONLY_5G', 'SIMONLY_3G']

# Output file
file = open('provData.txt', 'w')

# Initial values
hourly_count = 34
subscriber_id = 456700000

for day in range(19,26):
    for hour in range(0,24):
        if not hour:
            hourly_count = random.randint(33,43) 
        elif hour <= 11:
            hourly_count = hourly_count+1  
        else:
            hourly_count = hourly_count-1

        for rec_num in range(hourly_count):
            minute = random.randint(0,59)
            subscriber_id += 1
            if rec_num < 15:
                offerId = offers[rec_num % 4]
            else:
                offerId = offers[minute//3]
            
            date = '201806' + str(day) + str(hour).rjust(2,'0') + str(minute).rjust(2,'0') + str(rec_num).rjust(2,'0')

            file.write('INEAISOAP_addSubscriptionRequest|' + date + '||eer31w8|All procedures executed successfully.|0|' + 
                    str(subscriber_id) + '|' + str(subscriber_id) + '10332152985600010|' + offerId + '||||||||||\n')

print('finished')
file.close()