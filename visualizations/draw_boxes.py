import cv2
from cv2 import rectangle,putText,FONT_HERSHEY_SIMPLEX
from datasets.kitti.object2d.parser import Label
from pathlib import Path

COLOR_DICT = {"green": (0,200,0), "red": (0,0,255), "blue": (255,0,0)}

class Box:
    def __init__(self,img,label,color = "green",thickness = 2):
        self.img = self.get_image_copy(img)
        self.label = label.copy()
        self.color = self.set_color_tup(color) 
        self.thickness = thickness

    def get_image_copy(self,img): 
        img = cv2.imread(str(img)).copy()
        img = cv2.cvtColor(img, code = cv2.COLOR_BGR2RGB)
        return img
    
    def draw(self):
        pass


    def set_color_tup(self,color):
        '''Set color tuple in BGR format for OpenCV'''
        try:
            return COLOR_DICT[color]
        except KeyError as e:
            return COLOR_DICT["green"]



class Box_kitti_obj2d(Box):
    def __init__(self,img,label,color = "green",thickness = 2):
        super().__init__(img,label,color,thickness)   
        self.bbox = self.label["bbox"]
        self.type = self.label["type"]

    def draw2(self): #bbox = left, top, right, bottom
        img_box = self.img.copy()
        lx, ly, rx, ry = map(int, self.bbox)
        start_point = (lx,ly)
        end_point = (rx,ry)
        img_box = rectangle(img_box, start_point, end_point, self.color, self.thickness)
        img_box = putText(img_box,self.type,(lx,ly-5),FONT_HERSHEY_SIMPLEX,0.5,self.color,1)
        return img_box
    
    def draw(self):  # bbox = left, top, right, bottom
        img_box = self.img.copy()
        lx, ly, rx, ry = map(int, self.bbox)

        # Draw bounding box
        cv2.rectangle(
            img_box,
            (lx, ly),
            (rx, ry),
            self.color,
            self.thickness
        )

        # ---- Text parameters ----
        label = self.type
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7          # <-- larger text
        font_thickness = 2
        text_color = (255, 255, 255)  # white

        # Get text size
        (text_w, text_h), baseline = cv2.getTextSize(
            label, font, font_scale, font_thickness
        )

        # Background rectangle coords
        pad = 4
        bg_top_left = (lx, ly - text_h - baseline - 2 * pad)
        bg_bottom_right = (lx + text_w + 2 * pad, ly)

        # Clamp to image top (important!)
        if bg_top_left[1] < 0:
            bg_top_left = (bg_top_left[0], 0)

        # Draw filled background rectangle
        cv2.rectangle(
            img_box,
            bg_top_left,
            bg_bottom_right,
            self.color,
            thickness=-1  # filled
        )

        # Put text on top of background
        text_org = (lx + pad, ly - baseline - pad)
        cv2.putText(
            img_box,
            label,
            text_org,
            font,
            font_scale,
            text_color,
            font_thickness,
            cv2.LINE_AA
        )

        return img_box

         

{'type': 'Car', 'truncated': 0.8, 'occluded': 0, 'alpha': -2.09, 'bbox': [1013.39, 182.46, 1241.0, 374.0], 'dimensions': [1.57, 1.65, 3.35], 'location': [4.43, 1.65, 5.2], 'rotation_y': -1.42}

