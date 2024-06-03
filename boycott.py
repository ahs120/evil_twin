import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.popup import Popup
from kivy.graphics.texture import Texture
import sqlite3
from kivy.uix.image import Image
import pytesseract
from PIL import Image as PILImage
import cv2
import numpy as np

# إعداد قاعدة البيانات
conn = sqlite3.connect('test.db')
c = conn.cursor()

# إنشاء جدول إذا لم يكن موجودًا
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sector TEXT NOT NULL
)
''')
conn.commit()

# مثال على إدخال بيانات
# c.execute("INSERT INTO products (name, sector) VALUES ('ProductA', 'A')")
# c.execute("INSERT INTO products (name, sector) VALUES ('ProductB', 'B')")
# conn.commit()

class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.camera = Camera(play=False)
        layout.add_widget(self.camera)
        
        button = Button(text='See it', size_hint=(None, None), size=(100, 50))
        button.bind(on_press=self.capture)
        layout.add_widget(button)
        
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        
        return layout

    def capture(self, instance):
        self.camera.export_to_png("captured_image.png")
        self.process_image("captured_image.png")
    
    def process_image(self, image_path):
        # استخدام pytesseract لاستخراج النص من الصورة
        image = PILImage.open(image_path)
        text = pytesseract.image_to_string(image).strip()

        # البحث في قاعدة البيانات
        c.execute("SELECT sector FROM products WHERE name=?", (text,))
        result = c.fetchone()

        if result:
            sector = result[0]
            if sector == 'A':
                self.result_label.text = 'True'
            elif sector == 'B':
                self.result_label.text = 'False'
        else:
            self.result_label.text = 'غير معروف'

if __name__ == '__main__':
    CameraApp().run()

# اغلاق الاتصال بقاعدة البيانات عند الانتهاء
conn.close()
