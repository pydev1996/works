clc
clear all
close all
%第一类数据
mu1=[0 0];  %均值
S1=[0.3 0 ;0 0.35 ];  %协方差
data1=mvnrnd(mu1,S1,100);   %产生高斯分布数据
t1 = zeros(100,3);
t1(:,1) = 1;

%%第二类数据
mu2=[2.25 1.25 ];
S2=[0.3 0;0 0.35];
data2=mvnrnd(mu2,S2,100);
t2 = zeros(100,3);
t2(:,2) = 1;

%第三个类数据
mu3=[-2.25 1.5 ];
S3=[0.3 0;0 0.35];
data3=mvnrnd(mu3,S3,100);
t3 = zeros(100,3);
t3(:,3) = 1;

X =[data1;data2;data3];
figure(1);
scatter(X(:,1),X(:,2));
axis([-5,5,-4,6]);
hold on;

X = [ones(300,1),X];
T = [t1;t2;t3];
W = (X'*X)\(X'*T);%%least-square solution

deltW1 = W(:,1) - W(:,2);
deltW2 = W(:,1) - W(:,3);
deltW3 = W(:,2) - W(:,3);
x = -5:0.1:5;
plot(x,(deltW1(1) + deltW1(2)*x)/(-deltW1(3)),'r');
hold on 
plot(x,(deltW2(1) + deltW2(2)*x)/(-deltW2(3)),'g');
hold on
plot(x,(deltW3(1) + deltW3(2)*x)/(-deltW3(3)),'y');

Y = X*W;
[~,label] = max(Y,[],2);
figure(2)
scatter(X(label == 1,2),X(label == 1,3),'g');
axis([-5,5,-4,6]);
hold on
scatter(X(label == 2,2),X(label ==2 ,3),'b');
hold on
scatter(X(label == 3,2),X(label == 3,3),'r');