import cv2
import lowpass_filter
import breath_rates
import spectrogram
#def signalExtraction(video_path):
    
#init params
meanGrayLevels = []
############

#capture of the video
vidcap = cv2.VideoCapture(r"C:\Users\slabid\Desktop\breathing_signal_extraction_python\FLIROne\trials\Cropped_1.mp4")
#('C:/Users/slim94/Desktop/spyder_projects/Matlab_Signal_Extraction/FLIROne/trials/Cropped_1.mp4')
#vidcap = cv2.VideoCapture(video_path)
success,frame = vidcap.read()
######################

#Get the video props
#width = vidcap.get(3)
#print("width: ", width)
#height = vidcap.get(4)
#print("height: ", height)
fps = vidcap.get(5)
print("fps: ", fps)
total_frames = vidcap.get(7)
print("Total frames: ", total_frames)
################################################

#Loop all frames of the video
while vidcap.isOpened():
        #current_pos_in_video = vidcap.get(0) 
        #print("Current position in the video: ", current_pos_in_video) #in millisecond
        success,frame = vidcap.read()
        if success :
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                meanGrayLevels.append(grayFrame.mean())               
                cv2.imshow('video gray', grayFrame)  
        else:
                break 
        if(cv2.waitKey(1) == 27): #27 = touche escape
                break
            

#Add filter (lowpass) to smooth the breathing signal to get the respiratory rate 
smooth_data =  lowpass_filter.lowpassFilter(meanGrayLevels, fps)                
breath_rate = breath_rates.breathRates(smooth_data, total_frames, fps)
#Get the spectrogram of the breathing signal
spectrogram.sigSpectrogram(smooth_data)

#Wrap up everything
vidcap.release()
cv2.destroyAllWindows()