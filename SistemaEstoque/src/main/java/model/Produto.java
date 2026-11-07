package model;
public class Produto {
  private int id;
  private String nome;
  private String descricao;
  private String categoria;
  private double preco;
  private int quantidade;
  public int getId(){return id;} public void setId(int id){this.id=id;}
  public String getNome(){return nome;} public void setNome(String n){this.nome=n;}
  public String getDescricao(){return descricao;} public void setDescricao(String d){this.descricao=d;}
  public String getCategoria(){return categoria;} public void setCategoria(String c){this.categoria=c;}
  public double getPreco(){return preco;} public void setPreco(double p){this.preco=p;}
  public int getQuantidade(){return quantidade;} public void setQuantidade(int q){this.quantidade=q;}
}