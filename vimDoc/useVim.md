## Motions

    h   j   k   l
    w   e   b   W   E   b
    0   ^   $

        alias cdg=cd /d d:\doc\gitDoc\ubuntuMemo
        alias cdh=cd /d c:\Users\Administrator
        unalias=alias /d $1
        vi=vim $*

## Motions

    ^f  ^b  - move one  page down/up

    ^d  ^u  - move half page down/up

    H  M  L  - high / middle / low

    ^e  ^y

    (  )  {  }

    [[  ]]

    gg   G   <num>gg

## put text

    i   I   a   A   o   O
    c   C   s   S
    c2j  ci(  ci"

## Delete / Change
    d2j  d2k  d4e  d$  dd  dip  dib  dis  di"  di}  di)

## Indent
    >4j  >4k
    >ip
    <<   >>
    5>>  >3k

    Visully select multiple lines, the '>' or '<'

## Text Objects:
    w - words    s - sentences
    p - paragraphs    t - tags

    a - all   i - in
        Example:  ca"   ca(
    t - till
    f/F - find forward/backward

## Commands:
    d - delete    D - till end
    c - change    C - till end
    y - yank      Y - till end
    v - visually select

    yi)  vap  dt,  di'  ca[  va"

## Reapeat with '.'
    commands between ESCs
    You can C-v to select many words, apply operation with '.'

## Buffers
    :edit <filename>
    :ls  - show buffers
    :b <number>

## External commands
    :!<command>
    :-1read <filepath>
    :r !<command>

## Visully Select, then press '=' to align
    a
      b
    c
        d
     e

## Replace text
    :s/foo/bar/g     - replace on current line
    :%s/foo/bar/g    - replace all foos with bar in file
    (g means global)

## Additional commands:
    x  /  X   (after/before)
    p  /  P   (after/before)(below/above)
    dd /  yy  (whole line)
    D  /  C   (till line end)
    o  /  O   (below/above)

## Registers:
    You have 35 copy buffers

    "+ is the X server register,  "+y<motion>  or V"+y  to copy,  "+p  to paste

    "[1-9]  - history registers

    "0      - the yank register
    "[a-z]  - are named registers 
    "[A-Z]  - same as above but append

    "/  - current search
    "-  - small delete
    "=  - Expression register,  EG:  C-r=99*99
    "_  - black hole register,  EG:  "_y<motion>

    ":  - last :command
    ".  - last insert text
    "%  - filename of the current file
    "#  - filename of the alternate file

    v"+y   v"ay  "ap
    "+<motion>   "+p
    "*
    <insertMode>^r=<math-expression>
    ^r=sqrt(2)  : 1.414214

## History trace:
    v"+y   v"ay  "ap
    "+<motion>   "+p
    :earlier 2m
    u  R
    esc == ^[

## Marcro: record and play
    (record a macro)
    q<register>
    (do the things)
    q

    (play macro)
    @<register>

    You can C-v select, then play macro
    Marcros are saved as text, so you can edit them manually!

## Splits and Tabs, Buffers
    :ls check out the buffer list
    :bn
    :bp
    :b <number>   or    :b <filename>

    gt  - go to next tab
    gT  - go to Next tab
    :tabnew <filename>  - create a new tab

## Auto Completion:
    Syntax completion in insert mode:
        <C-n>  - next default completion
        <C-p>  - previous ...
    Omni-completion 
        <C-x><C-o>
    Programming completion:

        <C-x><C-f>  File paths  TEST: "/etc/apt/sources.list"
        <C-x><C-d>  Definition
        <C-x><C-]>  Tags
        <C-x><C-i>  Keywords
        <C-x><C-l>  Lines

    Others:
        <C-x><C-t>  Thesaurus
        <C-x><C-k>  Dictionary
        <C-x><C-s>  Spelling
        <C-x><C-v>  vim commands
        

## input weird characters
    In insert mode,  <C-k>a:  yields
    Check  :h digraphs for a list of them all!
    <C-v>  next char

## Snippets:  Snipmate and Ultisnips
    Better Snippets support
    Provide advanced completion features

## Windows

    <c-w>v  - vertical split
    <c-w>s  - horizontal split
    <c-w>n  - new buffer in a horizontal window

    <C-w>L  - Swap Position
    <C-w>l  - Switch Focus

    :vs <finelane>
    :vs

    <c-w>c  - close current window, useful for escaping from :h <anything>

    Tons of window commands! Check :h windows

## vim plus plus increment
    >

## Mark Position
    ma mb mc  'a 'b 'c

## Paste over
    yiw  viwp

## Upper/Lower Case:

    Visully select, 
        'U' to Upper
        'u' to Lower
        '~' to Swapcase

    g~~  g~<motion>
    gUU  gU<motion>
    guu  gu<motion>

## Plugins
    - Plugin vimanager: Vundle/Pathogen

    - nerdtree - file drawer

    - ctrlP - fuzzy file finder

    - fugitive - git tool
        :Gwrite
        :Gcommit -m 'update-log'
        :Gpush

    - Surround
    - syntastic - syntax checker/linter

## Ctags
    <C-]>  - jump to Definition
    <C-T>  - jump back
    :tags  - show tag stack

    Cscope:
        More powerful but confined to C/C++

## What is tmux
    Terminal multiplexer
    View and control multple consoles
    Preconfigure environments

## Change list --> g; g,
    Press g;
    Press g,

## gj  gk  - moto to actual line
    gj
    gk
    <number>|    - to a certain comumn
    ddO instead of S
    dbx instead of daw
    gUit

## Foldings
    "Add these 2 lines to RC file, save and load folds automatically"
    au BufWinLeave * mkview
    au BufWinEnter * silent loadview

## Further Resouces
    Practical Vim by Drew Neil
    Vimcasts by Drew Neil
    Vimtips wiki
    Vundle
    Vim Awesome

THE CRAZY FOX JUMPED OVER THE.LAZY.DOG.
