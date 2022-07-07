initDate = 'May 01, 1998'

Month = ''
Date = ''
Year = ''
def stripDateData():
    if ',' in (initDate[(len(Month)):(len(Month)+3)]):
        Date = initDate[(len(Month)+1)]
    else:
        Date = initDate[(len(Month)+1):(len(Month)+3)]
    return Date

if 'January' in initDate:
    Month = 'January'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'February' in initDate:
    Month = 'February'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'March' in initDate:
    Month = 'March'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'April' in initDate:
    Month = 'April'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'May' in initDate:
    Month = 'May'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'June' in initDate:
    Month = 'June'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'July' in initDate:
    Month = 'July'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'August' in initDate:
    Month = 'August'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'September' in initDate:
    Month = 'September'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'October' in initDate:
    Month = 'October'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'November' in initDate:
    Month = 'November'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()
elif 'December' in initDate:
    Month = 'December'
    Year = initDate[(len(initDate)-4):(len(initDate))]
    Date = stripDateData()

if len(Date) < 2:
    print('{}-{}-0{}'.format(Year, Month, Date))
else:
    print('{}-{}-{}'.format(Year, Month, Date))
