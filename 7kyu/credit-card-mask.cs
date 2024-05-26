// https://www.codewars.com/kata/5412509bd436bd33920011bc/train/csharp

public static class Kata
{
  // return masked string
  public static string Maskify(string cc)
  {
    if (cc.Length <= 4) 
    {
      return cc;
    }
    return new string('#', cc.Length - 4) + cc.Substring(cc.Length - 4, 4);
  }
}
