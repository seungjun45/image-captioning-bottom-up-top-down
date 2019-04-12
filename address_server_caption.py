# file address scripts
import platform
import os

addr_dataroot = os.path.join('codes', 'tools', 'data')

# sys.path.append('D:\\VQA\\BAN')
# BAN address
if (platform.system() == 'Linux'):
    addr_BAN = '../../VQA/BAN'
    addr_test_imgs = '../../Data_Share/Datas/VQA_COCO/Images/test2014'
    addr_train_imgs = '../../Data_Share/Datas/VQA_COCO/Images/train2014'
    addr_val_imgs = '../../Data_Share/Datas/VQA_COCO/Images/val2014'
    addr_hdf5path = '../../Data_Share/Datas/VQA_COCO/BottomUpPreTrain/hdf5'
    addr_coco_cap_train_path = '../../Data_Share/Datas/VQA_COCO/annotations/captions_train2014.json'
    addr_coco_cap_val_path = '../../Data_Share/Datas/VQA_COCO/annotations/captions_val2014.json'
    addr_coco_cap_test_path = '../../Data_Share/Datas/VQA_COCO/annotations/image_info_test2015.json'
    addr_coco_cap_test_dev_path = '../../Data_Share/Datas/VQA_COCO/annotations/image_info_test-dev2015.json'
    addr_coco_cap_test2014_path = '../../Data_Share/Datas/VQA_COCO/annotations/image_info_test2014.json'
    addr_cider_score_path = '../../XAI/coco_caption_jiasen3'
    addr_vqae_val_path = '../../Data_Share/Datas/VQA-E/VQA-E_val_set.json'
    addr_vqae_train_path = '../../Data_Share/Datas/VQA-E/VQA-E_train_set.json'
    addr_hdf5fix_path = '../../Data_Share/Datas/VQA_COCO/BottomUpPreTrain/hdf5'
    addr_pkl_path = '../../Data_Share/Datas/VQA_COCO/BottomUpPreTrain/pkl'
    addr_BU_path = '../../Data_Share/Datas/VQA_COCO/BottomUpPreTrain'

elif (platform.system() == 'Windows'):
    addr_BAN = 'D:\\VQA\\BAN'
    addr_test_imgs = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\test2014'
    addr_train_imgs = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\train2014'
    addr_val_imgs = 'D:\\Data_Share\\Datas\\VQA_COCO\\Images\\val2014'
    addr_hdf5path = '../../Data_Share/Datas/VQA_COCO/BottomUpPreTrain/hdf5'
    addr_coco_cap_train_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\annotations\\captions_train2014.json'
    addr_coco_cap_val_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\annotations\\captions_val2014.json'
    addr_coco_cap_test_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\annotations\\image_info_test2015.json'
    addr_coco_cap_test_dev_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\annotations\\image_info_test-dev2015.json'
    addr_coco_cap_test2014_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\annotations\\image_info_test2014.json'
    addr_cider_score_path = 'D:\\XAI\\coco_caption_jiasen3'
    addr_vqae_val_path = 'D:\\Data_Share\\Datas\\VQA-E\\VQA-E_val_set.json'
    addr_vqae_train_path = 'D:\\Data_Share\\Datas\\VQA-E\\VQA-E_train_set.json'

    addr_hdf5fix_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\BottomUpPreTrain\\hdf5'
    addr_pkl_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\BottomUpPreTrain\\pkl'

    addr_BU_path = 'D:\\Data_Share\\Datas\\VQA_COCO\\BottomUpPreTrain'