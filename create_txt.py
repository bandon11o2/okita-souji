import os
import shutil


datasetname = '7class'

dir_main = './dataset'
new_dir = dir_main+'/data'

if os.path.exists(new_dir):
	shutil.rmtree(new_dir)
os.mkdir(new_dir)

train_dir = dir_main+'/images/train'
img_names = next(os.walk(train_dir))[2]
img_paths = [train_dir+'/'+aa for aa in img_names]
content = ''
for img_path in img_paths:
	content += img_path + '\n'
content = content[:-1]
with open(new_dir+'/'+'train.txt','w') as fw:
	fw.write(content)

test_dir = dir_main+'/images/test'
img_names = next(os.walk(test_dir))[2]
img_paths = [test_dir+'/'+aa for aa in img_names]
content = ''
for img_path in img_paths:
	content += img_path + '\n'
content = content[:-1]
with open(new_dir+'/'+'test.txt','w') as fw:
	fw.write(content)

content = 'car' +'\n' + 'bus' +'\n' + 'truck'+'\n' + 'bike'+'\n'+ 'motor'+'\n'+'person'+'\n'+'rider'
with open(new_dir+'/'+datasetname+'.name','w') as fw:
	fw.write(content)
content = 'classes=7' + '\n' + 'train='+new_dir+'/'+'train.txt'+'\n'+'valid='+new_dir+'/'+'test.txt' + '\n' + 'names='+new_dir+'/'+datasetname+'.name'
with open(new_dir+'/'+datasetname+'.data','w') as fw:
	fw.write(content)

