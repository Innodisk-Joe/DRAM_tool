import cv2
import configparser

def Initialization_config(path,header):
    try:
        config = configparser.ConfigParser()
        config.read(path)
        config_items=config.items(header)      
        return config_items
    except:
        return False 

def get_optimal_font_scale(width,text,fontface):
    for scale in range(59,10,-1):
        textSize = cv2.getTextSize(text, fontFace=fontface, fontScale=scale/10, thickness=1)
        new_width = textSize[0][0]
        if (new_width < width*0.8):
            return scale/10
    return 1
