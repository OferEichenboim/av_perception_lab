class KittiObj2DLabel:
    def __init__(self,label_dict):
        self.type = label_dict["type"]
        self.truncated = label_dict["truncated"]
        self.occluded = label_dict["occluded"]
        self.alpha = label_dict["alpha"]
        self.bbox = KittiObj2DBbox(label_dict["bbox"])
        self.dimensions = label_dict["dimensions"]
        self.location = label_dict["location"]
        self.rotation_y = label_dict["rotation_y"]  
        self.path = label_dict["file_path"]

        

class KittiObj2DBbox:
    def __init__(self,bbox): #lx, ly, rx, ry = map(int, self.bbox)
        self.lx, self.ly, self.rx, self.ry = bbox[0], bbox[1], bbox[2], bbox[3]
        self.start_point = (self.lx,self.ly)
        self.end_point = (self.rx,self.ry)

    #TODO: normalize the bounding box to the (H,W) of the image - 


class ImageLabels():
    def __init__(self,image_path,labels):
        self.image_path = image_path
        self.labels = labels

    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self,idx):
        return self.labels[idx]

