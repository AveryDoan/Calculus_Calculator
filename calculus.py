# Import necessary modules
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
import sympy as sp

# Create a new class Calculator
class Calculator(QWidget):
    # Define a constructor method that sets window properties and calls init_ui() to initialize the user interface
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculus Calculator')
        self.setFixedSize(400, 400)
        self.init_ui()
    # Define a method to initialize the user interface
    def init_ui(self):
        
        # Create QLabel and QLineEdit objects for each input field, and a QLabel object to display the result
        label_func = QLabel('Function f(x):')
        self.edit_func = QLineEdit()

        label_x = QLabel('Variable x:')
        self.edit_x = QLineEdit()

        label_a = QLabel('Left endpoint a:')
        self.edit_a = QLineEdit()

        label_b = QLabel('Right endpoint b:')
        self.edit_b = QLineEdit()

        label_result = QLabel('')
        self.result = QLabel('')
        
        # Create QPushbutton objects for each operation, and connect them to their respective methods
        btn_limit = QPushButton('Calculate Limit')
        btn_limit.clicked.connect(self.calculate_limit)

        btn_derivative = QPushButton('Calculate Derivative')
        btn_derivative.clicked.connect(self.calculate_derivative)

        btn_extrema = QPushButton('Find Extrema')
        btn_extrema.clicked.connect(self.find_extrema)

        btn_integral = QPushButton('Calculate Integral')
        btn_integral.clicked.connect(self.calculate_integral)

        btn_gradient = QPushButton('Gradient Descent')
        btn_gradient.clicked.connect(self.find_extrema_gradient_descent)


        # Add all the widgets to a QVBoxLayout
        vbox = QVBoxLayout()
        vbox.addWidget(label_func)
        vbox.addWidget(self.edit_func)
        vbox.addWidget(label_x)
        vbox.addWidget(self.edit_x)
        vbox.addWidget(label_a)
        vbox.addWidget(self.edit_a)
        vbox.addWidget(label_b)
        vbox.addWidget(self.edit_b)
        vbox.addWidget(btn_limit)
        vbox.addWidget(btn_derivative)
        vbox.addWidget(btn_extrema)
        vbox.addWidget(btn_gradient)
        vbox.addWidget(btn_integral)
        vbox.addWidget(label_result)
        vbox.addWidget(self.result)
        
        # Set the QVBoxLayout as the layout for the QWidget
        self.setLayout(vbox)
        
    # Define a method to calculate the limit of a function    
    def calculate_limit(self):
        
         # Get the function, variable, and limit point from the input fields
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())
        x0 = self.edit_a.text()
        if x0 != '':
        #cannot put the function together because -oo and oo is not float and cannot translate to float
            if x0 == 'oo': #calculate when reach infinity 
                lim = sp.limit(f, x, x0)
                msg_box = QMessageBox()
                msg_box.setText(f'Limit: {lim}')
                msg_box.exec_()
                
            if x0 == '-oo':
                lim = sp.limit(f,x,x0)
                msg_box = QMessageBox()
                msg_box.setText(f'Limit: {lim}')
                msg_box.exec_()
                
            else:
                lim = sp.limit(f, x, float(x0))
                msg_box = QMessageBox()
                msg_box.setText(f'Limit: {lim}')
                msg_box.exec_()
        else:
            msg_box = QMessageBox()
            msg_box.setText("Please enter x0")
            msg_box.exec_()


    def calculate_derivative(self):
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())
        derivative = sp.diff(f, x)
        msg_box = QMessageBox()
        msg_box.setText(f'Derivative: {derivative}')
        msg_box.exec_()
 
            # ... (Continuing from the previous code)

    # Define a method to find extrema using derivative
    def find_extrema(self):

        # Get the function and variable from the input fields
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())

        # Calculate the derivative of the function
        f_prime = f.diff(x)

        # Find critical points by equating the derivative to zero and solving for x
        critical_points = sp.solve(f_prime, x)

        # Evaluate the second derivative at each critical point
        extrema = []
        for point in critical_points:
            f_double_prime = f_prime.diff(x)
            second_derivative = f_double_prime.subs(x, point)

            # Determine if it's a maximum or minimum
            if second_derivative > 0:
                extrema.append((point, 'Minimum'))
            elif second_derivative < 0:
                extrema.append((point, 'Maximum'))
            else:
                extrema.append((point, 'Unknown'))

        # Display the extrema in a message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Extrema')
        msg_box.setText('Extrema:')

        if len(extrema) > 0:
            text = " "
            for i in extrema:
                x_val = i[0]
                y_val = f.subs(x, x_val)
                text += f'Point ({x_val}, {y_val}), Type: {i[1]}\n'
            msg_box.setText(text)
        else:
            msg_box.setText('No extrema found.')
        msg_box.exec_()

        # ... (Continuing from the previous code)

    # Define a method to find extrema using gradient descent
    def find_extrema_gradient_descent(self):
        # Get the function, variable, and interval from the input fields
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())
        a = float(self.edit_a.text())
        b = float(self.edit_b.text())

        # Set the learning rate and maximum number of iterations
        learning_rate = 0.1
        max_iterations = 100

        # Initialize the current point and iteration counter
        x_current = (a + b) / 2  # Use the midpoint of the interval as the starting point
        iteration = 0

        # Perform gradient descent to find the extremum
        while iteration < max_iterations:

            # Calculate the derivative of the function at the current point
            f_prime = f.diff(x)
            f_prime_current = f_prime.subs(x, x_current)

            # Update the current point using the gradient descent formula
            x_current = x_current - learning_rate * f_prime_current

            # Check if the current point is within the interval [a, b]
            if x_current < a or x_current > b:
                break

            iteration += 1

        # Evaluate the function at the final point
        extremum = f.subs(x, x_current)

        # Display the extremum in a message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Extrema')
        msg_box.setText(f'Extremum: {extremum}')
        msg_box.exec_()



    def calculate_integral(self):
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())
        a = self.edit_a.text()
        b = self.edit_b.text()
        #have to do separately
        if (a == '') and (b == ''):
            indefinite_integral = sp.integrate(f, x)
            msg_box = QMessageBox()
            msg_box.setText(f'Integral: {indefinite_integral} + C')
            msg_box.exec_()
        else:
            a = float(a)
            b = float(b)
            definite_integral = sp.integrate(f, (x, a, b))
            msg_box = QMessageBox()
            msg_box.setText(f'Integral: {definite_integral} + C')
            msg_box.exec_()


       
if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
