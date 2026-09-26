from google import genai

# 1. 填入你之前在 Google AI Studio 拿到的 API Key
# 記得一定要用英文雙引號 "" 包起來
MY_KEY = "AIzaSyBrhNSpLgIeJqcGr7_6wIeiQ0ONPDP4Pbs"

print("正在連線至 Gemini 大腦...")

try:
    # 2. 初始化客戶端
    client = genai.Client(api_key=MY_KEY)
    
    # 3. 呼叫最新的免費輕量模型
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='請用一句繁體中文跟正在努力學 Python 的我說聲早安！',
    )
    
    print("\n🤖 Gemini 回答：")
    print(response.text)

except Exception as e:
    print("\n❌ 連線失敗，錯誤原因：", e)
