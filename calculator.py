import tkinter as tk
import math

class app (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple calculator')
        self.minsize(500,300)
        #create input field
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(self,textvariable=self.input_text,justify='right',width=30)
        self.input_field.grid(row=0,column=0,padx=10,pady=10,columnspan=5)

        #create buttons
        buttons = [
            '7','8','9','/','sin',
            '4','5','6','*','cos',
            '1','2','3','-','tan',
            '0','.','=','+','sqrt',
            'AC','DEL','CH'
        ]
        row = 1
        col = 0
        for button in buttons:
            def button_action(x=button): return self.button_click(x)
            tk.Button(self,text=button,width=5,command=button_action).grid(row=row,column=col,padx=5,pady=5)
            col += 1
            if col > 4:
                row += 1
                col = 0
        
        #creat history box
        self.history_lable = tk.Label(self,text='Histoy')
        self.history_lable.grid(row=0,column=6)
        self.history_text = tk.Text(self,width=25,height=8)
        self.history_text.grid(row=1,column=6,rowspan=4,padx=5,pady=5)



    def button_click(self,x):
        if x == 'AC':
            self.input_text.set('')
        elif x == 'DEL':
            current_text = self.input_text.get()
            new_text = current_text[:-1]
            self.input_text.set(new_text)
        elif x == 'CH':
            self.history_text.delete('1.0',tk.END)
        elif x == '=':
            result = eval(self.input_text.get())
            self.input_text.set(result)
            self.history_text.insert(tk.END,self.input_text.get()+"\n")
        elif x == 'sin':
            self.input_text.set(math.sin(int(self.input_text.get())))
        elif x == 'cos':
            self.input_text.set(math.cos(int(self.input_text.get())))
        elif x == 'tan':
            self.input_text.set(math.tan(int(self.input_text.get())))
        elif x == 'sqrt':
            self.input_text.set(math.sqrt(int(self.input_text.get())))

        else:
            current_text = x
            new_text = self.input_text.get() + current_text
            self.input_text.set(new_text)
    


window = app()
window.mainloop()