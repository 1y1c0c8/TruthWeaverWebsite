import pandas as pd
import json

from pytrends.request import TrendReq
from newsapi import NewsApiClient

from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import pytz

import pycountry

import mysql.connector
import ast

# pre-processing
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# train model
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

import pickle
import cloudpickle
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

from collections import Counter

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import newspaper

class DataAnalyst:

  def __init__(self, highlight='en-US', timezone=360):
    self.pytrend = TrendReq(hl=highlight, tz=timezone)
    self.sec = Secretary()

  # Return daily trending keyword in list form
  def get_trend_list(self, keywords=[], len=10):
    self.sec.tm('<--DA, GET TREND LIST START-->')

    df_trending = self.pytrend.trending_searches()
    if len!='all':
      self.sec.tm('<--DA, GET TREND LIST END-->')
      return df_trending[0].to_list()[:len]
    else:
      self.sec.tm('<--DA, GET TREND LIST END-->')
      return df_trending[0].to_list()
  
  # Return daily trending keyword in string form
  def get_trend_str(self):
    self.sec.tm('<--DA, GET TREND STR START-->')
    list_trending = self.pytrend.trending_searches()[0].to_list()[:10]
    self.sec.tm('<--DA, GET TREND STR END-->')
    return ', '.join(list_trending)

class Anchor:
  def __init__(self):
    self.kn = Knocker()
    self.sec = Secretary()
    # hoffforcomputerscience
    # self.newsapi = NewsApiClient(api_key='7d4f79fdcf034e309d21501b9a29cc94') 
    # gmail
    # self.newsapi = NewsApiClient(api_key='ccf45382a43e4da0bde39dc6102f6719')
    # f74096255
    self.newsapi = NewsApiClient(api_key='826a7cdfde9c4465b35284f21c769e49')
    

  def source(self):
    return self.newsapi.get_sources()

  def search_news_with_keyword(self, str_kw, date=date.today(), interval=3, loc='US'):
    self.sec.tm('<--AN, SEARCH NEWS WITH KEYWORD START-->')
    relative_articles = self.newsapi.get_everything(q=str_kw,
                                               sources='bbc-news, cnn, \
                                               financial-post, the-wall-street-journal, \
                                               the-verge, hacker-news, \
                                               bbc-sport, bleacher-report, espn-cric-info, football-italia, espn, four-four-two, fox-sports, talksport, \
                                               buzzfeed, ign, \
                                               medical-news-today, \
                                               national-geographic, \
                                               new-scientist, next-big-future',
                                               from_param=self.kn.n_days_ago(startDate=date, interval=3),
                                               to=date.today(),
                                               language='en',
                                               sort_by='relevancy')
    self.sec.tm('<--AN, SEARCH NEWS WITH KEYWORD END-->')
    return relative_articles
  
  def search_news_with_keyword_second_layer(self, str_kw, date=date.today(), interval=3, loc='US', category="Break news"):
    self.sec.tm('<--AN, SEARCH NEWS WITH KEYWORD SECOND LAYER START-->')

    if category == "Break news" or category == "politics":
      relative_articles = self.newsapi.get_everything(q=str_kw,
                                                sources='associated-press, reuters, \
                                                business-insider, business-insider-uk, fortune, \
                                                ars-technica, engadget, recode, techcrunch, techradar, the-verge, \
                                                espn, four-four-two, fox-sports, \
                                                entertainment-weekly, ign, polygon',
                                                from_param=self.kn.n_days_ago(startDate=date, interval=3),
                                                to=date.today(),
                                                language='en',
                                                sort_by='relevancy')
    elif category == "sport":
      relative_articles = self.newsapi.get_everything(q=str_kw,
                                               sources='associated-press, reuters, \
                                               espn, four-four-two, fox-sports' ,
                                               from_param=self.kn.n_days_ago(startDate=date, interval=3),
                                               to=date.today(),
                                               language='en',
                                               sort_by='relevancy')
    elif category == "entertainment":
      relative_articles = self.newsapi.get_everything(q=str_kw,
                                                sources='associated-press, reuters, \
                                                entertainment-weekly, ign, polygon',
                                                from_param=self.kn.n_days_ago(startDate=date, interval=3),
                                                to=date.today(),
                                                language='en',
                                                sort_by='relevancy')
    elif category == "business":
      relative_articles = self.newsapi.get_everything(q=str_kw,
                                                sources='associated-press, reuters, \
                                                business-insider, business-insider-uk, fortune' ,
                                                from_param=self.kn.n_days_ago(startDate=date, interval=3),
                                                to=date.today(),
                                                language='en',
                                                sort_by='relevancy')
    elif category == "tech":
      relative_articles = self.newsapi.get_everything(q=str_kw,
                                                sources='associated-press, reuters, \
                                                ars-technica, engadget, recode, techcrunch, techradar, the-verge' ,
                                                from_param=self.kn.n_days_ago(startDate=date, interval=3),
                                                to=date.today(),
                                                language='en',
                                                sort_by='relevancy')
    self.sec.tm('<--AN, SEARCH NEWS WITH KEYWORD SECOND LAYER END-->')
    return relative_articles

