import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, sys, cv2
import argparse

manhole_net_path="manhole_net"
model_path="final_models"
prototxt_path="final_prototxt"

NETS={"resnet50_rfcn_class_12_iter_100000":("resnet50_rfcn_class_12_iter_100000.prototxt","resnet50_rfcn_class_12_iter_100000.caffemodel")}

CONF_THRESH = 0.8
NMS_THRESH = 0.3
def detect(img,net_name="resnet50_rfcn_class_12_iter_100000",mode='gpu',gpu_id=0):
    cfg.TEST.HAS_RPN = True

    prototxt_name,model_name=NETS[net_name]
    prototxt=os.path.join(cfg.ROOT_DIR,manhole_net_path,prototxt_path,prototxt_name)
    model=os.path.join(cfg.ROOT_DIR,manhole_net_path,model_path,model_name)

    if not os.path.isfile(model):
        raise IOError(('{:s} not found.\n').format(model))

    if not os.path.isfile(prototxt):
        raise IOError(('{:s} not found.\n').format(prototxt))

    if mode=="gpu":
        caffe.set_mode_gpu()
        caffe.set_device(gpu_id)
        cfg.GPU_ID = gpu_id
    elif mode=="cpu":
        caffe.set_mode_cpu()

    net = caffe.Net(prototxt, model, caffe.TEST)

    print '\n\nLoaded network {:s}'.format(model)

    return im_detect(net, img)
