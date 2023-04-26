import cv2
import numpy as np
import utils
import argmanager
import DRAM

args=argmanager.get_args()

csv_path=None
for row in utils.Initialization_config(args.configpath,f'PATH'):
    if row[0]=='csv':
        csv_path=row[1]

dram_manager=DRAM.DRAM_alignment(csv_path)
transrole=np.array([4024/dram_manager.width,1866/dram_manager.height])
test=np.zeros([1866,4024,3],dtype=np.uint8)
for key,val in dram_manager.data[args.type].items():
    if 'box' in val:
        box=np.array(val['box']*transrole,dtype=np.int32)
        font_scale=utils.get_optimal_font_scale(box[1][0]-box[0][0],str(key),cv2.FONT_HERSHEY_PLAIN)
        cv2.putText(test, str(key), box[0]-[0,5], cv2.FONT_HERSHEY_PLAIN,font_scale, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(test,box[0],box[1],(0,255,0),3)
    else:
        point=np.array(val['point']*transrole,dtype=np.int32)
        cv2.putText(test, str(key), point-[10,15], cv2.FONT_HERSHEY_PLAIN, 1 , (0, 0, 255), 2, cv2.LINE_AA)
        cv2.circle(test,point,5,(0,0,255),3)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',test)
if cv2.waitKey(0) and 0xFF == ord('q'):
    cv2.destroyAllWindows()