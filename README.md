# Basic Calculator App

This is a simple web-based calculator application built using Streamlit. The app allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Error handling for division by zero
- Reset functionality

## Installation

To run this app, you'll need to have Python and Streamlit installed. If you don't have Streamlit installed, you can do so using pip:

```sh
pip install streamlit
```

## Usage
1. Clone this repository or copy the code to your local machine.
```
git clone <repository-url>
```
2. Navigate to the directory containing the code.
```
cd <repository-directory>
```
3. Run the main.py using Streamlit:
```sh
streamlit run main.py
```
4. Once the app is running, Streamlit will provide a local URL (usually http://localhost:8501). Open this URL in your web browser to use the calculator app.

## Code Explanation
#### **Functions**
```calculate(operation, num1, num2=0)```: This function performs the basic arithmetic operations based on the selected operation. It supports addition, subtraction, multiplication, and division. It also handles division by zero by returning an error message.

```main()```: This is the main function that runs the Streamlit app. It sets up the UI, takes user input, performs calculations, and displays the results.

#### **Streamlit Components**
```st.title()```: Display text in title formatting. \
```st.sidebar.title()```: Sets the title for the sidebar. \
```st.sidebar.selectbox()```: Creates a dropdown menu in the sidebar for selecting the arithmetic operation. \
```st.number_input()```: Creates input fields for the user to enter numbers. \
```st.button()```: Creates buttons for performing calculations and resetting the app. \
```st.success()```: Displays the result of the calculation. \
```st.error()```: Displays error messages. \
```st.experimental_rerun()```: Reruns the app to reset the input fields.

## Acknowledgments
[Streamlit Documentation](https://docs.streamlit.io/)<br>
[Python Documentation](https://docs.python.org/3.11/)
