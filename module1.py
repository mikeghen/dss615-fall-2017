
filename = 'inpatient_payments_data.csv'
index = 0

with open(filename, 'r') as inpatient_payments_data:
    for datum in inpatient_payments_data:
        values = datum.split(',')

        if index == 0:
            header_1 = values[-1]
            header_2 = values[-2]
            header_3 = values[-3]
        else:
            value_1 = float(values[-1].replace('$',''))
            value_2 = float(values[-2].replace('$',''))
            value_3 = float(values[-3].replace('$',''))

        index++
        
        print value_1, value_2, value_3
