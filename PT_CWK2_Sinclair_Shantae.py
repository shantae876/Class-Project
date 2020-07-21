from tkinter import *
                                        
window = Tk()
window.title ("Workplaces")
window.geometry ('500x250')
window.resizable(False,False)
window['background']='#9324ea'


def checkanswer():

  placeofemploy=workplaces.index(listworkplaces.get(listworkplaces.curselection()))
  persons = employees.index(listemployees.get(listemployees.curselection()))

  if(placeofemploy == persons):
    results.set('CORRECT')

  else:
    results.set('INCORRECT')


personslabel = Label(window,text="Person",fg= 'white', bg='black',font = " Cambria 12 bold")
personslabel.grid(row=0,column=1,sticky=N)
workplacelabel=Label(window,text="Workplace", fg= 'white',bg='black', font = " Cambria 12 bold")
workplacelabel.grid(row=0,column=2,sticky=N)
employees=["John Anderson","Yvonne Bryan","Peter Brown","Rick Grant","William Clarke"]
employees_Names = StringVar()
workplaces=["ABN Enterprises","PLB Planet","Daily Radio","Rick's Cafe","EKY Factory"]
workplaces_list = StringVar()
listemployees = Listbox(window,width=20,height=5,listvariable=employees_Names,exportselection=0,bg='black',fg='white',font="Cambria 10 ",highlightbackground='pink' )
listemployees.grid (padx=50,pady=30,row=1,column=1)
listworkplaces = Listbox(window, width = 20, height = 5,listvariable=workplaces_list,exportselect=0,bg='black',fg='white',font="Cambria 10 ",highlightbackground='pink')
listworkplaces.grid (padx=50, pady=21,row=1,column=2)


sort_employees = list(employees)
sort_workplaces = list(workplaces)
sort_employees.sort()
sort_workplaces.sort()

employees_Names.set(tuple(sort_employees))
workplaces_list.set(tuple(sort_workplaces))


matchbtn= Button(window,text="Determine if Match is Correct",command=checkanswer,fg="black",bg='pink',width=25, font= "Cambria 10 bold", )
matchbtn.grid(row=30,column=1,columnspan=2,sticky=S)

answerlable= Label(window,text= "Answer:", fg="black", bg='pink',font="Cambria 10 bold")
answerlable.grid(row=35,column=1,columnspan=2 )
results=StringVar()
                                                     
                                                     

entryanswer = Entry(window, width = 14, textvariable = results, state='readonly', font = "Cambria 10")
entryanswer.grid(row=35,column=2,pady=10,padx=(10),sticky=S)
    


window.mainloop()  
 










