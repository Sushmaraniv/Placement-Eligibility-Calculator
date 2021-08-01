from tkinter import *
from PIL import ImageTk,Image
import pyttsx3

root=Tk()
root.title("Placements eligibility Calculator")
root.geometry ("700x360")

load = Image.open("image1.jpg")
pic = ImageTk.PhotoImage(load)


img = Label(root, image=pic)
img.image = pic
img.place(x=0, y=0)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talkk(text):
    engine.say(text)
    engine.runAndWait()


def Calculation() :
    name=str(nameentry.get())
    aptitude=int(aptitudeentry.get())
    technical=int(technicalentry.get())
    group_discussion=int(group_discussionentry. get())

    total=(aptitude+technical+group_discussion)

    Label(text=f"{total}", font="arial 15 bold",width=14).place(x=250,y=210)

    average=int (total/3)
    Label(text=f"{average}", font="arial 15 bold",width=14).place(x=250,y=240)


    if average>=80:
        grade="Congratulations,you're selected to HR round"
    elif average>=70 and average<80:
        grade = "You have been shortlisted for HR round"
    else:
       grade = "Better luck next time"



    Label(text=f"{grade}", font="arial 15 bold" ,bg="white",fg="black",width=35).place(x=250,y=270)

    responce= name +"\n" +grade
    talkk(responce)


sub = Label(root, text="Name:",font="arial 10",bg= "blue" , fg='white')
sub1 = Label(root, text="Aptitude:", font="arial 10",bg= "blue" , fg='white')
sub2 = Label(root, text="Technical:", font="arial 10",bg= "blue" , fg='white')
sub3 = Label(root, text="Group Discussion:", font="arial 10",bg= "blue" , fg='white')
total = Label(root, text="Total:", font="arial 10")
avg = Label(root, text="Average:", font="arial 10")
grade = Label(root, text="Selected to next round or not ? ", font="arial 10")

sub.place(x=50, y=20)
sub1.place(x=50, y=70)
sub2.place(x=50, y=120)
sub3.place(x=50,y=170)
total.place(x=50,y=210)
avg .place(x=50, y=240)
grade.place(x=50, y=270)

namevalue=StringVar()
aptitudevalue=StringVar()
technicalentryvalue=StringVar()
group_discussionvalue=StringVar()

nameentry=Entry(root, textvariable=namevalue, font="arial 15", width=15)
aptitudeentry=Entry(root, textvariable=aptitudevalue, font="arial 15", width=15)
technicalentry=Entry(root, textvariable=technicalentryvalue, font="arial 15", width=15)
group_discussionentry=Entry(root, textvariable=group_discussionvalue, font="arial 15", width=15)

nameentry.place(x=250,y=20)
aptitudeentry. place(x=250,y=70)
technicalentry.place(x=250,y=120)
group_discussionentry . place(x=250,y=170)

Button(text="Result", font="arial 15", bg="black",fg="white", bd=10, command=Calculation) . place(x=50,y=300)
Button (text="Exit", font="arial 15", bg="black",fg="white", bd=10, width=8, command=lambda:exit()).place(x=350,y=300)

root.mainloop()
