n=1;
max=25;
while [ "$n" -le "$max" ]; do
  foo=$(printf "day_%02d" $n)
  echo $foo
  mkdir "$foo"
  echo "#!/usr/bin/env python" > "$foo/$foo.py"
  n=`expr "$n" + 1`;
done
