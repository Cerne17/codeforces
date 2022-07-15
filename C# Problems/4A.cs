// int n = Convert.ToInt32(Console.ReadLine());
int n = int.Parse(Console.ReadLine());
int mod = n%2;
if (n == 2)
{
    Console.WriteLine("NO");
}
else if (mod==0)
{
    Console.WriteLine("YES");
} else {
    Console.WriteLine("NO");
}