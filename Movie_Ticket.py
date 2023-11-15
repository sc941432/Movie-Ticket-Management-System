from tkinter import *
import mysql.connector


root=Tk()
root.title("Administrator")
conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')

c=conn.cursor()
'''c.execute("""CREATE TABLE movie_data(
        movie_id integer primary key,
        movie_name text ,
        release_date text,
        director text,
        producer text,
        actors text,
        duration text,
        rating text
        )""")'''
#first table
def submit():
    
    
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor() 
    c.execute("INSERT INTO movie_data values(%(movie_id)s,%(movie_name)s,%(release_date)s,%(director)s,%(producer)s,%(actors)s,%(duration)s,%(rating)s)",
            {
                'movie_id':movie_id.get(),
                'movie_name':movie_name.get(),
                'release_date':release_date.get(),
                'director':director.get(),
                'producer':producer.get(),
                'actors':actors.get(),
                'duration':duration.get(),
                'rating':rating.get()
            }
    )

    conn.commit()
    conn.close()

    movie_id.delete(0,END)
    movie_name.delete(0,END)
    release_date.delete(0,END)
    director.delete(0,END)
    producer.delete(0,END)
    actors.delete(0,END)
    duration.delete(0,END)
    rating.delete(0,END)


def display():
    print("Movie_ID , Movie name ,release date,director,producer,actor,duration,rating \n")
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    c.execute("SELECT * FROM movie_data")
    records=c.fetchall()
    print(records)
    print_records=''
   
    for record in records:
        print_records +=str(record) +"\n"
        #print_records +=str(record[0]) +" " + str(record[1]) + " " +str(record[6]) +"\n"

    query_label=Label(root,text=print_records)
    query_label.grid(row=16,column=0,columnspan=2)

    conn.commit()
    conn.close()


def delete():
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    c.execute("DELETE FROM movie_data where movie_id=" + delete_box.get())

    conn.commit()
    conn.close()
    

def update():
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor() 
    record_id=delete_box.get()
    c.execute("""UPDATE movie_data set
        movie_name=%(name)s,
        release_date=%(release)s,
        director=%(dir)s,
        producer=%(pro)s,
        actors=%(act)s,
        duration=%(dur)s,
        rating=%(rat)s

        where movie_id="""+record_id,
        {   'id': record_id,
            'name':movie_name_editor.get(),
            'release':release_date_editor.get(),
            'dir':director_editor.get(),
            'pro':producer_editor.get(),
            'act':actors_editor.get(),
            'dur':duration_editor.get(),
            'rat':rating_editor.get()
        }
        )

    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor=Tk()
    editor.title("Update")

    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    record_id=delete_box.get()

    c.execute("SELECT * FROM movie_data where movie_id=" + record_id)
    records=c.fetchall()
    
    #global variables for text box names
    global movie_id_editor
    global movie_name_editor
    global release_date_editor
    global director_editor
    global producer_editor
    global actors_editor
    global duration_editor
    global rating_editor




    movie_name_editor=Entry(editor,width=30)
    movie_name_editor.grid(row=0,column=1,padx=20)

    release_date_editor=Entry(editor,width=30)
    release_date_editor.grid(row=1,column=1,padx=20)

    director_editor=Entry(editor,width=30)
    director_editor.grid(row=2,column=1,padx=20)

    producer_editor=Entry(editor,width=30)
    producer_editor.grid(row=3,column=1,padx=20)

    actors_editor=Entry(editor,width=30)
    actors_editor.grid(row=4,column=1,padx=20)

    duration_editor=Entry(editor,width=30)
    duration_editor.grid(row=5,column=1,padx=20)

    rating_editor=Entry(editor,width=30)
    rating_editor.grid(row=6,column=1,padx=20)


    #labels 
    movie_name_label=Label(editor,text="Movie name")
    movie_name_label.grid(row=0,column=0)

    release_date_label=Label(editor,text="release_date")
    release_date_label.grid(row=1,column=0)

    director_label=Label(editor,text="director")
    director_label.grid(row=2,column=0)

    producer_label=Label(editor,text="producer")
    producer_label.grid(row=3,column=0)

    actors_label=Label(editor,text="actor")
    actors_label.grid(row=4,column=0)

    duration_label=Label(editor,text="Duration(in hours)")
    duration_label.grid(row=5,column=0)

    rating_label=Label(editor,text="Rating(out of 10)")
    rating_label.grid(row=6,column=0)


    for record in records:
        movie_name_editor.insert(0,record[1])
        release_date_editor.insert(0,record[2])
        director_editor.insert(0,record[3])
        producer_editor.insert(0,record[4])
        actors_editor.insert(0,record[5])
        duration_editor.insert(0,record[6])
        rating_editor.insert(0,record[7])

    #button to save
    edit_btn=Button(editor,text="save records",command=update)
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=137)


