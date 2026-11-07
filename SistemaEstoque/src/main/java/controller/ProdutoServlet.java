package controller;
import java.io.IOException;
import java.util.List;
import dao.ProdutoDAO;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import model.Produto;

@WebServlet("/produtos")
public class ProdutoServlet extends HttpServlet {
  private ProdutoDAO dao = new ProdutoDAO();
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    String acao = req.getParameter("acao");
    if("excluir".equals(acao)){ dao.excluir(Integer.parseInt(req.getParameter("id"))); resp.sendRedirect("produtos"); return; }
    if("editar".equals(acao)){
      req.setAttribute("p", dao.buscarPorId(Integer.parseInt(req.getParameter("id"))));
      req.getRequestDispatcher("editar.jsp").forward(req, resp); return;
    }
    List<Produto> lista = dao.listar();
    double valorTotal=0; int qtdTotal=0;
    for(Produto p: lista){ valorTotal+=p.getPreco()*p.getQuantidade(); qtdTotal+=p.getQuantidade(); }
    req.setAttribute("lista", lista);
    req.setAttribute("valorTotal", valorTotal);
    req.setAttribute("quantidadeTotal", qtdTotal);
    req.getRequestDispatcher("produtos.jsp").forward(req, resp);
  }
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    Produto p = new Produto();
    p.setNome(req.getParameter("nome"));
    p.setDescricao(req.getParameter("descricao"));
    p.setCategoria(req.getParameter("categoria"));
    p.setPreco(Double.parseDouble(req.getParameter("preco")));
    p.setQuantidade(Integer.parseInt(req.getParameter("quantidade")));
    if("atualizar".equals(req.getParameter("acao"))){
      p.setId(Integer.parseInt(req.getParameter("id"))); dao.atualizar(p);
    } else { dao.inserir(p); }
    resp.sendRedirect("produtos");
  }
}