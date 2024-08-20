# Human Verification System

## Overview

The Human Verification System is a Python-based graphical application that verifies if the user is a human by displaying an image and asking the user to identify it. The project uses the Tkinter library for the graphical interface and the PIL library for image processing. The program randomly selects an image from a specified directory and prompts the user to identify the correct object from a set of options.

## Features

- **Image Display:** The application displays an image from a specified directory.
- **Randomized Options:** The options for identifying the image are shuffled to ensure randomness.
- **Verification Process:** The user is prompted to select the correct description of the displayed image. If the correct option is selected, the user is successfully verified. Otherwise, the user can try again.
- **User-Friendly Interface:** The application has a simple, intuitive GUI designed using the Tkinter library.

## Getting Started

### Prerequisites

- **Python 3.x**
- **PIL (Pillow)** library

You can install the required library using pip:

```bash
pip install pillow
```

## Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/YourUsername/Human_Verification_System.git
```
Navigate to the project directory:
```bash
cd Human_Verification_System
```
Run the application:
```bash
python human_verification.py
```
Directory Setup
Place the images you want to use for the verification in a directory on your system. Update the directory variable in the on_verify_click() function to point to your image directory:
directory = "C:\\Users\\YourUsername\\Path\\To\\Images"
The application supports the following image formats: .png, .jpg, .jpeg, .gif.

## Usage
Launch the application. A window will appear with a prompt asking if you are human.
Click "Click here to verify". The application will randomly select and display an image from the specified directory.
Identify the image by clicking the correct option from the provided choices. The options are shuffled each time.
Verification Result: If you select the correct option, you will see a "Verified Successfully" message. If not, you'll be prompted to try again.

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## Acknowledgments
This project was developed by Your Name. It was created as a fun and interactive way to verify that a user is human.
