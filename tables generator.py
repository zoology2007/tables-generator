print("Welcome to tables generator, where you can learn tables")
tables = int (input ("which number do you want the tables of?"))
for i in range(1,100000):
    print(tables,"*",i ,"=",tables*i)