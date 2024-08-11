
# Alien Invasion

Alien Invasion is a Python game project developed using the Pygame library. This README provides detailed instructions for setting up the project environment and running the game.

## Dependencies

To run this project, you need to install several dependencies. The required dependencies are:

- `distlib==0.3.8`
- `filelock==3.14.0`
- `platformdirs==4.2.2`
- `pygame==2.6.0`
- `virtualenv==20.26.2`

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Create a Virtual Environment

To avoid conflicts with other Python projects, it's recommended to create a virtual environment. Run the following command:

```
virtualenv venv
```
This will create a directory named venv in your project folder that will contain a separate Python environment.

### 2. Activate the Virtual Environment

Activate the virtual environment to start using it:

```
venv\Scripts\activate
```

You should see (venv) at the beginning of your command prompt, indicating that the virtual environment is active.

### 3. Create a requirements.txt File

To simplify the installation of dependencies, you should create a requirements.txt file if it does not already exist. Add the following content to requirements.txt:

```
distlib==0.3.8
filelock==3.14.0
platformdirs==4.2.2
pygame==2.6.0
virtualenv==20.26.2
```

### 4. Install Dependencies
With the virtual environment activated, install all required dependencies using pip:

```
pip install -r requirements.txt
```

This command reads the requirements.txt file and installs the specified packages.

### 5. Run the Project
To start the game, execute the alien_invasion.py script:

```
python alien_invasion.py
```

This will launch the Alien Invasion game.