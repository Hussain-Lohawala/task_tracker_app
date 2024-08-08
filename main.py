import json 
import os 
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.label import Label 
from kivy.uix.checkbox import CheckBox 
from kivy.uix.spinner import Spinner 
from kivymd.uix.pickers import MDDatePicker
 
class Task: 
 
    def __init__(self, name, category='', due_date='', priority='Low', completed=False): 
        self.name = name 
        self.category = category 
        self.due_date = due_date 
        self.priority = priority 
        self.completed = completed 
 
    def to_dict(self): 
        return { 
            'name': self.name, 
            'category': self.category, 
            'due_date': self.due_date, 
            'priority': self.priority, 
            'completed': self.completed 
        } 
 
class TaskTrackerApp(App): 
 
    def build(self): 
        self.tasks = self.load_tasks() 
        layout = BoxLayout(orientation='vertical') 
        self.task_input = TextInput(hint_text='Enter task', size_hint_y=None, height=40) 
        self.category_spinner = Spinner(text='Select Category', values=('Work', 'Personal', 'Other'), size_hint_y=None, height=40) 
        self.priority_spinner = Spinner(text='Priority', values=('Low', 'Medium', 'High'), size_hint_y=None, height=40) 
        add_task_btn = Button(text='Add Task', size_hint_y=None, height=40) 
        add_task_btn.bind(on_press=self.add_task) 
        layout.add_widget(self.task_input) 
        layout.add_widget(self.category_spinner) 
        layout.add_widget(self.priority_spinner) 
        layout.add_widget(add_task_btn) 
        self.task_list = BoxLayout(orientation='vertical', size_hint_y=None) 
        layout.add_widget(self.task_list) 
        self.update_task_list() 
        return layout 
 
    def load_tasks(self): 
        if os.path.exists('data/tasks.json'): 
            with open('data/tasks.json', 'r') as file: 
                tasks_data = json.load(file) 
                return [Task(**task) for task in tasks_data] 
        return [] 
 
    def save_tasks(self): 
        with open('data/tasks.json', 'w') as file: 
            json.dump([task.to_dict() for task in self.tasks], file) 
 
    def add_task(self, instance): 
        task_name = self.task_input.text 
        if task_name: 
            task = Task( 
                name=task_name, 
                category=self.category_spinner.text, 
                priority=self.priority_spinner.text 
            ) 
            self.tasks.append(task) 
            self.save_tasks() 
            self.task_input.text = '' 
            self.update_task_list() 
 
    def update_task_list(self): 
        self.task_list.clear_widgets() 
        for task in self.tasks: 
            task_label = Label(text=f"{task.name} - {task.category} - {task.due_date} - {task.priority}") 
            completed_checkbox = CheckBox(active=task.completed) 
            completed_checkbox.bind(active=lambda checkbox, value: self.toggle_task_completion(task)) 
            self.task_list.add_widget(task_label) 
            self.task_list.add_widget(completed_checkbox) 
 
    def toggle_task_completion(self, task): 
        task.completed = not task.completed 
        self.save_tasks() 
        self.update_task_list() 
 
if __name__ == '__main__': 
    TaskTrackerApp().run() 
from kivymd.uix.pickers import MDDatePicker 
            self.due_date_input = TextInput(hint_text='Enter Due Date', size_hint_y=None, height=40) 
        date_picker_btn = Button(text='Pick Due Date', size_hint_y=None, height=40) 
        date_picker_btn.bind(on_press=self.open_date_picker) 
        layout.add_widget(date_picker_btn) 
    def open_date_picker(self, instance): 
        date_picker = MDDatePicker() 
        date_picker.bind(on_save=self.set_due_date) 
        date_picker.open() 
    def set_due_date(self, instance, value, *args): 
            self.due_date_input.text = value.strftime('m-d') 
