from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
import sympy as sp


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculus Calculator')
        self.setFixedSize(400, 400)
        self.init_ui()

    def init_ui(self):
        label_func = QLabel('Function f(x):')
        self.edit_func = QLineEdit()

        label_x = QLabel('Variable x:')
        self.edit_x = QLineEdit()

        label_a = QLabel('Left endpoint a:')
        self.edit_a = QLineEdit()

        label_b = QLabel('Right endpoint b:')
        self.edit_b = QLineEdit()

        label_result = QLabel('Result:')
        self.result = QLabel('')

        btn_limit = QPushButton('Calculate Limit')
        btn_limit.clicked.connect(self.calculate_limit)

        btn_derivative = QPushButton('Calculate Derivative')
        btn_derivative.clicked.connect(self.calculate_derivative)

        btn_extrema = QPushButton('Find Extrema')
        btn_extrema.clicked.connect(self.find_extrema)

        btn_integral = QPushButton('Calculate Integral')
        btn_integral.clicked.connect(self.calculate_integral)

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
        vbox.addWidget(btn_integral)
        vbox.addWidget(label_result)
        vbox.addWidget(self.result)
        self.setLayout(vbox)

    def calculate_limit(self):
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())
        x0 = self.edit_a.text()
        while x0 != '':
        #cannot put the function together because -oo and oo is not float and cannot translate to float
            if x0 == 'oo': #calculate when reach infinity 
                lim = sp.limit(f, x, x0)
                msg_box = QMessageBox()
                msg_box.setText(f'Limit: {lim}')
                msg_box.exec_()
                break
            if x0 == '-oo':
                lim = sp.limit(f,x,x0)
                msg_box = QMessageBox()
                msg_box.setText(f'Limit: {lim}')
                msg_box.exec_()
                break
            else:
                lim = sp.limit(f, x, float(x0))
                msg_box = QMessageBox()
                msg_box.setText(f'Limit: {lim}')
                msg_box.exec_()
                break
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

    def find_extrema(self):
        f = sp.sympify(self.edit_func.text())
        x = sp.Symbol(self.edit_x.text())
        df = sp.diff(f, x)
        eqs = [df,]
        points = sp.solve(eqs, x)
        hessian = sp.Matrix([[sp.diff(sp.diff(f, x), y) for x in [x]] for y in [x]])
        for p in points:
            sub_matrix = hessian.subs(x, p)
            if sub_matrix.det() > 0:
                msg_box = QMessageBox()
                msg_box.setText(f'Local minimum at {p}')
                msg_box.exec_()
            elif sub_matrix.det() < 0:
                msg_box = QMessageBox()
                msg_box.setText(f'Local maximum at {p}')
                msg_box.exec_()
            else:
                msg_box = QMessageBox()
                msg_box.setText(f'Cannot determine extrema at {p}')
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
            msg_box.setText(f'Integral: {indefinite_integral}')
            msg_box.exec_()
        else:
            a = float(a)
            b = float(b)
            definite_integral = sp.integrate(f, (x, a, b))
            msg_box = QMessageBox()
            msg_box.setText(f'Integral: {definite_integral}')
            msg_box.exec_()

       
if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()