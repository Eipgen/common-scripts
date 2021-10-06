
parallel [options] [command [arguments]] < list_of_arguments 
parallel [options] [command [arguments]] (::: arguments|:::: argfile(s))... 
cat ... | parallel --pipe [options] [command [arguments]] 

常用选项：
::: 后面接参数
:::: 后面接文件
-j、--jobs   并行任务数
-N  每次输入的参数数量
--xargs会在一行中输入尽可能多的参数
-xapply 从每一个源获取一个参数（或文件一行）
--header  把每一行输入中的第一个值做为参数名
-m   表示每个job不重复输出“背景”（context）
-X   与-m相反，会重复输出“背景文本”
-q  保护后面的命令
--trim  lr 去除参数两头的空格，只能去除空格，换行符和tab都不能去除
--keep-order/-k   强制使输出与参数保持顺序 --keep-order/-k
--tmpdir/ --results   都是保存文件，但是后者可以有结构的保存
--delay  延迟每个任务启动时间
--halt  终止任务
--pipe    该参数使得我们可以将输入（stdin）分为多块（block）
--block  参数可以指定每块的大小

parallel echo :::A B C ::: D E F | tee a.txt

A D
A E
A F
B D
B E
B F
C D
C E
C F

parallel --xapply echo ::: A B C ::: D E F
A D
B E
C F
--arg-sep和--arg-file-sep指定分隔符替代 ::: 或 ::::
parallel -k --arg-sep ,,, echo ,,, a b ,,, c d
a c
a d
b c
b d
使用 \n 做为参数定界数.可以使用 -d 改变

parallel -E stop echo ::: A B stop C D
提前结束
构建命令，命令可以是一个脚本文件
parallel ::: ls 'echo foo' pwd

parallel -C, -k -j100% "echo '$1' | bc -l"

parallel --jobs 4 -m echo ::: {1..10}
1 2 3
4 5 6
7 8 9
10
去除空格
parallel --trim lr echo pre-{}-post ::: ' A '
# 使用64个任务执行128个休眠命令
time parallel -N0 -j64 sleep 1 ::: {1..128}

并行转换图片
find . -name "*jpeg" | parallel -I% --max-args 1 convert % %.png



