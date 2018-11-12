"=============================================================================
" main.vim --- Main file of SpaceVim
" Copyright (c) 2016-2017 Shidong Wang & Contributors
" Author: Shidong Wang < wsdjeg at 163.com >
" URL: https://spacevim.org
" License: GPLv3
"=============================================================================

" Enable nocompatible
if has('vim_starting')
  " set default encoding to utf-8
  " Let Vim use utf-8 internally, because many scripts require this
  set encoding=utf-8
  if &compatible
    set nocompatible
  endif
  " python host
  if !empty($PYTHON_HOST_PROG)
    let g:python_host_prog  = $PYTHON_HOST_PROG
  endif
  if !empty($PYTHON3_HOST_PROG)
    let g:python3_host_prog = $PYTHON3_HOST_PROG
  endif
endif
" Detect root directory of SpaceVim
let g:_spacevim_root_dir = fnamemodify(expand('<sfile>'),
      \ ':p:h:gs?\\?'.((has('win16') || has('win32')
      \ || has('win64'))?'\':'/') . '?')
lockvar g:_spacevim_root_dir
try
  call SpaceVim#begin()
catch
  " Update the rtp only when SpaceVim is not contained in runtimepath.
  let &runtimepath .= ',' . fnamemodify(g:_spacevim_root_dir, ':p:h:h')
  call SpaceVim#begin()
endtry

call SpaceVim#custom#load()

call SpaceVim#end()
" vim:set et sw=2 cc=80:

" * * * * * * * * * * * * * * User Settings * * * * * * * * * * * * * * * * * *
  set path+=**
  vnoremap <F2> "+y

" Mapleader
  let mapleader=','
  nnoremap <leader>rc :tabnew ~/.SpaceVim/config/main.vim<cr>
  nnoremap ;ee :qa!<cr>
  nnoremap ;fe :q!<cr>
  nnoremap ;fw :up<cr>

" 行号开关
  nnoremap ;ll :set nu! rnu!

" 大小写(正常模式和插入模式可用)
  nnoremap ;u viWU
  inoremap ;u viWUea

" 插入模式下移动光标
  nnoremap ;a 0
  nnoremap ;f $
  inoremap <m-j> <down>
  inoremap <m-k> <up>
  inoremap <m-h> <left>
  inoremap <m-l> <right>

  inoremap <m-i> <esc>Bi
  inoremap <m-o> <esc>Ea
  inoremap <m-u> <esc>0i
  inoremap <m-p> <esc>$a

" 插入模式下删除
  inoremap <M-m> <esc>xi
  inoremap <M-,> <delete>

" Tabs (标签操作)
  nnoremap <leader>to :tabnew<space>
  nnoremap <leader>t, :tabNext<cr>
  nnoremap <leader>t. :tabnext<cr>
  nnoremap <leader>tt :tabonly<cr>
  nnoremap <leader>ta :tabfirst<cr>
  nnoremap <leader>tf :tablast<cr>

" Github
  nnoremap ;ga <esc>:! git add .<cr>
  nnoremap ;gc <esc>:! git commit -m ''<left>
  nnoremap ;gp <esc>:! git push<cr>
  nnoremap ;gs <esc>:! git config --global user.name "losacii" && git config --global user.email 'losacii5@gmail.com'
  nnoremap ;sv <esc>:! cp % ~/Documents/ubuntuMemo/vimDoc/configs/init_for_Spacevim.vim

" au BufWinLeave * mkview
" au BufWinEnter * silent loadview
