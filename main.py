from time import sleep
from PIL import Image, ImageDraw

def path_input():
    filePath = input("Enter Path of Image: ")

    while filePath.startswith("\""):
        filePath = filePath[1:]

    while filePath.endswith("\""):
        filePath = filePath[:-1]

    return filePath

def terminate():
    print("Terminating", end="")
    for i in range(3):
        print(".", end="")
        sleep(0.4)
    exit(0)


def image_resize():
    return image.resize((newWidth, newHeight))


def create_image():
    draw = ImageDraw.Draw(img)

    for y in range(height):
        for x in range(width):
            r, g, b = colorPixels[(x, y)]
            draw.point((x, y), (r, g, b))



print("Enter 'Quit', 'Exit', or '0' to Terminate...")

i = 1
while True:
    path = path_input()

    if path.lower() in ['quit', 'exit', '0']:
        terminate()

    try:
        image = Image.open(path)
    except FileNotFoundError:
        print("\033[0;31mProvided File Not Found\033[0m")
        continue
    except:
        print("\033[0;31mSomething went wrong when opening the file!\033[0m")
        continue

    newWidth = int(input("Enter width: "))
    if newWidth == 0: terminate()

    newHeight = int(input("Enter height: "))
    if newHeight == 0: terminate()

    image = image.convert("RGB")

    width, height = image.size
    image = image_resize()
    width, height = image.size

    colorPixels = image.load()

    img = Image.new("RGB", (width, height), (0, 0, 0))
    create_image()
    img.save(f"{path} {width}x{height} {i}.png")
    print(f"Scaled image created as \"{path} {width}x{height} {i}.png\" in the execution directory")

    i += 1


