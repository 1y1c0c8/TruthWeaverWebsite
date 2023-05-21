## 現況
- 加入images到圈圈中

## prompt
- 以下是我的html程式碼，我想請你幫我優化這段程式碼，讓chartContainer的圈圈中可以顯示對應的News Category的英文，先不用添加圖片，感謝。

## 回覆
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
  <title>Home Page</title>
  <style>
    /* 新增CSS樣式 */
    #chartContainer {
      max-width: 100%;
      height: auto;
      margin: 0 auto;
      display: block;
    }
    .category-label {
      text-anchor: middle;
      font-size: 12px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div id="home-page">
    <div class="banner">
      <h1 class="centered-title brusher-font">TruthWeaver</h1>
    </div>
    <div class="content">
      <svg id="chartContainer"></svg> <!-- 移除 width 和 height 屬性 -->
    </div>
    <div class="bottom-nav">
      <a href="{{ url_for('home') }}"><img src="{{ url_for('static', filename='home-button-black.png') }}" alt="Home Page"></a>
      <a href="{{ url_for('search') }}"><img src="{{ url_for('static', filename='search-button-black.png') }}" alt="Search Page"></a>
    </div>
  </div>

  <script src="https://d3js.org/d3.v6.min.js"></script>
  <script>
    // 定義新聞類別的數量和列表
    var newsCategories = ['entertainment', 'politics', 'technology', 'entertainment', 'sports', 'politics', 'sports', 'technology', 'entertainment', 'sports', 'sports','sports','sports'];

    // 定義新聞類別
    var categories = ['general', 'business', 'technology', 'sports', 'entertainment', 'science', 'health', 'politics'];

    // 計算各個新聞類別的出現次數
    var categoryCounts = {};
    newsCategories.forEach(function(category) {
      if (categories.includes(category)) {
        if (categoryCounts[category]) {
          categoryCounts[category]++;
        } else {
          categoryCounts[category] = 1;
        }
      }
    });

    // 計算最大和最小的出現次數
    var maxCount = d3.max(Object.values(categoryCounts));
    var minCount = d3.min(Object.values(categoryCounts));

    // 設定圓圈的最小和最大半徑
    var minRadius = 50;
    var maxRadius = 100;

    // 創建SVG容器
    var svg = d3.select("#chartContainer")
      .attr("width", "100%") // 設定寬度為100%以符合響應式網頁
      .attr("height", "500"); // 設定高度

    // 計算圓圈的半徑比例
    var radiusScale = d3.scaleLinear()
      .domain([minCount, maxCount])
      .range([minRadius, maxRadius]);

    // 創建圓圈元素
    var circles = svg.selectAll("circle")
      .data(Object.entries(categoryCounts))
      .enter()
      .append("circle")
      .attr("class", "category-circle")
      .attr("cx", function(d, i) { return (i % 3) * 150 + 75; })
      .attr("cy", function(d, i) { return Math.floor(i / 3) * 150 + 75; })
      .attr("r", function(d) { return Math.max(radiusScale(d[1]), minRadius); }) // 修正半徑最小值
      .style("fill", function(d) { return getCategoryColor(d[0]); });

    // // 添加标签元素
    // circles.each(function(d) {
    //   var category = d[0];
    //   var radius = Math.max(radiusScale(d[1]), minRadius);

    //   d3.select(this)
    //     .append("text")
    //     .attr("class", "category-label")
    //     .attr("dy", radius + 12)
    //     .text(category);
    // });
    // 添加标签元素

    // 添加标签元素
    circles.each(function(d, i) {
      var category = d[0];
      var radius = Math.max(radiusScale(d[1]), minRadius);

      svg.append("text")
        .attr("class", "category-label")
        .attr("transform", function() {
          var x = (i % 3) * 150 + 75;
          var y = Math.floor(i / 3) * 150 + 75;
          return "translate(" + x + "," + y + ")";
        })
        .attr("dy", radius + (-radius)) // 透過dy調整位置
        .attr("text-anchor", "middle")  // 水平居中对齐
        .text(category);
    });

    // 添加标签元素
    // circles.each(function(d, i) {
    //   var category = d[0];
    //   var radius = Math.max(radiusScale(d[1]), minRadius);

    //   svg.append("text")
    //     .attr("class", "category-label")
    //     .attr("transform", function() {
    //       var x = (i % 3) * 150 + 75;
    //       var y = Math.floor(i / 3) * 150 + 75 - radius - 12; // 修改此行，向上移动标签
    //       return "translate(" + x + "," + y + ")";
    //     })
    //     .attr("text-anchor", "middle") // 水平居中对齐
    //     .text(category);
    // });



    // 定義新聞類別對應的顏色
    function getCategoryColor(category) {
      var colorMap = {
        'entertainment': 'blue',
        'politics': 'red',
        'technology': 'green',
        'sports': 'orange',
        'general': 'yellow',
        'business': 'purple',
        'science': 'pink',
        'health': 'cyan'
      };
      return colorMap[category] || 'gray';  // 預設為灰色
    }
  </script>
</body>
</html>

```

## 結果
- 加入圖片失敗，換成加入文字。文字加得很成功。