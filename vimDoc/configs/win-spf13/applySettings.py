import os
os.system('cls')

localDir = 'C:/Users/Administrator'
spfdir = 'C:\Users\Administrator\.spf13-vim-3'
gitDir = 'C:/Users/Administrator/Documents/gitDoc/ubuntuMemo/vimDoc/configs/win-spf13'


files = ".vimrc .vimrc.before .vimrc.bundles".split()

for f in files:
    pathFrom = os.path.join(spfdir, f)
    pathTo   = os.path.join(gitDir, f)
    command = "ln {} {}".format(pathFrom, pathTo)
    print command
    # os.system(command

pfrom = os.path.join(localDir, ".vimrc.local")
pto = os.path.join(gitDir, ".vimrc.local")
command = "ln {} {}".format(pfrom, pto)
print command
