set number              "显示行号
set autoindent          "自动对齐
set smartindent         "智能对齐
set showmatch           "括号匹配模式
set ruler               "显示状态行
set tabstop=4           "tab键为4个空格
set shiftwidth=4        "换行时行间交错使用4个空格
set cindent             "C语言格式对齐
syntax enable
syntax on               "自动语法高亮
" color scheme
set t_Co=256
colo molokai
" hilight function name
autocmd BufNewFile,BufRead * :syntax match cfunctions "\<[a-zA-Z_][a-zA-Z_0-9]*\>[^()]*)("me=e-2 
autocmd BufNewFile,BufRead * :syntax match cfunctions "\<[a-zA-Z_][a-zA-Z_0-9]*\>\s*("me=e-1
hi cfunctions ctermfg=81

hi Type ctermfg=118 cterm=none 
hi Structure ctermfg=118 cterm=none
hi Macro ctermfg=161 cterm=bold
hi PreCondit ctermfg=161 cterm=bold
set cursorline

filetype plugin on
let g:pydiction_location='~/.vim/after/ftplugin/pydiction/complete-dict'
