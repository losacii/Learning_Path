===
    i    I
    s    S
    c    C
    a    A
    o    O

===
    %    [    ]     ''     ma  mb  mc  'a  'b  'c
    0    $    ^
    w    W
    b    B
    e    E
    f    F   t
    H M L <num>gg   G   gg
    C-e   C-y
===
    /    ?    n    p
    *    #    (bounded, unbounded)
    g*   g#
    n    N

=== Yank, Paste

    y   p   P

    yiw    viwp

    2yy     yj     yk

    y4k     y4j

=== u = undo stuff
    Ctrl-R - redo stuff

    C-v  kkkk    I/A  stuff    Esc

    :r! seq 1 32

    C-a   C-x    ( increment,  decrement )

    3i<stuff><esc>

    ~      - Toggle the case of character
    g~iw   - Toggle case of entire word

"<reg>
    "ay    "ayy
    "ap

    :reg     ( list regs )

y - yank
q - macros
m - mark

Advanced motions:

    () - sentences
    {} - paragraphs, next empty line

        di(   di{

    ;  - Repeat last motion forward
    ,  - Repeat last motion backward

    ]] / [[     move between Sections
    %  - matching brace/paren/bracket/tag
    $  - End of line

3>>
5<<

>3k
>5j

Managing multiple files at once:

    :tabnew [file]       - Open a new tab with given file (or empty file)
    gt or :tabn[ext]     - Next tab
    gT or :tabp[revious] - Previous tab
    :tabm[ove] # - Move current tab to position # (zero-indexed), no argument = end
    :tabc        - Close current tab
    :tabo        - Close all other tabs except current:tabnew [file]       - Open a new tab with given file (or empty file)
    gt or :tabn[ext]     - Next tab
    gT or :tabp[revious] - Previous tab
    :tabm[ove] # - Move current tab to position # (zero-indexed), no argument = end
    :tabc        - Close current tab
    :tabo        - Close all other tabs except current

https://github.com/shawncplus/dotfiles/tree/master/.vim

[MY PERFECT VIM CONFIGURATION]
https://github.com/sebbekarlsson/i3/blob/master/.vimrc


How to add Line numbers:
    :r !seq 1 16
    C-v      yank these numbers or 'x' to cut them
    P        (paste after, Paster before)

1.line
2.line
3.line
4.line
5.line
6.line
7.line
8.line
9.line
10.line
11.line
12.line
13.line
14.line
15.line
16.line





































