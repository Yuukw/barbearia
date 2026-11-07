package dao;
import java.sql.Connection;
import java.sql.DriverManager;

public class Conexao {
  public static Connection conectar() {
    try {
      Class.forName("com.mysql.cj.jdbc.Driver");
      return DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/estoque_db?useSSL=false&serverTimezone=UTC",
        "root", "SUA_SENHA_AQUI"); // TROCA AQUI tua senha do MySQL
    } catch (Exception e) {
      e.printStackTrace();
      return null;
    }
  }
}