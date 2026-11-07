<%@ page contentType="text/html;charset=UTF-8" %>
<html><head><title>Login - Beleza Pro</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body{background-image:url('https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=1600&q=80');background-size:cover;background-position:center;min-height:100vh;display:flex;align-items:center;justify-content:center}
body::before{content:'';position:fixed;inset:0;background:linear-gradient(135deg, rgba(255,183,197,.85), rgba(255,105,180,.65), rgba(180,80,150,.75));z-index:0}
.card{position:relative;z-index:1;border:none;border-radius:22px;padding:32px;width:100%;max-width:400px;box-shadow:0 20px 50px rgba(180,40,100,.4);background:rgba(255,255,255,.96)}
.logo{font-size:48px}
.btn-rosa{background:linear-gradient(135deg,#ff5e8a,#ff8fab);border:none;padding:12px;border-radius:12px;font-weight:bold;color:white}
.btn-rosa:hover{background:#ff5e8a;color:white}
input{border-radius:12px !important;padding:12px !important}
</style></head>
<body>
<div class="card text-center">
  <div class="logo">💄</div>
  <h3 class="fw-bold" style="color:#d63384">Beleza <span style="color:#ff8fab">Pro</span></h3>
  <p class="text-muted small">Estoque da sua loja de maquiagem</p>
  <form action="login" method="post" class="text-start mt-3">
    <label class="fw-bold small">Usuário</label>
    <input class="form-control mb-3" name="usuario" placeholder="Ex: admin" required>
    <label class="fw-bold small">Senha</label>
    <input class="form-control mb-3" type="password" name="senha" placeholder="••••" required>
    <button class="btn btn-rosa w-100">Entrar ✨</button>
  </form>
</div>
</body></html>