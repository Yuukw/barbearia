<%@ page contentType="text/html;charset=UTF-8" %>
<html><head><title>Editar - Beleza Pro</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body{background-image:url('https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=1600&q=80');background-size:cover;background-position:center;min-height:100vh;display:flex;align-items:center;justify-content:center}
body::before{content:'';position:fixed;inset:0;background:rgba(255,228,235,.92);z-index:0}
.card{position:relative;z-index:1;border:none;border-radius:22px;padding:30px;width:100%;max-width:480px;box-shadow:0 20px 40px rgba(214,51,132,.25)}
.btn-rosa{background:#ff5e8a;border:none;color:white;font-weight:bold;padding:12px;border-radius:12px}
</style></head>
<body>
<div class="card">
  <h4 class="fw-bold" style="color:#7a2048">✏️ Editar <span style="color:#ff5e8a">Maquiagem</span></h4>
  <form action="produtos" method="post">
    <input type="hidden" name="acao" value="atualizar">
    <input type="hidden" name="id" value="${p.id}">
    <label class="fw-bold small mt-3">Nome</label><input class="form-control" name="nome" value="${p.nome}" required>
    <label class="fw-bold small mt-2">Descrição</label><input class="form-control" name="descricao" value="${p.descricao}">
    <label class="fw-bold small mt-2">Categoria</label><input class="form-control" name="categoria" value="${p.categoria}" required>
    <label class="fw-bold small mt-2">Preço</label><input class="form-control" type="number" step="0.01" name="preco" value="${p.preco}" required>
    <label class="fw-bold small mt-2">Quantidade</label><input class="form-control" type="number" name="quantidade" value="${p.quantidade}" required>
    <div class="d-flex gap-2 mt-4"><button class="btn btn-rosa flex-fill">Salvar Alterações 💖</button><a href="produtos" class="btn btn-secondary flex-fill">Cancelar</a></div>
  </form>
</div>
</body></html>