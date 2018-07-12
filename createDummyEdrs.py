#! python3
# createDummyData.py - create dummy edr records

import os, random, datetime

# Offer List
OFFERIDS = {'1' :{'name': 'POSTPAID_4G', 'type': 'postpaid', 'weight': 110},
            '2' :{'name': 'ROAM_A',      'type': 'postpaid', 'weight': 90},
            '3' :{'name': 'ROAM_B',      'type': 'postpaid', 'weight': 95},
            '4' :{'name': 'MOBILE_LG',   'type': 'postpaid', 'weight': 60},
            '5' :{'name': 'MOBILE_SM',   'type': 'postpaid', 'weight': 60},
            '6' :{'name': 'MOBILE_MD',   'type': 'postpaid', 'weight': 30},
            '7' :{'name': 'MOBILE_XL',   'type': 'postpaid', 'weight': 30},
            '8' :{'name': 'COMBO_8',     'type': 'postpaid', 'weight': 15},
            '9' :{'name': 'COMBO_9',     'type': 'postpaid', 'weight': 15},
            '10':{'name': 'COMBO_10',    'type': 'postpaid', 'weight': 10},
            '11':{'name': 'COMBO_11',    'type': 'postpaid', 'weight': 10},
            '12':{'name': 'COMBO_12',    'type': 'postpaid', 'weight': 15},
            '13':{'name': 'COMBO_13',    'type': 'postpaid', 'weight': 5},
            '14':{'name': 'COMBO_14',    'type': 'postpaid', 'weight': 8},
            '15':{'name': 'COMBO_15',    'type': 'postpaid', 'weight': 9},
            '16':{'name': 'COMBO_16',    'type': 'postpaid', 'weight': 9},
            '17':{'name': 'COMBO_17',    'type': 'postpaid', 'weight': 9},
            '18':{'name': 'COMBO_18',    'type': 'postpaid', 'weight': 0},
            '19':{'name': 'POSTPAID_3G', 'type': 'postpaid', 'weight': 0},
            '20':{'name': 'POSTPAID_5G', 'type': 'postpaid', 'weight': 0},
            '21':{'name': 'PRESIM_8',    'type': 'prepaid',  'weight': 80},
            '22':{'name': 'PRESIM_15',   'type': 'prepaid',  'weight': 65},
            '23':{'name': 'PRESIM_38',   'type': 'prepaid',  'weight': 10},
            '24':{'name': 'PRESIM_50',   'type': 'prepaid',  'weight': 2},
            '25':{'name': 'PREPAID_D',   'type': 'prepaid',  'weight': 5},
            '26':{'name': 'PREPAID_1',   'type': 'prepaid',  'weight': 0},
            '27':{'name': 'PREPAID_2',   'type': 'prepaid',  'weight': 0},
            '28':{'name': 'PREPAID_3',   'type': 'prepaid',  'weight': 0}}

offerSelectionList = []
for id, offer in OFFERIDS.items():
    offerSelectionList += [id] * offer['weight']

# Notification channel list
notifChannelSelectionList = ['SMS'] * 6 + ['EMAIL'] * 3 + ['GCM']

# Create provisioning EDR records
def writeProvRec(fileHandle, recDate, subsId, offerName):
    fileHandle.write('INEAISOAP_addSubscriptionRequest|' + recDate + '||eer31w8|All procedures executed successfully.|0|' + 
        str(subsId) + '|' + str(subsId) + '10332152985600010|' + offerName + '||||||||||\n')

# Create Notification EDR records
def writeNotifRec(fileHandle, recDate, subsId, offerName, offerType):
    channel = random.choice(notifChannelSelectionList)
    if channel == 'SMS':
        destination = subsId
    elif channel == 'EMAIL':
        destination = str(subsId) + '@example.com'
    else:
        destination = 'app'

    if random.randint(1,10) == 1:
        notifType = 'OFFER_EXPIRE_REMINDER'
    else:
        notifType = 'THR_NOTIF'

    fileHandle.write(channel + '|' + str(recDate) + '|140212990605056_1529936186|' + str(subsId) + '|' + str(subsId) + '|' + 
        offerType + '||' + str(destination) + '|' + notifType + '|' + offerName + '|986756458100025152614080010|||||||\n')

def createEdrs(outFile, type, recsPerHour, subsIdStart, recDayStart, recDayEnd=None):
    file = open(outFile, 'w')    
    subscriber_id = subsIdStart
    record_day = datetime.datetime.strptime(DAY_START, '%Y%m%d')
    if recDayEnd is not None:
        lastRecDay = datetime.datetime.strptime(recDayEnd, '%Y%m%d')
    else:
        lastRecDay = datetime.datetime.now()
    hourly_count = recsPerHour

    while record_day <= lastRecDay:
        for hour in range(24):
            if not hour:
                hourly_count = random.randint(recsPerHour - 2, recsPerHour + 3) 
            elif hour <= 11:
                hourly_count = hourly_count+1
            else:
                hourly_count = hourly_count-1

            for rec_num in range(hourly_count):
                minute = random.randint(0,59)
                record_date = record_day.strftime('%Y%m%d') + str(hour).zfill(2) + str(minute).zfill(2) + str(rec_num).zfill(2)

                subscriber_id += 1
                offerId = random.choice(offerSelectionList)
                offerName = OFFERIDS[offerId]['name']
                offerType = OFFERIDS[offerId]['type']

                if type == 'PROV':
                    writeProvRec(file, record_date, subscriber_id, offerName)
                elif type == 'NOTIF':
                    writeNotifRec(file, record_date, subscriber_id, offerName, offerType)
                else:
                    raise Exception('Unknown type: {}'.format(type))
        
        # Increment record day
        record_day = record_day + datetime.timedelta(days=1)
    
    # File generated. Close file.
    file.close()

# Output file
OUPUT_FILE = 'provData.txt'

# Initial values
HOURLY_COUNT = 34
SUBS_ID_START = 456700000
DAY_START = '20180601'      # YYYYMMDD
DAY_END = ''                # YYYYMMDD 

createEdrs('provData.txt', 'PROV', 34, SUBS_ID_START, DAY_START)
createEdrs('notifData.txt', 'NOTIF', 34, SUBS_ID_START, DAY_START)

print('finished')