## 現況
- bottom-nav botton 觸發範圍RWD

## prompt
- 我希望調整每一個news block的高度，你可以幫我基於下列程式碼做優化嗎？
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

.bottom-nav a {
  position: relative;
}

/* 調整 top、left、right、bottom 的值以擴大觸發範圍
.bottom-nav a::before {
  content: "";
  position: absolute;
  top: -60px; 
  left: -300px;
  right: -300px;
  bottom: -60px;
}

@media (max-width: 600px) {
  .bottom-nav {
    flex-direction: column;
  }
} */

.bottom-nav a::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -800%;
  right: -800%;
  bottom: -50%;
  /* transform: translate(-50%, -50%); */
}

/* @media (max-width: 768px) {
  .bottom-nav a::before {
    top: -25%;
    left: -25%;
    right: -25%;
    bottom: -25%;
  }
} */

.bottom-nav a img {
  width: 36px;
  height: 36px;
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
  margin-top: 200px; /* 調整上邊距的數值，使整個區塊向下移動 */
}

/* 新增CSS樣式 */
#chartContainer {
  max-width: 100%;
  height: auto;
  margin: 50px;
  margin-bottom: 200px;
  /* display: block; */
  display: flex; /* 使用flex布局 */
  justify-content: right; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
  border: 1px solid black; /* 添加框線樣式 */
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
- 我想在News block(news-banner)的物件上方增加文字，我希望有一個標題、兩到三個tag和一個可以擺多媒體（影片/圖）檔案的位置。我希望的位置是標題左上，tag左下，多媒體右側。左側與右側的比例大概是3:2。請幫我修改news-banner物件或是剛剛的css的內容。
```html
<div class="news-banner">
  <p>News 1</p>
</div>
```

## 回覆

## 結果
- 先留著code，有空再修