import time
import re
import os

t = time.time()

reponame = os('git remote get-url origin')
#reponame = 'https://github.com/satishbraju/unit.git'
name = re.split('/', reponame )
gitname = name[4]
real_name = re.split('.git', gitname)
r_name = real_name[0]
tagname = "%s-%s" %(r_name,t)
#filename = "%s/%s-patchdata.json" % (stgloc, release)

print(tagname)