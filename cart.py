class Produto:
  def __init__(self, nome, preco, quantidade=1):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

  def subtotal(produto):
    return produto.preco * produto.quantidade

  def calcular_total(produtos):
    total = 0
    subtotal = 0

    for p in produtos:
      total += subtotal(p)

    if total > 100:
      total * 0.9

    return total

  def aplicar_cupom(total, cupom):
    if cupom == "DESC10":
      return total * 0.10
    elif cupom == "DESC20":
      return total * 0.20
    else:
      return total

  def frete(total):
    if total > 200:
      return 0
    return 20