import datetime as d
print("Yesterday: ", d.datetime.now()-d.timedelta(1))
print("Today: ", d.datetime.now())
print("Tomorrow: ", d.datetime.now()+d.timedelta(1))