# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/kieselnb/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

zstyle ':completion:*' menu select

autoload -Uz promptinit
promptinit
prompt redhat

alias yeet='yay -Rsn'
alias ls='ls --color=auto'
alias grep='grep --color=auto'

eval $(thefuck --alias)

function _whatis() {
    case $1 in
        "life")
            echo "worth living"
            ;;
        "love")
            echo "baby don't hurt me"
            ;;
        *)
            whatis $@
    esac
}
alias whatis='_whatis'

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
