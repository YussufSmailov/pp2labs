import datetime as d
cur=d.datetime.now()
a=cur.replace(microsecond=0)
print(a)