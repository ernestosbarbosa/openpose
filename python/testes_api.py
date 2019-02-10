import sys
import cv2
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/../../python')

from openpose import *

params = dict()
params["logging_level"] = 3
params["output_resolution"] = "-1x-1"
params["net_resolution"] = "-1x368"
params["model_pose"] = "BODY_25"
params["alpha_pose"] = 0.6
params["scale_gap"] = 0.3
params["scale_number"] = 1
params["render_threshold"] = 0.05
params["num_gpu_start"] = 0
params["disable_blending"] = False
params["default_model_folder"] = dir_path + "/../../../models/"

openpose = OpenPose(params)

while 1:
    cap = cv2.VideoCapture('../../../examples/media/4.mp4')

    if (cap.isOpened()== False): 
      print("Erro ao abrir o arquivo")

    f = open("capture.json","w+")
    f.write("[")

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            keypoints, output_image = openpose.forward(frame, True)
#            print(keypoints)
            f.write(json.dumps(keypoints.tolist()))
            f.write(",")
#            cv2.imshow("output", output_image)
#            cv2.waitKey(15)
        else: 
            break
    
    f.write("[]]")
    f.close()
    cap.release()
#    cv2.destroyAllWindows()
    break


