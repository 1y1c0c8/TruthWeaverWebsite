from flask import Flask, jsonify, render_template
import os
from utils import web_interface, Anchor, Knocker, Secretary, Reader
import json

app = Flask(__name__, template_folder='../src', static_folder='../static')

# 定義路由端點，處理根目錄的 GET 請求
# @app.route('/', methods=['GET'])
# def hello():
#     return 'Hello, World!'

@app.route('/')
def home():
    # da = DataAnalyst()
    wi = web_interface()
    sec = Secretary()

    #==========================
    update_mode = True
    show_mode = not update_mode
    #==========================
    target_loc = 'America/New_York'
    target_d = wi.get_target_loc_date_with_interal_from_kn(loc=target_loc, interval=0)

    if update_mode:
        # 更新DB的trend_list
        wi.update_trend_infoBlock_with_db(loc=target_loc)
        # 從DB取出trend_list
        trend_list = wi.get_trend_list_from_db(date=target_d)

        # 強制寫入first layer news進入file
        wi.store_trend_news_in_file_with_rd(trend_list=trend_list, date=target_d)
        # 從file讀出titles
        news_title_group = wi.get_news_title_group_from_file_with_rd(date=target_d)

        # predict first layer titles
        category_list = wi.predict_title_group_with_svc(news_title_group)
        sec.print_readable(category_list)
        # 寫入category dict進file
        wi.store_category_json_in_file_with_rd(trend_list=trend_list, category_list=category_list, date=target_d)
        # 從file讀出category dict
        category_dict = wi.get_trend_category_dict_from_file_with_rd(date=target_d)
        sec.print_readable(category_dict)
        # category_list = category_list[0]
        # 並且轉換格式
        category_list = sec.trend_category_dict_transfer(trend_category_dict=category_dict)
        sec.print_readable(category_list)

        # 從DB取出塊狀data，取得update datetime
        cur_infoBlock = wi.get_trend_infoBlock_from_db_with_db(date=target_d)
        update_dt = cur_infoBlock[2]

    if show_mode:
        # 從DB取出trend_list
        trend_list = wi.get_trend_list_from_db(date=target_d)

        # 從file讀出category dict
        category_dict = wi.get_trend_category_dict_from_file_with_rd(date=target_d)
        sec.print_readable(category_dict)
        # category_list = category_list[0]
        # 並且轉換格式
        category_list = sec.trend_category_dict_transfer(trend_category_dict=category_dict)
        sec.print_readable(category_list)
        
        # 從DB取出塊狀data，取得update datetime
        cur_infoBlock = wi.get_trend_infoBlock_from_db_with_db(date=target_d)
        update_dt = cur_infoBlock[2]

    return render_template("home_page.html", 
                           update_datetime=update_dt, 
                           len=len(trend_list), trend_list=trend_list, 
                           category_list=category_list)

# show all trend kw news
@app.route('/search')
def search():
    wi = web_interface()

    #==========================
    update_mode = False
    show_mode = not update_mode
    #==========================
    target_loc = 'America/New_York'
    target_d = wi.get_target_loc_date_with_interal_from_kn(loc=target_loc, interval=0)


    


    return render_template("search_page.html")

@app.route('/content')
def content():
    wi = web_interface()

    #==========================
    update_mode = False
    show_mode = not update_mode
    #==========================
    target_loc = 'America/New_York'
    target_d = wi.get_target_loc_date_with_interal_from_kn(loc=target_loc, interval=0)

    
    


    return render_template("search_page.html")


if __name__ == '__main__':
    app.run()
