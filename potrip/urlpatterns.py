# 在 potrip/urlpatterns.py 裡面
from django.contrib import admin
from django.urls import path

# 同時匯入 hello 專案與 dice 專案的視圖函式
from app1.views import sayhello, hello2, hello3, hello4
from app1.pattern_views import dice, dice2, dice3, show, filter
# app2 
from django.contrib import admin
from django.urls import path
from app2.views import gemini_chat_api, chat_page

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ======= 專案一：Hello 練習系列網址 =======
    path('hello/', sayhello),                   # 網址：/hello/
    path('hello2/<str:username>', hello2),      # 網址：/hello2/名字
    path('hello3/<str:username>', hello3),      # 網址：/hello3/名字
    path('hello4/<str:username>', hello4),      # 網址：/hello4/名字
    
    # ======= 專案二：Dice 骰子練習系列網址 =======
    path('dice/', dice),                        # 網址：/dice/
    path('dice2/', dice2),                      # 網址：/dice2/
    path('dice3/', dice3),                      # 網址：/dice3/
    path('show/', show),                        # 網址：/show/
    path('filter/', filter),                    # 網址：/filter/


    #======== 專案app2 ======================
    #記得要在檔案上方確認有沒有 from . import views 喔！
    path('api/chat/', gemini_chat_api, name='gemini_chat_api'),
    path('chat/', chat_page, name='chat_page'),

]
