" gonna create my own this time

" protects from unexpected things the distro might have done
set nocompatible

" intelligently indent based on filetype
filetype indent plugin on

" syntax highlighting
syntax on

" turn on line numbers
set number

" use spaces instead of tabs
" indentation settings to use 4 spaces
set shiftwidth=4
set expandtab
set softtabstop=4

" better command-line completion
set wildmenu

" show partial commands in the last line of the screen
set showcmd

" highlight searches
set hlsearch

" case insensitive search, except when capital letters are included
set ignorecase
set smartcase

" backspace over autoindent, line breaks, and start of insert
set backspace=indent,eol,start

" enable use of mouse
set mouse=a

" set colorscheme to be more visible
colorscheme ron

" highlight 80th column for easier line wrap
set cc=80
highlight ColorColumn ctermbg=DarkGray
