import tkinter as tk
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("My to-do list ")

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else :
        tkinter.messagebox.showwarning(title="Attention ! !",message="To add a task, please enter some task  ")

def task_removing():
    
    index_todo =todo_box.curselection()
    if index_todo :
        todo_box.delete(index_todo)
    else:
        tkinter.messagebox.showwarning(title="Attention !!", message="To delete a task , you must select a task !!")

def task_complete():
    index_todo =todo_box.curselection()
    if index_todo :
        task=todo_box.get(index_todo)
        todo_box.itemconfig(index_todo,{'bg' : 'gray','fg':'blue'})
        tkinter.messagebox.showinfo("task completed",f'task"{task}" marked as completed .')
    else:
        tkinter.messagebox.showwarning(title ="warning !!", message =" Please select a task to mark as complete.")
            
   
def clear_all_tasks():
    todo_box.delete(0,tk.END)

list_frame = tkinter.Frame(root, background="black")
list_frame.pack()

todo_box = tkinter.Listbox(list_frame,height=30,width=80)
todo_box.pack(side=tkinter.LEFT)

scroller =tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command = list_frame.yview)


task_add = tkinter.Entry(root,width=80)
task_add.pack()

add_task_button =tkinter.Button(root,text="Click to add task ",font=("arial",20,"bold"),background="green",width=30,command=task_adding)
add_task_button.pack()

remove_task_button =tkinter.Button(root,text="Click to remove task ", font =("arial",20,"bold"), background ="pink",width=30,command=task_removing)
remove_task_button.pack()


complete_task_button =tkinter.Button(root,text="Click to complete task ",font=("arial",20,"bold"), background="yellow",width=30,command = task_complete)
complete_task_button.pack()

clear_all_task_button=tkinter.Button(root,text="Click to clear all tasks ",font=("arial",20,"bold"), background="red",width=30,command = clear_all_tasks)
clear_all_task_button.pack()
root.mainloop()

