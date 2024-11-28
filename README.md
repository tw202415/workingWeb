# **公司專用瀏覽器**

這是一款為公司設計的多分頁瀏覽器，使用 Python 和 PyQt5 開發。瀏覽器內置公司特定連結，提供專業且簡潔的用戶界面，專為提高員工工作效率而設計。

---

## **功能特色**

- **多分頁瀏覽**：支援多個分頁，方便同時打開多個網頁。
- **預設菜單**：快速訪問公司重要網站：
  - 公司首頁：[www.elf.com.tw](https://www.elf.com.tw)
  - 文檔系統：[book.elfvip.com](https://book.elfvip.com/#/wiki)
  - 104 打卡系統：[pro.104.com.tw](https://pro.104.com.tw/)
  - 內部對話系統：[elf-im](https://elf-im.elf.tw/#/login)
- **明暗模式切換**：一鍵切換明暗主題，適應不同使用環境。
- **響應式設計**：根據窗口大小動態調整界面元素，保持美觀與實用性。
- **專業 UI 設計**：簡潔大方的界面風格，適合公司使用場景。

---

## **安裝步驟**

### **1. 環境要求**
- 安裝 Python（建議使用 3.8 或更高版本）。
- 安裝必要的 Python 套件：
  ```bash
  pip install PyQt5 PyQtWebEngine
  ```

### **2. 克隆專案**
從 GitHub 克隆此專案：
```bash
git clone https://github.com/tw202415/workingWeb.git
cd workingWeb
```

### **3. 運行應用**
執行主程式：
```bash
python company_browser.py
```

---

## **檔案結構**

```plaintext
workingWeb/
├── dist/                     # 發行版本文件夾（包含可執行文件）
├── icons/                    # 圖標文件夾（包含明暗模式切換圖標）
├── src/                      # 瀏覽器源代碼
│   └── company_browser.py    # 主程式
├── README.md                 # 專案說明文件
└── .gitignore                # Git 忽略文件配置
```

---

## **使用方法**

1. 運行 `company_browser.py` 開啟應用程式。
2. 使用左側菜單快速訪問預設的公司網站。
3. 添加、關閉或切換分頁以滿足多任務需求。
4. 點擊設置圖標切換明暗模式。

---
