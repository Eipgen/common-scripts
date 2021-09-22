alias lt='ls --human-readable --size -1 -S --classify'
alias mnt='mount | grep -E ^/dev | column -t'
alias gh='history|grep'
alias left='ls -t -1'
alias count='find . -type f | wc -l'
alias cpv='rsync -ah --info=progress2'
alias startgit='cd `git rev-parse --show-toplevel` && git checkout master && git pull'
alias tcn='mv --force -t ~/.local/share/Trash '
alias cg='cd `git rev-parse --show-toplevel`'

#alias vfzf="vim $(fzf)"
#alias dfzf="cd $(find * -type d | fzf)"
