# InsightView: A Local Data Visualization Tool

## Stage 1: Setup and Initialization

### Objectives:
- Set up the project with a focus on modularity.
- Ensure scalability and maintainability from the start.

### Steps:
#### Project Setup:
- Create a clean folder structure:
  ```
  insightview/
  ├── main.py      # Main application entry point
  ├── ui/          # UI components
  │   ├── main_window.py  # Main application window
  │   ├── table_widget.py # Dataset table widget
  │   └── chart_widget.py # Chart rendering canvas
  ├── core/        # Core logic
  │   ├── file_handler.py # File upload and parsing
  │   ├── data_cleaner.py # Data cleaning functions
  │   ├── chart_manager.py # Chart management logic
  │   └── settings.py      # Global settings and constants
  ├── assets/      # Icons, themes, and other static assets
  ├── requirements.txt
  └── README.md
  ```

#### Environment Setup:
- Install dependencies:
  ```bash
  pip install pandas matplotlib PyQt5
  ```
- Use virtual environments (venv) to isolate dependencies.

#### Create the Main Window:
- Use PyQt’s QMainWindow as the base and load modular widgets from the ui folder.
- Maintain separation between UI and core logic.

### Good Practices:
- Follow single responsibility principle (each file/class does one thing).
- Use constants in a settings.py file for easy maintenance.
- Avoid comments by naming functions and variables descriptively.
