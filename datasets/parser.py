from .label import KittiObj2DLabel

class KittiObj2DParser():
    def __init__(self,file_path):
        self.file_path = file_path
        self.parse_results = self.parse()
        #       self.label_list = [Label(self.parse_results[i]) for i in range(len(self.parse_results))]

    def parse(self):
        with open(self.file_path,'r') as f:
            lines = f.readlines()
        
        labels = []
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
                'rotation_y': float(elements[14]),
                'file_path': self.file_path
            }
            labels.append(obj_dict)

        return labels
 
