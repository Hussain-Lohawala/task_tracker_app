# Task Tracker App 
 
This is an advanced mobile application developed using Python and the Kivy framework. The app provides a user-friendly interface to manage tasks with the following features: 
 
- **Add Tasks:** Enter and add tasks to your list. 
- **Delete Tasks:** Remove tasks from your list. 
- **Persist Tasks:** Tasks are saved to and loaded from a JSON file, ensuring persistence across app restarts. 
- **Scrollable Task List:** Tasks are displayed in a scrollable view. 
 
## Setup Instructions 
 
1. Clone the repository: 
\`\`\`bash 
git clone https://github.com/hussain-lohawala/task_tracker_app.git 
\`\`\` 
 
2. Navigate to the project directory: 
\`\`\`bash 
cd task_tracker_app 
\`\`\` 
 
3. Create and activate a virtual environment: 
\`\`\`bash 
python -m venv venv 
venv\Scripts\activate  
\`\`\` 
 
4. Install the dependencies: 
\`\`\`bash 
pip install -r requirements.txt 
\`\`\` 
 
5. Run the application: 
\`\`\`bash 
python main.py 
\`\`\` 
 
## Usage 
 
- Enter a task in the input field and click "Add Task" to add it to your task list. 
- Click "Delete" next to a task to remove it from the list. 
- Tasks are automatically saved and loaded from the `data/tasks.json` file. 
