from django.db import models

class ChatLog(models.Model):
    """
    這是一張對話紀錄表。
    Django 會自動在 SQLite/MySQL 裡面幫我們建立對應的 Table！
    """
    # 1. 紀錄是誰說的話：'user' 代表用戶，'ai' 代表 Gemini
    sender = models.CharField(max_length=10, verbose_name="發送者")
    
    # 2. 紀錄說話的內容：用 TextField 才可以存很長很長的對話
    content = models.TextField(verbose_name="對話內容")
    
    # 3. 紀錄說話的時間：自動記錄存入資料庫的那一秒鐘
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="對話時間")

    class Meta:
        ordering = ['created_at'] # 讓資料預設照時間順序排列

    def __str__(self):
        return f"[{self.sender}]: {self.content[:20]}..."
