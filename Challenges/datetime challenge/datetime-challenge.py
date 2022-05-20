import datetime
import pytz

portland = datetime.datetime.now()
newyork = datetime.datetime.now(pytz.timezone('America/New_York'))
london = datetime.datetime.now(pytz.timezone('Europe/London'))

pHour = portland.strftime("%H")
pTime = portland.strftime("%X")
if int(pHour) >= 8 and int(pHour) < 17:
    print("It is {} in Portland, we are currently open!".format(pTime))
else:
    print("It is {} in Portland, we are currently closed. :(".format(pTime))

nyHour = newyork.strftime("%H")
nyTime = newyork.strftime("%X")
if int(nyHour) >= 8 and int(nyHour) < 17:
    print("It is {} in New York, we are currently open!".format(nyTime))
else:
    print("It is {} in New York, we are currently closed. :(".format(nyTime))


lHour = london.strftime("%H")
lTime = london.strftime("%X")
if int(lHour) >= 8 and int(lHour) < 17:
    print("It is {} in London, we are currently open!".format(lTime))
else:
    print("It is {} in London, we are currently closed. :(".format(lTime))
