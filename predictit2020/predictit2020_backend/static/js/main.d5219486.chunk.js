(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{52:function(e,t,a){e.exports=a(69)},57:function(e,t,a){},59:function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},60:function(e,t,a){},69:function(e,t,a){"use strict";a.r(t);var n=a(0),o=a.n(n),r=a(7),c=a.n(r),i=a(33),l=a(9),s=(a(57),a(39)),d=a(29),u=a.n(d),p=a(36),m=a(17),v=(a(59),a(60),a(43)),f=a.n(v),b={AL:9,AK:3,AZ:11,AR:6,CA:55,CO:9,CT:7,DC2:3,DE:3,FL:29,GA:16,HI:4,ID:4,IL:20,IN:11,IA:6,KS:6,KY:8,LA:8,ME:4,MD:10,MA:11,MI:16,MN:10,MS:6,MO:10,MT:3,NE:5,NV:6,NH:4,NJ:14,NM:5,NY:29,NC:15,ND:3,OH:18,OK:7,OR:7,PA:20,RI:4,SC:9,SD:3,TN:11,TX:38,UT:6,VT:3,VA:13,WA:12,WV:5,WI:10,WY:3},h=a(101),y=a(100);function g(e){document.cookie;if(document.cookie&&""!==document.cookie)for(var t=document.cookie.split(";"),a=0;a<t.length;a++){var n=t[a].split("="),o=Object(m.a)(n,2),r=o[0],c=o[1];if(e===(r=r.trim()))return c}return null}var E=function(e){var t=o.a.useState(0),a=Object(m.a)(t,2),n=a[0],r=a[1],c=o.a.useState({}),l=Object(m.a)(c,2),d=l[0],v=l[1],E=o.a.useState({democrats:0,republicans:0}),x=Object(m.a)(E,2),k=x[0],O=x[1],S=o.a.useState(""),w=Object(m.a)(S,2),N=w[0],C=w[1],T=o.a.useState(""),j=Object(m.a)(T,2),D=j[0],A=j[1],I=o.a.useState(""),_=Object(m.a)(I,2),M=_[0],J=_[1],L=o.a.useState(!1),R=Object(m.a)(L,2),W=R[0],F=R[1],P=o.a.useState(void 0),V=Object(m.a)(P,2),Y=V[0],B=V[1],K=51==Object.keys(d).length,H=new Date<new Date(2020,10,3),G=function(e){var t={};return e&&e.split("?")[1].split("&").forEach((function(e){var a=e.split("=");t[a[0]]=decodeURIComponent(a[1])})),t}(e.location.search).view_id;return o.a.useEffect((function(){(function(){var e=Object(p.a)(u.a.mark((function e(){var t,a,n,o;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(G){e.next=6;break}return e.next=3,fetch("/load/");case 3:t=e.sent,e.next=9;break;case 6:return e.next=8,fetch("/load/?view_id=".concat(G));case 8:t=e.sent;case 9:if(403!==t.status){e.next=13;break}r(2),e.next=31;break;case 13:return e.next=15,t.json();case 15:a=e.sent,n=a.base_url,A(n),o=JSON.parse(a.prediction),J("".concat(n,"/static/build/index.html?view_id=").concat(o.id)),B(a.username),delete o.number_correct,delete o.id,delete o.user,o.ID=o.IDA,delete o.IDA,O({democrats:o.electoral_votes_dem,republicans:o.electoral_votes_rep}),delete o.electoral_votes_dem,delete o.electoral_votes_rep,v(o),r(1);case 31:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}})()()}),[]),o.a.createElement("div",{className:"App"},0===n?"Loading":2===n?"Not Logged in properly, or invalid ID, unable to load":1===n&&o.a.createElement(o.a.Fragment,null,o.a.createElement("div",{style:{position:"relative",marginTop:"50px"}},o.a.createElement("div",{style:{position:"absolute",left:"0px",top:"10px",height:"40px",width:"".concat(k.republicans/538*100,"%"),background:"red"}}),o.a.createElement("div",{style:{position:"absolute",right:"0px",top:"10px",height:"40px",width:"".concat(k.democrats/538*100,"%"),background:"navy"}}),o.a.createElement("div",{style:{position:"absolute",left:"5%",top:"0px",color:"#999"}},o.a.createElement("h3",null,"Republicans: ",k.republicans)),o.a.createElement("div",{style:{position:"absolute",right:"5%",top:"0px",color:"#999"}},o.a.createElement("h3",null,"Democrats: ",k.democrats)),void 0!==G&&o.a.createElement("div",{style:{paddingTop:"100px"}},o.a.createElement("h1",null,Y,"'s map")),o.a.createElement("div",{style:{paddingTop:"100px"}},o.a.createElement(f.a,{customize:d,onClick:function(e){if(!G){C("");var t="DC"==e.target.dataset.name?"DC2":e.target.dataset.name,a=JSON.parse(JSON.stringify(d));t in a?"navy"===a[t].fill?(a[t].fill="red",O({democrats:k.democrats-b[t],republicans:k.republicans+b[t]})):(a[t].fill="navy",O({democrats:k.democrats+b[t],republicans:k.republicans-b[t]})):(a[t]={fill:"navy"},O(Object(s.a)(Object(s.a)({},k),{},{democrats:k.democrats+b[t]}))),v(a)}}}))),H?o.a.createElement(o.a.Fragment,null,o.a.createElement("div",null,void 0===G&&o.a.createElement(h.a,{onClick:function(){var e=Object(p.a)(u.a.mark((function e(t){var a;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=g("csrftoken"),e.next=3,fetch("/save/",{method:"POST",mode:"cors",headers:{"X-CSRFToken":a,"Content-Type":"application/json"},body:JSON.stringify({states:d,electoralVotes:k})});case 3:200===e.sent.status?C("Saved! You're all set! (You can modify it until November 3rd)"):C("Did not save properly!  Please try clicking save again");case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),variant:"contained",disabled:!K,color:"primary",style:{marginTop:"50px"}},K?"Save My Prediction":"Not Finished")),void 0===G&&o.a.createElement("div",{style:{marginTop:"50px"}},o.a.createElement("p",null,"Share Link"),o.a.createElement(y.a,{value:M,style:{width:"75%"},onClick:function(e){e.target.select(),document.execCommand("copy"),F(!0),setTimeout((function(){F(!1)}),1500)}})),void 0===G&&o.a.createElement("p",{style:{paddingBottom:"200px"}},W?"Copied!":"Click to copy to Clipboard"),void 0!==G&&H&&o.a.createElement("div",{style:{marginTop:"50px"}},"This is ",Y,"'s prediction for the 2020 election, what's yours?  Give it a try yourself here!",o.a.createElement("div",{style:{paddingBottom:"200px"}},o.a.createElement(i.b,{to:"//".concat(D),target:"_blank"},"Predict the Election")))):void 0===G&&o.a.createElement("p",null,"It is November 3rd (Or after) and you can't update your prediction anymore."),o.a.createElement("p",null,N)))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(o.a.createElement(o.a.StrictMode,null,o.a.createElement(i.a,null,o.a.createElement(l.a,{link:"/",component:E}))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[52,1,2]]]);
//# sourceMappingURL=main.d5219486.chunk.js.map