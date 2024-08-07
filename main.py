from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.scrollview import ScrollView 
 
class TaskTrackerApp(App): 
    def build(self): 
        self.tasks = self.load_tasks() 
        self.layout = BoxLayout(orientation='vertical') 
 
        self.task_input = TextInput(hint_text='Enter a task', size_hint=(1, 0.1)) 
        self.layout.add_widget(self.task_input) 
 
        self.add_task_button = Button(text='Add Task', size_hint=(1, 0.1)) 
        self.add_task_button.bind(on_press=self.add_task) 
        self.layout.add_widget(self.add_task_button) 
 
        self.task_list_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.8)) 
 
        self.scroll_view = ScrollView(size_hint=(1, 0.8)) 
        self.scroll_view.add_widget(self.task_list_layout) 
        self.layout.add_widget(self.scroll_view) 
 
        self.display_tasks() 
 
        return self.layout 
 
    def add_task(self, instance): 
        task_text = self.task_input.text 
        if task_text: 
            self.tasks.append(task_text) 
            self.task_input.text = '' 
            self.save_tasks() 
            self.display_tasks() 
 
    def delete_task(self, task_label): 
        task_text = task_label.text 
        if task_text in self.tasks: 
            self.tasks.remove(task_text) 
            self.save_tasks() 
            self.display_tasks() 
 
    def display_tasks(self): 
        self.task_list_layout.clear_widgets() 
        for task in self.tasks: 
            task_label = Label(text=task, size_hint=(1, None), height=40) 
            delete_button = Button(text='Delete', size_hint=(0.2, 1)) 
            delete_button.bind(on_press=lambda instance, task_label=task_label: self.delete_task(task_label)) 
 
            task_layout = BoxLayout(size_hint=(1, None), height=40) 
            task_layout.add_widget(task_label) 
            task_layout.add_widget(delete_button) 
 
            self.task_list_layout.add_widget(task_layout) 
 
    def load_tasks(self): 
        if os.path.exists('data/tasks.json'): 
            with open('data/tasks.json', 'r') as file: 
                return json.load(file) 
        return [] 
 
    def save_tasks(self): 
        with open('data/tasks.json', 'w') as file: 
            json.dump(self.tasks, file) 
 
if __name__ == "__main__": 
    TaskTrackerApp().run() 
