opencv_createsamples -img Cats_Test167.png -bg bg.txt -info info/info.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1300

opencv_createsamples -info info/info.lst -num 1300 -w 20 -h 20 -vec positives.vec

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 650 -numNeg 900 -numStages 10 -w 20 -h 20

# opencv_traincascade -data data -vec positives.vec -bg bg.txt -precalcValBufSize 256 -precalcIdxBufSize 256 -numPos 1200 -numNeg 1000 -nstages 20 -minhitrate 0.999 -maxfalsealarm 0.5 -w 50 -h 50 -nonsym -baseFormatSave

