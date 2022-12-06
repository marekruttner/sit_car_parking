import cv2
import numpy as np
from tflite_support.task import processor
from random import randint

_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_COLOR = (255, 0, 0)

"""
for i, detections in enumerate(_COLOR):
  if _COLOR in detection_result.detections:
    np.random.random(size=3) * 255

"""
"""
bar = ["0, 0, 255", "0, 255, 0", "255, 0, 0"]

for indx, detections in enumerate(bar):
"""


def visualize(
        image: np.ndarray,
        detection_result: processor.DetectionResult,
) -> np.ndarray:
    for detection in detection_result.detections:
        # Draw bounding_box
        bbox = detection.bounding_box
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
        category = detection.classes[0]
        class_name = category.class_name
        if class_name == 'car':
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