class Secretary:

  def __init__(self):
    # self.switch = True
    self.switch = False

  # tp for "test message"
  def tm(self, msg):
    if self.switch:
      print(msg)

  # remove specific punctuation
  def del_mark(self, str, mark):
    self.tm('<--SEC, DEL MARK S&E-->')
    return str.strip(mark)

  # predict-used function
  def pick_max(self, pending_list):
    # 使用Counter計算元素出現次數
    counter = Counter(pending_list)

    # 使用most_common()方法取得出現次數最多的元素
    most_common = counter.most_common(1)

    # 如果有多個元素出現次數相同，返回第一個出現的元素
    return most_common[0][0] if most_common else None
  
  # print list, dict data in json form
  def print_readable(self, collection, len='all'):
    self.tm('<--SEC, PRINT READABLE START-->')
    # print(json.dumps(collection, indent=2)) -->  can't print escape cahracters
    if len != 'all':
      print(json.dumps(collection[:len], indent=2).encode('utf-8').decode('unicode_escape'))  
    else:
      print(json.dumps(collection, indent=2).encode('utf-8').decode('unicode_escape'))
    self.tm('<--SEC, PRINT READABLE END-->')

  # remove non-used columns of news info
  def clean_article_info(self, new_info, delNum, skipNull=True):
    self.tm('<--SEC, CLEAN ARTICLE INFO START-->')
    if skipNull:
      return_list = []

      for article in new_info:
        news_id = article['source']['id']
        if (news_id != None):
          return_list.append(article)
      print('News *', len(return_list))
      self.tm('<--SEC, [SKIP NULL] CLEAN ARTICLE INFO END-->')
      return return_list
    
    else:
      for article in new_info:
        del article['author']
        del article['description']
        del article['content']
      print('News *', len(new_info))
      self.tm('<--SEC, [NOT SKIP NULL] CLEAN ARTICLE INFO END-->')
      return new_info

  # sort news by date
  def sort_news_by_date(self, list_Data):
    data = sorted(list_Data, key=lambda article: article['publishedAt'], reverse=True)
    return data
  
  # trend keywords - category (json) -> category list (list)
  def trend_category_dict_transfer(self, trend_category_dict):
  
    format_list = []

    print(type(trend_category_dict))

    for category in trend_category_dict:
      for time in range(len(trend_category_dict[category])):
        format_list.append(category)

    return format_list

  # used when get trend list out of DB
  def ls_to_str(self, ls):
    self.tm('<--SEC, LS TO STR S&E-->')
    return ', '.join(ls)

  def str_to_ls(self, str):
    self.tm('<--SEC, STR TO LS S&E-->')
    return str.split(', ')

  #*************************************************
  def id_is_null(self, article):
    news_id = article['source']['id']
    if news_id is None or news_id == "":
      return False
  # 把一個trend kw的所有新聞標題抓出來，以title list回傳
  def get_title(self, ls_info):
    self.tm('<--SEC, GET TITLE START-->')
    ls_title = []
    for info in ls_info:
      ls_title.append(info["title"])
    self.tm('<--SEC, GET TITLE END-->')
    return ls_title
  def get_date(self, ls_info):
    self.tm('<--SEC, GET DATE START-->')
    ls_date = []
    for info in ls_info:
      ls_date.append(info["publishedAt"])
    self.tm('<--SEC, GET DATE END-->')
    return ls_date
  def get_name(self, ls_info):
    self.tm('<--SEC, GET NAME START-->')
    ls_name = []
    for info in ls_info:
      ls_name.append(info['source']['id'])
    self.tm('<--SEC, GET NAME END-->')
    return ls_name
  #*************************************************

