### Dont use Arrow keys:
    h   j   k   l
    w   e   b   W   E   b
    ^e  ^y  ^f  ^b
    H   M   L   (   )   {   }
    gg  G   <Number>gg   [[  ]]

    (key caster: show what you are typing, on screen)

### put text
    i   I   a   A   o   O
    c   C   s   S

### Delete / Change
    d2j  d2k  d4e  d$  dd  dip  dib  dis  di"  di}  di)

### Indent
    >4j  >4k
    >ip

### test objects:
    w - words
    s - sentences
    p - paragraphs
    t - tags

    a - all
    i - in
    t - till
    f - find (forward)
    F - find (backward)

### Commands:
    d - delete    D - till end
    c - change    C - till end
    y - yank      Y - till end
    v - visually select

    yi)  vap  dt,  di'  ca[  va"

### Reapeat with '.'
    commands between ESCs

    You can C-v to select, then repeat a operation with '.'

### Additional commands:
    dd /  yy  (whole line)
    D  /  C   (till line end)
    ^  /  $
    I  /  A
    p  /  P   (after/before)(below/above)
    o  /  O   (below/above)
    x  /  X   (after/before)

### Registers:
    v"+y
    "/
    ":
    "*
    "%
    <insertMode>^r

### History trace:
    :earlier 2m
    u  R
    esc == ^[

### Marcro
    (record a macro)
    q<register>
    (do the things)
    q

    (play macro)
    @<register>

    You can C-v select, then play macro

### Mark Position
    ma mb mc  'a 'b 'c

### Paste over
    yiw  viwp

### Upper/Lower Case:

    Visully select, then 'U' to Upper, 'u' to Lower

    viWU - Upper a word
    viwu - Lower a word

### Indent
    5>>
    >3k

    Visully select multiple lines, the '>' or '<'


### Plugins
    - vundle - Plugin vimanager

    - nerdtree - file drawer
        ma

    - ctrlP - fuzzy file finder

    - fugitive - git tool
        :Gwrite
        :Gcommit -m 'update-log'
        :Gpush

    - syntastic - syntax checker/linter

### What is tmux
    Terminal multiplexer
    View and control multple consoles
    Preconfigure environments

The Crazy fox jumped over the.lazy.dog.
