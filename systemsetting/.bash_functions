function cl(){
  DIR="$*";
  #if not DIR given,go home
    if [ $# -lt 1 ]; then
        DIR=$HOME;
  fi;
  builtin cd "${DIR}" &&\
  #use you command
    ls -F --color=auto
}
