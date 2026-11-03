from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime, time, timedelta
import json, os, urllib.parse

app = FastAPI()

DB_FILE = "agendamentos.json"
ZAP_BARBEIRO = "5561999999999"  # <<< TROCA PELO NUMERO DO BARBEIRO COM 55 NA FRENTE

SERVICOS = {
    "corte": {"nome": "Corte", "preco": 40, "duracao": 30},
    "barba": {"nome": "Barba", "preco": 30, "duracao": 30},
    "corte_barba": {"nome": "Corte + Barba", "preco": 60, "duracao": 60},
}

class Agendamento(BaseModel):
    nome: str
    whatsapp: str
    data: str
    horario: str
    servico: str

def load_db():
    if not os.path.exists(DB_FILE): return []
    try:
        with open(DB_FILE, "r") as f: return json.load(f)
    except: return []

def save_db(data):
    with open(DB_FILE, "w") as f: json.dump(data, f, indent=2, ensure_ascii=False)

def gerar_slots(data_str):
    slots=[]; d=datetime.strptime(data_str, "%Y-%m-%d").date()
    atual=datetime.combine(d, time(8,0)); fim=datetime.combine(d, time(18,0))
    while atual <= fim:
        slots.append(atual.strftime("%H:%M")); atual+=timedelta(minutes=30)
    return slots

@app.get("/horarios-disponiveis")
def horarios(data: str, servico: str="corte"):
    agendados=load_db()
    ocupados=[a["horario"] for a in agendados if a["data"]==data]
    livres=[s for s in gerar_slots(data) if s not in ocupados]
    return {"livres": livres}

@app.post("/agendar")
def agendar(dados: Agendamento):
    agendados=load_db()
    if dados.horario in [a["horario"] for a in agendados if a["data"]==dados.data]:
        return {"status":"erro","msg":"Horário já ocupado"}
    agendados.append(dados.dict()); save_db(agendados)
    texto=f"💈 NOVO AGENDAMENTO!\n\nCliente: {dados.nome}\nServiço: {SERVICOS[dados.servico]['nome']} - R${SERVICOS[dados.servico]['preco']}\nData: {dados.data} às {dados.horario}\nZap cliente: {dados.whatsapp}"
    link_zap=f"https://wa.me/{ZAP_BARBEIRO}?text={urllib.parse.quote(texto)}"
    return {"status":"ok","msg":f"✅ Agendado {dados.data} às {dados.horario}","zap_link":link_zap}

@app.get("/admin-data")
def admin_data(): return load_db()

@app.delete("/admin-delete/{data}/{horario}")
def delete_ag(data: str, horario: str):
    ag=load_db(); novo=[a for a in ag if not (a["data"]==data and a["horario"]==horario)]; save_db(novo); return {"status":"ok"}

