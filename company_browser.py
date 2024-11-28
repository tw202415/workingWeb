import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QSplitter, QFrame, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon

def resource_path(relative_path):
    """
    獲取資源的絕對路徑，適用於本地執行和打包後的環境。
    """
    if hasattr(sys, '_MEIPASS'):  # PyInstaller 打包後的臨時資料夾
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class CompanyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("公司專屬瀏覽器")

        # 初始化狀態
        self.menu_visible = True
        self.light_mode = True  # 預設為開燈模式

        # 主框架
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 使用 QSplitter 將菜單和主內容分開
        self.splitter = QSplitter(Qt.Horizontal, self.central_widget)

        # 左側菜單框架
        self.menu_frame = QFrame()
        self.menu_frame.setFixedWidth(250)  # 設定固定寬度
        self.menu_layout = QVBoxLayout()
        self.menu_layout.setAlignment(Qt.AlignTop)  # 向上對齊
        self.menu_layout.setSpacing(15)  # 控制按鈕間距
        self.menu_frame.setLayout(self.menu_layout)

        # 添加原始四個菜單按鈕
        self.add_menu_buttons()

        # 添加小按鈕區域（水平佈局）
        self.small_buttons_layout = QHBoxLayout()
        self.small_buttons_layout.setAlignment(Qt.AlignLeft)  # 置左
        self.menu_layout.addStretch()  # 增加彈性空間，將水平佈局推到底部
        self.menu_layout.addLayout(self.small_buttons_layout)

        # 添加「純圖片按鈕」
        self.add_small_button(resource_path("moon.png"), self.toggle_light_mode)  # 初始圖案為 moon

        # 主內容區域（多分頁瀏覽器）
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)  # 啟用分頁關閉
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # 在分頁中添加首頁
        self.add_tab("https://www.elf.com.tw", "公司首頁")

        # 添加箭頭按鈕（位於菜單和主內容之間）
        self.toggle_menu_button = QPushButton("←")
        self.toggle_menu_button.setFixedWidth(30)  # 固定寬度
        self.toggle_menu_button.setObjectName("toggle_menu_button")
        self.toggle_menu_button.clicked.connect(self.toggle_menu)

        # 將菜單、箭頭按鈕和多分頁瀏覽器加入分隔器
        self.splitter.addWidget(self.menu_frame)
        self.splitter.addWidget(self.toggle_menu_button)
        self.splitter.addWidget(self.tabs)
        self.splitter.setStretchFactor(0, 1)  # 菜單佔少部分空間
        self.splitter.setStretchFactor(2, 5)  # 主瀏覽區域佔主要空間

        # 將分隔器設置為主框架
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.addWidget(self.splitter)

        # 設定樣式
        self.apply_light_mode()

    def add_menu_buttons(self):
        # 添加左側的四個按鈕
        buttons = {
            "公司首頁": "https://www.elf.com.tw",
            "文檔系統": "https://book.elfvip.com/#/wiki",
            "104登入": "https://pro.104.com.tw/",
            "對話軟體": "https://elf-im.elf.tw/#/login"
        }

        for label, url in buttons.items():
            button = QPushButton(label)
            button.setObjectName("menu_button")
            button.clicked.connect(lambda _, link=url, name=label: self.add_tab(link, name))
            self.menu_layout.addWidget(button)

    def add_tab(self, url, name):
        # 創建新分頁
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))

        # 調整網頁縮放比例
        browser.setZoomFactor(1.2)  # 1.0 表示 100%，1.2 表示 120%

        # 在分頁中顯示
        self.tabs.addTab(browser, name)
        self.tabs.setCurrentWidget(browser)  # 切換到新分頁

    def close_tab(self, index):
        # 處理分頁關閉
        self.tabs.removeTab(index)

    def toggle_menu(self):
        # 控制菜單顯示或隱藏
        if self.menu_visible:
            self.menu_frame.hide()
            self.toggle_menu_button.setText("→")  # 更換為右箭頭
        else:
            self.menu_frame.show()
            self.toggle_menu_button.setText("←")  # 更換為左箭頭
        self.menu_visible = not self.menu_visible  # 切換狀態

    def toggle_light_mode(self):
        # 切換燈光模式並更新按鈕圖案
        self.light_mode = not self.light_mode
        if self.light_mode:
            self.apply_light_mode()
            self.update_small_button_icon(0, resource_path("moon.png"))  # 開燈顯示 moon
        else:
            self.apply_dark_mode()
            self.update_small_button_icon(0, resource_path("sun.png"))  # 關燈顯示 sun

    def add_small_button(self, icon_path, callback):
        # 添加純圖片按鈕到水平佈局
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(button.sizeHint())
        button.setStyleSheet("border: none; background: none;")  # 移除背景和邊框
        button.clicked.connect(callback)
        self.small_buttons_layout.addWidget(button)

    def update_small_button_icon(self, index, icon_path):
        # 更新水平佈局中的按鈕圖案
        button = self.small_buttons_layout.itemAt(index).widget()
        if button:
            button.setIcon(QIcon(icon_path))

    def apply_light_mode(self):
        # 開燈模式樣式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QPushButton {
                border-radius: 10px;
                background-color: #E0F7FA;
                color: #006064;
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
                font-family: 'Microsoft JhengHei';
            }
            QPushButton:hover {
                background-color: #B2EBF2;
            }
            QPushButton:pressed {
                background-color: #80DEEA;
                border: 1px solid #004D40;
            }
            #menu_button {
                background-color: #FFF9C4;
                color: #827717;
            }
        """)

    def apply_dark_mode(self):
        # 關燈模式樣式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #212121;
            }
            QPushButton {
                border-radius: 10px;
                background-color: #424242;
                color: #E0E0E0;
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
                font-family: 'Microsoft JhengHei';
            }
            QPushButton:hover {
                background-color: #616161;
            }
            QPushButton:pressed {
                background-color: #757575;
                border: 1px solid #E0E0E0;
            }
            #menu_button {
                background-color: #757575;
                color: #FFFFFF;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompanyBrowser()
    window.show()
    sys.exit(app.exec_())
