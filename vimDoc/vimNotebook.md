/home/vi/Documents/ubuntuMemo/vimDoc/vimNotebook.md
## MOTIONS:

    h  j  k  l

    gg   G   <number>gg

    ( Ctrl + g  -  show current postion )

    0   $

    H   M   L

    w   e   b   W   E   B

    gj  gk  - move cursor in line

    (   )   - between sentences
    {   }   - between Paragraphs


    f<char>   find to   char
    t<char>   till char (berore char)
    ft<char>  find till char

        df.
        cf"
        vip
        cis

    e - means 'to end', 'with end'

## Quick Tips
    S for ddO
    daw for dbx

## TEXT OBJECTS:
    > word, sentence, block, paragraph
    > w     s         b      p
    ci" - change in quotes
    
## History position

	<Ctrl+i>  向新位置跳转
	<Ctrl+o>  向旧位置跳转

## Last point in the change list:
        g;
        g,

## SAVE, CLOSE:

    <esc>:w<cr>

    <esc>:w <filename><cr>

    <esc>:q!<cr>     强行退出（不保存）

    <esc>:wq!<cr>    强行保存退出

## Delete

	x

	dw（从当前位置，删除到下一word之前）    diw (只删除所在位置的word)

	dd    dgg   dG   D

	d2j   d2k

	d0    d$

## Write, Insert, Append

	i  I  a  A

	c  C  s  S

	ciw   ca"   cib   cip

	c2j  向下删除2行（共3行），并且开始写入

	o    在下面创建新行，开始写入

	O    在上面创建新行，开始写入



## Back, forward

	U  恢复本行最初状态

	u  全局回退

	<Ctrl-r>  全局前进



## Paste

	p 粘贴在之后   

	<number>p 多次粘贴

	P 粘贴在之前


## Replace

	r  替换单个字符

	R  持续替换多个字符


## Search

	/<searchString><cr>

	n  下一个

	N  上一个

	:set ic    设置查找时忽略大小写(Ignore Case) 
	:set noic  相反操作

	:set   hlsearch
	:set nohlsearch

## Search word on this position

    *   n   N


## Brackets pair:

	%

## Search / Replace

	:%s/old/new/g    整个文件全部替换
	:%s/old/new/gc   整个文件全部替换，逐一询问
	:#,#s/old/new/g    按行数，局部选取替换

	:s/old/new/g     本行替换所有
	:s/old/new/g     本行替换第一个


## Outer terminal commands:

	:!<command>

	example:
		!dir
		:!ls
		:!pwd
		:!python %
		:!source %


## Visual Select, Save them as file

	v<motion>:w <filename><cr>


## Read in file, or 'outer terminal output of commands

	:r !<order>

	example:
		:r !ls
		:r ../filename<cr>


## Powerful HELP system:
	<help>
	<F1>
	:help
	:help w



## vimrc files

	vim ~/.vimrc

	:r $VIMRUNTIME/vimrc_example.vim 读入外部文件


## Autocomplete 1

	命令输入一部分，可用<Tab>切换， 用<Ctrl+d>显示列表；

## Autocomplete 2

    ^n  ^n  ^p
    
    ^xf
		example:
			path = "../../<Ctrl+x>f


## Buffers

    :ls
    :b <name><tabs>


## Registers

    "ay4e
    "by4w
    
    "ap
    "bp

	VisualSelect > "ay  |  "ay3j

	"+p  -  + is the [SYSTEM REGISTER]
	"*p
    
	:reg - view the contents of registers
	
    "0 - the yank register
	"[1-9] - history register
	"[a-z] - named register

	"/  - current search pattern
	"-  - small delete
	"=  - expression register
	"_  - black hole register 
	":  - last :command
	".  - last inserted text
	"%  - filename of current buffer
	:h registers   -  for help
			example: 
					"_y2j
					d2j"_
					^r:
					^r.

## System Clipboard

	"+Y    or   "+yy

	"+y4j

## Macro

    qa<do stuff>q
    qb<do stuff>q

    @a
    @b

## Plugins
    
    Nerdtree
    Ctrlp
    Surround

~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 

/home/vi/Documents/Notebooks/vim_notebook.md
### Normal mode
### insert mode
    iI  xi cC S  oO

### visual mode, v V C-v
### substitute mode,  r, R, <visual mode>:s

:e! filename     放弃当前文件，编辑新文件
:e!              重新加载当前文件

:ctrl+g     显示: 文件名、进度
gf               打开光标处文件路径的文件

:w
:wq
:waq!

ZZ 或 :x         保存>退出
:saveas newFileName   另存为

:Sex    水平分割窗口，开文件系统
:Vex    垂直分割窗口，开文件系统

h j k l gj gk
<Enter>  或加号， 光标移动到下一行非空字符
-        减号

wW eE bB 0 ^ $ gg G
<num>gg   <num>j
()  {}   句，段  
fc f f f       寻找字符c, 继续寻找
前缀数字使用上面的操作

0  g0  $  g$
50|    移动到50列
50%    移动到文档百分比
50gg   移动到50行
5j 5k  向下/向上 移动5行

zz     当前行，显示在中部
zt                   顶部
zb     当前行，移动到底部

ma   'a
mA   'A    全局标记，重启vim仍然有效
:delmarks! 删除所有标记

iI  oO  cC  Ss

yy  yaw  dis  ci"   <operation><range>

:m,ny   复制m到n行， 类似有 :m,nd

d/foo<cr>  删除，直到内容foo

pP         之后，之前粘贴

"cyy   "cp    寄存器保存，粘贴
:reg          显示寄存器内容
              例如： "%p 粘贴当前文件名 
"+yy          系统剪切板

aw, as, ap, ab 与 y d c v 进行组合

常用替换：
<Visual Mode>  :s/old/new/g    可视模式
:l1,l2s/old/new/g              行号范围
:%s/old/new/g                  %表示全局
    0 首行
    $ 尾行
    . 本行
    % 所有行

正则表达式：
    ^  行首
    $  行尾
    \d  十进制数
    \s  空格
    \S  非空格
    \a  英文字母
    \|  或
    \\  表示\
    \.  表示.
    .   任意字符