class Knocker:
  def __init__(self):
    self.dt_format = "%Y-%m-%d %H:%M:%S"
    self.d_format = "%Y-%m-%d"
    self.sec = Secretary()

  # python str format datetime
  def str_2_dt(self, str, time=True):
    self.sec.tm('<--KN, STR 2 DT S&E-->')
    return datetime.strptime(str, self.dt_format) if time else datetime.strptime(str, self.d_format)

  # transfer dt to str & to format
  def dt_2_str(self, dt, time=True):
    self.sec.tm('<--KN, DE 2 STR S&E-->')
    return dt.strftime(self.dt_format) if time else dt.strftime(self.d_format)

  # 將datetime去除時區資訊
  def dt_without_tzinfo(self, dt):
    self.sec.tm('<--KN, DT WITHOUT TZINFO START-->')
    str_dt = self.dt_2_str(dt)
    self.sec.tm('<--KN, DT WITHOUT TZINFO END-->')
    return self.str_2_dt(str_dt)

  # loc='洲/國家'，詳見tzinfo.txt or pytz.all_timezones
  def target_loc_datetime(self, loc):
    self.sec.tm('<--KN, TARGET LOC DATETIME START-->')
    # local time
    local_tz = pytz.timezone('Asia/Taipei')
    local_date = datetime.now(local_tz)

    # 轉成目標國家的時區
    target_tz = pytz.timezone(loc)
    target_date = local_date.astimezone(target_tz)

    target_date = self.dt_without_tzinfo(target_date)
    self.sec.tm('<--KN, TARGET LOC DATETIME END-->')
    return target_date

  # 取得startDate n天之前的dt
  def n_days_ago(self, startDate, interval):
    self.sec.tm('<--KN, N DAYS AGO S&E-->')
    return startDate - relativedelta(days=interval)
  
class Navigator:
  
  def __init__(self):
    self.sec = Secretary()
  
  # numeric: TW:158, US:840, JP:392
  def get_country_code2(self, country_num):
    self.sec.tm('<--NG, GET COUNTRY CODE2 S&E-->')
    return pycountry.countries.get(numeric=country_num).alpha_2
  
