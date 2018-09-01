######## Image Object Detection Using Tensorflow-trained Classifier ######

#importing necessary packages for image classification#
import os
import cv2
import numpy as np
import tensorflow as tf
import sys

sys.path.append("..")


#imported utilities also visualization_utils_db for fruits database

from utils import label_map_util
from utils import visualization_utils_DB as vis_util

# Name of the directory that contains the object detection models
MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'test_mango.jpg'

CWD_PATH = os.getcwd()


#path to the frozen_inference.pb file for object detection
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph_mango.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','mango_labelmap.pbtxt')

# Path to image
PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

NUM_CLASSES = 1


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


#this opens the images
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)


(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})



#this function imported from visualization utils is used to draw the box around the images and detect  the object
vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=8,
    min_score_thresh=0.80)


cv2.imshow('Object detector', image)

cv2.waitKey(0)

cv2.destroyAllWindows()
