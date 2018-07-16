# -*- coding: utf-8 -*-
import time
import numpy as np
import tensorflow as tf
import sys
import os

sys.path.append("research")
sys.path.append("research/object_detection")

from utils import label_map_util
from utils import visualization_utils as vis_util
from matplotlib import pyplot as plt
from PIL import Image


# 预测模型所在路径及文件名
PATH_TO_LABELS = os.path.join('research/object_detection/data','mscoco_label_map.pbtxt')
PATH_TO_CKPT ='frozen_inference_graph.pb'
NUM_CLASSES =90
# For the sake of simplicity we will use only 2 images:
# image1.jpg
# image2.jpg
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = 'image'
image_path = 'image/fruit.jpg'
warm_up_image_path = 'image/warm_up_pic.jpg'
# TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image.jpg') ]
# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:   # 读入训练的模型
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS) # 对应的标签
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories) # 标签对应的名称 及 索引

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


sess = tf.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
# Each box represents a part of the image where a particular object was detected.
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
# Each score represent how level of confidence for each of the objects.
# Score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

def warm_up():
    print 'warm-up......'
    image1 = Image.open(warm_up_image_path)
    image1_np = load_image_into_numpy_array(image1)
    image1_np_expanded = np.expand_dims(image1_np, axis=0)
    for i in range(0, 10):
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: image1_np_expanded})
    print 'warn-up finished'


def recg():
    image = Image.open(image_path)
    image_np = load_image_into_numpy_array(image)
    image_np_expanded = np.expand_dims(image_np, axis=0)
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_np_expanded})
    print scores
    print classes
    # print num
    # print category_index
    obj_dict ={}
    reslult = ''
    obj_dict[0] = ''
    for i in range(5):
        if scores[0][i] >0.60:
            obj_dict[i] = category_index[classes[0][i]]['name']
            print obj_dict[i]
    result = obj_dict[0]
    for i in range(1,5):
        if i in obj_dict and obj_dict[i]!= result:
            result = 'error'
            break
    return result
# Visualization of the results of a detection.
'''
vis_util.visualize_boxes_and_labels_on_image_array(
  image_np,
  np.squeeze(boxes),
  np.squeeze(classes).astype(np.int32),
  np.squeeze(scores),
  category_index,
  use_normalized_coordinates=True,
  line_thickness=8)
plt.figure(figsize=IMAGE_SIZE)
plt.imshow(image_np)
plt.show()
'''

def release():
    sess.close()

warm_up()

