#open tmux auto
if [ -z "$TMUX" ]; then
tmux attach -t default || tmux new -s default
fi

#initialize bash_alias
if [ -e $HOME/.bash_aliases ];then
source $HOME/.bash_aliases
fi

#initialze bash_funtions
if [ -e $HOME/.bash_functions ]; then
source $HOME/.bash_functions
fi
