package controller;
import java.io.IOException;
import java.util.List;
import dao.ProdutoDAO;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.Produto;
@WebServlet("/relatorio")
public class RelatorioServlet extends HttpServlet {
  @Override
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    List<Produto> lista = new ProdutoDAO().listar();
    req.setAttribute("lista", lista);
    req.getRequestDispatcher("relatorio.jsp").forward(req, resp);
  }
}