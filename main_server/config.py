from easydict import EasyDict as edict
__C=edict()

conf=__C

#commend sent from client
__C.SEARCH_BY_NAME=0
__C.SEARCH_BOUNDING_BOX=1
__C.SERRCH_COORDINATE=2
__C.IMAGE_ANALYSIS=3

#map engine code
__C.GOOGLE=0
__C.BAIDU=1

#cache path
__C.CACHE='cache'
__C.ANNOTATION='annotation'

#number of image analysis server
__C.NUMBER_OF_IMAGE_ANALYSIS_SERVER=1

#image analysis server address
__C.ADDRESSES=['http://tangshitao.51vip.biz:54123/detect/']