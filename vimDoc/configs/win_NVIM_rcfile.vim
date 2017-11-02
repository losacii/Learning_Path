" C:\tools\neovim\Neovim\share\nvim\sysinit.vim

" Basic settings:
    syntax on
    set number
    set relativenumber
    set autoindent
    set smartindent
    set tabstop=4
    set softtabstop=4
    set shiftwidth=4
    set shiftround
    set expandtab
    set expandtab
    set hlsearch
    set ic " Ignore Case

    set mouse-=a
    set pastetoggle=<F12>

" Paste Current time
    map <F2> i<C-R>=strftime("%c")<CR><Esc>

" [ON / OFF] for line Numbers
    nnoremap ;l :set nonumber!<CR>:set norelativenumber!<CR>

"mapleader things
    "Set mapleader
        let mapleader=','

    "Save file
        nnoremap <leader>w <esc>:up<cr>"±£´æ
        inoremap <leader>w <esc>:up<cr>

    "Quit all
        nnoremap <leader>E <esc>:qa!<cr>"Ö±½ÓÍË³ö
        inoremap <leader>E <esc>:qa!<cr>
        nnoremap <leader>e <esc>:q!<cr>"Ö±½ÓÍË³ö
        inoremap <leader>e <esc>:q!<cr>

    "Run python code
        inoremap <leader>x <esc>:! python %<cr>
        nnoremap <leader>x <esc>:! python %<cr>

    "Easily jump to begin of end of line
        nnoremap <leader><leader> ^
        nnoremap <leader>hl :set nohlsearch!

        nnoremap <leader>. $

        inoremap <M-j> <Down>
        inoremap <M-k> <Up>
        inoremap <M-l> <Right>
        inoremap <M-h> <Left>

        inoremap <M-i> <esc>bi
        inoremap <M-o> <esc>ea
        inoremap <M-u> <Home>
        inoremap <M-p> <End>

        inoremap <M-,> <esc>xi
        inoremap <M-.> <Delete>
        nnoremap <M-,> hx

    " Add Empty Lines
		inoremap <c-j> <esc>o<esc>kA
		inoremap <c-k> <esc>O<esc>jA
		nnoremap <c-j> o<esc>k
		nnoremap <c-k> O<esc>j

	" Tabs
		nnoremap <leader>to <esc>:tabnew<space>
		nnoremap <leader>t, <esc>:tabNext<cr>
		nnoremap <leader>t. <esc>:tabnext<cr>
		nnoremap <leader>tx <esc>:tabclose<cr>
		nnoremap <leader>tt <esc>:tabonly<cr>
		nnoremap <leader>ta <esc>:tabfirst<cr>
		nnoremap <leader>tf <esc>:tablast<cr>
		nnoremap ; :

    "Github Update
        nnoremap <leader>ga <esc>:! git add .
        nnoremap <leader>gc <esc>:! git commit -m ''<left>
        nnoremap <leader>gp <esc>:! git push
        nnoremap <leader>gs <esc>:! git config --global user.name 'losacii' && git config --global user.email 'losacii5@gmail.com'

    "UPPER / lower
        inoremap ;u <esc>viwUea
        nnoremap ;u <esc>viwU
