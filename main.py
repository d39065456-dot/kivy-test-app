from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Tablet için klavye ayarını kapat
Window.softinput_mode = "below_target"

class SimpleTestApp(App):
    def build(self):
        self.title = "Kivy Test Uygulaması"
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(
            text="👋 Merhaba!\nBu bir test uygulaması.\nButona bas!",
            font_size='24sp',
            halign='center',
            valign='middle'
        )
        
        button = Button(
            text="Tıkla Beni",
            font_size='20sp',
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5}
        )
        button.bind(on_press=self.button_clicked)
        
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout
    
    def button_clicked(self, instance):
        self.label.text = "✅ Butona tıklandı!\n\nHarika çalışıyor 🎉\n\nAPK'n hazır!"

if __name__ == "__main__":
    SimpleTestApp().run()
