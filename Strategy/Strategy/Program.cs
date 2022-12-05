using System;

namespace CalculadoraStrategy
{
    class Program
    {
        static void Main(string[] args)
        {
            Calcular calculadora = new Calcular();
            while(true)
            {
                Console.WriteLine("Informe o primeiro valor");
                double valor1 = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("Informe o segundo valor");
                double valor2 = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("-------------------------------");
                Console.WriteLine("1 - Somar");
                Console.WriteLine("2 - Subtrair");
                Console.WriteLine("3 - Dividir");
                Console.WriteLine("4 - Multiplicar");
                string opcao = Console.ReadLine();
                if(opcao=="1")
                {
                    calculadora.calcular = new Somar();
                    calculadora.CalcularOperacao(valor1, valor2);
                }
                if (opcao == "2")
                {
                    try
                    {
                        calculadora.calcular = new Subtrair();
                        calculadora.CalcularOperacao(valor1, valor2);
                    }
                    catch 
                    {
                        Console.WriteLine("Erro na operacao");
                    }
                }
                if(opcao=="3")
                {
                    try
                    {
                        calculadora.calcular = new Dividir();
                        calculadora.CalcularOperacao(valor1, valor2);
                    }
                    catch (Exception ex)
                    {

                        Console.WriteLine("Erro na operacao : " + ex.InnerException);
                    }
                }
                if (opcao == "4")
                {
                    calculadora.calcular = new Multiplicar();
                    calculadora.CalcularOperacao(valor1, valor2);
                }
            }
        }
    }

    public class Calcular
    {
        public Calculadora calcular { get; set; }

        public void CalcularOperacao(double v1, double v2)
        {
            Console.WriteLine(calcular.Operacao(v1,v2));
        }
    }


    public abstract class Calculadora
    {
        public abstract double Operacao(double n1,double n2);
    }


    public class Somar : Calculadora
    {
        public override double Operacao(double v1, double v2)
        {
            return v1 + v2;
        }
    }
    public class Subtrair : Calculadora
    {
        public override double Operacao(double v1, double v2)
        {
            if (v2 > v1)
                throw new InvalidOperationException();

            return v1 - v2;
        }
    }
    public class Multiplicar : Calculadora
    {
        public override double Operacao(double v1, double v2)
        {
            return v1 * v2;
        }
    }
    public class Dividir : Calculadora
    {
        public override double Operacao(double v1, double v2)
        {
            if (v2 == 0)
                throw new InvalidOperationException();

            return v1/v2;
        }
    }

}
