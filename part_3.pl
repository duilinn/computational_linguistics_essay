s --> (np, vp); (advp, s); (c, s); (adj, s); (np).
advp --> (adv); (pp); (adv, np, pp).
adv --> [almost]; [now]; [so]; [often].
adjp --> (adj); (adj, pp).
adj --> [economic]; [high]; [our]; [challenging]; [hard]; [total]; [my]; [new]; [significant]; [state_of_the_art]; [local].
det --> [one]; [these]; ["27"]; [other].
np --> (det, n); (adj, n); (n, n);(n); (n, pp); (pron); (pron, s); (det, n, s); (n1, c, n2); (n, vp); (n3, n), (adjp, np); (n4, n4).
n1 --> np.
n2 --> np.
n3 --> (n, n); (n).
n4 --> (n3, n3).
n --> [year]; [pandemic]; [restrictions]; [sectors]; [conditions]; [inflation]; [energy]; [costs]; [pressure]; [businesses]; [urgency]; [climate]; [action]; [planet]; [future]; [generations]; [course]; [part]; [irelands]; [response]; [war]; [ukraine]; [hard]; [solidarity]; [understanding]; [societys]; [cohesion]; [well_being]; [funding]; ["2023"]; [department]; [funding]; [place]; [schools]; [irish]; [language]; [assistant]; [baitweets]; [research]; [desire]; [youth]; [radio]; [service]; [findings]; [support]; [centre]; [tglurgan]; [groups].
pp --> (p, s); (p, np); (p, vp); (p, np, pp);(p, p).
p --> [after]; [with]; [on]; [of]; [for]; [in]; [up]; [to]; [out].
vp --> (v); (v, np); (v, np, pp); (advp, vp);  (aux, vp); (v, pp); (v1, c, v2); (v, vp); (v, np, vp); (v, pp, np); (v, adjp).
v1 --> vp.
v2 --> vp.
v --> [ended]; [face]; [putting]; [tackle]; [safeguard]; [play]; [done]; [reinforce]; [supported]; [is]; [follows]; [enable]; [employ]; [carried]; [show]; [planned]; [be]; [repair]; [use].
c --> [and]; [so]; [to]; [by]; [as]; [that].
pron --> [they]; [we]; [it]; [everything].
aux --> [must]; [can]; [continue]; [have]; (adv, adv).

%d1 = [almost,one,year,after,pandemic,restrictions,ended,these,sectors,now,face,challenging,economic,conditions,with,high,inflation,and,energy,costs,putting,pressure,on,businesses].
%d2 = [they,must,tackle,the,urgency,of,climate,action,so,we,can,safeguard,our,planet,for,future,generations].
%d3 = [and,of,course,they,must,play,our,part,in,irelands,response,to,the,war,in,the,ukraine].
%d4 = [as,we,have,so,often,done,in,hard,times,these,sectors,continue,to,reinforce,our,resilience,solidarity,and,understanding,and,support,societys,cohesion,and,well_being].
%d5 = [total,funding,for,"2023",for,the,sectors,supported,by,my,department,is,as,follows].

%s1 = [funding,is,now,in,place,to,enable,up,to,"27",schools,employ,an,irish,language,assistant].
%s2 = [baitweets,have,carried,out,research,on,the,desire,for,a,new,irish,language,youth,radio,service].
%s3 = [delighted,these,findings,show,significant,support,for,it].
%s4 = [a,new,state_of_the_art,centre,planned,for,tglurgan,and,other,local,groups].
%s5 = [we,must,be,able,to,repair,everything,that,we,use].

% s(X, []).