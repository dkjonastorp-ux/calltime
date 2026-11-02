# Bygger forhåndsvisningen (artifact) ud fra appens index.html
import re,sys
s=open(sys.argv[1]).read()
for pat in [r'<meta name="apple-mobile-web-app[^>]*>\n',r'<meta name="mobile-web-app-capable"[^>]*>\n',r'<meta name="theme-color"[^>]*>\n',r'<link rel="manifest"[^>]*>\n',r'<link rel="apple-touch-icon"[^>]*>\n',r'<script src="https://www.gstatic.com[^>]*></script>\n',r'<script src="firebase-config.js"></script>\n']:
    s=re.sub(pat,'',s)
s=s.replace("if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){});});}",'')
s=s.replace('<title>CallTime</title>','<title>CallTime forhåndsvisning</title>')
demo='''/* forhåndsvisning: eksempeldata, ingen login */
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
s=s.replace(b, demo+"loadLocal();if(!S.jobs.length)S=demoData();render();setBadge('Forhåndsvisning – eksempeldata');")
s=s.replace('<main>','<main>\n<div style="font-size:12px;color:var(--mut);margin-bottom:10px">Forhåndsvisning med eksempeldata. Kommentér direkte på siden; ændringer kommer først ud i den rigtige app, når Claude lægger dem på GitHub.</div>',1)
open(sys.argv[2],'w').write(s)
