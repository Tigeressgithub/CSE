%%Generate

%% object declaration

case(8, a, 90, 5000, 3033, 65).
case(9, a, 240, 5000, 3033, 160).
case(10, a, 40, 5000, 3033, 25).
referee(19, i, 360, 2000, 0).
referee(20, i, 600, 6000, 0).
referee(21, e, 480, 2000, 1200).
referee(22, e, 480, 6000, 4000).
prefType(19, a, 3).
prefType(20, a, 1).
prefType(21, a, 2).
prefType(22, a, 3).
prefRegion(19, 3033,3).
prefRegion(20, 3033,1).
prefRegion(21, 3033,3).
prefRegion(22, 3033,3).
externalMaxDamage(10000).



%:- not assign(8,19). :- not assign(9,19). :- not assign(10,21).
%Generate

%referee(Rid, Type, Max_workload, Prev_workload, Prev_payment).
%case(Cid, Type, Effort, Damage, Postc, Payment).

%output

%Define domain and codomain of the assign
{assign(Cid,Rid):referee(Rid,_,_,_,_)}=1:-case(Cid,_,_,_,_,_).


%:- assign(Cid,Rid1), assign(Cid,Rid2), Rid1!=Rid2 .

newEffort(Cid,Rid,Effort):- assign(Cid,Rid), case(Cid,_,Effort,_,_,_).
%totalEff(Rid,Effort):- newEffort(Cid,Rid,Effort).
%totalEff(Rid,Effort):- newEffort(Cid1,Rid,Effort1), newEffort(Cid2,Rid,Effort2), Cid1 != Cid2, Effort = Effort1+Effort2.
%#show totalEff/2.
totalEff(Rid,Effort1):- Effort1 = #sum{Effort,Cid,Rid: newEffort(Cid,Rid,Effort)}, referee(Rid, Type, Max_workload, Prev_workload, Prev_payment).
%#show totalEff/2.

%payment
%{payment(Cid,Rid,Type,Payment): case(Cid,_,_,_,_,Payment)}=1 :- assign(Cid,Rid), referee(Rid,Type,_,_,_).
{payment(Cid,Rid,e,Payment): case(Cid,_,_,_,_,Payment)}=1 :- assign(Cid,Rid), referee(Rid,e,_,_,_).
%:- payment(Cid,Rid,Type,Payment),payment(Cid1,Rid,Type,Payment),Cid!=Cid1. 
%:- {payment(Cid,Rid,Type,Payment): assign(Cid,Rid)} =0, case(Cid,_,_,_,_,Payment).
%:- payment(_,_,X,_), X=e.



%%%% Hard Constraint %%%%%
%:~ referee(Rid,_,Max_workload,Prev_workload,_), totalEff(Rid,Effort1), Temp = Prev_workload + Effort1, Max_workload < Temp.[1@1]
%:- referee(Rid,_,Max_workload,Prev_workload,_), totalEff(Rid,Effort1), Temp = Prev_workload + Effort1, Max_workload < Temp.
:- referee(Rid,_,Max_workload,Prev_workload,_), totalEff(Rid,Effort1), Temp = Effort1, Max_workload < Temp.


%#show referee/5.
%#show totalEff/2.


%maxWL(Rid,Max_workload,Temp) :- referee(Rid,_,Max_workload,Prev_workload,_), totalEff(Rid,Effort1), Temp = Prev_workload + Effort1.
%#show maxWL/3.

%prefRegion(Rid, Postc, Pref).
%:~ prefRegion(Rid, Postc, Pref), assign(Cid,Rid), case(Cid, Type, Effort, Damage, Postc, Payment), Pref = 0. [1@1]
:- prefRegion(Rid, Postc, Pref), assign(Cid,Rid), case(Cid, Type, Effort, Damage, Postc, Payment), Pref = 0.


%prefType(Rid, Caset, Pref).
%:~ prefType(Rid, Caset, Pref), assign(Cid,Rid), case(Cid, Caset, Effort, Damage, Postc, Payment), Pref = 0. [1@1]
:- prefType(Rid, Caset, Pref), assign(Cid,Rid), case(Cid, Caset, Effort, Damage, Postc, Payment), Pref = 0.


%:~ assign(Cid,Rid), case(Cid, Type, Effort, Damage, Postc, Payment),referee(Rid, e, Max_workload, Prev_workload, Prev_payment), externalMaxDamage(T), T<Damage. [1@1]
:- assign(Cid,Rid), case(Cid, Type, Effort, Damage, Postc, Payment),referee(Rid, e, Max_workload, Prev_workload, Prev_payment), externalMaxDamage(T), T<Damage.

%totalEff(Rid,Effort1):- Effort1 = #sum{Effort,Cid,Rid: newEffort(Cid,Rid,Effort)}, referee(Rid, Type, Max_workload, Prev_workload, Prev_payment).
%newDamage(Cid,Rid,Dmg):- assign(Cid,Rid), case(Cid,_,_,Dmg,_,_).
%totalDamage(Rid,Dmg):- Dmg = #sum{Damage,Cid,Rid: newDamage(Cid,Rid,Damage)}, referee(Rid, Type, Max_workload, Prev_workload, Prev_payment).
%:- referee(Rid,e,Max_workload,Prev_workload,_), totalDamage(Rid,Dmg), externalMaxDamage(Max),Dmg>=Max.

%%%%%%%%%%%%%%%%%%%%%%%%% Soft Constraints %%%%%%%%%%%%%%%%%%%%%%

%paymentToExternals(Total) :- Total = #sum{Pay,Rid,e: payment(_,Rid,e,Pay)}.
:~ Total = #sum{Pay,Rid,e: payment(_,Rid,e,Pay)}, CAPenalty =16*Total. [CAPenalty@0,1]

