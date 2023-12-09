import turtle
from rndv2 import*
import rndv2
import math
def translate_and_draw(pointlist, translation_vector):
    """
    Translates a 2D point using homogeneous coordinates and draws both the original
    and translated points using the turtle library.

    Parameters:
    - original_point: A tuple representing the point in homogeneous coordinates (px, py).
    - translation_vector: A tuple representing the translation (a, b).

    Returns:
    a list of translated points to be flattened 
    

        """
    
    def translate_point_turtle(point, translation_vector,LOC):
        translated_point=[]
        px, py = point  # this portion of the code is taken reference from chatgpt
        a, b = translation_vector
        line=str(int(px) + a),str(int(py) + b),LOC
        # Perform translation
        translated_point.append(line)


        return translated_point
    tranedlist=[]
    # Perform translation
    for obj in pointlist:
            if obj=="":
                pass
            else:
                    try:
                        line2=translate_point_turtle([obj[0],obj[1]],translation_vector,obj[2])
                        tranedlist.append(line2)
                    except ValueError:
                        line2=translate_point_turtle([obj[1],obj[2]],translation_vector,obj[3])
                        tranedlist.append(line2)
    return tranedlist        

