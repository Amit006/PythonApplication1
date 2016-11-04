import datetime

print(datetime.date.today())
currentDate=datetime.date.today()
print("hi there",currentDate.strftime('please Attend your event %A, %B %d in the year %Y') ) 
print(currentDate)
print(currentDate.month)
print(currentDate.year)
print("my new date is ",currentDate.strftime('%d %b %y'))
print(currentDate.isoformat())

#  birthday code
dateofbirth = str(input("enter your dateofbirth(mm/dd/yyyy)::"))
birthdate=datetime.datetime.strptime(dateofbirth,'%m/%d/%y')
print(birthdate) 
age_year = (currentDate.year - birthdate.year)
print(age_days)

