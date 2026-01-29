import copy

class Parser():
    def __init__(self,label_path):
        self.label_path = label_path
        self.parse_results = self.parse_label_file()
        self.label_list = [Label(self.parse_results[i]) for i in range(len(self.parse_results))]

    def parse_label_file(self):
        with open(self.label_path,'r') as f:
            lines = f.readlines()
        parse_results = []
        for line in lines:
            elements = line.strip().split(' ')
            obj_dict = {
                'type': elements[0],
                'truncated': float(elements[1]),
                'occluded': int(elements[2]),
                'alpha': float(elements[3]),
                'bbox': [float(elements[4]), float(elements[5]), float(elements[6]), float(elements[7])],
                'dimensions': [float(elements[8]), float(elements[9]), float(elements[10])],  # height, width, length
                'location': [float(elements[11]), float(elements[12]), float(elements[13])],  # x, y, z
                'rotation_y': float(elements[14])
            }
            parse_results.append(obj_dict)

        return parse_results
    
class Label():
    def __init__(self,label_dict):
        self.label_dict = label_dict
        self.type = label_dict["type"]
        self.truncated = label_dict["truncated"]
        self.occluded = label_dict["occluded"]
        self.alpha = label_dict["alpha"]
        self.bbox = Bbox(label_dict["bbox"])
        self.dimensions = label_dict["dimensions"]
        self.location = label_dict["location"]
        self.rotation_y = label_dict["rotation_y"]  

    def __str__(self):
        string = f"{self.label_dict}"
        return string
    
    def copy(self):
        return Label(copy.deepcopy(self.label_dict))
        

class Bbox():
    def __init__(self,bbox): #lx, ly, rx, ry = map(int, self.bbox)
        self.lx = bbox[0]
        self.ly = bbox[1]
        self.rx = bbox[2]
        self.ry = bbox[3]
        self.start_point = (self.lx,self.ly)
        self.end_point = (self.rx,self.ry)

    #TODO: normalize the bounding box to the (H,W) of the image - 
