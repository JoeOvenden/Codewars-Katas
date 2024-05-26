// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/csharp

using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static string DuplicateEncode(string word)
  {
    word = word.ToLower();
    
    string newString = "";
    foreach (char c in word) 
    {
      newString += (word.Count(x => x == c) == 1) ? "(" : ")";
    }
    
    return newString;
  }
}