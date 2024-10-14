**Data Cleaning and Preprocessing App**
First of all 
create Virtual Environment in your Visual Studio code.
To create a virtual environment in Visual Studio Code (VS Code), follow these steps:

### Step 1: Install Python
Ensure you have Python installed. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

### Step 2: Install Python Extension for VS Code
1. Open VS Code.
2. Click on the Extensions icon in the sidebar or press `Ctrl + Shift + X`.
3. Search for **Python** and install the extension developed by Microsoft.

### Step 3: Create a Virtual Environment
1. Open a terminal in VS Code (press `Ctrl + ` or go to **Terminal > New Terminal**).
2. Navigate to your project folder using the `cd` command. Example:
   ```bash
   cd path/to/your/project
   ```
3. Run the following command to create a virtual environment:
   - For Windows:
     ```bash
     python -m venv venv
     ```
   - For Mac/Linux:
     ```bash
     python3 -m venv venv
     ```

   This creates a folder named `venv` in your project directory, which contains your virtual environment.

### Step 4: Activate the Virtual Environment
- For Windows:
  ```bash
  .\venv\Scripts\Activate
  ```
- For Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

After activation, your terminal prompt will change to indicate that you're working within the virtual environment.

### Step 5: Set the Python Interpreter in VS Code
1. Press `Ctrl + Shift + P` to open the Command Palette.
2. Search for **Python: Select Interpreter** and click it.
3. Choose the interpreter from the `venv` directory, which usually looks like `./venv/bin/python`.

### Step 6: Install Packages 
You can now install packages one by one into the virtual environment using `pip`. 
```bash
pip install streamlit
pip install matoplotlib
pip install seaborn
```

Then you need to paste command
```
 streamlit run F:\NAVTTC\Data_cleaning_app\main.py
```
And yout App will open in Browser

![image](https://github.com/user-attachments/assets/8070141a-8e61-4f06-a3b2-648d4f57074c)

