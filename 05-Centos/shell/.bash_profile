alias bashprofile='vim ~/.bash_profile'
alias bashcolor='vim ~/.minttyrc'
alias gitconfig='vim ~/.gitconfig'
alias sourcebash='source ~/.bash_profile'

alias .='cd ~'
alias ..='cd ..'
alias ...='cd ../..'
alias e='exit'
alias cls='clear'

alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
alias gitpush='git add . && git commit -m "auto deploy" && git push'

alias sysoff='sudo shutdown -s -t 0'
alias sysre='sudo shutdown -r -t 0'

alias host='code /c/Windows/System32/drivers/etc/hosts'

alias ali="ssh root@47.96.174.116"
alias to-ali="scp -rp ~/share root@47.96.174.116:~/"
alias from-ali="scp -rp root@47.96.174.116:~/share ~/"

alias pi='ssh pi@10.69.106.136'
alias to-pi="scp -rp ~/share pi@10.69.106.136:~/ "
alias from-pi="scp -rp pi@10.69.106.136:~/share  ~/"

alias knowhosts="vim /c/Users/chuandr/.ssh/known_hosts"

#export PS1="\[\e[31m\]\u\[\e[m\]\[\e[36m\]@\[\e[m\]\[\e[32m\]\h\[\e[m\] - \[\e[35m\]\w\[\e[m\] "

alias ls="ls -Glha --color=auto"
