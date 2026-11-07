<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<html><head><title>Relatório - Beleza Pro</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body{background:#fff0f5;font-family:'Segoe UI',Arial}
.header{background:linear-gradient(135deg,#ff5e8a,#ff8fab);color:white;border-radius:18px;padding:25px}
.card{border:none;border-radius:16px;box-shadow:0 8px 25px rgba(214,51,132,.12)}
@media print{ .no-print{display:none !important} }
</style></head>
<body>
<div class="container py-4">
  <div class="header d-flex justify-content-between align-items-center">
    <div><h3 class="fw-bold mb-0">💄 Relatório - Beleza Pro</h3><small>Loja de Maquiagem | Estoque Atual | Aluna: Mitchelle</small></div>
    <div class="no-print"><button onclick="window.print()" class="btn btn-light fw-bold">🖨️ Imprimir / Salvar PDF</button> <a href="produtos" class="btn btn-dark">← Voltar</a></div>
  </div>
  <div class="card p-4 mt-4">
    <table class="table">
      <thead><tr><th>Produto</th><th>Categoria</th><th>Preço</th><th>Qtd</th><th>Subtotal</th></tr></thead>
      <tbody><c:forEach var="p" items="${lista}"><tr><td><b>${p.nome}</b><br><small class="text-muted">${p.descricao}</small></td><td><span class="badge bg-light text-dark border">${p.categoria}</span></td><td><fmt:formatNumber value="${p.preco}" type="currency" currencySymbol="R$ "/></td><td>${p.quantidade}</td><td><fmt:formatNumber value="${p.preco * p.quantidade}" type="currency" currencySymbol="R$ "/></td></tr></c:forEach></tbody>
    </table>
    <div class="text-end mt-3"><h4>Valor Total: <span style="color:#d63384"><fmt:formatNumber value="${valorTotal}" type="currency" currencySymbol="R$ "/></span></h4><small class="text-muted">Total de itens: ${quantidadeTotal} | Produtos: ${lista.size()}</small></div>
  </div>
  <p class="text-center text-muted small mt-3">Relatório gerado pelo Sistema Beleza Pro - Mitchelle - Novembro/2026</p>
</div>
</body></html>