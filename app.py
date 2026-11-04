from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json, os
from datetime import datetime

app = FastAPI()

SERVICOS = {
    "corte": {"nome": "Corte", "preco": 30, "duracao": 30},
    "barba": {"nome": "Barba", "preco": 20, "duracao": 30},
    "corte_barba": {"nome": "Corte + Barba", "preco": 50, "duracao": 60},
    "sobrancelha": {"nome": "Sobrancelha", "preco": 15, "duracao": 15},
}
SENHA_BARBEIRO = "Felipeperfil1"
WHATSAPP = "5561984747116"
ARQ = "agendamentos.json"

def carregar():
    if not os.path.exists(ARQ): return {}
    try: return json.load(open(ARQ))
    except: return {}

def salvar(d): json.dump(d, open(ARQ,"w"), indent=2, ensure_ascii=False)

opcoes = "".join([f'<option value="{k}">{v["nome"]} - R${v["preco"]}</option>' for k,v in SERVICOS.items()])

HTML_HOME = f"""
<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Barbearia Elite</title>
<style>body{{font-family:Inter,Arial;background:#0f0f0f;color:#fff;margin:0;padding:20px}}.card{{max-width:480px;margin:auto;background:#1a1a1a;padding:20px;border-radius:12px}}input,select,button{{width:100%;padding:12px;margin:6px 0;border-radius:8px;border:none}}button{{background:#25D366;color:#fff;font-weight:bold;cursor:pointer}}.hora{{display:inline-block;padding:10px 14px;margin:4px;background:#2a2a2a;border-radius:8px;cursor:pointer}}.hora.sel{{background:#25D366}}</style>
</head><body><div class="card">
<h2>Barbearia Elite</h2>
<input id="nome" placeholder="Seu nome">
<select id="servico">{opcoes}</select>
<input id="data" type="date">
<div id="horarios"></div>
<button onclick="agendar()">Agendar no WhatsApp</button>
<br><br><a href="/admin" style="color:#888">Sou o barbeiro</a>
</div>
<script>
let sel=null;const dataInput=document.getElementById('data');dataInput.valueAsDate=new Date();
async function carregar(){{
  const data=dataInput.value;const serv=document.getElementById('servico').value;
  const res=await fetch(`/horarios-disponiveis?data=${{data}}&servico=${{serv}}`);const horas=await res.json();
  const div=document.getElementById('horarios');div.innerHTML='';
  horas.forEach(h=>{{const b=document.createElement('div');b.className='hora';b.innerText=h;b.onclick=()=>{{document.querySelectorAll('.hora').forEach(x=>x.classList.remove('sel'));b.classList.add('sel');sel=h}};div.appendChild(b)}})
}}
async function agendar(){{
  if(!sel)return alert('Escolha horário');const nome=document.getElementById('nome').value;if(!nome)return alert('Digite nome');
  const serv=document.getElementById('servico').value;const data=dataInput.value;
  await fetch(`/agendar?data=${{data}}&horario=${{sel}}&nome=${{nome}}&servico=${{serv}}`);
  const nomeServ=document.getElementById('servico').options[document.getElementById('servico').selectedIndex].text;
  const msg=`Olá! Agendamento: ${{nome}} - ${{nomeServ}} em ${{data}} às ${{sel}}`;
  window.open(`https://wa.me/{WHATSAPP}?text=${{encodeURIComponent(msg)}}`,'_blank');carregar();
}}
document.getElementById('servico').addEventListener('change',carregar);dataInput.addEventListener('change',carregar);carregar();
</script></body></html>
"""

HTML_ADMIN = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Admin</title>
<style>body{font-family:Inter,Arial;background:#0f0f0f;color:#fff;padding:20px}.card{max-width:750px;margin:auto;background:#1a1a1a;padding:20px;border-radius:12px}</style>
</head><body><div class="card"><h2>Agenda - Barbeiro</h2>
<input type="password" id="senha" placeholder="Digite senha"><button onclick="check()">Entrar</button>
<div id="conteudo" style="display:none"><input id="filtroData" type="date"><div id="lista"></div></div>
</div>
<script>
let senhaOk='';
async function check(){const s=document.getElementById('senha').value;const r=await fetch('/admin-data?senha='+s);if(r.status==401){alert('Senha errada');return}senhaOk=s;document.getElementById('conteudo').style.display='block';load()}
async function load(){const res=await fetch('/admin-data?senha='+senhaOk);let dados=await res.json();const f=document.getElementById('filtroData').value;let html='';for(let data in dados){if(f && data!=f)continue;for(let hora in dados[data]){let a=dados[data][hora];html+=`<div style="padding:8px;border-bottom:1px solid #333">${data} ${hora} - ${a.nome} - ${a.servico} <button onclick="deletar('${data}','${hora}')">Cancelar</button></div>`}}document.getElementById('lista').innerHTML=html||'Vazio'}
async function deletar(data,horario){if(!confirm('Cancelar '+data+' '+horario+'?'))return;await fetch(`/admin-delete/${data}/${horario}?senha=`+senhaOk);load()}
document.getElementById('filtroData').addEventListener('change',load);setInterval(load,5000);
</script></body></html>
"""

@app.get("/admin", response_class=HTMLResponse)
def admin_page(): return HTML_ADMIN

@app.get("/admin-data")
def admin_data(senha: str = ""):
    if senha != SENHA_BARBEIRO: return HTMLResponse("Não autorizado", status_code=401)
    return carregar()

@app.get("/admin-delete/{data}/{horario}")
def admin_delete(data: str, horario: str, senha: str = ""):
    if senha != SENHA_BARBEIRO: return HTMLResponse("Não autorizado", status_code=401)
    dados=carregar()
    if data in dados and horario in dados[data]: del dados[data][horario]; salvar(dados)
    return {"ok": True}

@app.get("/", response_class=HTMLResponse)
def home(): return HTML_HOME

@app.get("/horarios-disponiveis")
def horarios(data: str, servico: str):
    dados=carregar(); ocupados=dados.get(data, {})
    todos=["08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30"]
    livres=[h for h in todos if h not in ocupados]
    return livres

@app.get("/agendar")
def agendar(data: str, horario: str, nome: str, servico: str):
    dados=carregar()
    if data not in dados: dados[data]={}
    dados[data][horario]={"nome": nome, "servico": servico, "data": data, "horario": horario}
    salvar(dados)
    return {"ok": True}