class DB:
  def __init__(self):
    # 資料庫連接設定
    config = {
        'user': 'root',
        'password': 'H0fff0rC0mpu7eR$ciencE',
        'host': 'localhost',
        'database': 'tw_trend_search',
        'raise_on_warnings': True
    }
    self.kn = Knocker()
    self.da = DataAnalyst()
    self.sec = Secretary()
    
    self.cnx = mysql.connector.connect(**config)
    self.cursor = self.cnx.cursor()

  # 不能直接使用insert_trend_info，除了測試以外，只能在update_today_trend中使用
  def insert_today_info(self, tableN='us_history_trend'):
    self.sec.tm('<---DB, INSERT TODAY INFO START-->')

    trend_list = self.da.get_trend_list()
    print('[DB insert today info]')
    print(trend_list)
    trend_str = self.sec.ls_to_str(trend_list)
    trend_json = json.dumps(trend_str)
    date_dt = self.kn.target_loc_datetime('America/New_York').date()

    query = "INSERT INTO {} (keyword_list, timestamp) VALUES (%s, %s)".format(tableN)
    data = (trend_json, date_dt)
    self.cursor.execute(query, data)
    self.cnx.commit()

    self.sec.tm('<--DB, INSERT TODAY INFO END-->')

  # 運作很正常，就是更新當天的trend info到DB，如果今天的資料不存在就會insert
  def update_today_trend(self, loc='America/New_York', tableN='us_history_trend'):
    self.sec.tm('<--DB, UPDATE TODAY INFO START-->')
    
    # 取得目的地的current date
    target_d = self.kn.target_loc_datetime(loc=loc).date()
    # 試圖從db取出current date的info，沒有的話會得到False
    today_info = self.get_date_info(date=target_d, tableN=tableN)

    if not today_info:
      self.insert_today_info(tableN)
      self.sec.tm('<--DB, [INSERT] UPDATE TODAY INFO END-->')
    else:
      # 取得要填入資料庫的資料
      target_dt = self.kn.target_loc_datetime(loc=loc)
      
      trend_string = self.da.get_trend_str() 
      trend_json = json.dumps(trend_string)
      
      # 取得最新的ID
      query = "SELECT MAX(id) FROM {};".format(tableN)
      self.cursor.execute(query)
      result = self.cursor.fetchone()
      last_id = result[0]
      # 將今天的資料填入資料庫
      query = "UPDATE {} SET keyword_list = %s, timestamp = %s WHERE id = %s;".format(tableN)
      timestamp = target_dt
      data = (trend_json, timestamp, last_id)
      self.cursor.execute(query, data)
      self.cnx.commit()
      self.sec.tm('<--DB, [UPDATE] UPDATE TODAY INFO END-->')

  # 1)記得是"date"，如果使用kn.target_loc_datetime()，請記得搭配.date()使用，
  # 不然db.get_date_info怎麼抓資料都是得到False
  # 2)記得先update再get會比較好
  def get_date_info(self, date, tableN='us_history_trend'):
    self.sec.tm('<--DB, GET DATE INFO START-->')
    str_date = self.kn.dt_2_str(date)
    query = f"SELECT * FROM {tableN} WHERE DATE(timestamp) = %s"
    self.cursor.execute(query, (str_date,))
    content = self.cursor.fetchall()

    if not content:
      self.sec.tm('<--DB, [FAIL] GET DATE INFO END-->')
      return False
    else:
      self.sec.tm('<--DB, [SUCCESS] GET DATE INFO END-->')
      return content

  # delete newest infoBlock(塊狀data) in DB table "us_trend_history"
  def delete_info(self, tableN='us_history_trend', del_today=False):
    self.sec.tm('<--DB, DELETE INFO START-->')
    target_d = self.kn.target_loc_datetime(loc='America/New_York').date()

    if not del_today:
      self.sec.tm('<--DB, [NOT DEL TODAY]-->')
      query = f"SELECT DATE(timestamp) FROM {tableN} ORDER BY id DESC LIMIT 1"
      self.cursor.execute(query)
      result = self.cursor.fetchone()

      if result and result[0] == target_d:
        self.sec.tm('<--DB, [MEET TODAY INFO] DELETE INFO-->')
        return  # 不刪除最新資料

    query = f"DELETE FROM {tableN} ORDER BY id DESC LIMIT 1"
    self.cursor.execute(query)
    self.cnx.commit()
    self.sec.tm('<--DB, DELETE INFO END-->')

  def close(self):
    self.cursor.close()
    self.cnx.close()

# read text file
class Reader:
  def __init__(self):
    self.sec = Secretary()
    self.kn = Knocker()
    self.an = Anchor()

# 測一下
  def write_news_info_to_file(self, path, list, loc='America/New_York'):
    self.sec.tm('<--RD, WRITE NEWS INFO TO FILE START-->')
    
    date = self.kn.target_loc_datetime(loc=loc).date()

    news_list = []
    with open(path, 'w') as f:
      for kw in list:
        print(kw)
        temp_news_info_list = self.an.search_news_with_keyword(kw)        
        
        sorted_by_date_news_list = self.sec.sort_news_by_date(list_Data=temp_news_info_list['articles'])
        
        clean_news_list_I = self.sec.clean_article_info(sorted_by_date_news_list[:10], [0])
        # self.sec.print_readable(clean_news_list_I)

        clean_news_list_II = self.sec.clean_article_info(clean_news_list_I[:10], [0], skipNull=False)
        print(clean_news_list_II, file=f)
    self.sec.tm('<--RD, WRITE NEWS INFO TO FILE END-->')

  def read_news_info_from_file(self, path):
    self.sec.tm('<--RD, GET TREND INFO FROM FILE START-->')
    
    news_group = []
    with open(path, 'r') as f:
      line = f.readline()
      while line:
          news_group.append(ast.literal_eval(line.strip('"')))
          line = f.readline()

    self.sec.tm('<--RD, GET TREND INFO FROM FILE END-->')
    return news_group

  def write_news_category_to_file(self, path, trend_list, category_list):
    self.sec.tm('<--RD, WRITE NEWS CATEGORY TO FILE START-->')

    trend_category_dict = {
        "politics": [],
        "sport": [],
        "business": [],
        "entertainment": [],
        "tech": [],
        "Break news": []
    }

    for keyword, category in zip(trend_list, category_list):
        if category in trend_category_dict:
            trend_category_dict[category].append(keyword)

    sec.print_readable(trend_category_dict)

    trend_category_js = json.dumps(trend_category_dict)
    with open(path, 'w') as f:
      f.write(trend_category_js)
    # with open(path, 'w') as f:
    #     for category, keywords in trend_category_dict.items():
    #         print(category, file=f)
    #         for keyword in keywords:
    #             print(keyword, file=f)
    #         print('', file=f)

    self.sec.tm('<--RD, WRITE NEWS CATEGORY TO FILE END-->')

  def read_trend_category_dict_from_file(self, path):
    trend_category_dict = {}

    with open(path, 'r', encoding='utf-8') as f:
      trend_category_dict = json.load(f)
    
    return trend_category_dict
  
  def write_dedicate_news(self, dedicate_news_group, path):
    
    with open(path, 'w') as f:

      for dedicate_news_list in dedicate_news_group:
        
        sorted_by_date_news_list = self.sec.sort_news_by_date(list_Data=dedicate_news_list['articles'])
        
        clean_news_list_I = self.sec.clean_article_info(sorted_by_date_news_list[:3], [0])
        # self.sec.print_readable(clean_news_list_I)

        clean_news_list_II = self.sec.clean_article_info(clean_news_list_I[:3], [0], skipNull=False)
        print(clean_news_list_II, file=f)

