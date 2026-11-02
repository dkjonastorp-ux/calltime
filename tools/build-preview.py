# Bygger forhåndsvisningen (artifact) ud fra appens index.html
import re,sys
s=open(sys.argv[1]).read()
for pat in [r'<meta name="apple-mobile-web-app[^>]*>\n',r'<meta name="mobile-web-app-capable"[^>]*>\n',r'<meta name="theme-color"[^>]*>\n',r'<link rel="manifest"[^>]*>\n',r'<link rel="apple-touch-icon"[^>]*>\n',r'<script src="https://www.gstatic.com[^>]*></script>\n',r'<script src="firebase-config.js"></script>\n']:
    s=re.sub(pat,'',s)
s=s.replace("if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){});});}",'')
s=s.replace('<title>CallTime</title>','<title>CallTime forhåndsvisning</title>')
demo='''/* forhåndsvisning: eksempeldata, ingen login */
function testJob(){
  var mon=isoWeek(ld(new Date())).mon,T=[
    [-21,'08:00','18:30',0],[-20,'07:00','19:15',1],[-19,'10:00','20:00',0],[-18,'12:00','23:30',0],[-17,'08:30','17:00',0.5],
    [-14,'06:00','16:45',0],[-13,'09:00','21:15',0],[-12,'11:30','22:45',1.5],[-10,'07:30','18:00',0],[-9,'14:00','02:00',0],
    [-8,'10:00','16:00',0],[-7,'08:00','20:30',0],[-6,'09:15','19:45',0],[-5,'07:45','18:15',0.75],[-4,'13:00','23:00',0],
    [-3,'08:00','19:00',0],[-2,'16:00','03:30',0],[-1,'10:00','14:00',0]];
  return {id:'dtest',name:'Test',agr:'fiktion',grp:'1-4',single:false,rate:3345.6,days:T.map(function(t,i){return {id:'dt'+i,date:isoAdd(mon,t[0]),start:t[1],end:t[2],tr:t[3],unv:i%5===3?'u':'v',gear:i%3===0?['Steadicam']:(i%4===1?['Cyclo Lite']:[]),note:''};})};
}

function demoData(){
  var y=function(n){var d=new Date();d.setDate(d.getDate()-n);return ld(d);};
  return {updated:1,jobs:[
    {id:'dj1',name:'Kryb',agr:'fiktion',grp:'1-4',single:false,rate:3000,days:[
      {id:'dd1',date:y(0),start:'08:00',end:'',tr:0,unv:'v',gear:['Steadicam'],note:'Location dag'},
      {id:'dd2',date:y(1),start:'07:30',end:'19:15',tr:1,unv:'v',gear:['Steadicam'],note:''},
      {id:'dd3',date:y(2),start:'10:30',end:'16:30',tr:0,unv:'v',gear:[],note:''}]},
    {id:'dj2',name:'Bilreklame',agr:'reklame',grp:'1-4',single:false,rate:6000,days:[
      {id:'dd4',date:y(6),start:'06:00',end:'20:30',tr:0.5,unv:'v',gear:['Steadicam','Cyclo Lite'],note:'Nattescene'}]}]};
}
'''
b="loadLocal();render();initSync();"
assert b in s
s=s.replace(b, demo+"loadLocal();if(!S.jobs.length)S=demoData();if(!S.jobs.some(function(x){return x.id==='dtest';}))S.jobs.unshift(testJob());render();setBadge('Forhåndsvisning – eksempeldata');")
s=s.replace('<main>','<main>\n<div style="font-size:12px;color:var(--mut);margin-bottom:10px">Forhåndsvisning med eksempeldata. Kommentér direkte på siden; ændringer kommer først ud i den rigtige app, når Claude lægger dem på GitHub.</div>',1)
open(sys.argv[2],'w').write(s)
