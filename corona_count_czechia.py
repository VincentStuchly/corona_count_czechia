import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import bs4, requests, time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)


disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 10
top = padding
x = 0

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('font.ttf', 22)

while True:
    disp.clear()
    disp.display()
    res = requests.get('http://www.idnes.cz')
    res.raise_for_status()
    exampleSoup = bs4.BeautifulSoup(res.text,'html.parser')
    extrakt = exampleSoup.select('.megapruh-counts')
    a = extrakt[0].getText()

    # Write two lines of text.
    draw.text((x, top),a[12:17] ,  font=font, fill=255)
    draw.text((x, top+30),'cases' ,  font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(3600)

