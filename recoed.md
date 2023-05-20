## 現況
- 調整標題顏色
- 調整search button顏色（圖）

## prompt
我有一個路徑為"img/search-button-white.png"的圖檔，我希望可以將這個圖檔顯示在以下程式碼所表示的物件上，請幫我修改html檔案或css檔案以符合我的需求。
----------
"search_page.html"
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
      <button id="search-button">搜尋</button>
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
      <a href="home_page.html"><img src="../img/home-button-black.png" alt="Home"></a>
      <a href="search_page.html"><img src="../img/search-button-black.png" alt="Search"></a>
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

----------
"css檔案片段"
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
----------

## 結果
- 自己調好
- ChatGPT做得很讚