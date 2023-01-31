import random
#part A
weeks=16
print(weeks, type(weeks))
classes=4
print(classes,type(classes))
tuition=4200
print(tuition, type(tuition))
cost_per_week=((tuition / classes)/ weeks)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
classes_per_week=9
print(classes_per_week,type(classes_per_week))
cost_per_class=(cost_per_week/classes_per_week)
print(cost_per_class, type(cost_per_class))
print("Cost per class", cost_per_class)
#part B
random.randint(1,10)
listlab1=["hello",17,3.32,"lab1","47"]
randomlab1=random.choice(listlab1)
print(randomlab1)