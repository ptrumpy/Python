from tkinter import *
from tkinter import ttk
import psycopg2
import sys


class Employee:

    def __init__(self, wind):
        self.wind = wind
        self.wind.title('Employees')

        frame = LabelFrame(self.wind, text="Add New Record")
        frame.grid(row=0, column=1)

        Label(frame, text='Name:').grid(row=1, column=1)
        self.name = Entry(frame)
        self.name.grid(row=1, column=2)

        Label(frame, text='Age:').grid(row=2, column=1)
        self.age = Entry(frame)
        self.age.grid(row=2, column=2)

        Label(frame, text='Designation:').grid(row=3, column=1)
        self.designation = Entry(frame)
        self.designation.grid(row=3, column=2)

        Label(frame, text='Salary:').grid(row=4, column=1)
        self.salary = Entry(frame)
        self.salary.grid(row=4, column=2)

        ttk.Button(frame, text='Add Record',command = self.adding).grid(row=5, column=2)
        self.message = Label(text='', fg='red')
        self.message.grid(row=5, column=0)

        self.tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3', '#4'))
        self.tree.grid(row=6, column=0, columnspan=5)
        self.tree.heading('#1', text='Name', anchor=W)
        self.tree.heading('#2', text='Age', anchor=W)
        self.tree.heading('#3', text='Designation', anchor=W)
        self.tree.heading('#4', text='Salary', anchor=W)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=200)
        self.tree.column('#4', stretch=NO, minwidth=0, width=200)

        ttk.Button(text='Delete Record').grid(row=7, column=0)
        ttk.Button(text='Edit Record').grid(row=7, column=1)

        self.viewing_records()

    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * from pd.emp_data'
        with psycopg2.connect(user="postgres",
                              password="Erj020912",
                              host="127.0.0.1",
                              port="5432",
                              database="Dev") as conn:
            cur = conn.cursor()
            cur.execute(query)

        for row in cur:
            self.tree.insert('', 'end', values=row)
        cur.close()
        conn.close()

    def validation(self):
        return len(self.name.get()) != 0 and len(self.age.get()) !=0 and len(self.designation.get()) !=0 and len(self.salary.get()) !=0

    def adding(self):
        if self.validation():
            query = 'Insert into pd.emp_data(name, age, designation, salary) VALUES(%s,%s,%s,%s)'
            parameters = (self.name.get(), int(self.age.get()), self.designation.get(), int(self.salary.get()),)
            with psycopg2.connect(user="postgres",
                                  password="Erj020912",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Dev") as conn:
                cur = conn.cursor()
                cur.execute(query, parameters)
        else:
            self.message['text'] = 'Not all fields are filled in'
        self.viewing_records()



if __name__ == '__main__':
    wind = Tk()
    application = Employee(wind)
    wind.mainloop()
