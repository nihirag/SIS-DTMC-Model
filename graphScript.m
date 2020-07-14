clear
set(0,'DefaultAxesFontSize', 18)
beta=1;
g=0.25;
b=0.25;
R0=beta/(b+g);
N=100;
init=2;
dt=0.01;
time=25;
sim=3;
for j=1:sim
i(1)=init;
for t=1:time/dt
r=rand; % uniform random number
birth=beta*i(t)*(N-i(t))/N*dt; 
death=(b+g)*i(t)*dt;
if r<=birth
i(t+1)=i(t)+1;
elseif r>birth && r<=birth+death
i(t+1)=i(t)-1;
else
i(t+1)=i(t);
end
end
if j==1
    stairs([0:dt:time],i,'r-','LineWidth',2);
hold on
elseif j==2 
    stairs([0:dt:time],i,'g-','LineWidth',2);
else
    stairs([0:dt:time],i,'b-','LineWidth',2);
end
end
ylabel("Infected")
xlabel("Time Steps")
