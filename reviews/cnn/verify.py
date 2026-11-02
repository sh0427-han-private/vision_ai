from pathlib import Path
import functools,http.server,threading,json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)));threading.Thread(target=server.serve_forever,daemon=True).start()
rows=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in [(1600,950),(1440,810),(1366,768),(1280,720),(390,844),(430,900)]:
  page=browser.new_page(viewport={'width':w,'height':h});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(f'http://127.0.0.1:{server.server_port}/notes/cnn.html');page.evaluate('document.fonts.ready');page.wait_for_timeout(1500)
  page.locator('img').evaluate_all("es=>es.forEach(e=>e.loading='eager')");page.wait_for_function("[...document.images].every(i=>i.complete)")
  math=page.evaluate("!!window.MathJax?.startup?.promise")
  assert math, 'MathJax failed to load'
  page.evaluate('MathJax.startup.promise')
  values=[]
  for i in range(9):
   page.locator('#conv-position').evaluate('(e,i)=>{e.value=i;e.dispatchEvent(new Event("input"))}',i)
   output=list(map(int,page.locator('#conv-output span').all_inner_texts()));selected=page.locator('#conv-output .selected').inner_text()
   assert output==[3,3,0]*3 and int(selected)==output[i]
   assert page.locator('#conv-input span').evaluate_all("es=>es.filter(e=>e.style.background==='rgb(36, 84, 216)').length")==9
   values.append(int(selected))
  page.locator('#conv-position').evaluate('(e)=>{e.value=0;e.dispatchEvent(new Event("input"))}')
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');doc=c.send('DOM.getDocument')['root']['nodeId'];node=c.send('DOM.querySelector',{'nodeId':doc,'selector':'#conv-input span'})['nodeId'];fonts=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
  data=page.evaluate('''()=>({overflow:document.documentElement.scrollWidth>innerWidth,tracking:getComputedStyle(document.querySelector('h1')).letterSpacing,broken:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overviewFigures:document.querySelectorAll('#overview figure').length,convFigures:document.querySelectorAll('#convolution figure').length,mathErrors:document.querySelectorAll('mjx-merror').length})''')
  assert not data['overflow'] and not data['broken'] and data['overviewFigures']==1 and data['convFigures']==1 and not data['mathErrors'] and not errors,(w,data,errors)
  assert all('Pretendard' in f['familyName'] and f['isCustomFont'] for f in fonts)
  if w==1440:
   page.screenshot(path=str(OUT/'desktop.png'))
   page.locator('#overview').screenshot(path=str(OUT/'overview.png'))
   page.locator('#convolution').screenshot(path=str(OUT/'convolution.png'))
  if w==390:page.screenshot(path=str(OUT/'mobile.png'))
  rows.append({'viewport':[w,h],**data,'fonts':fonts,'mathjax_loaded':math,'selected_values':values,'errors':errors});page.close()
 browser.close()
assert 32*3*3*3+32==896 and 256*64+64*64*9+64*256==69632 and 256*256*9==589824
(OUT/'validation.json').write_text(json.dumps({'cases':rows,'passed':True,'limits':['Existing paper SVG typography is retained; not claimed Pretendard','No full chapter scientific peer review or user approval']},ensure_ascii=False,indent=2)+'\n')
server.shutdown();print('PASS six viewports, all9 convolution positions, font/loading/duplicates/overflow and parameter arithmetic')
