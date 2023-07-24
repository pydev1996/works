clc
clear all
close all
[num,txt,raw] = xlsread('C:\Users\m.siddique\Downloads\Coal Flot Data.xlsx') ;
raw
txt
[num,txt,raw] = xlsread('C:\Users\m.siddique\Downloads\HHV_coal.xlsx') ;
raw
txt
mu1=[0 0];  
S1=[0.3 0 ;0 0.35 ];  
data1=mvnrnd(mu1,S1,100);  
t1 = zeros(100,3);
t1(:,1) = 1;

mu2=[2.25 1.25 ];
S2=[0.3 0;0 0.35];
data2=mvnrnd(mu2,S2,100);
t2 = zeros(100,3);
t2(:,2) = 1;

mu3=[-2.25 1.5 ];
S3=[0.3 0;0 0.35];
data3=mvnrnd(mu3,S3,100);
t3 = zeros(100,3);
t3(:,3) = 1;
T = [t1;t2;t3];

X =[data1;data2;data3];
 figure(1);
scatter(X(:,1),X(:,2));
axis([-5,5,-4,6]);
hold on;

m1 = sum(data1)/length(data1);
m2 = sum(data2)/length(data2);
m3 = sum(data3)/length(data3);
m = sum(X)/length(X);

mtmp = [repmat(m1,length(data1),1);repmat(m2,length(data2),1);repmat(m3,length(data3),1)];
xtmp = X-mtmp;
Sw = xtmp'*xtmp;

Sb = length(data1)*(m1-m)'*(m1-m) +... 
        length(data2)*(m2-m)'*(m2-m) + ...
            length(data3)*(m3-m)'*(m3-m);
        
J = Sw\Sb;
[V,~] = eigs(J,1);
x = -5:0.1:5;
plot(x,V(1)*x/-V(2),'r');

y = X*V;
 ptmp = X - repmat(m,length(X),1);
 p = ptmp'*ptmp;
 [Vp,~] = eigs(p,1);
 plot(x,Vp(1)*x/-Vp(2),'g');
 figure(2);
 hist(y,40);

