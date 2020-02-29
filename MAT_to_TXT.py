import json
import glob
import cv2
'''
person_dict = json.loads('/home/anubhav/test_digitStruct.json','r')
print(person['filename'])
'''
with open('/home/anubhav/test_digitStruct.json') as f:
  datas = json.load(f)
files=glob.glob('/home/anubhav/Datasets/SVHN_DATASET/test/')
path='/home/anubhav/Datasets/SVHN_DATASET/test/'
txt_path='/home/anubhav/darknet/data/img/'
train=open("/home/anubhav/darknet/data/train.txt","w+")
for data in datas:
	temp=data
	filename=temp['filename']
	na=(filename.split("."))[0]
	print("etracted file nmae",na)
	f=open(txt_path+na+".txt","w+")
	img=cv2.imread(path+filename)
	imgh,imgw,_=img.shape
	print(imgw,imgh)
	box=temp['boxes']
	for number in box:
		label=int(number['label'])
		if label==10:
			label=0
		height=number['height']
		width=number['width']
		left=number['left']
		top=number['top']
		abs_x=abs(round((left+(width/2))/imgw,6))
		abs_y=abs(round((top+(height/2))/imgh,6))
		abs_height=abs(round((height/imgh),6))
		abs_width=abs(round(width/imgw,6))
		f.write(str(label)+" "+str(abs_x)+" "+str(abs_y)+" "+str(abs_width)+" "+str(abs_height)+"\n")
		#img=cv2.rectangle(img,(int(left),int(top)),(int(left+width),int(top+height)),(0,255,0),1)
		#img = cv2.putText(img,str(label), (int(left)-1,int(top)-1), cv2.FONT_HERSHEY_SIMPLEX,1, (0,255,0), 1, cv2.LINE_AA) 
		#print("Label height width left top ",label, height ,width ,left ,top )
		#print("Label height width left top ",label, abs_height ,abs_width ,abs_x ,abs_y )
	cv2.imwrite(txt_path+filename,img)
	#cv2.imshow("number",img)
	train.write("data/img/"+filename+"\n")
	f.close()
	#key=cv2.waitKey(0)
	#if key & 0xFF == ord('q'):
	#	break
#cv2.destroyAllWindows()

print("Processed All images")
train.close()
	
'''
5.0 0.22033898305084745 0.3611111111111111 0.1864406779661017 0.5
4.0 0.3898305084745763 0.6388888888888888 0.22033898305084745 0.5

'''

