cur=con.cursor()
cur.executr('''select first_name,last_name,salary from rmployee order by salary desc;''')
emp=cur.fetchall()
n=int(input('enter value of n:'))
print(emp[n-1])
