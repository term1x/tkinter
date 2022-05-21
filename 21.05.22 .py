import tkinter
from tkinter import ttk


Data = [(3, 'm1hag', 17450, 12), (4, 'adamrus', 4100, 8), (5, 'hayastan', 460000, 17), (6, 'govnar', 1000, 2), (7, 'term1x', 7629, 15), (8, 'term1x', 7629, 15), (9, 'term1x', 7629, 15), (10, 'term1x', 7629, 15), (11, 'm1hag', 2450, 12), (12, 'adamrus', 4100, 8), (13, 'hayastan', 10000, 17), (14, 'govnar', 1000, 2), (15, 'term1x', 2353, 23), (16, 'm1hag', 2353, 23), (17, 'adamrus', 4456, 50), (18, 'adamrus', 7000, 23), (19, 'govnar', 4068, 24), (20, 'govnar', 1000, 2), (21, 'govnar', 1000, 2)]
def fill_table(user_table , data):
    for i in range(len(data)):
        User_table.insert(parent='', index='end', iid=i, text='', values=(data[i]))





WIDTH = 1200
HEIGHT = 600

master=tkinter.Tk()
canvas = tkinter.Canvas(master , bg='#FFFFFF',
                        width=WIDTH,height=HEIGHT)

master.geometry('1000x400')
frame = tkinter.Frame(master)
frame.pack()
User_table = ttk.Treeview(frame)
User_table['columns'] = ('id' , 'name' , 'cash' , 'year')
User_table.pack()
User_table.heading('id' , text = 'id')
User_table.heading('name' , text = 'name')
User_table.heading('cash' , text = 'cash')
User_table.heading('year' , text = 'year')
User_table.column('#0' , width = 0)
Search_button = tkinter.Button(text = 'Найти' , width = 12 , height = 2 )
Search_button.config(command = fill_table(User_table , Data))

search = ''
Search_entry = tkinter.Entry(textvariable = search)
#fill_table(User_table, Data)
Search_entry.pack()
Search_button.pack()
canvas.pack()
master.mainloop()
