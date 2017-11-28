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

## Windows
    <C-w>L  - Swap Position
    <C-w>l  - Switch Focus
    :vs <finelane>
    :vs

## External commands
    :!<command>
    :-1read <filepath>
    :r !<command>

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
    v"+y   v"ay  "ap
    "+<motion>   "+p
    "/
    ":
    "*
    "%
    <insertMode>^r<math-expression>

## History trace:
    :earlier 2m
    u  R
    esc == ^[

## Marcro
    (record a macro)
    q<register>
    (do the things)
    q

    (play macro)
    @<register>

    You can C-v select, then play macro

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
    - vundle - Plugin vimanager

    - nerdtree - file drawer
        ma

    - ctrlP - fuzzy file finder

    - fugitive - git tool
        :Gwrite
        :Gcommit -m 'update-log'
        :Gpush

    - syntastic - syntax checker/linter

## What is tmux
    Terminal multiplexer
    View and control multple consoles
    Preconfigure environments

THE CRAZY FOX JUMPED OVER THE.LAZY.DOG.
