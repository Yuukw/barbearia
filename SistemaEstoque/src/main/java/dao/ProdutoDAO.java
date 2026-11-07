package dao;
import java.sql.*;
import java.util.*;
import model.Produto;

public class ProdutoDAO {
  // Padrão DAO - separa o SQL do Servlet
  public List<Produto> listar() {
    List<Produto> lista = new ArrayList<>();
    try (Connection con = Conexao.conectar();
         PreparedStatement ps = con.prepareStatement("SELECT * FROM produtos ORDER BY id");
         ResultSet rs = ps.executeQuery()) {
      while(rs.next()){
        Produto p = new Produto();
        p.setId(rs.getInt("id"));
        p.setNome(rs.getString("nome"));
        p.setDescricao(rs.getString("descricao"));
        p.setCategoria(rs.getString("categoria"));
        p.setPreco(rs.getDouble("preco"));
        p.setQuantidade(rs.getInt("quantidade"));
        lista.add(p);
      }
    } catch(Exception e){ e.printStackTrace(); }
    return lista;
  }

  public void inserir(Produto p){
    try (Connection con = Conexao.conectar();
         PreparedStatement ps = con.prepareStatement("INSERT INTO produtos(nome,descricao,quantidade,preco,categoria) VALUES(?,?,?,?,?)")){
      ps.setString(1,p.getNome()); ps.setString(2,p.getDescricao());
      ps.setInt(3,p.getQuantidade()); ps.setDouble(4,p.getPreco()); ps.setString(5,p.getCategoria());
      ps.executeUpdate();
    } catch(Exception e){ e.printStackTrace(); }
  }

  public Produto buscarPorId(int id){
    try (Connection con = Conexao.conectar();
         PreparedStatement ps = con.prepareStatement("SELECT * FROM produtos WHERE id=?")){
      ps.setInt(1,id); ResultSet rs = ps.executeQuery();
      if(rs.next()){
        Produto p = new Produto();
        p.setId(rs.getInt("id")); p.setNome(rs.getString("nome"));
        p.setDescricao(rs.getString("descricao")); p.setCategoria(rs.getString("categoria"));
        p.setPreco(rs.getDouble("preco")); p.setQuantidade(rs.getInt("quantidade"));
        return p;
      }
    } catch(Exception e){ e.printStackTrace(); }
    return null;
  }

  public void atualizar(Produto p){
    try (Connection con = Conexao.conectar();
         PreparedStatement ps = con.prepareStatement("UPDATE produtos SET nome=?,descricao=?,quantidade=?,preco=?,categoria=? WHERE id=?")){
      ps.setString(1,p.getNome()); ps.setString(2,p.getDescricao());
      ps.setInt(3,p.getQuantidade()); ps.setDouble(4,p.getPreco());
      ps.setString(5,p.getCategoria()); ps.setInt(6,p.getId());
      ps.executeUpdate();
    } catch(Exception e){ e.printStackTrace(); }
  }

  public void excluir(int id){
    try (Connection con = Conexao.conectar();
         PreparedStatement ps = con.prepareStatement("DELETE FROM produtos WHERE id=?")){
      ps.setInt(1,id); ps.executeUpdate();
    } catch(Exception e){ e.printStackTrace(); }
  }

  public boolean validarLogin(String usuario, String senha){
    try (Connection con = Conexao.conectar();
         PreparedStatement ps = con.prepareStatement("SELECT * FROM usuarios WHERE usuario=? AND senha=?")){
      ps.setString(1,usuario); ps.setString(2,senha);
      return ps.executeQuery().next();
    } catch(Exception e){ e.printStackTrace(); return false; }
  }
}