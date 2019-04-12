"""
Reads in a tsv file with pre-trained bottom up attention features and
stores it in HDF5 format.  Also store {image_id: feature_idx}
 as a pickle file.
Hierarchy of HDF5 file:
{ 'image_features': num_images x num_boxes x 2048 array of features
  'image_bb': num_images x num_boxes x 4 array of bounding boxes }
"""


import os
import io
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import base64
import csv
import h5py
import pickle
import numpy as np
import utils
from tqdm import tqdm
from address_server_caption import *
import os
import pdb

decrement = True
maxInt = sys.maxsize

while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

FIELDNAMES = ['image_id', 'image_w', 'image_h', 'num_boxes', 'boxes', 'features']



infile = os.path.join(addr_BU_path,'test2014_36/test2014_resnet101_faster_rcnn_genome_36.tsv')
test_data_file = os.path.join(addr_hdf5path,'test201436.hdf5')
test_indices_file = os.path.join(addr_pkl_path,'test201436_imgid2idx.pkl')
test_ids_file = os.path.join(addr_pkl_path,'test201436_ids.pkl')

feature_length = 2048
num_fixed_boxes = 36


if __name__ == '__main__':
    h_test = h5py.File(test_data_file, "w")

    if os.path.exists(test_ids_file):
        test_imgids = pickle.load(open(test_ids_file, 'rb'))
    else:
        test_imgids = utils.load_imageid(addr_test_imgs)
        pickle.dump(test_imgids, open(test_ids_file, 'wb'),protocol=2)


    test_indices = {}

    test_img_features = h_test.create_dataset(
        'image_features', (len(test_imgids), num_fixed_boxes, feature_length), 'f')
    test_img_bb = h_test.create_dataset(
        'image_bb', (len(test_imgids), num_fixed_boxes, 4), 'f')
    test_spatial_img_features = h_test.create_dataset(
        'spatial_features', (len(test_imgids), num_fixed_boxes, 6), 'f')

    test_counter = 0
    unknown_ids = []

    print("reading tsv...")
    print('%d image_ids left...' % len(test_imgids))
    with open(infile, "r+") as tsv_in_file:
        reader = csv.DictReader(tsv_in_file, delimiter='\t', fieldnames=FIELDNAMES)
        for item in reader:
            item['num_boxes'] = int(item['num_boxes'])
            item['boxes'] = bytes(item['boxes'], 'utf')
            item['features'] = bytes(item['features'], 'utf')
            image_id = int(item['image_id'])
            image_w = float(item['image_w'])
            image_h = float(item['image_h'])
            bboxes = np.frombuffer(
                base64.decodestring(item['boxes']),
                dtype=np.float32).reshape((item['num_boxes'], -1))

            box_width = bboxes[:, 2] - bboxes[:, 0]
            box_height = bboxes[:, 3] - bboxes[:, 1]
            scaled_width = box_width / image_w
            scaled_height = box_height / image_h
            scaled_x = bboxes[:, 0] / image_w
            scaled_y = bboxes[:, 1] / image_h

            box_width = box_width[..., np.newaxis]
            box_height = box_height[..., np.newaxis]
            scaled_width = scaled_width[..., np.newaxis]
            scaled_height = scaled_height[..., np.newaxis]
            scaled_x = scaled_x[..., np.newaxis]
            scaled_y = scaled_y[..., np.newaxis]

            spatial_features = np.concatenate(
                (scaled_x,
                 scaled_y,
                 scaled_x + scaled_width,
                 scaled_y + scaled_height,
                 scaled_width,
                 scaled_height),
                axis=1)

            if image_id in test_imgids:
                test_imgids.remove(image_id)
                test_indices[image_id] = test_counter
                test_img_bb[test_counter, :, :] = bboxes
                test_img_features[test_counter, :, :] = np.frombuffer(
                    base64.decodestring(item['features']),
                    dtype=np.float32).reshape((item['num_boxes'], -1))
                test_spatial_img_features[test_counter, :, :] = spatial_features
                test_counter += 1
            else:
                unknown_ids.append(image_id)
        print('%d unknown_ids...' % len(unknown_ids))

    if len(test_imgids) != 0:
        print('Warning: test_image_ids is not empty')

    pickle.dump(test_indices, open(test_indices_file, 'wb'))
    h_test.close()
    print("done!")