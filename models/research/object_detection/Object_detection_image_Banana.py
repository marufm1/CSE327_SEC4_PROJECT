#importing all the necessary dependencies
import os
import cv2
import numpy as np
import tensorflow as tf
import sys


sys.path.append("..")

#Here we are using a newly modified visualization_utils_DB which was edited previously for adding the database support
from utils import label_map_util
from utils import visualization_utils_DB as vis_util

#Getting the inference graph folder and image name
MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'test_banana.jpg'


CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph_banana.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','banana_labelmap.pbtxt')

# Path to image
PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

#The number of object to be detected is 1 as this file and frozen graph is only for Banana
NUM_CLASSES = 1

#label map path
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

num_detections = detection_graph.get_tensor_by_name('num_detections:0')

image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)

(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})

#This part is used for visualizing the rectangular box on the image and also show the information 
vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=8,
    min_score_thresh=0.50)

#Added the window size so that a bigger image is shown 

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800,700)

cv2.imshow('image', image)


cv2.waitKey(0)

cv2.destroyAllWindows()
