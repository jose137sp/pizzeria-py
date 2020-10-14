from tkinter import *
from tkinter import messagebox

# window (ventana) principal
ventana = Tk()
ventana.configure(background="white")
ventana.title("Papa's John")
ventana.geometry("800x700")
titulo = Label(ventana, text="BIENVENIDO A PAPA'S JOHN PIZZA", 
                fg="black", 
                padx=300, 
                pady=10, 
                font=('Verdana', 20))
titulo.pack()

# declaracion de variables
precio = DoubleVar()
price = DoubleVar()
suma = DoubleVar()
total = DoubleVar()
descuento = DoubleVar()
in1_valor = IntVar()
in2_valor = IntVar()
in3_valor = IntVar()
in4_Valor = IntVar()
in5_Valor = IntVar()
subtotal = StringVar()


# funtion to get final values

def submit():
    total=0.00
    descuento=0.00
    global suma
    cant_num.config(text=str(cantidad.get()))
    sub_total=0.00
    suma=precio.get()
    if in1_valor.get():
        suma=suma+1.00
        suma_result.config(text="$"+str(suma))
    if in2_valor.get():
        suma=suma+1.50
        suma_result.config(text="$"+str(suma))
    if in3_valor.get():
        suma=suma+2.00
        suma_result.config(text="$"+str(suma))
    if in4_Valor.get():
        suma=suma+1.20
        suma_result.config(text="$"+str(suma))
    if in5_Valor.get():
        suma=suma+2.00
        suma_result.config(text="$"+str(suma))
    suma=suma*float(cantidad.get())
    suma_result.config(text="$"+str(suma))

    #total_price.config(text="$" + str(suma))
    if precio.get()==20.00:
        total_price.config(text="$"+str(suma))
        if suma >=30:
            descuento=0.05
            desc.config(text="5%")
            total=suma-(suma*0.05)
            total_price.config(text="$"+str(total))

        elif (suma >= 20 and suma <= 30):
            descuento=0.02
            desc.config(text="2%")
            total = suma - (suma * 0.02)
            total_price.config(text="$" + str(total))
        else:
            total=suma
            total_price.config(text="$" + str(total))
    else:
        total = suma
        desc.config(text="0%")
        total_price.config(text="$" + str(total))


#manejo de error_cantiad de ingredientes
def error_cant():
    n = 0
    if in1_valor.get():
        n = n + 1

    if in2_valor.get():
        n = n + 1
    if in3_valor.get():
        n = n + 1

    if in4_Valor.get():
        n = n + 1

    if in5_Valor.get():
        n = n + 1

    if n > 3:
        messagebox.showerror("¡Alerta!","Solo puede elegir 3 ingredientes para su rica pizza...")





#labelFrame tamnanos
tamaños = LabelFrame(ventana, text="Tamaño de la pizza a escoger",
                     fg="black",
                     bg="white",
                     padx=20,
                     pady=40,
                     font=('Verdana', 16),
                     relief=GROOVE)
tamaños.place(x=25, y=60, anchor=NW)
# buttons-opciones de pizza + cantidad
pizzA = Radiobutton(tamaños, text="Personal\t\t\t $7.00",
                    value=7.00,
                    variable=precio,
                    fg="black",
                    bg="white",
                    padx=20,
                    pady=10,
                    font=('Verdana', 16))
pizzA.pack(anchor=W)
pizzaB = Radiobutton(tamaños, text="Combo\t\t\t $20.00",
                     value=20.00,
                     variable=precio,
                     fg="black",
                     bg="white",
                     padx=20,
                     pady=10,
                     font=('Verdana', 16))
pizzaB.pack(anchor=W)
detail = Label(tamaños, text="PIZZA FAMILIAR + SODA 2L",
               anchor="w",
               justify=LEFT,
               fg="black",
               bg="white",
               padx=20,
               pady=10,
               font=('Verdana', 12))
detail.pack(anchor=W)

cant_label = Label(tamaños, text="Cantidad",
                   padx=20,
                   pady=10,
                   font=('Verdana', 16)).place(x=50, y=120)

