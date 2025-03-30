using Library.Domain;
using Library.Persistence;

namespace Library.ConsoleApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Book book = new Book("Wiedźmin", "Andrzej Sapkowski", 1993, "123-456-789", 10, 49.99m);
            BooksRepository repository = new BooksRepository();

            Console.WriteLine("Obiekty zostały utworzone poprawnie!");
            Console.ReadKey();
        }
    }
}
