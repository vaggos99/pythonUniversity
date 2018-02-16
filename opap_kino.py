import urllib
import json
import datetime
import urllib.request

def compare_lists():
    s=0
    for i in range(10):
        for j in range(20):
            if numbers[i]==tmp[j]:
                s+=1
    if s>4:
        s=1
    else:
        s=0
    return s



now=datetime.date.today()
year=now.year
month=now.month
days=(now - datetime.date(year,month, 1)).days
numbers=[]
for i in range(10):
    num=int(input('give me a number:'))
    while num<0 or num>80:
        num=int(input('give me a number between 0 and 80:'))
    for j in range(i):
        if num==numbers[j]:
            num=int(input('give me a different number:'))
            
    numbers.append(num)
koina=[]
imera=[]
for i in range(days):
    now=now-datetime.timedelta(days=1)
    date=now.strftime('%d-%m-%Y')
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date
    with urllib.request.urlopen(url) as response:
        html = response.read()
    data=json.loads(html)
   
    dedomena=data['draws']['draw']
    r=0
    imera.append(now)
    for k in dedomena:
        tmp=k['results']
        r+=compare_lists()
    koina.append(r)
a=koina.index(max(koina))
print('Στις '+str(imera[a])+' θα ειχες τις περισσοτερες επιτυχιες')
    
    

