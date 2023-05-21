## 現況
- 使用flask讓home page, search page串連，bottom-nav運作正常

## prompt
有關按鈕js code的html檔案如下，我希望可以擴大按鈕的範圍，目前是要準確地按在圖片上才能進行頁面的切換，我希望可以在不改變現有外觀的前提下，擴大「頁面切換按鈕」的觸發面積。
----------
poject_folder/
    src/
        home_page.html
        search_page.html
    static/
        home-button-black.png
        search-button-black.png
        search-button-white.png
        style.css
    server.py
----------
```html
<!-- home_page.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- <link rel="stylesheet" type="text/css" href="style.css"> -->
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
  <title>Home Page</title>
</head>
<body>
  <div id="home-page">
    <div class="banner">
      <h1 class="centered-title brusher-font">TruthWeaver</h1>
    </div>
    <div class="content">
      <div class="square-object d3-object">
        <p>D3.js</p>
      </div>
    </div>
    <div class="bottom-nav">
      <a href="home_page.html"><img src="../static/home-button-black.png" alt="Home Page"></a>
      <a href="search_page.html"><img src="../static/search-button-black.png" alt="Search Page"></a>
    </div>
  </div>
</body>
</html>
```
----------
```html
<!-- search_page.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Search Page</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div id="search-page">
    <div class="search-bar">
      <input type="text" id="search-input" placeholder="輸入關鍵字...">
      <button id="search-button" class="search-button-img">搜尋</button>
    </div>
    <div class="content">
      <div class="news-blocks">
        <div class="news-banner">
          <p>News 1</p>
        </div>
        <div class="news-banner">
          <p>News 2</p>
        </div>
        <div class="news-banner">
          <p>News 3</p>
        </div>
        <div class="news-banner">
          <p>News 4</p>
        </div>
        <div class="news-banner">
          <p>News 5</p>
        </div>
        <div class="news-banner">
          <p>News 6</p>
        </div>
        <div class="news-banner">
          <p>News 7</p>
        </div>
        <div class="news-banner">
          <p>News 8</p>
        </div>
        <div class="news-banner">
          <p>News 9</p>
        </div>
        <div class="news-banner">
            <p>News 10</p>
        </div>
      </div>
    </div>
    <div class="bottom-nav">
      <a href="home_page.html"><img src="../static/home-button-black.png" alt="Home"></a>
      <a href="search_page.html"><img src="../static/search-button-black.png" alt="Search"></a>
    </div>
  </div>

  <script>
    // JavaScript程式碼可以在這裡添加
    // 將搜索欄的操作邏輯放在這裡
    const searchButton = document.getElementById("search-button");
    const searchInput = document.getElementById("search-input");

    searchButton.addEventListener("click", function () {
      const keyword = searchInput.value;
      // 在這裡執行相應的搜尋操作
      // 可以呼叫API、擷取資料，或者執行其他操作
      console.log("搜尋關鍵字：" + keyword);
    });
  </script>
</body>
</html>
```
----------
```css
/* style.css */
/* General */
body {
  background-color: #003366;
  color: #CCCCCC;
  margin: 0;
  padding: 0;
}

/* Bottom Navigation */
.bottom-nav {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #f2f2f2;
  padding: 20px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 999;
}

.bottom-nav a img {
  width: 36px;
  height: 36px;
}

@media (max-width: 600px) {
  .bottom-nav {
    flex-direction: column;
  }
}

/* Home Page */
#home-page .banner {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #CCCCCC;
  
}

#home-page .banner h1 {
  font-family: Brusher, cursive;
  font-size: 48px;
  margin-top: 5px;
  font-weight: bold;
  color: #003366;
  padding: 0px;
  height: 42px;
}

#home-page .content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 400px);
}

#home-page .square-object {
  border: 2px solid #CCCCCC;
  border-radius: 10px;
  width: 200px;
  height: 200px;
  background-color: #FFFFFF;
  display: flex;
  justify-content: center;
  align-items: center;
}

#home-page .square-object p {
  color: #FF0000;
  font-size: 20px;
}

/* Search Page */
#search-page .search-bar {
  position: sticky;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #CCCCCC;
  padding: 20px;
  z-index: 999;
}

#search-page .search-bar input[type="text"] {
  padding: 10px;
  font-size: 16px;
  border-radius: 4px;
  border: none;
  outline: none;
}

#search-page .search-bar button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #003366;
  color: #FFFFFF;
  border: none;
  border-radius: 4px;
  margin-left: 10px;
  text-indent: -9999px;
}

#search-page .search-bar button.search-button-img {
  background-image: url("../static/search-button-white.png"); /* 圖片的路徑 */
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  /* 其他樣式設定 */
}

#search-page .content {
  margin-top: 100px;
  padding: 20px;
}

#search-page .news-blocks {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 20px;
}

.news-banner {
  background-color: #CCCCCC;
  border: 1px solid #CCCCCC;
  border-radius: 8px;
  height: 100px;
  display: flex;
  align-items: center;
  padding: 10px;
}

.news-banner p {
  color: #FF0000;
}
```
----------
```python
<!-- server.py -->
from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='src', static_folder='static')

# # 定義路由端點，處理根目錄的 GET 請求
# @app.route('/', methods=['GET'])
# def hello():
#     return 'Hello, World!'

@app.route('/')
def home():
    return render_template("home_page.html")

# 定義另一個路由端點，處理 /get_keywords 的 GET 請求
@app.route('/get_keywords', methods=['GET'])
def get_keywords():
    # 在這裡呼叫您的 Python 函數以獲取關鍵字列表
    keywords = ['Keyword 1', 'Keyword 2', 'Keyword 3']
    
    # 將關鍵字列表回傳為 JSON 格式
    return jsonify(keywords)

if __name__ == '__main__':
    app.run()
```
----------

## 回覆
如果您不想改變 .bottom-nav 的高度，但仍希望擴大「Home Page」和「Search Page」按鈕的觸發範圍，您可以使用 CSS 的 ::before 或 ::after 偽元素來實現。這將允許您在不影響 .bottom-nav 外觀的情況下，增加可點擊的區域。

以下是修改後的 CSS 範例：
```css
/* style.css */

.bottom-nav a {
  position: relative;
}

.bottom-nav a::before {
  content: "";
  position: absolute;
  top: -10px; /* 調整 top、left、right、bottom 的值以擴大觸發範圍 */
  left: -10px;
  right: -10px;
  bottom: -10px;
}

.bottom-nav a img {
  width: 36px;
  height: 36px;
}

```

## 結果
- 調整非常成功，雖然觸發距離多長是通過測試測出來的