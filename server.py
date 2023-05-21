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
