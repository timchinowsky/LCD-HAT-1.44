import LCD_1in44
import LCD_Config

from PIL import Image,ImageDraw,ImageFont,ImageColor
from time import sleep

def main():
    LCD = LCD_1in44.LCD()

    print("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)
    LCD.LCD_ShowImage(image,0,0)

    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
	
    sleep(5)
    print("***draw line")
    draw.line([(0,0),(127,0)], fill = "BLUE",width = 5)
    draw.line([(127,0),(127,127)], fill = "BLUE",width = 5)
    draw.line([(127,127),(0,127)], fill = "BLUE",width = 5)
    draw.line([(0,127),(0,0)], fill = "BLUE",width = 5)
    LCD.LCD_ShowImage(image,0,0)

    sleep(5)
    print("***draw rectangle")
    draw.rectangle([(18,10),(110,20)],fill = "RED")
    LCD.LCD_ShowImage(image,0,0)

    sleep(5)
    print("***draw text")
    draw.text((33, 22), 'WaveShare ', fill = "BLUE")
    draw.text((32, 36), 'Electronic ', fill = "BLUE")
    draw.text((28, 48), '1.44inch LCD ', fill = "BLUE")

    LCD.LCD_ShowImage(image,0,0)
    LCD_Config.Driver_Delay_ms(500)

    sleep(5)
    print("***show image")

    image = Image.open('time.bmp')
    LCD.LCD_ShowImage(image,0,0)

if __name__ == '__main__':
    main()

