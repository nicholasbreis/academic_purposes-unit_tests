from cart import Produto

def test_subtotal():
    assert Produto.subtotal(Produto("Caneta", 2,10)) == 20
    assert Produto.subtotal(Produto('Livros', 50,2)) == 100
    