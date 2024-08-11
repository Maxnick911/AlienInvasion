# Alien Invasion

Alien Invasion is a Python game project developed using the Pygame library. This README provides detailed instructions for setting up the project environment and running the game.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Dependencies](#dependencies)
- [Running the Game](#running-the-game)
- [Troubleshooting](#troubleshooting)

## Project Overview

Alien Invasion is a Python game built using the Pygame library. The objective of the game is to defend Earth from waves of invading aliens. The player controls a spaceship and must shoot down aliens while avoiding their attacks.

## Setup Instructions

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**

    Clone this repository with:

    ```bash
    git clone https://github.com/Maxnick911/alien_invasion
    ```

2. **Navigate into the Project Directory**

    ```bash
    cd alien_invasion
    ```

3. **Install `virtualenv`**

    If `virtualenv` is not installed, install it using pip:

    ```bash
    pip install virtualenv
    ```

4. **Setup Environment**

    Create a virtual environment:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

5. **Install Dependencies**

    This project requires the Pygame library. Install it using pip:

    ```bash
    pip install pygame==2.6.0
    ```

## Running the Game

Once you have set up the environment and installed the dependencies, you can run the game with:

```bash
python alien_invasion.py
```
