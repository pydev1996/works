data =  xlsread('C:\Users\m.siddique\Downloads\Coal Flot Data.xlsx') ;
x = data(:,1:8);
y = data(:,7);
m = length(y);


y2 = (y-min(y))/(max(y)-min(y));

for i = 1:8
    x2(:,i) = (x(:,i)-min(x(:,i)))/(max(x(:,i))-min(x(:,i)));
end

xt=x2';
yt=y';
hiddenLayerSize = [9,5];
net = fitnet(hiddenLayerSize);
net.layers{1}. transferFcn = 'logsig';
net.layers{2}. transferFcn = 'logsig';
net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 30/100;
net.divideParam.testRatio = 0/100;
[net,tr] = train(net, xt, yt);

yTrain = (net(xt(:,tr.trainInd)));
yTrainTrue = (yt(tr.trainInd));
sqrt(mean((yTrain-yTrainTrue).^2))

r2train = 1 - (((yTrain-yTrainTrue).^2)/(yTrain-mean(yTrain)))

rmsetrain = sqrt(mean((yTrain-yTrainTrue).^2))

yVal = (net(xt(:,tr.valInd)));
yValTrue = (yt(tr.valInd));
sqrt(mean((yVal-yValTrue).^2))

r2val = 1 - (((yVal-yValTrue).^2)/(yVal-mean(yVal)))
%mseval = (mean((yVal-yValTrue).^2))
rmseval = sqrt(mean((yVal-yValTrue).^2))





