import mysql.connector
class House:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="Home")
            print(self.con)
        except:
            print('Failed to connect the database')
    def create(self,id,name,members,place,gender):
        try:
            cursor=self.con.cursor()
            query='insert into house(id,name,members,place,gender)values(%s,%s,%s,%s,%s)'
            data=(id,name,members,place,gender)
            cursor.execute(query,data)
            self.con.commit()
        except:
            print('failed to create')

    def read(self):
        try:
            cursor=self.con.cursor()
            query='select * from house'
            cursor.execute(query,)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print('no records found')
        except:
            print('failed to read all records')
    def retrieve(self,id):
        cursor = self.con.cursor()
        query='select * from house where id = %s'
        data=(id,)
        cursor.execute(query,data)
        record=cursor.fetchone()
        if record:
            print(record)
        else:
            print('no record found')
    def update(self,name,members,place,gender,id):
        cursor=self.con.cursor()
        query='update house set name=%s,members=%s,place=%s,gender=%s where id =%s'
        data=(name,members,place,gender,id)
        cursor.execute(query,data)
        self.con.commit()
        if cursor.rowcount>0:
            print('updated successfully')
        else:
            print('no record found')
    def delete(self,id):
        cursor=self.con.cursor()
        query='delete from house where id = %s'
        data=(id,)
        cursor.execute(query,data)
        self.con.commit()
        if cursor.rowcount>0:
            print('deleted succsefully')
        else:
            print('no record found')
h=House()
while(1):
    print('1 for create')
    print('2 for retrieve')
    print('3 for reading')
    print('4 for update')
    print('5 for delete')
    print('6 for exiting')
    ch=int(input('enter your choice'))
    if ch==1:
        id=int(input('enter the id'))
        name=input('enter the name')
        members=int(input('enter the number members'))
        place=input('enter the place name')
        gender=input('enter the gender from the option(male,female)')
        h.create(id,name,members,place,gender)
    elif ch==2:
        h.read()
    elif ch==3:
        id=int(input('enter the id'))
        h.retrieve(id)
    elif ch==4:
        id=int(input('enter the id'))
        name=input('enter the name')
        members=int(input('enter the number members'))
        place=input('enter the place name')
        gender=input('enter the gender from the option(male,female)')
        h.update(name,members,place,gender,id)
    elif  ch==5:
        id=int(input('enter the id'))
        h.delete(id)
    elif ch==6:
        exit()
    # else:
    #     print('invalid input')

