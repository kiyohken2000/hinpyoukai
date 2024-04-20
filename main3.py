import face_recognition
from PIL import Image, ImageDraw

offset_x = 2
offset_y = 2

grid_width = 1
grid_height = 200

load_image = face_recognition.load_image_file("image.jpg")

face_locations = face_recognition.face_locations(load_image)

face_locations = sorted(face_locations, key=lambda x: (x[0] // grid_height, x[1] // grid_width))

pil_image = Image.fromarray(load_image)
draw = ImageDraw.Draw(pil_image)

cnt = 0

for (top, right, bottom, left) in face_locations:
    cnt = cnt + 1
    draw.text((right + offset_x, top + offset_y), f'({cnt})', fill='black', stroke_fill='white', stroke_width=4)

del draw

pil_image.save("output_image.jpg")