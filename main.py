
  
# كود لبرنامج تنزيل الفيديوهات من اليوتيوب  شغال \\\\\||||\\\
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from pytube import YouTube
import threading

class VideoDownloaderApp(App):
    def build(self):
        # تخطيط عمودي لواجهة التطبيق
        layout = BoxLayout(orientation='vertical')
        
        # حقل إدخال لنص URL
        self.url_input = TextInput(hint_text="أدخل رابط الفيديو هنا")
        layout.add_widget(self.url_input)
        
        # زر تنزيل الفيديو
        download_button = Button(text="تنزيل الفيديو")
        download_button.bind(on_press=self.download_video)
        layout.add_widget(download_button)
        
        # ملصق لعرض الرسائل
        self.message_label = Label(text="")
        layout.add_widget(self.message_label)
        
        return layout
    
    def download_video(self, instance):
        # الحصول على رابط الفيديو من حقل الإدخال
        video_url = self.url_input.text
        
        if video_url:
            # تنزيل الفيديو في خيط جديد لتجنب تجميد واجهة المستخدم
            threading.Thread(target=self._download, args=(video_url,)).start()
    
    def _download(self, video_url):
        try:
            # إنشاء كائن YouTube
            yt = YouTube(video_url)
            
            # اختيار أفضل تدفق فيديو وصوت متاح
            stream = yt.streams.get_highest_resolution()
            
            # تنزيل الفيديو
            stream.download()
            
            # عرض رسالة نجاح
            self.message_label.text = f"تم تنزيل الفيديو: {yt.title}"
        except Exception as e:
            # عرض رسالة خطأ
            self.message_label.text = f"حدث خطأ: {str(e)}"

if __name__ == "__main__":
    VideoDownloaderApp().run()