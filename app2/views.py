# ==================== views.py 最底部的最終完整程式碼 ====================
from django.http import JsonResponse
from django.shortcuts import render # 💡 確保這行有在 views.py 開頭引入
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from google.genai import types
import os

from google import genai
from app2.models import ChatLog # 💡 記得引入我們剛剛註冊成功的資料庫模型

# ----------------- 函式 1：負責處理打字與 AI 連線（要存資料庫） -----------------
@csrf_exempt
def gemini_chat_api(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        
        if not user_message:
            return JsonResponse({"error": "請輸入訊息"}, status=400)
            
        try:
            # 💾 動作 A：用戶一送出問題，立刻存入一筆資料庫紀錄
            ChatLog.objects.create(sender="user", content=user_message)

            # 呼叫大腦思考
            # 1. 取得當前台灣時間與日期
            
            now_taiwan = timezone.localtime(timezone.now())
            today_str = now_taiwan.strftime("%Y 年 %m 月 %d 日 %A") 
            
            # 2. 設定系統指示，把今天日期灌進去
            sys_instruction = f"你是AI 智慧助理。今天是 {today_str}。請務必根據這個日期精準回答時間、節日與天氣相關問題。"
            
            api_key = os.getenv("GEMINI_API_KEY")
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction=sys_instruction,
                )
            )
            
            ai_reply = response.text

            # 💾 動作 B：AI 回話成功，也立刻存入一筆資料庫紀錄
            ChatLog.objects.create(sender="ai", content=ai_reply)
            
            return JsonResponse({"reply": ai_reply})
            
        except Exception as e:
            return JsonResponse({"error": f"AI connection failed: {str(e)}"}, status=500)
            
    return JsonResponse({"error": "請使用 POST 方法請求"}, status=405)


# ----------------- 函式 2：負責讓瀏覽器打開對話網頁畫面（要用 render） -----------------

#def chat_page(request):
    """
    這個函式負責在用戶輸入 http://127.0.0.1/chat 時，
    用 render 把漂亮的 ai_chat.html 網頁畫面呈現出來。
    """
    #return render(request, "ai_chat.html")

def chat_page(request):
    # 💡 撈出所有對話紀錄
    history_logs = ChatLog.objects.all()
    # 💡 透過 render 傳給 ai_chat.html
    return render(request, "ai_chat.html", {"history_logs": history_logs})