## second table
def show_submit():
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()

    
    c.execute("INSERT INTO show_data values(%(show_id)s,%(movie_id)s,%(st_time)s,%(end_time)s,%(show_date)s,%(price)s)",
                {
                    'show_id':show_id.get(),
                    'movie_id':movie_id.get(),
                    'st_time':st_time.get(),
                    'end_time':end_time.get(),
                    'show_date':show_date.get(),
                    'price':price.get(),   
                }
        )

    conn.commit()
    conn.close()

    show_id.delete(0,END)
    movie_id.delete(0,END)
    st_time.delete(0,END)
    end_time.delete(0,END)
    show_date.delete(0,END)
    price.delete(0,END)

def display_shows():
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    c.execute("SELECT * FROM show_data")
    records=c.fetchall()
    print(records)
    print_records=''

    for record in records:
        print_records +=str(record) +"\n"


    query1_label=Label(show,text=print_records)
    query1_label.grid(row=13,column=0,columnspan=2)

    conn.commit()
    conn.close()

def delete_show():
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    c.execute("DELETE FROM show_data where show_id=" + delete_show_box.get())
    c.execute("DELETE FROM book_data where show_id=" + delete_show_box.get())
    conn.commit()
    conn.close()


def info_submit():

    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()

    c.execute("INSERT INTO book_data values(%(m_id)s,%(s_id)s,%(t_id)s,%(ca_name)s,%(e_id)s,%(p_no)s,%(s_no)s)",
                {
                    'm_id':movie_id_book.get(),
                    's_id':show_id_book.get(),
                    't_id':t_id.get(),
                    'ca_name':c_name.get(),
                    'e_id':email_id.get(),
                    'p_no':phone_no.get(),  
                    's_no':seat_no.get() 
                }
        )

    conn.commit()
    conn.close()

    show_id_book.delete(0,END)
    movie_id_book.delete(0,END)
    t_id.delete(0,END)
    c_name.delete(0,END)
    email_id.delete(0,END)
    phone_no.delete(0,END)
    seat_no.delete(0,END)



def display_registered():

    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    c.execute("SELECT * FROM book_data")
    records=c.fetchall()
    print(records)
    print_records=''

    for record in records:
        print_records +=str(record) +"\n"


    query1_label=Label(book_show,text=print_records)
    query1_label.grid(row=13,column=0,columnspan=2)

    conn.commit()
    conn.close() 


def create_ticket_view():
    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    c.execute("""
    CREATE OR REPLACE VIEW ticket_view AS
    SELECT bd.*, sd.st_time, sd.end_time, sd.show_date, sd.price, md.movie_name
    FROM book_data bd
    JOIN show_data sd ON bd.show_id = sd.show_id
    JOIN movie_data md ON bd.movie_id = md.movie_id;
    """)

    conn.commit()
    conn.close()

# Call the function to create the view
create_ticket_view()

from tkinter import Toplevel, Label

def display_ticket():
    current_ticket_id = t_id.get()

    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()

    c.execute("SELECT * FROM ticket_view WHERE t_id=%s", (current_ticket_id,))
    records = c.fetchall()

    # Create a new Toplevel window
    ticket_window = Toplevel()
    ticket_window.title("Ticket Details")

    if records:
        for label, value in zip(["Movie ID", "Show ID", "Ticket ID", "Customer Name", "Email ID", "Phone No", "Seat No"], records[0]):
            label_text = f"{label}: {value}"
            label_widget = Label(ticket_window, text=label_text)
            label_widget.pack(anchor="w")

        separator = Label(ticket_window, text="-" * 30)
        separator.pack(anchor="w")
    else:
        no_record_label = Label(ticket_window, text="No record found for the provided Ticket ID.")
        no_record_label.pack()

    conn.commit()
    conn.close()



