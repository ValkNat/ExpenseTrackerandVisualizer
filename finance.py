#imports
import tkinter as tk
from tkinter import *
from tkinter import filedialog, simpledialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar, DateEntry
import csv
import os

#tkinter initialization + setup
t = Tk()
t.geometry("700x700")
t.title("Expenses Tracker")

#overarching expenses list
expenses = []

#Opens up visual GUI for adding expense
def addExpense():
    title = simpledialog.askstring("Title of expense", "Title of expense?")
    cost = simpledialog.askinteger("Cost of expense:", "Cost of expense?")
    date = simpledialog.askstring("Date of expense:", "Date of expense?")
    expense = {"title": title, "cost": cost, "date": date}
    expenses.append(expense)
    expense_list.insert(0, expense)

#updates or initializes the pie-chart
def update_pie_chart():
    costs=[expense['cost'] for expense in expenses]
    titles = [expense['title'] for expense in expenses]
    pie_chart.clear()
    pie_chart.pie(costs, labels=titles, autopct='%1.1f%%')
    pie_chart.set_title('Expenses')
    pie_chart.figure.tight_layout()
    pie_canvas.draw()
    pie_canvas.get_tk_widget().pack()

#saves the expenses to a CSV file - checks if file already exists and creates if it doesn't
def save_to_csv():
    keys = expenses[0].keys()
    try:
        with open('expenses.csv', 'r', newline='') as output_file:
         if os.path.exists('expenses.csv'):
              with open('expenses.csv', 'a', newline='') as output_file:
                  dict_writer = csv.DictWriter(output_file, keys)
                  dict_writer.writerows(expenses) 
    except FileNotFoundError:
             with open('expenses.csv', 'w', newline='') as output_file:
                 dict_writer = csv.DictWriter(output_file, keys)
                 dict_writer.writeheader()
                 dict_writer.writerows(expenses)

#tkinter widget initialization + setup
add_expense_button = tk.Button(text = "Add Expense", command=addExpense)
add_expense_button.pack()
expense_list = Listbox()
expense_list.pack(fill="x")
visualize_expenses = tk.Button(text = "Visualize Expenses", command=update_pie_chart)
visualize_expenses.pack()
save_expenses = tk.Button(text = "Save Expenses", command=save_to_csv)
save_expenses.pack()

#pie-chart setup using matplotlib
pie_figure, pie_chart = plt.subplots()
pie_canvas = FigureCanvasTkAgg(pie_figure, master=t)

#run tkinter
t.mainloop()