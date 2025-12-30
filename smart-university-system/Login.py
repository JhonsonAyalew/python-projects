import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPoint

from Login_ui import Ui_Login
# from SuperAdmin import SuperAdmin  # uncomment when SuperAdmin exists


class Login(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Window settings
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Signals
        self.ui.pushButton_2.clicked.connect(self.login)
        self.ui.close.clicked.connect(self.close)

        self.oldPosition = QPoint()

        self.show()

    # -------------------- WINDOW DRAG --------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.oldPosition
            self.move(self.pos() + delta)
            self.oldPosition = event.globalPosition().toPoint()

    # -------------------- LOGIN LOGIC --------------------
    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jhon1995",
                database="ambo_university",
                auth_plugin="mysql_native_password"
            )

            cursor = conn.cursor()
            cursor.execute(
                "SELECT username FROM superadminlogin WHERE username=%s AND password=%s",
                (username, password)
            )

            result = cursor.fetchone()
            conn.close()

            if result:
                # self.main = SuperAdmin()
                # self.main.show()
                self.close()
            else:
                self.ui.error.setText("Username or password not correct")

        except mysql.connector.Error as e:
            self.ui.error.setText("Database connection error")
            print("DB Error:", e)


# -------------------- MAIN --------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec())
