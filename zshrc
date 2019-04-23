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
alias ls='ls -F'

# add dotnet tools to path
export PATH=$PATH:$HOME/.dotnet/tools
# also disable telemetry for dotnet
export DOTNET_CLI_TELEMETRY_OPTOUT=1