class Paparazzi:
  def __init__(self):
    self.nlp = spacy.load("en_core_web_sm")
    self.sec = Secretary()

  def recognize_character(self, text, top=False):
    self.sec.tm('<--PR, RECOGNIZE CHARACTER START-->')
    # 傳遞報導文字給 SpaCy NER 模型進行處理
    doc = self.nlp(text)

    if top:
      self.sec.tm('<--PR, [TOP] RECOGNIZE CHARACTER-->')
      # 儲存所有的 PERSON 實體
      persons = set()

      # 逐一迭代每個偵測到的命名實體
      for entity in doc.ents:
        if entity.label_ == "PERSON" :
          persons.add(entity.text)

      # 計算 PERSON 實體與報導文字的相似度
      vectorizer = TfidfVectorizer()
      text_vector = vectorizer.fit_transform([text] + list(persons))
      similarity_scores = cosine_similarity(text_vector)[0][1:]

      # 取得前三個相似度最高的 PERSON 實體
      top_three_persons = [person for _, person in sorted(zip(similarity_scores, persons), reverse=True)[:3]]

      # 輸出結果
      print("與報導最相關的前三個人物：")
      for person in top_three_persons:
        print(person)
      self.sec.tm('<--PR, RECOGNIZE CHARACTER END-->')
    else:
      self.sec.tm('<--PR, [ALL] RECOGNIZE CHARACTER-->')
      for entity in doc.ents:
        if entity.label_ == "PERSON" :
          print(entity)
      self.sec.tm('<--PR, RECOGNIZE CHARACTER END-->')

  def recognize_event(self, text, top=False):
    self.sec.tm('<--PR, RECOGNIZE EVENT START-->')
    # 傳遞報導文字給 SpaCy NER 模型進行處理
    doc = self.nlp(text)

    if top:
      self.sec.tm('<--PR, [TOP] RECOGNIZE EVENT START-->')
      # 儲存所有的 EVENT 實體
      events = set()

      # 逐一迭代每個偵測到的命名實體
      for entity in doc.ents:
        if entity.label_ == "EVENT":
          events.add(entity.text)

      # 計算 EVENT 實體與報導文字的相似度
      vectorizer = TfidfVectorizer()
      text_vector = vectorizer.fit_transform([text] + list(events))
      similarity_scores = cosine_similarity(text_vector)[0][1:]

      # 取得前三個相似度最高的 EVENT 實體
      top_three_events = [event for _, event in sorted(zip(similarity_scores, events), reverse=True)[:3]]

      # 輸出結果
      print("與報導最相關的前三個事件：")
      for event in top_three_events:
        print(event)
      self.sec.tm('<--PR, RECOGNIZE EVENT END-->')
    else:
      self.sec.tm('<--PR, [ALL] RECOGNIZE EVENT START-->')
      for entity in doc.ents:
        if entity.label_ == "EVENT":
          print(entity)
      self.sec.tm('<--PR, RECOGNIZE EVENT END-->')

