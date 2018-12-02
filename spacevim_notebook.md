### filepath: /home/vi/Documents/ubuntuMemo/spacevim_notebook.md
### Web reference: https://spacevim.org/grep-on-the-fly-in-spacevim/

### Open multipule files
    vim -o3 f1 f2    : open f1 f2 and emptyfile
    vim -O
    vim -p           : with tabs

### 布局保存-恢复
  :mksession <fp.vim>
  vim -S <fp.vim>

### gf  : Go to this file
    ^o  : Go back

### Settings file
  ~/.SpaceVim/config/main.vim

  get it from github:
  wget -O ~/.SpaceVim/config/main.vim https://www.github.com/.......

  sychronize to git folder:

  link it with ;rc shotcut
  nnoremap <leader>rc :tabnew ~/.SpaceVim/config/main.vim<cr>


### <spc> fvd  >>  layer denite
  Open layer file with <space>fvd
  Add 'denite'
  Restart vim

### denite snippets

  Ctrl+p  >>  find "____.snip" >> Edit your own

  ^j  ^k
  Ctrl+T  : open it with a new tab

  Time Stamps:   dd  dt  df  lmod 
  File Path:     path  fname  bname

### surround: ys<motion>
  yss"
  ys3e(
  cs"}    : change surround example

### multipule select
  <space>se
  h  l  a  i
  esc
  S  <or>  Di

### FlyGrep:
  <space>sp               : or <space>s/
  <space>sS              : Search in current file
  SPC s g G              : Open Flygrep

  Ctrl+[jk]
  <tab> <shift>+<tab>    : Down, up

  <C-a> <C-e>  :beginning, end
  <C-k> <C-u>  :remove line
  <C-w>     : remove word before

### File Tree
  SPC f t
  yy
  SPC f /
  sv sg

### Splited windows
  :38vs newfile      :55sp newfile
  <space> [1-9]
  <space> w <tab>
  <space> w d
  <space> w [hjkl]
  <space> w [HJKL]
  <space> w M     : equals to  :only  (close other windows)
  <space> w [r/R] : Rotate window

### sort: 多行文字排序典型举例：

  命令  :3,+5!sort -r
  作用  把[第3行]及[后5行]反向排序(共6行)：

  解析：分为3小段：
    :
    3,+5
    !sort -r

### Previous positons:  
  g;
  ''

### Registers
  ^r<reg>    : usage
  ^r%        : put file name here
  :h Registers    :get help

  "/  current search pattern
  "=  expression register (使用数学式)
  "_  black hole register
  ":  last : command
  %   filename

  0       : yank reg
  "[1~9]  : history regs
  "[a-z]  : named regs


### 大小写
  gUU   gUiw

### Buffers
  :ls     : list them
  :b<n>   : to open it
  :b<tab>   (^o  : to go back)

### Motions:
  h j k l 0 ^ $
  gg  G  <n>gg  :<n><cr>
  ^f  ^f  ^d  ^u
  <n>|  横向

  f<char>
  /<search_Pattern>

  H  zt
  M  zz
  L  zb

  gj  gk  g0  g$  (motion in a wrapped line)

### Text Object
  w   : word
  s   : sentence     ()
  p   : paragraph    {}
  b   : block

  example:  diw daw vip  ysip  yss"  dj   d}
            gUip  gUis

### Scroll screen
  ^e
  ^y
  zt  zz  zb

### Macros
  qx
  <do_stuff>
  q
  @x

### Windows & Tabs
  <space>[1-9]
  :only   :tabonly
  :tabnew  :tabnext  :tabNext  :tabfirst ...

### Auto Complete
  ^n   : basic    ^p   : go up
  <C-x><C-f>   : file path
  <C-x><C-d>   : Definition
  <C-x><C-i>   : Keywords [syntax highlighted]
  <C-x><C-]>   : Tags
  <C-x><C-l>   : lines (match similar line)
  ^n  ^y  ^e

### :digraph  ⇒ Special characters :
  (vimdoc digraph)
  ^k:e    ë
  ^k-e    ē
  ^k=e    €
    2s
    ss
    >=  <=  =>  !=
    Sb    ∙
    W*    Ω
    OK    ✓
    Ic    ◙

### Template, read in a file
    5r <filepath>    : read file below line 5
  
### Spacevim: Jump (EasyMotion)

    <leader><leader>[sfF]  : jump to char
    <leader><leader>w      : jump to word

    w [Fsf]  eE  bB j k nN ~ F向左 s两边 f向右

    SPC j j   : to a char
    SPC j u   : to an url

    :h easymotion >> custom keys
        map ;i <Plug>(easymotion-s)

### Line number
    SPC t n

### 断行
    gq<motion>    ⇒  gqq  gqip  gqG