def book():
    global movie_id_book
    global show_id_book
    global book_show
    global t_id
    global c_name
    global email_id
    global phone_no
    global seat_no

    book_show=Tk()
    book_show.title("Booking")


    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    '''c.execute("""CREATE TABLE book_data(
        movie_id integer NOT NULL,
        show_id integer NOT NULL,
        t_id integer primary Key,
        c_name text ,
        email_id text,
        phone_no text,
        seat_no text UNIQUE
        )""")'''

    record_id=select_m_id.get()

    #entry boxes
    movie_id_book=Entry(book_show,width=30,)
    movie_id_book.grid(row=0,column=1,padx=10,pady=10)

    show_id_book=Entry(book_show,width=30,)
    show_id_book.grid(row=1,column=1,padx=10,pady=10)

    t_id=Entry(book_show,width=30)
    t_id.grid(row=2,column=1,padx=10,pady=10)

    c_name=Entry(book_show,width=30)
    c_name.grid(row=3,column=1,padx=10,pady=10)

    email_id=Entry(book_show,width=30)
    email_id.grid(row=4,column=1,padx=10,pady=10)

    phone_no=Entry(book_show,width=30)
    phone_no.grid(row=5,column=1,padx=10,pady=10)

    seat_no=Entry(book_show,width=30)
    seat_no.grid(row=6,column=1,padx=10,pady=10)



    #labels

    movie_id_book_label=Label(book_show,text="Selected Movie ID")
    movie_id_book_label.grid(row=0,column=0)

    show_id_book_label=Label(book_show,text="Selected Show ID")
    show_id_book_label.grid(row=1,column=0)

    t_id_label=Label(book_show,text="Ticket ID")
    t_id_label.grid(row=2,column=0)

    c_name_label=Label(book_show,text="Customer Name")
    c_name_label.grid(row=3,column=0)

    email_id_label=Label(book_show,text="Customer Email ID")
    email_id_label.grid(row=4,column=0)

    phone_no_label=Label(book_show,text="Phone NO")
    phone_no_label.grid(row=5,column=0)

    seat_no_label=Label(book_show,text="Seat No")
    seat_no_label.grid(row=6,column=0)

    movie_id_book.insert(0,record_id)
    record_id=select_s_id.get()
    show_id_book.insert(0,record_id)

    #button

    submit_btn=Button(book_show,text="submit",command=info_submit)
    submit_btn.grid(row=7,column=0,columnspan=1,pady=10,padx=10,ipadx=100)

    ticket_btn=Button(book_show,text="display",command=display_ticket)
    ticket_btn.grid(row=7,column=1,columnspan=2,pady=10,padx=10,ipadx=100)

    ticket_btn=Button(book_show,text="All Customers ",command=display_registered)
    ticket_btn.grid(row=8,column=1,columnspan=2,pady=10,padx=10,ipadx=100)






def show_data():
    global show
    global record_id
    #global variables for text box names
    global movie_id
    global show_id
    global st_time
    global end_time
    global show_date
    global price
    global delete_show_box
    global select_m_id
    global select_s_id

    
    
    show=Tk()
    show.title("shows arrangement")


    conn=mysql.connector.connect(host='localhost',password='root',user='root',database='Movie_Management_system')
    c=conn.cursor()
    '''c.execute("""CREATE TABLE show_data(
        show_id integer primary key,
        movie_id integer NOT NULL,
        st_time text ,
        end_time text,
        show_date text,
        price text
        )""")'''

    record_id=delete_box.get()

    #entry boxes for shows table
    show_id=Entry(show,width=30,)
    show_id.grid(row=0,column=1,padx=10,pady=10)

    movie_id=Entry(show,width=30,)
    movie_id.grid(row=1,column=1,padx=10,pady=10)

    st_time=Entry(show,width=30,)
    st_time.grid(row=2,column=1,padx=10,pady=10)

    end_time=Entry(show,width=30,)
    end_time.grid(row=3,column=1,padx=10,pady=10)

    show_date=Entry(show,width=30,)
    show_date.grid(row=4,column=1,padx=10,pady=10)

    price=Entry(show,width=30,)
    price.grid(row=5,column=1,padx=10,pady=10)

    delete_show_box=Entry(show,width=30,)
    delete_show_box.grid(row=7,column=1,padx=10,pady=10)

    select_m_id=Entry(show,width=30)
    select_m_id.grid(row=9,column=1,padx=10,pady=10)

    select_s_id=Entry(show,width=30)
    select_s_id.grid(row=9,column=3,padx=10,pady=10)

    #labels

    show_id_label=Label(show,text="Show ID")
    show_id_label.grid(row=0,column=0)

    movie_id_label=Label(show,text="Movie ID")
    movie_id_label.grid(row=1,column=0)

    st_time_label=Label(show,text="Start time")
    st_time_label.grid(row=2,column=0)

    end_time_label=Label(show,text="End time")
    end_time_label.grid(row=3,column=0)

    show_date_label=Label(show,text="Show Date")
    show_date_label.grid(row=4,column=0)

    price_label=Label(show,text="Price")
    price_label.grid(row=5,column=0)

    delete_show_box_label=Label(show,text="Select Show ID")
    delete_show_box_label.grid(row=7,column=0)

    select_m_id_label=Label(show,text="Select movie ID")
    select_m_id_label.grid(row=9,column=0)

    select_s_id_label=Label(show,text="Select show ID")
    select_s_id_label.grid(row=9,column=2)

    movie_id.insert(0,record_id)

    #buttons

    sub_btn=Button(show,text="Add record to database",command=show_submit)
    sub_btn.grid(row=6,column=0,columnspan=1,pady=10,padx=10,ipadx=100)

    dis_btn=Button(show,text="Show record",command=display_shows)
    dis_btn.grid(row=6,column=2,columnspan=2,pady=10,padx=10,ipadx=100)

    del_btn=Button(show,text="delete show",command=delete_show)
    del_btn.grid(row=8,column=1,columnspan=1,pady=10,padx=10,ipadx=100)

    book_btn=Button(show,text="Booking",command=book)
    book_btn.grid(row=10,column=1,columnspan=1,pady=10,padx=10,ipadx=100)








    

#entry boxes
movie_id=Entry(root,width=30,)
movie_id.grid(row=1,column=1,padx=10,pady=10)

movie_name=Entry(root,width=30)
movie_name.grid(row=2,column=1,padx=10,pady=10)

release_date=Entry(root,width=30)
release_date.grid(row=3,column=1,padx=10,pady=10)

director=Entry(root,width=30)
director.grid(row=4,column=1,padx=10,pady=10)

producer=Entry(root,width=30)
producer.grid(row=5,column=1,padx=10,pady=10)

actors=Entry(root,width=30)
actors.grid(row=6,column=1,padx=10,pady=10)

duration=Entry(root,width=30)
duration.grid(row=7,column=1,padx=10,pady=10)

rating=Entry(root,width=30)
rating.grid(row=8,column=1,padx=10,pady=10)

#delete entry box
delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=10,pady=10)



#labels
#labels 

movie_id_label=Label(root,text="Movie ID")
movie_id_label.grid(row=1,column=0)

movie_name_label=Label(root,text="Movie name")
movie_name_label.grid(row=2,column=0)

release_date_label=Label(root,text="release date(dd/mm/yyyy)")
release_date_label.grid(row=3,column=0)

director_label=Label(root,text="directors")
director_label.grid(row=4,column=0)

producer_label=Label(root,text="producers")
producer_label.grid(row=5,column=0)

actors_label=Label(root,text="actors")
actors_label.grid(row=6,column=0)

duration_lebel=Label(root,text="Duration(in hours)")
duration_lebel.grid(row=7,column=0)

rating_label=Label(root,text="rating(out of 10)")
rating_label.grid(row=8,column=0)

delete_box_lebel=Label(root,text="Enter Movie ID")
delete_box_lebel.grid(row=10,column=0)


#buttons
#submit button
submit_btn=Button(root,text="Add record to database",command=submit)
submit_btn.grid(row=9,column=0,columnspan=1,pady=10,padx=10,ipadx=100)

#display button
display_btn=Button(root,text="Show records",command=display)
display_btn.grid(row=9,column=1,columnspan=2,pady=10,padx=10,ipadx=100)

#button for delete
delete_btn=Button(root,text="Delete records",command=delete)
delete_btn.grid(row=11,column=0,columnspan=1,pady=10,padx=10,ipadx=137)

#update button
edit_btn=Button(root,text="edit records",command=edit)
edit_btn.grid(row=11,column=1,columnspan=2,pady=10,padx=10,ipadx=137)

#customer button
cus_btn=Button(root,text="Shows_data Table",command=show_data)
cus_btn.grid(row=11,column=3,columnspan=3,pady=10,padx=10,ipadx=137)



conn.commit()
conn.close()
root.mainloop()