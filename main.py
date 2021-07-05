from tkinter import *
import time






root=Tk()

root.title("Temperature converter")


def main_window(root):

  
  myframe=Frame(root,width=500,height=400)
  
  myframe.pack()
  
  mylabel=Label(myframe,text="Choose wich unit you want to convert")
  
  mylabel.grid(row=0,column=1,pady=4)


 
  fahrenheit_to_celsius_button=Button(myframe,text="Fahrenheit to celsius",command=lambda:[myframe.destroy(),fahrenheit_to_celsius_page()])


  
  fahrenheit_to_celsius_button.grid(row=1,column=1,pady=5,padx=4)


  
  Celsius_to_fahrenheit=Button(myframe,text="Celsius to fahrenheit",command=lambda:[myframe.destroy(),celcius_to_fahrenheit_page()])
 
  Celsius_to_fahrenheit.grid(row=2,column=1,pady=4,padx=5)
    
    



def fahrenheit_to_celsius_page():

  

  def give_answer():
    try:
      

      initial_temperature=fahrenheit_entry.get()
      
      celcius_temperature=(float(initial_temperature)-32)*(5/9)
      print(celcius_temperature)
     
      answer_label_celcius=Label(myframe2,text=("{0:.2f}".format(celcius_temperature))+" °C")
    
      answer_label_celcius.grid(row=3,column=0)

      
    except ValueError:

      exception_label=Label(myframe2,text="You need to enter a valid value")
      
      
      exception_label.config(fg="red")
      exception_label.grid(row=1,column=0)
     
      exception_label.after(2000, exception_label.destroy)

      
      
      print("You need to enter a value")
      
    
  myframe2=Frame(root,width=500,height=400)
 
  myframe2.pack()


  fahrenheit_label=Label(myframe2,text="Enter the temperature in fahrenheit")
 
  fahrenheit_label.grid(row=0,column=0,padx=10,pady=10)

  fahrenheit_entry=Entry(myframe2)

  fahrenheit_entry.grid(row=2,column=0)

  fahrenheit_button=Button(myframe2,text="Submit",command=give_answer)

  fahrenheit_button.grid(row=4,column=0,padx=10,pady=10,sticky="e")
  
  back_button=Button(myframe2,text="Back",command=lambda:[myframe2.destroy(),main_window(root)])
  back_button.grid(row=4,column=0,sticky="w",padx=10,pady=10)

    

    



def celcius_to_fahrenheit_page():


  def give_answer2():
    try:
      
      
      initial_temperature2=celsius_entry.get()
      
      fahrenheit_temperature=(float(initial_temperature2)*9/5)+32
      print(fahrenheit_temperature)
      
      answer_label_fahrenheit=Label(myframe3,text=("{0:.2f}".format(fahrenheit_temperature))+" °F")
      
      answer_label_fahrenheit.grid(row=4,column=0)
    except ValueError:

      exception_label2=Label(myframe3,text="You need to enter a valid value")
       
      exception_label2.config(fg="red")
      exception_label2.grid(row=1,column=0)
      
      exception_label2.after(2000, exception_label2.destroy)

  myframe3=Frame(root,width=500,height=400)
  myframe3.pack()
 
  fahrenheit_label=Label(myframe3,text="Enter the temperature in Celcius")
  fahrenheit_label.grid(row=0,column=0,padx=10,pady=10)
  
  celsius_entry=Entry(myframe3)
  celsius_entry.grid(row=2,column=0)
  celsius_button=Button(myframe3,text="Submit",command=give_answer2)
  celsius_button.grid(row=5,column=0,padx=10,pady=10,sticky="e")

  back_button2=Button(myframe3,text="Back",command=lambda:[myframe3.destroy(),main_window(root)])
  back_button2.grid(row=5,column=0,sticky="w")

main_window(root)


root.mainloop()