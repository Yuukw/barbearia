<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<html><head><title>Estoque - Beleza Pro</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body{background-image:url('https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=1600&q=80');background-size:cover;background-attachment:fixed;background-position:center;min-height:100vh}
body::before{content:'';position:fixed;inset:0;background:rgba(255,228,235,.92);z-index:0}
.container{position:relative;z-index:1}
.card{border:none;border-radius:18px;box-shadow:0 8px 25px rgba(214,51,132,.15)}
.card-top{border-left:6px solid #ff5e8a}
.btn-rosa{background:#ff5e8a;border:none;color:white;font-weight:bold;border-radius:10px}
.btn-rosa:hover{background:#e84393;color:white}
.btn-editar{background:#ffb6c9;border:none;color:#7a2048;font-weight:bold;border-radius:8px}
.badge-rosa{background:#ffe0ec;color:#d63384}
h2{color:#7a2048}
</style></head>
<body>
<div class="container py-4">
  <div class="d-flex justify-content-between align-items-center mb-4">
    <h2 class="fw-bold">💄 Beleza <span style="color:#ff5e8a">Pro</span> <small class="fs-6 text-muted">- Estoque de Maquiagem</small></h2>
    <div><a href="relatorio" class="btn btn-light shadow-sm">📄 Relatório</a> <a href="login.jsp" class="btn btn-danger">Sair</a></div>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-md-4"><div class="card card-top p-3 text-center"><small class="text-muted">💰 VALOR TOTAL</small><h3 class="fw-bold" style="color:#d63384"><fmt:formatNumber value="${valorTotal}" type="currency" currencySymbol="R$ "/></h3></div></div>
    <div class="col-md-4"><div class="card card-top p-3 text-center"><small class="text-muted">🧴 QUANTIDADE TOTAL</small><h3 class="fw-bold" style="color:#d63384">${quantidadeTotal} itens</h3></div></div>
    <div class="col-md-4"><div class="card card-top p-3 text-center"><small class="text-muted">✨ PRODUTOS</small><h3 class="fw-bold" style="color:#d63384">${lista.size()} cadastrados</h3></div></div>
  </div>

  <div class="card p-4 mb-4">
    <h5 class="fw-bold" style="color:#7a2048">➕ Cadastrar Maquiagem</h5>
    <form action="produtos" method="post" class="row g-2 mt-1">
      <div class="col-md-3"><input class="form-control" name="nome" placeholder="Ex: Batom Matte" required></div>
      <div class="col-md-3"><input class="form-control" name="descricao" placeholder="Ex: Vermelho - Ruby Woo"></div>
      <div class="col-md-2"><select class="form-select" name="categoria" required><option value="">Categoria...</option><option>Batom</option><option>Base</option><option>Sombra</option><option>Rímel</option><option>Blush</option><option>Iluminador</option><option>Pincéis</option><option>Skincare</option></select></div>
      <div class="col-md-2"><input class="form-control" type="number" step="0.01" name="preco" placeholder="Preço R$" required></div>
      <div class="col-md-1"><input class="form-control" type="number" name="quantidade" placeholder="Qtd" required></div>
      <div class="col-md-1"><button class="btn btn-rosa w-100">Cadastrar</button></div>
    </form>
  </div>

  <div class="card p-4">
    <table class="table table-hover align-middle">
      <thead><tr><th>ID</th><th>Produto</th><th>Descrição</th><th>Categoria</th><th>Preço</th><th>Qtd</th><th>Subtotal</th><th>Ações</th></tr></thead>
      <tbody>
      <c:forEach var="p" items="${lista}">
        <tr><td>${p.id}</td><td><b style="color:#7a2048">${p.nome}</b></td><td>${p.descricao}</td>
        <td><span class="badge badge-rosa">${p.categoria}</span></td>
        <td><fmt:formatNumber value="${p.preco}" type="currency" currencySymbol="R$ "/></td><td>${p.quantidade}</td>
        <td><b><fmt:formatNumber value="${p.preco * p.quantidade}" type="currency" currencySymbol="R$ "/></b></td>
        <td><a href="produtos?acao=editar&id=${p.id}" class="btn btn-sm btn-editar">✏️ Editar</a>
        <a href="produtos?acao=excluir&id=${p.id}" class="btn btn-sm btn-danger" onclick="return confirm('Excluir essa make?')">Excluir</a></td></tr>
      </c:forEach>
      </tbody>
    </table>
  </div>
</div>
</body></html>