using System;

class Program
{
   
    static void Calcular(int a, int b, out int soma, out int produto)
    {
        soma = a + b;
        produto = a * b;
    }

    static void Main(string[] args)
    {
        int x = 5, y = 3;
        int s, p;

        // Chamando a função com variáveis out
        Calcular(x, y, out s, out p);

        Console.WriteLine($"x = {x}, y = {y}");
        Console.WriteLine($"Soma = {s}, Produto = {p}");
    }
}
