initDate = 'May 26, 2022'

Month = ''
Date = ''
Year = ''
if 'January' in initDate:
    Month = 'January'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'February' in initDate:
    Month = 'February'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'March' in initDate:
    Month = 'March'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'April' in initDate:
    Month = 'April'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'May' in initDate:
    Month = 'May'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'June' in initDate:
    Month = 'June'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'July' in initDate:
    Month = 'July'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'August' in initDate:
    Month = 'August'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'September' in initDate:
    Month = 'September'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'October' in initDate:
    Month = 'October'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'November' in initDate:
    Month = 'November'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
elif 'December' in initDate:
    Month = 'December'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]

if len(Date) < 2:
    print('{}-{}-0{}'.format(Year, Month, Date))
else:
    print('{}-{}-{}'.format(Year, Month, Date))
