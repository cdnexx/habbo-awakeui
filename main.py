from PyQt5 import QtWidgets

from habbo_awakeui import UiMainWindow
import json
import pyautogui


def read_config():
    with open("config.json") as config_file:
        configs = json.load(config_file)
    start_time = configs["timeConfig"]["startTime"]
    between_time = configs["timeConfig"]["betweenTime"]
    travel_time = configs["timeConfig"]["travelTime"]
    return start_time, between_time, travel_time


config = read_config()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(start_time=config[0], between_time=config[1], travel_time=config[2])
    ui.setup_ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