class ClassifierSVC:

  def tokenize(self, text):
    return word_tokenize(text)

  def remove_stopwords(self, tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if not token in stop_words]

  def stem(self, tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

  def remove_punctuation(self, text):
    return text.translate(str.maketrans('', '', string.punctuation))
  
  # predict
  def predict(self,hl):
      self.sec.tm('<--WI, PREDICT START-->')
      headline = hl
      processed_headline = self.pp.remove_punctuation(headline.lower())
      tokens = self.pp.tokenize(processed_headline)
      tokens = self.pp.remove_stopwords(tokens)
      tokens = self.pp.stem(tokens)
      processed_headline = ' '.join(tokens)
      
      headline_vectorized = self.vectorizer.transform([processed_headline])
      predicted_category = self.classifier.predict(headline_vectorized)
      self.sec.tm('<--WI, PREDICT END-->')
      return predicted_category
    
  def predict_news_group_category(self, title_group):
    category_list = []

    for title_list in title_group:
      if title_list == []:
        category_list.append('Break news')
      else:
        pending = []
        for title in title_list:
          pending_category = self.predict(title)[0]
          pending.append(pending_category)
        dicided_category = self.sec.pick_max(pending)
        category_list.append(dicided_category)
    # self.sec.print_readable(category_list)
    return category_list



class web_interface:
  def __init__(self):
    self.sec = Secretary()
    self.da = DataAnalyst()
    self.db = DB()
    self.an = Anchor()
    self.kn = Knocker()
    self.rd = Reader()
    self.svc = ClassifierSVC()

    self.store_parent_path = 'backend/relative_data/'

    path_classifier = '/Users/h0ff/Desktop/test/backend/classifier.pkl'
    # with open(path_classifier, 'rb') as file:
    #   self.classifier = pickle.load(file)
    self.classifier = pickle.load(open(path_classifier, 'rb'))
    path_vectorizer = '/Users/h0ff/Desktop/test/backend/vectorizer.pkl'
    # with open(path_vectorizer, 'rb') as file:
    #   self.vectorizer = pickle.load(file)
    self.vectorizer = pickle.load(open(path_vectorizer, 'rb'))
    
  # 透過class Knocker取得target_d
  def get_target_loc_date_with_interal_from_kn(self, loc, interval):
    startDate = self.kn.target_loc_datetime(loc=loc).date()
    return self.kn.n_days_ago(startDate=startDate, interval=interval)


  # 透過class DB更新database的trend infoBlock(塊狀data)
  def update_trend_infoBlock_with_db(self, loc='America/New_York'):
    self.sec.tm('<--WI, UPDATE TREND START-->')
    self.db.update_today_trend(loc=loc)
    self.sec.tm('<--WI, UPDATE TREND END-->')

  # 透過class DB從database取出trend infoBlock （無更新，本來是先更新再取出，會有資料不一致的問題）
  # General form，使用者可以透過這個function取出infoBlock，進一步parse目標欄位(date)
  def get_trend_infoBlock_from_db_with_db(self, date, tableN='us_trend_history', loc='America/New_york'):
    data = self.db.get_date_info(date=date)
    
    # 取出current trend
    infoBlock = data[0]

    return infoBlock

  # 透過class DBdatabase取出trend list
  # Specific form
  def get_trend_list_from_db(self, date, tableN='us_trend_history', loc='America/New_York'):
    self.sec.tm('<--WI, GET TREND LIST FROM DB START-->')
    
    infoBlock = self.get_trend_infoBlock_from_db(date=date)    
    info_trend_str = infoBlock[1]

    info_trend_str = self.sec.del_mark(info_trend_str, '"')

    return_ls = self.sec.str_to_ls(info_trend_str)
    # self.sec.print_readable(return_ls)
    self.sec.tm('<--WI, GET TREND LIST FROM DB END-->')
    return return_ls


  # 透過class Reader將first layer news寫入檔案
  def store_trend_news_in_file_with_rd(self, trend_list, date):
    self.sec.tm('<--WI, WRITE TREND NEWS START-->')
    path = self.store_parent_path + 'trend_news/' + str(date) + '.txt'
    self.rd.write_news_info_to_file(path=path, list=trend_list)
    self.sec.tm('<--WI, WRITE TREND NEWS END-->')

  # 透過class Reader從file讀出first layer news的titles
  def get_news_title_group_from_file_with_rd(self, date):
    self.sec.tm('<--WI, GET NEWS FROM TITLE GROUP FROM FILE START-->')
    
    path = self.store_parent_path + 'trend_news/' + str(date) + '.txt'
    news_info_list = self.rd.read_news_info_from_file(path=path)

    news_title_group = []

    for news_info in news_info_list:
      temp_news_title_list = []
      for news in news_info:
        temp_news_title_list.append(news['title'])
      news_title_group.append(temp_news_title_list)
    
    self.sec.tm('<--WI, GET NEWS FROM TITLE GROUP FROM FILE END-->')
    return news_title_group


  # 透過class ClassifierSVC預測新聞類別
  def predict_title_with_svc(self, title):
    category = self.svc.predict(hl=title)
    return category

  # 透過class ClassifierSVC預測一個title list的類別
  def predict_title_group_with_svc(self, title_group):
    category_list = self.svc.predict_news_group_category(title_group=title_group)
    return category_list


  # 透過class Reader將trend keyword - category dict (in json)寫入file
  def store_trend_category_dict_in_file_with_rd(self, trend_list, category_list, date):
    self.sec.tm('<--WI, WRITE CATEGORY START-->')
    path = self.store_parent_path + 'category/' + str(date) + '.txt'
    self.rd.write_news_category_to_file(path=path, trend_list=trend_list, category_list=category_list)
    self.sec.tm('<--WI, WRITE CATEGORY END-->')

  # 透過class Reader將trend keyword - category dict (in json)從file讀出
  def get_trend_category_dict_from_file_with_rd(self, date):
    self.sec.tm('<--WI, GET CATEGORY LIST FROM FILE START-->')
    
    path = self.store_parent_path + 'category/' + str(date) + '.txt'

    trend_category_dict={}
    trend_category_dict = self.rd.read_trend_category_dict_from_file(path)
    self.sec.tm('<--WI, GET CATEGORY LIST FROM FILE END-->')
    return trend_category_dict




  # def write_dedicate_news(self, dedicate_news_list, date):
  #   self.sec.tm('<--WI, WRITE DEDICATE NEWS START-->')
  #   path = 'backend/dedicate_news/' + str(date) + '.txt'
  #   self.rd.write_news_info_to_file(path=path, list=dedicate_news_list, date=date)
  #   self.sec.tm('<--WI, WRITE DEDICATE NEWS END-->')

  def get_dedicate_news_group_with_an(self, date):
    read_path = 'backend/category/' + str(date) + '.txt'
    trend_category_dict = self.rd.read_trend_category_dict_from_file(path=read_path)

    dedicate_news_group = []
    for category in trend_category_dict:
      for kw in trend_category_dict[category]:
        kw_dedicate_news_list = self.an.search_news_with_keyword_second_layer(kw, category=category)
        dedicate_news_group.append(kw_dedicate_news_list)

    sec.print_readable(dedicate_news_group)

    write_path = 'backend/dedicate_news/' + str(date) + '.txt'
    self.rd.write_dedicate_news(dedicate_news_group=dedicate_news_group, path=write_path)

  
  #*************************************************
  def get_news_title_group_with_an(self, date):
    self.sec.tm('<--WI, GET NEW TITLE GROUP WITH DA START-->')

    news_info_ls = []

    self.db.update_today_trend()
    info = self.db.get_date_info(date=date)
    infoBlock = info[0]
    trend_str = self.sec.del_mark(infoBlock[1], '"')
    trend_list = self.sec.str_to_ls(trend_str)

    for kw in trend_list[:2]:
      temp_news_info_list = self.an.search_news_with_keyword(kw)
      
      # self.sec.tm('!!--TEMP_NEWS_INFO_LIST--!!')
      # print(temp_news_info_list)
      # self.sec.tm('!!--TEMP_NEWS_INFO_LIST--!!')

      temp_news_info_list = self.sec.clean_article_info(temp_news_info_list['articles'][:5], [0])
      temp_news_info_list = self.sec.clean_article_info(temp_news_info_list, [0], skipNull=False)

      news_info_ls.append(temp_news_info_list)

    self.sec.tm('<--WI, GET NEW TITLE GROUP WITH DA END-->')
    return news_info_ls
  #*************************************************
  
kn = Knocker()
db = DB()
sec= Secretary()
da = DataAnalyst()
rd = Reader()
an = Anchor()
wi = web_interface()

target_d = kn.target_loc_datetime(loc='America/New_York').date()
