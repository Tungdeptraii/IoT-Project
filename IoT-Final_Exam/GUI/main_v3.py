import sys
import time
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QSizePolicy,
    QMessageBox, QFileDialog
)
from PyQt5.QtCore import QTimer
from otherwindow import Ui_OtherWindow
from uart import Ui_MainWindow
from function import Function_UI
import serial.tools.list_ports
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
#plt.style.use('fast')


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.other_window = None
        self.ouic = None

        self.serial = Function_UI()
        self.pv_values = []
        self.sp_values = []
        self.temp_values = []
        self.time_values = []

        self.start_time = time.time()
        self.csv_file = None
        self.csv_writer = None
        self.last_saved_time = time.time()

        for baud in self.serial.baudList.keys():
            self.uic.baud_List.addItem(baud)
        self.uic.baud_List.setCurrentText('9600')

        self.update_ports()
        self.uic.connect_Button.clicked.connect(self.connect_serial)
        self.uic.update_Button.clicked.connect(self.update_ports)
        self.serial.data_available.connect(self.split)
        self.uic.clear_Button.clicked.connect(self.clear)
        self.uic.send_Button_2.clicked.connect(self.send_data)
        self.uic.send_Button.clicked.connect(self.send_pid)
        self.uic.actionad.triggered.connect(self.open_zn)
        

        # Timer to periodically update plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)  # Update plot every 100ms

        # Timer to save data every 1 second
        self.save_timer = QTimer()
        self.save_timer.timeout.connect(self.save_data)
        self.save_timer.start(50)  # Save data every 10ms 

        # Initialize matplotlib canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        # Set layout for graphicsView
        layout = QVBoxLayout(self.uic.graphicsView)
        layout.addWidget(self.canvas)

        self.is_connected = False

    def connect_serial(self):
        if self.uic.connect_Button.isChecked():
            port = self.uic.port_List.currentText()
            baud = self.uic.baud_List.currentText()
            self.serial.serialPort.port = port
            self.serial.serialPort.baudrate = int(baud)
            try:
                self.serial.connect_serial()
                if self.serial.serialPort.is_open:
                    self.is_connected = True  
                    self.uic.connect_Button.setText("Connected")
                    # self.uic.connect_Button.setStyleSheet(
                    #     "background-color: #e74242; color: #ffffff; border: 0.5px solid #ffffff;"
                    # )

                    # Prompt to create CSV file
                    file_path, _ = QFileDialog.getSaveFileName(
                        self.main_win, "Save data to CSV", "", "CSV Files (*.csv)"
                    )
                    if file_path:
                        self.csv_file = open(file_path, mode="w", newline="")
                        self.csv_writer = csv.writer(self.csv_file)
                        self.csv_writer.writerow(["Time (s)", "SP", "PV1", "PV2"])  # Header
                    else:
                        self.uic.connect_Button.setChecked(False)  # Cancel connection if no file selected

            except serial.SerialException as e:
                QMessageBox.critical(
                    self.main_win,
                    "Error",
                    f"Can not connect to {port}: {str(e)}"
                )
                self.uic.connect_Button.setChecked(False)
        else:
            self.serial.disconnect_serial()
            self.is_connected = False 
            self.uic.connect_Button.setText("Connect")
            self.uic.connect_Button.setStyleSheet("")
            if self.csv_file:
                self.csv_file.close()  # Close CSV file when disconnecting
                self.csv_file = None
                self.csv_writer = None
                QMessageBox.information(self.main_win, "Info", "CSV file saved successfully!")


    def send_data(self):
        data_send = self.uic.send_Text.toPlainText().strip()
        if data_send:
            self.serial.send_data(f"SETPOINT-{data_send}\n")
        self.uic.send_Text.clear()

    def send_pid(self):
        data_kp = self.uic.send_Text_2.toPlainText().strip()
        data_ki = self.uic.send_Text_3.toPlainText().strip()
        data_kd = self.uic.send_Text_4.toPlainText().strip()

        if data_kp:
            self.serial.send_pid(f"Kp-{data_kp}\n")
            self.uic.textBrowser_7.setPlainText(f"{data_kp}")

        if data_ki:
            self.serial.send_pid(f"Ki-{data_ki}\n")
            self.uic.textBrowser_6.setPlainText(f"{data_ki}")

        if data_kd:
            self.serial.send_pid(f"Kd-{data_kd}\n")
            self.uic.textBrowser_5.setPlainText(f"{data_kd}")

        self.uic.send_Text_2.clear()
        self.uic.send_Text_3.clear()
        self.uic.send_Text_4.clear()

    def update_ports(self):
        self.serial.update_port()
        self.uic.port_List.clear()
        self.uic.port_List.addItems(self.serial.portList)

    def split(self, data):
        try:
            # Parse data from serial (e.g., "23.4,45.6,30.0,1200")
            values = data.split(",")
            if len(values) != 4:
                raise ValueError("Invalid data format")

            sp_value, pv_value, temp_value, pwm_value = map(float, values)
            current_time = time.time() - self.start_time

            # Append data to respective lists
            self.sp_values.append(sp_value)
            self.pv_values.append(pv_value)
            self.temp_values.append(temp_value)
            self.time_values.append(current_time)

            # Update text browsers
            self.update_text_browsers(sp_value, pv_value, temp_value, pwm_value, current_time)
        except ValueError as e:
            print(f"Error processing data: {data} -> {e}")

    def update_text_browsers(self, sp_value, pv_value, temp_value, pwm_value, current_time):
        self.uic.textBrowser.setPlainText(f"{sp_value:.2f}")
        self.uic.textBrowser_2.setPlainText(f"{pv_value:.2f}")
        self.uic.textBrowser_3.setPlainText(f"{temp_value:.2f}")
        self.uic.textBrowser_4.setPlainText(f"{pwm_value:.2f}")
        self.uic.textBrowser_8.setPlainText(f"{current_time:.2f}")

    def save_data(self):
        # Save data to CSV every second
        if self.csv_writer and self.csv_file and self.sp_values and self.pv_values and self.temp_values:
            current_time = time.time() - self.start_time
            sp_value = self.sp_values[-1]
            pv_value = self.pv_values[-1]
            temp_value = self.temp_values[-1]

            self.csv_writer.writerow([current_time, sp_value, pv_value, temp_value])
            self.last_saved_time = current_time

    def update_plot(self):
        current_time = time.time() - self.start_time
        retention_time = 900  # 15 minutes in seconds

        # Chỉ xóa dữ liệu nếu đang kết nối
        if self.is_connected:
            # Remove old data beyond retention time
            while self.time_values and self.time_values[0] < current_time - retention_time:
                self.time_values.pop(0)
                self.sp_values.pop(0)
                self.pv_values.pop(0)
                self.temp_values.pop(0)

        # Clear and prepare the plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if self.time_values:  # Ensure there is data to plot
            if self.uic.checkBox.isChecked():
                ax.plot(self.time_values, self.sp_values, label='SP', color='r', linewidth=1)
            if self.uic.checkBox_2.isChecked():
                ax.plot(self.time_values, self.pv_values, label='PV', color='b', linewidth=1)
            if self.uic.checkBox_3.isChecked():
                ax.plot(self.time_values, self.temp_values, label='Temp', color='g', linewidth=1)

            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Temperature')
            ax.set_ylim(5, 25)  # Temperature range
            ax.legend(loc='upper left')

        self.canvas.draw()


    def clear(self):
        self.sp_values.clear()
        self.pv_values.clear()
        self.temp_values.clear()
        self.time_values.clear()
        self.uic.textBrowser.clear()
        self.uic.textBrowser_2.clear()
        self.uic.textBrowser_3.clear()
        self.uic.textBrowser_4.clear()
        # self.uic.textBrowser_5.clear()
        # self.uic.textBrowser_6.clear()
        # self.uic.textBrowser_7.clear()
        self.start_time = time.time()

        
        self.uic.textBrowser_8.clear()
        
        self.start_time = time.time()

    # def open_zn(self):
    #     if self.other_window is None:
    #         self.other_window = QMainWindow()
    #         self.ouic = Ui_OtherWindow()
    #         self.ouic.setupUi(self.other_window)
    #         self.ouic.Cal_Button.clicked.connect(self.ziegler)
    #         self.ouic.Fill_Button.clicked.connect(self.fill)
    #     self.other_window.show()


    def open_zn(self):

        if self.other_window is None:
            self.other_window = QMainWindow()
            self.ouic = Ui_OtherWindow()
            self.ouic.setupUi(self.other_window)

            self.ouic.Cal_Button.clicked.connect(self.ziegler)
            self.ouic.Fill_Button.clicked.connect(self.fill)


            self.other_window.destroyed.connect(self.reset_other_window)

        self.other_window.show()

    def reset_other_window(self):
        self.other_window = None

    def ziegler(self):
        Kcr = self.ouic.send_Text_6.toPlainText().strip()
        Pcr = self.ouic.send_Text_5.toPlainText().strip()
        

        if Kcr and Pcr:
            Kcr = float(Kcr)
            Pcr = float(Pcr)
            Ti = Pcr / 2
            Td = Pcr / 8
            _kp = 0.6 * Kcr
            _ki = _kp / Ti
            _kd = _kp * Td
            self.ouic.Ti.setPlainText(f"{Ti}")
            self.ouic.Td.setPlainText(f"{Td}")
            self.ouic._Kp.setPlainText(f"{_kp}")
            self.ouic._Ki.setPlainText(f"{_ki}")   
            self.ouic._Kd.setPlainText(f"{_kd}")  

    def fill(self):
        kp_value = self.ouic._Kp.toPlainText().strip()
        ki_value = self.ouic._Ki.toPlainText().strip()
        kd_value = self.ouic._Kd.toPlainText().strip()

        self.uic.send_Text_2.setPlainText(kp_value)
        self.uic.send_Text_3.setPlainText(ki_value)
        self.uic.send_Text_4.setPlainText(kd_value)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.main_win.show()
sys.exit(app.exec_())
