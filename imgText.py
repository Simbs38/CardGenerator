import cv2


class ImgText:

    def __init__(self):
        pass

    @staticmethod
    def InsertText(cardInfo, card):
        img = ImgText.putText(card, cardInfo.name, 120, 750)
        img = ImgText.putText(img, cardInfo.text, 80, 850, fontScale = 0.8)
        if hasattr(cardInfo, 'prestige'):
            img = ImgText.putText(img, cardInfo.prestige, 700, 100)	
        return img
		

    @staticmethod
    def putText(image, text, x = 120, y0 = 700, dy = 30, font = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1,color = (0, 0, 0),thickness = 2):
        print(type(text))        
        print(text)
        if(type(text) != float):
            for i, line in enumerate(text.split('\\n')):
                y = y0 + i*dy
                print(line)
                cv2.putText(image, line, (x, y ), font, fontScale,color,thickness, cv2.LINE_AA) 
    	    
        return image