@app.get("/admin", response_class=HTMLResponse)
def admin_page():
    return """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Painel Barbeiro</title>
<style>body{font-family:Inter,Arial;background:#0f0f0f;color:#fff;padding:20px}.card{max-width:750px;margin:auto;background:#1a1a1a;border-radius:16px;padding:24px}h1{margin:0}.ag{padding:14px;background:#232323;border-radius:12px;margin:10px 0;display:flex;justify-content:space-between;align-items:center}button{padding:10px 14px;border-radius:8px;border:0;font-weight:700;cursor:pointer}.btn-zap{background:#25D366}.btn-del{background:#ff4444;color:#fff;margin-left:6px}</style></head><body><div class="card"><h1>💈 Painel do Barbeiro</h1><p id="total" style="color:#aaa">Carregando...</p><div style="display:flex;gap:8px;margin:12px 0"><input type="date" id="filtroData" style="flex:1;padding:12px;border-radius:10px;background:#232323;color:#fff;border:1px solid #333"><button onclick="document.getElementById('filtroData').value='';load()" style="background:#333;color:#fff">Limpar</button></div><div id="lista"></div><button onclick="load()" style="width:100%;margin-top:20px;background:#fff">🔄 Atualizar</button></div>
<script>
async function load(){const res=await fetch('/admin-data');let dados=await res.json();const f=document.getElementById('filtroData').value;if(f)dados=dados.filter(a=>a.data==f);document.getElementById('total').innerText=dados.length+' agendamentos';const div=document.getElementById('lista');div.innerHTML='';dados.sort((a,b)=>(a.data+a.horario).localeCompare(b.data+b.horario));dados.reverse().forEach(a=>{const el=document.createElement('div');el.className='ag';el.innerHTML=`<div><b>${a.data} - ${a.horario}</b><br>${a.nome} - ${a.servico}<br><small style="color:#aaa">${a.whatsapp}</small></div><div><a target="_blank" href="https://wa.me/55${a.whatsapp.replace(/\\D/g,'')}"><button class="btn-zap">Zap</button></a><button class="btn-del" onclick="deletar('${a.data}','${a.horario}')">X</button></div>`;div.appendChild(el);});}
async function deletar(data,horario){if(!confirm('Cancelar '+data+' '+horario+'?'))return;await fetch(`/admin-delete/${data}/${horario}`,{method:'DELETE'});load();}
document.getElementById('filtroData').addEventListener('change',load);load();setInterval(load,5000);
</script></body></html>"""

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Barbearia - Agenda</title>
<style>body{font-family:Inter,Arial;background:#0f0f0f;color:#fff;margin:0;padding:20px}.card{max-width:480px;margin:auto;background:#1a1a1a;border-radius:16px;padding:24px}label{display:block;margin:12px 0 6px;color:#ccc;font-size:14px}input,select,button{width:100%;padding:14px;border-radius:12px;border:1px solid #333;font-size:16px;box-sizing:border-box}input,select{background:#232323;color:#fff}button{background:#fff;color:#000;font-weight:800;margin-top:18px;cursor:pointer}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}.slot{padding:12px;background:#232323;border-radius:10px;text-align:center;cursor:pointer;border:1px solid #333}.slot.ocupado{background:#151515;color:#444;pointer-events:none}.slot.selecionado{background:#fff;color:#000;font-weight:700}.msg{margin-top:16px;padding:14px;border-radius:12px;display:none}</style></head><body><div class="card"><h1>💈 Barbearia Elite</h1><div style="color:#aaa;margin:6px 0 20px">8h às 19h • Agende em 30 seg</div><label>Serviço</label><select id="servico"><option value="corte">Corte - R$40</option><option value="barba">Barba - R$30</option><option value="corte_barba">Corte + Barba - R$60</option></select><label>Data</label><input type="date" id="data"><label>Horário</label><div id="slots" class="grid"></div><label>Seu nome</label><input id="nome" placeholder="Ex: João"><label>Seu WhatsApp</label><input id="zap" placeholder="61999999999"><button onclick="agendar()">Confirmar agendamento</button><div id="msg" class="msg"></div><div style="margin-top:18px;text-align:center"><a href="/admin" style="color:#666;font-size:13px">Sou o barbeiro - ver agenda</a></div></div>
<script>
let sel=null;const dataInput=document.getElementById('data');dataInput.valueAsDate=new Date();
async function carregar(){const res=await fetch(`/horarios-disponiveis?data=${dataInput.value}&servico=${document.getElementById('servico').value}`);const json=await res.json();const div=document.getElementById('slots');div.innerHTML="";const todos=[];for(let h=8;h<=18;h++){todos.push(String(h).padStart(2,'0')+":00");todos.push(String(h).padStart(2,'0')+":30");}todos.forEach(t=>{const el=document.createElement('div');el.className='slot';el.textContent=t;if(!json.livres.includes(t))el.classList.add('ocupado');el.onclick=()=>{document.querySelectorAll('.slot').forEach(s=>s.classList.remove('selecionado'));el.classList.add('selecionado');sel=t;};div.appendChild(el);});}
async function agendar(){if(!sel)return alert("Escolha horário");const nome=document.getElementById('nome').value;const zap=document.getElementById('zap').value;if(!nome||!zap)return alert("Preencha nome e zap");const payload={nome:nome,whatsapp:zap,data:dataInput.value,horario:sel,servico:document.getElementById('servico').value};const res=await fetch('/agendar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});const json=await res.json();const msg=document.getElementById('msg');msg.style.display='block';msg.textContent=json.msg;if(json.status=='ok'){msg.style.background='#143d2a';if(json.zap_link){window.open(json.zap_link,'_blank');}carregar();}else{msg.style.background='#3d1414';}}
dataInput.addEventListener('change',carregar);document.getElementById('servico').addEventListener('change',carregar);carregar();
</script></body></html>"""
