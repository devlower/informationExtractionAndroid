import tkinter as tk
from tkinter import *
from tkinter import ttk
from adb import get_contacts, get_name
from create_contact_list import createContactList
from compare_lists import compareLists

cel1_list = ""
cel2_list = ""

def guiInterface():

  tree = ""
  tree1 = ""
  tree2 = ""

  def compareContacts():

    try:
      compared_lists = compareLists(cel1_list, cel2_list)

      for item in compared_lists:
        tree.insert('', tk.END, values=item)
    except:
      pass

  def contactsCel1():

    global cel1_list

    cel1_list = cel_1.create()

    for item in cel1_list:
      tree1.insert('', tk.END, values=item)

    return cel1_list


  def contactsCel2():

    global cel2_list

    cel2_list = cel_2.create()

    for item in cel2_list:
     tree2.insert('', tk.END, values=item)
  
    return cel2_list


  class Contact():
 
    def create(self):
      device_name = get_name()
      path = f'C:\\Temp\\scan-android-device\\{device_name}.txt' 
      get_contacts(path)
      cel_list = createContactList(path)
      return cel_list

  cel_1 = Contact()
  cel_2 = Contact()

  window = Tk() 
  window.geometry('1500x600')
  window.resizable(True, True)
  window.title('Comparador de Lista de Contato')

  text = Label(window, text='')
  text.grid(column=0, row=0, padx=10, pady=10)
  text = Label(window, text='')
  text.grid(column=3, row=0, padx=10, pady=10)

  text = Label(window, text='Celular 1')
  text.grid(column=1, row=0, padx=10, pady=10)
  text = Label(window, text='Celular 2')
  text.grid(column=4, row=0, padx=10, pady=10)

  text = Label(window, text='Conecte via cabo USB o primeiro celular e clique no botão: "Obter Contatos Celular 1"').place(x = 900, y=300)

  Button(window, text="Obter Contatos Celular 1", command=contactsCel1, bg = "LIGHT GREY").place(x = 900, y=350)

  columns = ('nome_dos_contatos', 'num_tel', 'dt_creation')

  tree1 = ttk.Treeview(window, columns=columns, show='headings')

  tree1.heading('nome_dos_contatos', text='Nome dos Contatos')
  tree1.heading('num_tel', text='Número de Telefone')
  tree1.heading('dt_creation', text='Data de Criação do Contato')

  tree1.grid(row=2, column=1, sticky='nsew')

  # add a scrollbar
  scrollbar_Vert = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree1.yview)
  tree1.configure(yscroll=scrollbar_Vert.set)
  scrollbar_Vert.grid(row=2, column=2, sticky='ns')

  text = Label(window, text='Conecte via cabo USB o segundo celular e clique no botão: "Obter Contatos Celular 2"').place(x = 900, y=400)

  Button(window, text="Obter Contatos Celular 2", command=contactsCel2, bg = "LIGHT GREY").place(x = 900, y=450)
  
  columns = ('nome_dos_contatos', 'num_tel', 'dt_creation')

  tree2 = ttk.Treeview(window, columns=columns, show='headings')

  tree2.heading('nome_dos_contatos', text='Nome dos Contatos')
  tree2.heading('num_tel', text='Número de Telefone')
  tree2.heading('dt_creation', text='Data de Criação do Contato')

  tree2.grid(row=2, column=4, sticky='nsew')


  scrollbar_Vert = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree2.yview)
  tree2.configure(yscroll=scrollbar_Vert.set)
  scrollbar_Vert.grid(row=2, column=5, sticky='ns')


  # Comparação

  text = Label(window, text='Após obter os contatos dos dois aparelhos clique em "Comparar Contatos"').place(x = 900, y=500)

  Button(window, text="Comparar Contatos", command=compareContacts, bg = "LIGHT GREY").place(x = 900, y=550)

  text = Label(window, text='Quadro Comparativo')
  text.grid(column=1, row=4, padx=10, pady=10)

  columns = ('nome_dos_contatos_1', 'num_tel', 'nome_dos_contatos_2', 'dt_first_creation')

  tree = ttk.Treeview(window, columns=columns, show='headings')

  tree.heading('nome_dos_contatos_1', text='Nome dos Contatos celular 1')
  tree.heading('num_tel', text='Número de Telefone')
  tree.heading('nome_dos_contatos_2', text='Nome dos Contatos celular 2')
  tree.heading('dt_first_creation', text='Registrado há mais tempo em:')

  tree.grid(row=5, column=1, sticky='nsew')

  scrollbar_Vert = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
  tree.configure(yscroll=scrollbar_Vert.set)
  scrollbar_Vert.grid(row=5, column=2, sticky='ns')

  window.mainloop()
