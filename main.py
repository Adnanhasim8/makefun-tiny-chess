import json,os,urllib.request as R;X=TimeoutError
V=[0,100,300,320,500,950,0]
KN=(-31,-33,-14,-18,14,18,31,33);BD=(-17,-15,15,17);RD=(-16,-1,1,16);K8=BD+RD
B=[0]*128;HS=[];NN=0;NB=9e4;T={}
N=[chr(97+s%8)+chr(49+(s>>4))for s in range(128)]
def A(s,w):
 for d in-15*w,-17*w:
  t=s+d
  if not t&0x88 and B[t]==w:return 1
 for ds,tp,sl in((KN,2,0),(K8,6,0),(BD,3,1),(RD,4,1)):
  for d in ds:
   t=s+d
   if sl:
    while not t&0x88 and not B[t]:t+=d
    if not t&0x88 and B[t]in(tp*w,5*w):return 1
   elif not t&0x88 and B[t]==tp*w:return 1
 return 0
def G():
 ms=[];ap=ms.append
 for s,p in enumerate(B):
  if p*S<=0:continue
  t=abs(p)
  if t==1:
   d=16*S;r=s>>4;w=6-(S>0)*5;pr=r==7-w
   pv=lambda u:[ap(s|u<<7|x<<14)for x in((5,4,3,2)if pr else(0,))]
   for dd in d-1,d,d+1:
    u=s+dd
    if u&0x88:continue
    q=B[u]
    if dd==d:
     if q:continue
     pv(u)
     if r==w and not B[s+2*d]:ap(s|(s+2*d)<<7)
    elif(q and q*S<0)or u==EP:pv(u)
  else:
   for d in(KN,BD,RD,K8,K8)[t-2]:
    u=s+d
    while not u&0x88 and not B[u]:
     ap(s|u<<7)
     if t in(2,6):break
     u+=d
    if not u&0x88 and B[u]*S<0:ap(s|u<<7)
 for bt,kf,dr in((1,4,1),(2,4,-1))if S>0 else((4,116,1),(8,116,-1)):
  if C&bt and not(B[kf+dr]or B[kf+2*dr]or(dr<0 and B[kf-3]))and not A(kf,-S)+A(kf+dr,-S)+A(kf+2*dr,-S):ap(kf|(kf+2*dr)<<7)
 return ms
def MV(m,u):
 global S,C,EP
 f=m&127;t=(m>>7)&127;pr=m>>14
 if u:
  S=-S
  cp,C,EP,cs=HS.pop()
  p=B[t]
  B[f]=S if pr else p
  B[t]=0
  if cs>=0:B[cs]=cp
  elif cp:B[t]=cp
  if abs(p)==6:
   if t-f==2:B[f+3]=B[f+1];B[f+1]=0
   elif f-t==2:B[f-4]=B[f-1];B[f-1]=0
 else:
  p=B[f];cp=B[t];cs=-1
  if abs(p)==1 and not cp and f&7!=t&7:
   cs=t-16*S;cp=B[cs];B[cs]=0
  HS.append((cp,C,EP,cs))
  B[t]=pr*S if pr else p
  B[f]=0
  EP=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1
  if abs(p)==6:
   if t-f==2:B[f+1]=B[f+3];B[f+3]=0
   elif f-t==2:B[f-1]=B[f-4];B[f-4]=0
   C&=~3 if S>0 else ~12
  for sq,bt in(0,2),(7,1),(112,8),(119,4):
   if f==sq or t==sq:C&=~bt
  S=-S
def LM():
 r=[]
 for m in G():
  f=m&127;t=(m>>7)&127;cp=B[t]
  af=abs(B[f])
  if af==1 and f&7!=t&7:cp=cp or 1
  r.append((af-10*V[abs(cp)]if cp else-900 if m>>14 else 0,m))
 return sorted(r)
def E():
 e=0
 for s,p in enumerate(B):
  if p:
   t=abs(p);v=V[t]
   if t==1:v+=(s>>4 if p>0 else 7-s//16)*6
   elif t<4:v+=(s&7)*(7-s&7)+(s>>4)*(7-s//16)
   e+=v*p//abs(p)
 return e*S
def SE(a,b,d,pl):
 global BM,NN
 NN+=1
 if NN>NB:raise X
 w=A(B.index(6*S),-S)
 if d<=0:
  a=max(a,-9999 if w else E())
  if a>=b:return b
 k=(tuple(B),S,C,EP);h=T.get(k);a0=a
 if h and d>0 and pl and h[0]>=d:
  y=h[1]
  if h[2]==1:a=max(a,y)
  if h[2]==2:b=min(b,y)
  if a>=b or h[2]==0:return y
 ms=LM();lg=0;bm=0
 if d<=0 and not w:ms=[x for x in ms if x[0]]
 if h and h[3]:ms.sort(key=lambda x:x[0]-99999*(x[1]==h[3]))
 for kk,m in ms:
  MV(m,0)
  if A(B.index(-6*S),S):MV(m,1);continue
  lg+=1
  rd=d-2 if lg>4 and d>2 and not kk and not w else d-1
  try:
   v=-SE(-b if lg<2 else-a-1,-a,rd,pl+1)
   if rd<d-1 and v>a:v=-SE(-a-1,-a,d-1,pl+1)
   if lg>1 and a<v<b:v=-SE(-b,-a,d-1,pl+1)
  except X:MV(m,1);raise
  MV(m,1)
  if v>a:
   a=v;bm=m
   if not pl:BM=m
  if a>=b:break
 if not lg:return-10000+pl if w else 0 if d>0 else a
 if d>0:T[k]=(d,a,2*(a<=a0)+(a>=b),bm)
 return a
def FEN(f):
 global B,S,C,EP
 B=[0]*128;ps=f.split();s=112
 for ch in ps[0]:
  if ch=='/':s-=24
  elif'0'<ch<'9':s+=int(ch)
  else:B[s]=((ch<'a')*2-1)*('PNBRQK'.index(ch.upper())+1);s+=1
 S=2*(ps[1]=='w')-1
 C=sum(1<<i for i in range(4)if'KQkq'[i]in ps[2])
 EP=N.index(ps[3])if ps[3]!='-'else-1
def US(m):
 return N[m&127]+N[m>>7&127]+('  nbrq'[m>>14]if m>>14 else'')
def P(p,b):return json.load(R.urlopen(R.Request(os.getenv('MAKEFUN_ENV_URL')+p,data=json.dumps(b).encode())))
def GO(f,l):
 global NN
 FEN(f);ms=LM()
 m=ms[0][1];NN=0
 try:
  for dd in range(1,99):SE(-99999,99999,dd,0);m=BM
 except X:pass
 return US(m)if US(m)in l else l[0]
if __name__=='__main__':
 while 1:
  g=P('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':g=P('/move',{'game':g['game'],'move':GO(g['fen'],g['legal_moves'])})