orid(Rid,e,SumOrid) :- referee(Rid, e, _, _, Prev),payment(Cid,Rid,e,Payment), SumOrid=Prev+Payment.


%sumOfPay(Rid,e,Sum):- referee(Rid, e, _, _, Prev), Sum = #sum{Payment,Rid:payment(Cid,Rid,e,Payment)}.
%orid(Rid,e,SumOrid) :- referee(Rid, e, _, _, Prev),sumOfPay(Rid,e,Sum), SumOrid=Prev+Sum.

%orid(Rid,e,SumOrid) :- referee(Rid, e, _, _, Prev),Pay= #sum{Payment,Rid:payment(Cid,Rid,e,Payment)}, SumOrid=Prev+Pay.

sumOrid(SumO) :- SumO= #sum{SumA,Rid: orid(Rid,e,SumA)}.
numExternals(N):- N= #count{Rid,e: referee(Rid,e,_,_,_)},N>0.

% For your average payment external, write the A and B in separate line.
average_payment_external(Avg):- sumOrid(A),numExternals(B), Avg=A/B.




divergenceCost(Rid,e,|SumD-Avg|) :- orid(Rid,e,SumD), average_payment_external(Avg).

:~ orid(Rid,e,SumD), average_payment_external(Avg), CBPenalty = 7*(|SumD -Avg|). [CBPenalty@0,2]



workLoad(Rid,Type,Prev_workload+Eff):- referee(Rid,Type,_,Prev_workload,_),assign(Cid,Rid),case(Cid,_,Eff,_,_,_).
sumOfWorkLoad(Sum) :- Sum = #sum{Wl,Rid: workLoad(Rid,Type,Wl)}.
numOfRef(N) :- N = #count{Rid: referee(Rid,_,_,_,_)}.
averageWorkLoad(To) :- sumOfWorkLoad(Sum), numOfRef(N), To=Sum/N.

%costWL(Rid,|Wl-To|) :- workLoad(Rid,Type,Wl), averageWorkLoad(To).

:~ CCPenalty = 9 * |Wl-To|,workLoad(Rid,Type,Wl),averageWorkLoad(To). [CCPenalty@0,3]

%sumCostWL(S) :- S=#sum{W,Rid: costWL(Rid,W)}.

%#minimize{W,Rid: costWL(Rid,W)}.


%%%%% preference constraints %%%%%
%case(3, b, 120, 800, 1190, 31).
%prefType(1, a, 1).
%referee(1, i, 600, 220, 0).
% Hard constraint
:- prefType(Rid, Type, 0), case(Cid, Type,_, _, _, _), assign(Cid,Rid).
% computation
prefCost(Rid,Cost) :- prefType(Rid, Type, Pref), assign(Cid,Rid), Cost=3-Pref, case(Cid, Type,_, _, _, _).
%sumPrefCost(Cost):- Cost=#sum{C,Rid: prefCost(Rid,C) }.
:~ CDPenalty = 34 * Cost, Cost =#sum{C,Rid: prefCost(Rid,C) }. [CDPenalty,4]

% 
%#show sumPrefCost/1.
%#show assign/2.
%#show prefCost/2.

%%%%%% Region Constraints %%%%%%
%case(Cid, Type, Effort, Damage, Postc, Payment).
%prefRegion(Rid, Postc, Pref)
:- prefRegion(Rid,Postc,0), case(Cid, Type, Effort, Damage, Postc, Payment), assign(Cid,Rid).
%prefRegionCost(Rid,Cost) :- prefRegion(Rid,Postc,Pref), assign(Cid,Rid),case(Cid, Type, Effort, Damage, Postc, Payment) , Cost = 3-Pref.
:~ CEPenalty = 34 * Cost, prefRegion(Rid,Postc,Pref), assign(Cid,Rid),case(Cid, Type, Effort, Damage, Postc, Payment) , Cost = 3-Pref. [CEPenalty,5]




%CATotal(CAPenalty):- Total = #sum{Pay,Rid,e: payment(_,Rid,e,Pay)}, CAPenalty =16*Total.
%cATotal(Total*16):- Total = #sum{Pay,Rid,e: payment(_,Rid,e,Pay)}.
%cBTotal(
%cDTotal(Cost*34):- Cost =#sum{C,Rid: prefCost(Rid,C) }.
%div(Rid,e, CBPenalty) :- orid(Rid,e,SumD), average_payment_external(Avg), CBPenalty = 7*(|SumD -Avg|).
%cBTotal(Total) :- Total = #sum{CBPenalty,Rid:div(Rid,e, CBPenalty)}.
%:~ orid(Rid,e,SumD), average_payment_external(Avg), CBPenalty = 7*(|SumD -Avg|). [CBPenalty@0]


%:- not assign(8,19). :- not assign(9,19). :- not assign(10,21).

%:- not assign(16,32). :- not assign(17,32). 


%#show cDTotal/1.
%#show cATotal/1.
#show assign/2.


%#show prefRegion/2.
%#show prefRegionCost/2.

%#show assign/2.
%#show divergenceCost/3.
%#show costWL/2.

%Avg=A/B.
%#show assign/2.
%#show payment/4.
%#show paymentToExternals/1.
%#show orid/3.
%#show average_payment_external/1.
%#show divergenceCost/3.
%#show averageWorkLoad/1.
%#show cbCost/1.
%#show referee/5.
%#show assign/2.
%#show sumOfWorkLoad/1.
%#show numOfRef/1.
%#show costWL/2.
%#show averageWorkLoad/1.
%#show case/6.
%#show workLoad/3.


