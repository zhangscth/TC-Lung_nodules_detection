import os
COMPUTER_NAME = os.environ['COMPUTERNAME']
print("Computer: ", COMPUTER_NAME)

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
TRAIN_SUBSET_START_INDEX = 0
TRAIN_SUBSET_TRAIN_NUM = 15
TEST_SUBSET_START_INDEX = 0
TEST_SUBSET_TRAIN_NUM = 5
VAL_SUBSET_START_INDEX = 0
VAL_SUBSET_TRAIN_NUM = 5
SEGMENTER_IMG_SIZE = 320

BASE_DIR_SSD = "D:/Shi/python/TMCI/DSB2/DSB2017/data/"
BASE_DIR = "D:/Shi/python/TMCI/DSB2/DSB2017/data/"
EXTRA_DATA_DIR = "resources/"
# NDSB3_RAW_SRC_DIR = BASE_DIR + "ndsb_raw/stage12/"
RAW_SRC_DIR = BASE_DIR + "raw_data/"

TEST_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "test_extracted_images/"
TRAIN_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "train_extracted_images/"
VALIDATION_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "val_extracted_images/"
TEST_NODULE_DETECTION_DIR = BASE_DIR_SSD + "test_nodule_predictions/"
VAL_NODULE_DETECTION_DIR = BASE_DIR_SSD + "val_nodule_predictions/"
TRAIN_NODULE_DETECTION_DIR = BASE_DIR_SSD + "train_nodule_predictions/"
