/* 1.1 1.2 1.3 zadanie */
/*
 Console.WriteLine("Podaj swoje imię:");
var name = Console.ReadLine();
int result = 5 + 9;

Console.WriteLine("Hello " + name);
Console.WriteLine(result);
*/
/*zad 1 */
/*
using System;


    class Program
    {
        static void Main(string[] args)
        {
            // Deklaracja zmiennych
            int number = 21;
            float money = 37.21f;
            string text = "JIPP";
            bool isLogged = true;
            char myChar = 'T';
            decimal price = 19.99m;

            // Wyświetlenie zmiennych w konsoli
            Console.WriteLine("number: " + number);
            Console.WriteLine("money: " + money);
            Console.WriteLine("text: " + text);
            Console.WriteLine("isLogged: " + isLogged);
            Console.WriteLine("myChar: " + myChar);
            Console.WriteLine("price: " + price);
        }
    }

*/
/* zad 2 */
/*
using System;


    class Program
    {
        static void Main(string[] args)
        {
            string myAge = "Age: ";
            int wifeAge = 18;
            string result = myAge + wifeAge;  
            Console.WriteLine(result);
        }
    }
*/
/* zad 3 */
/*
using System;

    class Program
    {
        static void Main(string[] args)
        {
            bool isTrue = true;
            bool isFalse = false;
            bool isReallyTrue = true;

            bool and = isTrue && isFalse;
            bool or = isTrue || isReallyTrue;
            bool negative = !isFalse;

            Console.WriteLine("and: " + and);
            Console.WriteLine("or: " + or);
            Console.WriteLine("negative: " + negative);
        }
    }

*/
/* zad 4 */
/*
using System;

int a = 5;
int b = 12;

int add = a + b;
int sub = a - b;
double div = (double)a / b;  
int mul = a * b;
int mod = a % b;

Console.WriteLine("add: " + add);
Console.WriteLine("sub: " + sub);
Console.WriteLine("div: " + div);
Console.WriteLine("mul: " + mul);
Console.WriteLine("mod: " + mod);
*/

/* zad 5 */
/*
using System;

string a = "Ala";
string b = "ma";
string c = "Kota";
String result = a + " " + b + " " + c;

Console.WriteLine(result);

*/

/* zad 1 */
/*
using System;

int n1 = 10;
int n2 = 20;

if (n1 > n2)
{
    Console.WriteLine("n1 > n2");
}
else if (n1 < n2)
{
    Console.WriteLine("n2 >  n1");
}
else
{
    Console.WriteLine("n1 = n2");
}
*/
/* zad 2 */
/*
using System;

for (int i = 0; i < 10; i++)
{
    Console.WriteLine("C#");
}

int c = 0;
while (c < 10)
{
    Console.WriteLine("C#");
    c++;
}
*/
/* zad 3 */
/*
using System;

int n = 10;

for (int i = 0; i <= n; i++)
{
    if (i % 2 == 0)
        Console.WriteLine($"{i} - Parzysta");
    else
        Console.WriteLine($"{i} - Nieparzysta");
}
*/

/* zad 4 */
/*
using System;

int n = 5;

for (int i = 1; i <= n; i++)
{
    for (int j = 1; j <= i; j++)
    {
        Console.Write("* ");
    }
    Console.WriteLine();
}
*/
/* zad 1 */
/*
string[] colors = { "niebieski", "zielony", "żółty", "czerwony" };

Console.WriteLine("Mój pierwszy kolor to: " + colors[0]);
Console.WriteLine("Mój ostatni kolor to: " + colors[colors.Length - 1]);
*/
/* zad 2 */
/*
using System;

int[] numbers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

for (int i = 0; i < numbers.Length; i++)
{
    Console.WriteLine("Liczba: " + numbers[i]);
}

foreach (int number in numbers)
{
    Console.WriteLine("Liczba: " + number);
}

int index = 0;
while (index < numbers.Length)
{
    Console.WriteLine("Liczba: " + numbers[index]);
    index++;
}
*/
/* zad 3 */
/*
using System;
using System.Collections.Generic;

List<string> fruits = new List<string>();
fruits.Add("Pomarańcza");
fruits.Add("Jabłko");
fruits.Add("Granat");
fruits.Add("Kiwi");

fruits.Remove("Kiwi");

Console.WriteLine(string.Join(", ", fruits)); 

fruits.Remove("Pomarańcza");

if (fruits.Count > 0)
{
    fruits.RemoveAt(fruits.Count - 1);
}

foreach (string fruit in fruits)
{
    Console.WriteLine(fruit);
}
*/