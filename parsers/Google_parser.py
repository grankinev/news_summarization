
# coding: utf-8

# In[1]:


from GoogleNews import GoogleNews
googlenews = GoogleNews()

import time

import requests

import newspaper
from newspaper import Article
from newspaper import fulltext


# In[15]:


def googleparser (topic, depth):
    '''
    topic - тема новостного запроса
    depth - число опрашиваемых страниц поисковой выдачи
    
    Возвращает два списка: с текстами новостей и с проблемными ссылками 
    
    '''
    # 1. формирование массива ссылок
    gnews_links = []
    gnews=[]
    googlenews.search(topic)
    
    start_time = time.time()
    
    print('--- Формируется массив ссылок... ---')

    for i in range(1,depth):
        googlenews.clear()
        googlenews.getpage(i)
        for j in range(0, len(googlenews.gettext())):
            gnews.append(googlenews.gettext()[j])
            gnews_links.append(googlenews.getlinks()[j])

    print("--- На формирование массива затрачено %s секунд ---" % (time.time() - start_time))             
    print('--- Завершено. Получено %s ссылок ---' % len(gnews_links))   
    
    # 2. выгрузка новостей и формирование массива текстов
    
    body = []
    count = 0
    error_link = [] #массив с битыми ссылками

    #замеряем время
    start_time = time.time()

    print('--- Выгружаются новости... ---')

    for url in gnews_links:
        try:
            html = requests.get(url).text
            text = fulltext(html)
            body.append(text)
        except:
            error_link.append(gnews_links[count]) #иногда попадаются проблемные ссылки. Здесь мы будем сохранять их 
            pass
        count += 1

    print("--- Завершено. На выгрузку затрачено %s секунд ---" % (time.time() - start_time))             
    return body, error_link


# In[6]:


body, error = googleparser ('China', 2)

