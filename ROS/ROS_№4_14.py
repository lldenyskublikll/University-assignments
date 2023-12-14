from tkinter import Tk, Label, Button, filedialog, Entry
from PIL import Image, ImageOps, ImageFilter, ImageTk
import cv2
import numpy as np

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App") # Назва вікна
        self.root.geometry("900x700") # Розмір вікна

        # Додаткові змінні
        self.image_path = ""
        self.image_name = ""
        self.original_image = None
        self.processed_image = None
      
        # Оформлення вікна програми

        # Створення кнопки "Відкрити зображення"
        self.open_button = Button(root, text = "Open image", command = self.open_image)
        self.open_button.grid(row = 0, column = 3, columnspan = 4)

        # Створення кнопки "Зберегти зображення"
        self.save_button = Button(root, text = "Save image", command = self.save_image)
        self.save_button.grid(row = 0, column = 7)

        # Створення кнопки "Конвертувати зображення у PNG"
        self.convert_button_1 = Button(root, text = "Convert to PNG", command = self.convert_to_png)
        self.convert_button_1.grid(row = 1, column = 0)

        # Створення кнопки "Конвертувати зображення у JPEG"
        self.convert_button_2 = Button(root, text = "Convert to JPEG", command = self.convert_to_jpeg)
        self.convert_button_2.grid(row = 2, column = 0)

        # Створення кнопки "Інвертувати зображення"
        self.reverse_button = Button(root, text = "Reverse image", command = self.reverse_image)
        self.reverse_button.grid(row = 3, column = 0)

        # Створення кнопки "Змінити розміри зображення"
        self.resize_button = Button(root, text = "Resize image", command = self.resize_image)
        self.resize_button.grid(row = 4, column = 0)

        # Створення поля для вводу нової ширини зображення
        self.width = Label(root, text = 'New width:') 
        self.width.grid(row = 4, column = 2)

        self.newextension_1 = Entry(root) 
        self.newextension_1.grid(row = 4, column = 3)

        # Створення поля для вводу нової висоти зображення
        self.height = Label(root, text = 'New height:') 
        self.height.grid(row = 4, column = 7)

        self.newextension_2 = Entry(root) 
        self.newextension_2.grid(row = 4, column = 8)

        # Створення кноки "Використати Canny детектування границь" 
        self.canny_button = Button(root, text="Apply Canny Edge Detection", command=self.apply_canny_edge_detection)
        self.canny_button.grid(row=5, column=0)

        
            
        # Додаткова інформація про статус обробки та назву файлу
        self.label2 = Label(root, text = "Opened image:")
        self.label2.grid(row = 6, column = 0)

        self.label = Label(root, text = "Status: Choose image")
        self.label.grid(row = 7, column = 0)

        # Місце для виводу thumbnail-зображення у вікно
        self.preview_label = Label(root)
        self.preview_label.grid(row = 9, column = 0, columnspan = 4)


# Метод для відкриття зображення типу JPEG 
    def open_image(self): 
        self.image_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpg;*.jpeg")]) # Умова для відкриття зображень тільки типу JPEG
        self.image_name = self.image_path.split('/')[-1]
        self.original_image = Image.open(self.image_path) # Відкриття забраження
        self.processed_image = self.original_image.copy() # Копіювання зображення для подальшого відображення у вікні
        self.label2.config(text="Opened image: {}".format(self.image_name))
        self.show_preview() # Виклик методу для відображення обраного зображення


# Метод для конвертації зображення типу JPEG у зображення типу PNG
    def convert_to_png(self):
        if self.original_image:
            png_path = self.image_path[:-4] + ".png" # Шлях до директорії
            self.processed_image = self.original_image            
            self.original_image.save(png_path, "PNG") # Виклик методу для збереження зображення
            self.label.config(text = "Status: Image saved in PNG") 
            self.show_preview() # Виклик методу для відображення конвертованого зображення

# Метод для конвертації зображення типу JPEG у зображення типу JPEG
    def convert_to_jpeg(self):
        if self.original_image:
            png_path = self.image_path[:-4] + ".jpeg" # Шлях до директорії
            self.processed_image = self.original_image            
            self.original_image.save(png_path, "JPEG") # Виклик методу для збереження зображення
            self.label.config(text = "Status: Image saved in JPEG")
            self.show_preview() # Виклик методу для відображення конвертованого зображення

# Метод для інвертування зображення
    def reverse_image(self):
        if self.original_image:
            self.original_image = ImageOps.invert(self.original_image) # Інвертування зображення
            self.processed_image = self.original_image
            self.label.config(text = "Status: Image reversed")
            self.show_preview() # Виклик методу для відображення інвертованого зображення
        

# Метод для зміни розміру зображення
    def resize_image(self):
        if self.original_image:
            width = int(self.newextension_1.get())  # Отримання значення ширини зображення з поля для вводу значення
            height = int(self.newextension_2.get())  # Отримання значення висоти зображення з поля для вводу значення
            image = cv2.cvtColor(np.array(self.original_image), cv2.COLOR_RGB2BGR)  # Конвертація зображення в формат cv2
            resized_image = cv2.resize(image, (width, height))  # Зміна розмірів зображення за допомогою cv2.resize()
            resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)  # Конвертація зображення назад у формат RGB
            self.original_image = Image.fromarray(resized_image)  # Повернення зображення в формат PIL.Image
            self.processed_image = self.original_image
            self.label.config(text=f"Status: Image size changed to {width} x {height}")
            self.show_preview()  # Виклик методу для відображення обробленого зображення
          
           

# Метод для виконання Canny Edge Detection
    def apply_canny_edge_detection(self):
        if self.original_image:       
            image_cv = cv2.cvtColor(np.array(self.original_image), cv2.COLOR_RGB2BGR)# Конвертуємо зображення PIL у зображення OpenCV
            edges = cv2.Canny(image_cv, 25, 255, L2gradient=False)# Застосовуємо алгоритм Canny Edge Detection
            self.original_image = Image.fromarray(edges)# Конвертуємо зображення OpenCV у зображення PIL
            self.processed_image = self.original_image# Відображаємо зображення з краями Canny
            self.label.config(text="Status: Canny Edge Detection applied")
            self.show_preview()  # Виклик методу для відображення обробленого зображення

# Метод для виводу обробленого або ще необробленого зображення у вікно
    def show_preview(self):
        if self.processed_image:
            self.processed_image.thumbnail((500, 500)) # Конвертування зображення у thumbnail для зручного відображення у вікні
            self.preview_image = ImageTk.PhotoImage(self.processed_image)
            self.preview_label.config(image = self.preview_image)
            self.preview_label.image = self.preview_image


# Метод для збереження зображення у ту директорію, з якої воно було взято
    def save_image(self):
        png_path = self.image_path[:-4] + ".png" # Шлях до директорії
        self.original_image.save(png_path, "PNG") # Збереження зображення
        self.label.config(text = "Status: Image saved in PNG")


if __name__ == "__main__":
    root = Tk()
    app = ImageProcessingApp(root)
    root.mainloop()