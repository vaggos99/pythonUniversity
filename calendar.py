import datetime
try:
    year=int(input('give me the year:'))
except ValueError:
    print('give me an intiger')
try:
    month=int(input('give me the month:'))
except ValueError:
    print('give me an intiger')
date=datetime.date(year,month,1)
print(date.strftime('%B %Y'))
print('S'.ljust(3),'M'.ljust(3),'T'.ljust(3),'W'.ljust(3),'T'.ljust(3),'F'.ljust(3),'S'.ljust(3))
#βρησκω ποσες μερες εχει ο μηνας
days=(datetime.date(year, month+1, 1) - datetime.date(year,month, 1)).days
#βρησκω ποια μερα ειναι η 1η του μηνα
day_first=date.weekday()
#τοποθετω την πρωτη μερα στο ημερολογιο
if day_first==0:
    print(' '.ljust(3),date.strftime('%d').ljust(3),end=' ')
    x=2
elif day_first==1:
    print(' '.ljust(3),' '.ljust(3),date.strftime('%d').ljust(3),end=' ')
    x=3
elif day_first==2:
    print(' '.ljust(3),' '.ljust(3),' '.ljust(3),date.strftime('%d').ljust(3),end=' ')
    x=4
elif day_first==3:
    print(' '.ljust(3),' '.ljust(3),' '.ljust(3),' '.ljust(3),date.strftime('%d').ljust(3),end=' ')
    x=5
elif day_first==4:
    print(' '.ljust(3),' '.ljust(3),' '.ljust(3),' '.ljust(3),' '.ljust(3),date.strftime('%d').ljust(3),end=' ')
    x=6
elif day_first==5:
    print(' '.ljust(3),' '.ljust(3),' '.ljust(3),' '.ljust(3),' '.ljust(3),' '.ljust(3),date.strftime('%d').ljust(3),end=' ')
    x=7
elif day_first==6:
    print(date.strftime('%d').ljust(3),end=' ')
    x=1
#τοποθετω και τις υπολοιπες μερες
for i in range(2,days+1):
    date=date+datetime.timedelta(days=1)
    if x%7==0:
        print('')
    print(date.strftime('%d').ljust(3),end=' ')
    x+=1
    
    


