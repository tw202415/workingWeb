from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, allowed_urls, parent=None):
        super().__init__(parent)
        self.allowed_urls = allowed_urls

    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        # 檢查是否在允許的網址列表中
        if url.toString() not in self.allowed_urls:
            QMessageBox.warning(None, "禁止訪問", f"您嘗試訪問的網址被限制：{url.toString()}")
            return False  # 阻止導航
        return True  # 允許導航

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自訂瀏覽器")
        self.setGeometry(100, 100, 800, 600)

        # 設定允許的網址
        self.allowed_urls = [
            "https://www.elf.com.tw/",
            "https://another-allowed.com"
        ]
        self.home_url = self.allowed_urls[0]  # 設定首頁

        # 創建 WebEngineView
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # 使用自訂的 WebEnginePage
        self.browser.setPage(CustomWebEnginePage(self.allowed_urls))

        # 加載首頁
        self.browser.setUrl(QUrl(self.home_url))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
