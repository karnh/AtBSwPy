#! python3

import random, datetime

NUM_DAYS = 14
DAY_START=16
OFFERIDS = {'1':{'name': 'BP_GIGA',         'type': 'postpaid', 'weight': 100}, 
            '2':{'name': 'READYROAM_A',     'type': 'postpaid', 'weight': 90}, 
            '3':{'name': 'READYROAM_B',     'type': 'postpaid', 'weight': 95}, 
            '4':{'name': 'EASY_MOBILE_L',   'type': 'postpaid', 'weight': 60}, 
            '5':{'name': 'EASY_MOBILE_S',   'type': 'postpaid', 'weight': 60}, 
            '6':{'name': 'EASY_MOBILE_M',   'type': 'postpaid', 'weight': 30}, 
            '7':{'name': 'EASY_MOBILE_XL',  'type': 'postpaid', 'weight': 30}, 
            '8':{'name': 'SILVER_COMBO_1',  'type': 'postpaid', 'weight': 15}, 
            '9':{'name': 'SILVER_COMBO_2',  'type': 'postpaid', 'weight': 15}, 
            '10':{'name': 'YOUTH_COMBO_1',  'type': 'postpaid', 'weight': 10}, 
            '11':{'name': 'YOUTH_COMBO_2',  'type': 'postpaid', 'weight': 10}, 
            '12':{'name': 'YOUTH_COMBO_3',  'type': 'postpaid', 'weight': 15}, 
            '13':{'name': 'YOUTH_COMBO_6',  'type': 'postpaid', 'weight': 5}, 
            '14':{'name': 'COMBO_1',        'type': 'postpaid', 'weight': 8}, 
            '15':{'name': 'COMBO_2',        'type': 'postpaid', 'weight': 9}, 
            '16':{'name': 'COMBO_3',        'type': 'postpaid', 'weight': 9}, 
            '17':{'name': 'COMBO_6',        'type': 'postpaid', 'weight': 9}, 
            '18':{'name': 'COMBO_12',       'type': 'postpaid', 'weight': 9},
            '19':{'name': 'SIMONLY_3G',     'type': 'postpaid', 'weight': 9},
            '20':{'name': 'SIMONLY_5G',     'type': 'postpaid', 'weight': 9}, 
            '21':{'name': 'HISIM_8',        'type': 'prepaid',  'weight': 0}, 
            '22':{'name': 'HISIM_15',       'type': 'prepaid',  'weight': 0}, 
            '23':{'name': 'HISIM_38',       'type': 'prepaid',  'weight': 0}, 
            '24':{'name': 'HISIM_50',       'type': 'prepaid',  'weight': 0}, 
            '25':{'name': 'HIDATA',         'type': 'prepaid',  'weight': 0}, 
            '26':{'name': 'HITOURIST_1',    'type': 'prepaid',  'weight': 0}, 
            '27':{'name': 'HITOURIST_2',    'type': 'prepaid',  'weight': 0}, 
            '28':{'name': 'HITOURIST_3',    'type': 'prepaid',  'weight': 0}}

randomListInput = []

for id, offer in OFFERIDS.items():
    randomListInput += [id] * offer['weight']

mdn = 7474000000

cdrFile = open('cdrData.csv', 'w')

for day in range(NUM_DAYS):
    for hour in range(24):

        if hour > 8 and hour < 16:
            countsPerHour = random.randint(97,107)
        else:
            countsPerHour = random.randint(90,100)

        for recnum in range(countsPerHour):
            minute = random.randint(0,59)
            date = '201806' + str(DAY_START + day) + str(hour).zfill(2) + str(minute).zfill(2) + str(minute).zfill(2)
            date_timestamp = int(datetime.datetime.strptime(date, '%Y%m%d%H%M%S').replace(tzinfo=datetime.timezone.utc).timestamp())
            mdn += 1
            subsId = 'SI0005_12211_' + str(mdn)
            offerId = random.choice(randomListInput)
            offerName = OFFERIDS[str(offerId)]['name']
            usgIn = random.randint(0, 10000)
            usgOut = random.randint(50000, 100000)
            if random.randint(1,100) < 5:
                isRoaming = 'Y'
            else:
                isRoaming = 'N'

            cdrFile.write('1|' + str(offerId) + 
                    '||' + subsId + '23352152778240010|DomesticDataTeraBalance&Ec5@1530374400;' + subsId + ';1527782400||' +
                    str(mdn) + '||' + subsId + '|postpaid|1|' + str(date_timestamp) + '|' + str(date_timestamp) + 
                    '|c4-10-252-245-82-bdkepgolp.singtel.com;' + str(date_timestamp) + ';240|203.126.1.179|52801|103.1.85.178|3657464260|mvne-olp|66888|66888|0||#|' + 
                    isRoaming + '|Zone0||' + str(usgIn + usgOut) + '|' + str(usgIn) + '|' + str(usgOut) + 
                    '||3946492.000000000000|||IMEISV|ST0||2||mvne-olp|||||UPDATE_REQUEST||2001||\n')

cdrFile.close()
print('done')