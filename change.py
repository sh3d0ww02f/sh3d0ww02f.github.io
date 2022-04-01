import requests
import base64
import datetime
ss=["https://raw.githubusercontents.com/colatiger/v2ray-nodes/master/ss.md"]        
vmess=["https://raw.githubusercontents.com/colatiger/v2ray-nodes/master/vmess.md","https://raw.githubusercontents.com/wrfree/free/main/v2","https://proxies.bihai.cf/vmess/sub?c=CN,HK,TW,JP","https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg"]
trojan=["https://raw.githubusercontents.com/colatiger/v2ray-nodes/master/trojan.md","https://proxies.bihai.cf/trojan/sub"]
clash=["https://raw.githubusercontents.com/colatiger/v2ray-nodes/master/clash.yaml","https://free.kingfu.cf/clash/proxies?c=CN,HK,TW,JP","https://proxies.bihai.cf/clash/proxies?c=CN,HK,TW,JP"]
ssr=["https://raw.githubusercontents.com/wrfree/free/main/ssr","https://proxies.bihai.cf/ssr/sub"]
shadowrocket=["https://proxies.bihai.cf/clash/proxies?c=CN,HK,TW,JP,US"]
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
def log():
    now=datetime.datetime.utcnow()
    hour=str(int(datetime.datetime.utcnow().strftime("%H"))+8)
    year_month_day=now.strftime("%Y-%m-%d")
    log_time=year_month_day+","+hour
    with open("log.txt",'w')as f:
        f.write(log_time+"时 更新完毕")
    
    
def other(name,n_):
    result=[]
    for item in name:
        raw=requests.get(item,headers=headers).content
        tmp=base64.b64decode(raw).decode(errors="ignore").split("\n")[:-1]
        result.extend(tmp)
    with open(n_+".config",'w')as f:
        f.write(base64.b64encode(('\n'.join(list(set(result)))).encode()).decode())
def clash_handle():
    a1=requests.get(clash[0],headers=headers).text
    b1=requests.get(clash[1],headers=headers).text.replace("-","  -")
    c1=requests.get(clash[2],headers=headers).text.replace("-","  -")
    content=a1.replace("proxies:\n",b1).replace("proxies:\n",c1,1)
    content=a1
    with open("clash.yaml",'w',encoding="utf-8")as f:
        f.write(content)
def shadowrocket_handle():  
        with open("shadowrocket.yaml",'w',encoding="utf-8")as f:
            f.write(requests.get(shadowrocket[0],headers=headers).text)
        
def vmess_handle():
    other(vmess,"vmess")
def ssr_handle():
    other(ssr,"ssr")
def ss_handle():
    other(ss,"ss")
def trojan_handle():
    other(trojan,"trojan")
def handle_all():
    try:
        shadowrocket_handle()
    except:
        pass
    try:
        ssr_handle()
    except:
        pass   
    try:
        ss_handle()
    except:
        pass    
    try:
        clash_handle()
    except:
        pass        
    try:
        vmess_handle()
    except:
        pass        
    try:
        trojan_handle()
    except:
        pass    
    log()
def test_clash_new():
	try:
		resp=requests.get("https://sub.xeton.dev/sub?target=clash&url=https://newbird.cf/vmess.config").text
	except:
		resp=""
	with open("clash1.yaml",'w')as f:
		f.write(resp)
def update_html():
     target=["ssr",'ss','trojan','clash',"shadowrocket","v2"]
     l={}
     base="https://newbird.cf/{}.config"
     ssr=base.format("ssr")
     ss=base.format("ss")
     trojan=base.format("trojan")
     vmess=base.format("vmess")
     shadowrocket="https://newbird.cf/shadowrocket.yaml"
     clash="https://newbird.cf/clash.yaml"
     l.update({"ssr":ssr,"ss":ss,"trojan":trojan,"clash":clash,"shadowrocket":shadowrocket,"v2":vmess})
     head='''
          <html>
        <head>
         <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">  
            <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
            <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
        </head>
        <body>
     '''
     tail='''
      <script>
          function copyText(text, callback){ // text: 要复制的内容， callback: 回调
                    var tag = document.createElement('input');
                    tag.setAttribute('id', 'cp_hgz_input');
                    tag.value = text;
                    document.getElementsByTagName('body')[0].appendChild(tag);
                    document.getElementById('cp_hgz_input').select();
                    document.execCommand('copy');
                    document.getElementById('cp_hgz_input').remove();
                    if(callback) {callback(text)}
                }
          document.getElementById('ssr').onclick = function (){
                copyText( 'https://newbird.cf/ssr.config', function (){alert("复制成功")})
            }
          document.getElementById('ss').onclick = function (){
                copyText( 'https://newbird.cf/ss.config', function (){alert("复制成功")})
            }
          document.getElementById('trojan').onclick = function (){
                copyText( 'https://newbird.cf/trojan.config', function (){alert("复制成功")})
            }
          document.getElementById('v2').onclick = function (){
                copyText( 'https://newbird.cf/vmess.config', function (){alert("复制成功")})
            }
          document.getElementById('shadowrocket').onclick = function (){
                copyText( 'https://newbird.cf/shadowrocket.yaml', function (){alert("复制成功")})
            }
          document.getElementById('clash').onclick = function (){
                copyText( 'https://newbird.cf/clash.yaml', function (){alert("复制成功")})
            }
         </script>
        </body>
     </html>
     '''
     with open("log.txt",'r')as f:
        update_time=f.read()
        body=f"""
     <table class="table">
	<caption>{update_time}</caption>
   <thead>
      <tr>
         <th>类型</th>
         <th>订阅地址</th>
      </tr>
   </thead>
   <tbody>
    """
     for item in target:
      body=body+"""
            <tr>
         <td>"""+item+"""</td>
         <td>"""+l[item]+'''</td>
		  <td><button type="button" class="btn btn-info" id="'''+item+'''">复制到剪切板</button></td>
      </tr>
            '''
     body=body+"""
   </tbody>
</table>
     """
     html=head+body+tail
     with open("airport.html",'w',encoding="utf-8")as f:
        f.write(html)
handle_all()
update_html()    
test_clash_new()
