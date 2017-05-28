import pdb
import poserecog.pipe as pipe
import glob

config_path = 'model/model.config'
piper = pipe.Pipeline(config_path)

base_path = 'dataset/weizmann'
img_list = glob.glob(base_path+'/*.jpg')
scls = set([x.split('/')[-1].rsplit('_',1)[0] for x in img_list])
print '%d videos' % len(scls)

for c in scls:
  path =  '%s/%s_*.jpg' % (base_path,c)
  piper.process(path)

piper.plot_len_dist()
