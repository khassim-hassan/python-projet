# SRC/todo_app.py

import tkinter as tk
from tkinter import messagebox
from .todo_list import TodoList  # Import relative pour todo_list.py

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Liste de Tâches")

        self.todo_list = TodoList()

        # Frame principale
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Entrée pour les nouvelles tâches
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=10)
        self.task_entry.bind("<Return>", self.add_task_on_enter)

        # Frame pour les tâches
        self.tasks_frame = tk.Frame(self.frame)
        self.tasks_frame.grid(row=1, column=0, columnspan=2, pady=10)

        # Bouton pour supprimer une tâche
        self.delete_task_button = tk.Button(self.frame, text="Supprimer Tâche", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=0, columnspan=2, pady=5)

    def add_task_on_enter(self, event):
        self.add_task()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Attention", "Vous devez entrer une tâche.")

    def update_task_list(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        
        # Séparer les tâches complétées et non complétées
        non_completed_tasks = [task for task in self.todo_list.tasks if not task["completed"]]
        completed_tasks = [task for task in self.todo_list.tasks if task["completed"]]

        # Afficher les tâches non complétées en premier
        for task in non_completed_tasks + completed_tasks:
            var = tk.IntVar(value=task["completed"])
            cb = tk.Checkbutton(self.tasks_frame, text=task["task"], variable=var, onvalue=1, offvalue=0, command=self.update_task_status)
            cb.var = var  # Attache la variable à la case à cocher pour un accès ultérieur
            if task["completed"]:
                cb.configure(fg="grey", font=("Arial", 10, "overstrike"))
            else:
                cb.configure(fg="black", font=("Arial", 10, "normal"))
            cb.pack(anchor='w')

    def update_task_status(self):
        for cb in self.tasks_frame.winfo_children():
            task = cb.cget("text")
            if cb.var.get() == 1:
                self.todo_list.complete_task(task)
            else:
                for t in self.todo_list.tasks:
                    if t["task"] == task:
                        t["completed"] = False
        self.update_task_list()  # Mettre à jour l'affichage après avoir modifié le statut

    def delete_task(self):
        for cb in self.tasks_frame.winfo_children():
            if cb.var.get() == 1:
                task = cb.cget("text")
                self.todo_list.delete_task(task)
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
