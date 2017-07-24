(all commands are in lowercase)

$ who am i    |   (what is the time I logged in)

$ pwd | path working directory

$ clear | clear screen

$ cal | calender

$ cal 7 2017

$ date


$ date '+DATE: %m-%y%nTIME:%H:%M:%S'
DATE: 07-17


$ touch file1 file2 file3 file4 file4

$ mkdir My_dir_name

$ mkdir ~/Documents/MyDir

$ cd ~/Documents/MyDir


$ cat > testFile | write into a file (or new file)
xxxxxxxxx xx  xxx  xxxxx
^d

$ cat < testFile | read text out of a file
$ cat testFile


$ cat A B > C

$ mv <fileNameA> <fileNameB>

$ rm <fileName> <fileName1>
$ rm *.txt
$ rm *

(remove a directory)
$ rm -rf *
$ rm -r <dirName>
$ rmdir <dirName>

$ cp <fpA> <fpB>

(hard link)
ln <oldfileName> <newFileName>

(soft link is just a pointer)
ln -s <ori_file_name> <lnk_file_name>


umask

ls
ls <MyDir>
ls -l
(same as) ll
ls -a

(Change file Permissions)
chmod 764 <fileName>

uname -a



( Count lines, words, chars with 'wc')

file *

wc <fileName>
wc -l <fileName>
wc -w <fileName>


### Sort
> sort <fileName>
(this won't change the file, but show it sorted)


### cut through a file
cut -d"-" -f 1,3 players

### convert & copy file with 'dd'
dd if=test of=outfile conv=ucase

### manul, banner

man cat  (manu of 'cat')

banner "Hello World"

### compress -v <fileName>
compress -v <fileName>
zcat <fileName.z>
uncompress <fileName.z>

### Scripts 0
vim test.sh
  echo "Hello World!"
  #This is  a simple shell script.

  echo "This is my second script file."
  pwd
  ls
  seq 1 10
  banner "THE END"

  echo "Please enter you name:"
  read user_name
  echo "Hello $user_name, It's a fine day, isn't it?"



