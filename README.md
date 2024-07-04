# Calculator App

This is a simple web-based calculator application built using Streamlit. The app allows users to perform a variety of arithmetic operations, including trigonometric functions and memory storage capabilities.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Square Root
- Exponentiation
- Sine
- Cosine
- Tangent
- Error handling for division by zero and square root of negative numbers
- Memory functions (Store, Recall, Clear)
- Reset functionality

## Installation

To run this app, you'll need to have Python and Streamlit installed. If you don't have Streamlit installed, you can do so using pip:

```sh
pip install streamlit
```

## Usage
1. Clone this repository or copy the code to your local machine.
```
git clone https://github.com/MLVoyager3791/Calculator.git
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
```calculate(operation, num1, num2=0)```: This function performs the arithmetic and trigonometric operations based on the selected operation. It supports addition, subtraction, multiplication, division, square root, exponentiation, sine, cosine, and tangent. It also handles division by zero and square root of negative numbers by returning an error message.

```main()```: This is the main function that runs the Streamlit app. It sets up the UI, takes user input, performs calculations, displays the results, and handles memory functions.

#### **Streamlit Components**
```st.title()```: Display text in title formatting. \
```st.sidebar.title()```: Sets the title for the sidebar. \
```st.sidebar.selectbox()```: Creates a dropdown menu in the sidebar for selecting the arithmetic operation. \
```st.number_input()```: Creates input fields for the user to enter numbers. \
```st.button()```: Creates buttons for performing calculations and resetting the app. \
```st.success()```: Displays the result of the calculation. \
```st.error()```: Displays error messages. \
```st.sidebar.subheader()```: Sets a subheader in the sidebar. \
```st.session_state```: Stores and manages memory values. \
```st.experimental_rerun()```: Reruns the app to reset the input fields.

## Acknowledgments
[Streamlit Documentation](https://docs.streamlit.io/)<br>
[Python Documentation](https://docs.python.org/3.11/)

For me, this project has been an exciting journey in learning and exploring Streamlit's capabilities, providing a hands-on approach to understanding its functionalities.
