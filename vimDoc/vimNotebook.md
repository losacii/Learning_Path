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

	<Ctrl+i>  ����λ����ת
	<Ctrl+o>  ���λ����ת

## Last point in the change list:
        g;
        g,

## SAVE, CLOSE:

    <esc>:w<cr>

    <esc>:w <filename><cr>

    <esc>:q!<cr>     ǿ���˳��������棩

    <esc>:wq!<cr>    ǿ�б����˳�

## Delete

	x

	dw���ӵ�ǰλ�ã�ɾ������һword֮ǰ��    diw (ֻɾ������λ�õ�word)

	dd    dgg   dG   D

	d2j   d2k

	d0    d$

## Write, Insert, Append

	i  I  a  A

	c  C  s  S

	ciw   ca"   cib   cip

	c2j  ����ɾ��2�У���3�У������ҿ�ʼд��

	o    �����洴�����У���ʼд��

	O    �����洴�����У���ʼд��



## Back, forward

	U  �ָ��������״̬

	u  ȫ�ֻ���

	<Ctrl-r>  ȫ��ǰ��



## Paste

	p ճ����֮��   

	<number>p ���ճ��

	P ճ����֮ǰ


## Replace

	r  �滻�����ַ�

	R  �����滻����ַ�


## Search

	/<searchString><cr>

	n  ��һ��

	N  ��һ��

	:set ic    ���ò���ʱ���Դ�Сд(Ignore Case) 
	:set noic  �෴����

	:set   hlsearch
	:set nohlsearch

## Search word on this position

    *   n   N


## Brackets pair:

	%

## Search / Replace

	:%s/old/new/g    �����ļ�ȫ���滻
	:%s/old/new/gc   �����ļ�ȫ���滻����һѯ��
	:#,#s/old/new/g    ���������ֲ�ѡȡ�滻

	:s/old/new/g     �����滻����
	:s/old/new/g     �����滻��һ��


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

	:r $VIMRUNTIME/vimrc_example.vim �����ⲿ�ļ�


## Autocomplete 1

	��������һ���֣�����<Tab>�л��� ��<Ctrl+d>��ʾ�б�

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

:e! filename     ������ǰ�ļ����༭���ļ�
:e!              ���¼��ص�ǰ�ļ�

:ctrl+g     ��ʾ: �ļ���������
gf               �򿪹�괦�ļ�·�����ļ�

:w
:wq
:waq!

ZZ �� :x         ����>�˳�
:saveas newFileName   ���Ϊ

:Sex    ˮƽ�ָ�ڣ����ļ�ϵͳ
:Vex    ��ֱ�ָ�ڣ����ļ�ϵͳ

h j k l gj gk
<Enter>  ��Ӻţ� ����ƶ�����һ�зǿ��ַ�
-        ����

wW eE bB 0 ^ $ gg G
<num>gg   <num>j
()  {}   �䣬��  
fc f f f       Ѱ���ַ�c, ����Ѱ��
ǰ׺����ʹ������Ĳ���

0  g0  $  g$
50|    �ƶ���50��
50%    �ƶ����ĵ��ٷֱ�
50gg   �ƶ���50��
5j 5k  ����/���� �ƶ�5��

zz     ��ǰ�У���ʾ���в�
zt                   ����
zb     ��ǰ�У��ƶ����ײ�

ma   'a
mA   'A    ȫ�ֱ�ǣ�����vim��Ȼ��Ч
:delmarks! ɾ�����б��

iI  oO  cC  Ss

yy  yaw  dis  ci"   <operation><range>

:m,ny   ����m��n�У� ������ :m,nd

d/foo<cr>  ɾ����ֱ������foo

pP         ֮��֮ǰճ��

"cyy   "cp    �Ĵ������棬ճ��
:reg          ��ʾ�Ĵ�������
              ���磺 "%p ճ����ǰ�ļ��� 
"+yy          ϵͳ���а�

aw, as, ap, ab �� y d c v �������

�����滻��
<Visual Mode>  :s/old/new/g    ����ģʽ
:l1,l2s/old/new/g              �кŷ�Χ
:%s/old/new/g                  %��ʾȫ��
    0 ����
    $ β��
    . ����
    % ������

������ʽ��
    ^  ����
    $  ��β
    \d  ʮ������
    \s  �ո�
    \S  �ǿո�
    \a  Ӣ����ĸ
    \|  ��
    \\  ��ʾ\
    \.  ��ʾ.
    .   �����ַ�


