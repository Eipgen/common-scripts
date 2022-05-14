cat   all_out_select.sort  | while read line
do
IFS=' ' read -r -a array <<< $line
wget 'http://zinc15.docking.org/substances/'${array[0]}'.sdf'

cp -r ~/work/database/all_sdf/*/${array[0]}'.sdf'  .

done
