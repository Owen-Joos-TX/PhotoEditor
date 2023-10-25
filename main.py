from tkinter import Widget
from PIL import Image, ImageDraw
from kivy.app import App
from kivy.uix.screenmanager import Screen
import random
import math





class DisplayFrameApp(App):
    pass

image = ""
class Display(Screen):
    def getImage(self):
        self.ids.imageName.source = self.ids.textInput.text
    def loadImage(self):
        return image

    def pointillism(self):
        image = Image.open(self.ids.imageName.source)
        canvas = Image.new("RGB", (image.size[0], image.size[1]), "white")
        draw = ImageDraw.Draw(canvas)

        pixels = image.load()

        num_iterations = 5000

        for _ in range(num_iterations):
            x = random.randint(0, image.size[0] - 1)
            y = random.randint(0, image.size[1] - 1)

            pixel_color = pixels[x, y]
            size = random.randint(3, 5)

            ellipse_box = [(x, y), (x + size, y + size)]
            draw.ellipse(ellipse_box, fill=(pixel_color[0], pixel_color[1], pixel_color[2]))

        del draw  # Release the drawing context

        canvas.save("pointillism_output.png")
        self.ids.imageName.source = "pointillism_output.png"

    def apply_sobel_operator(self,image):
        sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

        grayscale_image = image.convert("L")

        output_image = Image.new("L", image.size)

        for x in range(1, image.width - 1):
            for y in range(1, image.height - 1):
                gx = 0
                gy = 0

                for i in range(3):
                    for j in range(3):
                        pixel_value = grayscale_image.getpixel((x + i - 1, y + j - 1))
                        gx += sobel_x[i][j] * pixel_value
                        gy += sobel_y[i][j] * pixel_value

                gradient_magnitude = int((gx ** 2 + gy ** 2) ** 0.5)

                threshold = 50
                if gradient_magnitude > threshold:
                    output_image.putpixel((x, y), 255)
                else:
                    output_image.putpixel((x, y), 0)

        return output_image

    def line_drawing(self):
        image = Image.open(self.ids.imageName.source)

        edges_image = self.apply_sobel_operator(image)

        contours = self.find_contours(edges_image)

        line_image = Image.new("L", image.size, color=0)
        draw = ImageDraw.Draw(line_image)

        for contour in contours:
            draw.line(contour, fill=255, width=1)

        line_image.save("line.png")
        self.ids.imageName.source = "line.png"

    def find_contours(self, binary_image):
        contours = []

        for x in range(binary_image.width):
            contour = []
            on_contour = False

            for y in range(binary_image.height):
                pixel_value = binary_image.getpixel((x, y))

                if on_contour and pixel_value == 0:
                    on_contour = False
                    contours.append(contour)
                    contour = []
                elif not on_contour and pixel_value == 255:
                    on_contour = True

                if on_contour:
                    contour.append((x, y))

        return contours
    def sepia(self):
        image = Image.open(self.ids.imageName.source)
        pixels = image.load()

        width, height = image.size
        for y in range(height):
            for x in range(width):
                pixels[x, y] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2])
                red = pixels[x, y][0] * .393 + pixels[x, y][1] * 0.769 + pixels[x, y][2] * 0.189
                green = pixels[x, y][0] * .349 + pixels[x, y][1] * 0.686 + pixels[x, y][2] * 0.168
                blue = pixels[x, y][0] * .272 + pixels[x, y][1] * 0.534 + pixels[x, y][2] * 0.131
                green = int(green)
                red = int(red)
                blue = int(blue)
                pixels[x, y] = (red, green, blue)
        image.save("sepia.png")
        self.ids.imageName.source = "sepia.png"

    def red(self):
        image = Image.open(self.ids.imageName.source)
        pixels = image.load()

        width, height = image.size
        for y in range(height):
            for x in range(width):
                pixels[x, y] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2])
                red = 255
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        image.save("red.png")
        self.ids.imageName.source = "red.png"
    def invert(self):
        image = Image.open(self.ids.imageName.source)
        pixels = image.load()

        width, height = image.size
        for y in range(height):
            for x in range(width):
                pixels[x, y] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2])
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        image.save("inverse.png")
        self.ids.imageName.source = "inverse.png"

    def pixel(self):
        pass

DisplayFrameApp().run()