cantidad = Spinbox(tamaños, width=5, from_=0, to=100)
cantidad.place(x=180, y=127)

# checkbos-Ingredientes
ingredientes = LabelFrame(ventana, 
                    text="Ingredientes (Maximo 3)", 
                    fg="black", 
                    bg="white", 
                    padx=27, 
                    pady=40,
                    font=('Verdana', 16), 
                    relief=GROOVE)
ingredientes.place(x=25, y=300, anchor=NW)

in1 = Checkbutton(ingredientes, text="Tres quesos\t\t$1.00",
                  variable=in1_valor,
                  fg="black",
                  offvalue=0,
                  command=error_cant,
                  onvalue=1,
                  padx=20,
                  pady=10,
                  font=('Verdana', 16))
in1.pack(anchor=W)
in2 = Checkbutton(ingredientes, text="Bacon\t\t\t$1.50",
                  offvalue=0,
                  onvalue=1,
                  variable=in2_valor,
                  command=error_cant,
                  fg="black",
                  padx=20,
                  pady=10,
                  font=('Verdana', 16))
in2.pack(anchor=W)
in3 = Checkbutton(ingredientes, text="Anchoas\t\t\t$2.00",
                  command=error_cant,
                  variable=in3_valor,
                  fg="black",
                  padx=20,
                  pady=10,
                  font=('Verdana', 16))
in3.pack(anchor=W)
in4 = Checkbutton(ingredientes, text="Peperroni\t\t\t$1.25",
                  command=error_cant,
                  variable=in4_Valor,
                  fg="black",
                  padx=20,
                  pady=10,
                  font=('Verdana', 16))
in4.pack(anchor=W)
in5 = Checkbutton(ingredientes, text="Chorizo\t\t\t$2.00",
                  command=error_cant,
                  variable=in5_Valor,
                  fg="black",
                  padx=20,
                  pady=10,
                  font=('Verdana', 16))
in5.pack(anchor=W)

# Button-llamado a funcion submit
sub_btn=Button(ingredientes, text='Submit', command=submit)
sub_btn.pack()

#Factura+resumen
resumen = LabelFrame(ventana, text="Factura", labelanchor='n',fg="blue", padx=27, pady=70,font=('Verdana', 16), relief=GROOVE)
resumen.place(x=740, y=300, anchor=E)

#Tipo de tamano
type_pizza =Label(resumen, text="Tamaño: $",fg="black", padx=1, pady=10,font=('OCR-A', 16))
type_pizza.grid(row=1, column=0)
type_pizza_price =Label(resumen, textvariable=precio,fg="black", padx=1, pady=10,font=('OCR-A', 16))
type_pizza_price.grid(row=1,column=1)

#cantidad reflejada
pizza_cant =Label(resumen, text="Cantidad",fg="black", padx=12, pady=10,font=('OCR-A', 16))
pizza_cant.grid(row=2, column=0)
cant_num =Label(resumen,text=" ",fg="black", padx=4, pady=10,font=('OCR-A', 16))
cant_num.grid(row=2, column=1)

#subtotal reflejado
suma_label =Label(resumen, text="Subtotal:",fg="black", padx=12, pady=10,font=('OCR-A', 16))
suma_label.grid(row=3, column=0)
suma_result =Label(resumen, text=" ",fg="black", padx=2, pady=10,font=('OCR-A', 16))
suma_result.grid(row=3, column=1)

#descuento reflejado
desc_label =Label(resumen, text="Descuento: ",fg="black", padx=2, pady=10,font=('OCR-A', 16))
desc_label.grid(row=4, column=0)
desc =Label(resumen, text=" ",fg="black", padx=2, pady=10,font=('Verdana', 16))
desc.grid(row=4, column=1)

#total_reflejado
total_label =Label(resumen, text="Total: ",fg="black", padx=12, pady=10,font=('OCR-A', 16))
total_label.grid(row=5, column=0)
total_price =Label(resumen, text=" ",fg="black", padx=2, pady=10,font=('OCR-A', 16))
total_price.grid(row=5, column=1)

ventana.mainloop()