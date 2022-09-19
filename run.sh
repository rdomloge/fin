FILE=Numberguessergame.py

docker run --mount type=bind,source=${PWD}/$FILE,target=/$FILE -ti python python $FILE