"""
import cv2
import numpy as np
from tflite_support.task import processor
from random import randint

_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_COLOR = (255, 0, 0)


def visualize(
        image: np.ndarray,
        detection_result: processor.DetectionResult,
) -> np.ndarray:
    for detection in detection_result.detections:
        category = detection.classes[0]
        class_name = category.class_name
        if class_name == 'car':
            # num_detections = detection.classes[2]
            for i in range(2):
                # Draw bounding_box
                bbox = detection.bounding_box
                start_point = bbox.origin_x, bbox.origin_y
                end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height

                cv2.rectangle(image, start_point, end_point, _COLOR, 3)

                # Draw label and score
                # category = detection.classes[0]
                # class_name = category.class_name
                probability = round(category.score, 2)
                result_text = class_name + ' (' + str(probability) + ')'
                text_location = (_MARGIN + bbox.origin_x,
                                 _MARGIN + _ROW_SIZE + bbox.origin_y)
                cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                            _FONT_SIZE, _COLOR, _FONT_THICKNESS)

                return image


"""
import cv2
import numpy as np
from tflite_support.task import processor
from random import randint
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours


_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_COLOR = (255, 0, 0)

def visualize(
        image: np.ndarray,
        detection_result: processor.DetectionResult,
) -> np.ndarray:


    for detection in detection_result.detections:
        print("detection one:")
        # print(detection_result.detections[0])
        det_A = detection_result.detections[0]
        det_Abb = det_A.bounding_box
        print(det_Abb)
        print("detection two:")
        # print(detection_result.detections[1])
        det_B = detection_result.detections[1]
        det_Bbb = det_B.bounding_box
        print(det_Bbb)

        l_start_point_A = det_Abb.origin_x + det_Abb.width, det_Abb.origin_y
        l_start_point_B = det_Bbb.origin_x, det_Bbb.origin_y

        # Draw bounding_box
        bbox = detection.bounding_box
        # print(detection)
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
        # print(bbox)
        # print(detection.classes[0])
        # print(detection)
        cv2.rectangle(image, start_point, end_point, _COLOR, 3)
        cv2.line(image, l_start_point_A, l_start_point_B, _COLOR, 3)
        D = dist.euclidean(l_start_point_A, l_start_point_B)
        D_metric = (D * 2.54) / 1000
        print(D_metric)
        _COLOR_R = (0, 255, 0)
        _COLOR_W = (0, 0, 255)

        # Draw label and score
        category = detection.classes[0]
        class_name = category.class_name
        probability = round(category.score, 2)
        result_text = class_name + ' (' + str(probability) + ')'
        text_location = (_MARGIN + bbox.origin_x,
                         _MARGIN + _ROW_SIZE + bbox.origin_y)
        cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    _FONT_SIZE, _COLOR, _FONT_THICKNESS)

        if D_metric <=3:
            cv2.putText(image, "{:.1f}m".format(D_metric), (1200, 1000),
                        cv2.FONT_HERSHEY_SIMPLEX, 10, _COLOR_W, 5)
        if D_metric >=3:
            cv2.putText(image, "{:.1f}m".format(D_metric), (1200, 1000),
                        cv2.FONT_HERSHEY_SIMPLEX, 10, _COLOR_R, 5)
    return image
# """
