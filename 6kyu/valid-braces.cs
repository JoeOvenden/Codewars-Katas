// https://www.codewars.com/kata/5277c8a221e209d3f6000b56

using System;
using System.Linq;
using System.Collections.Generic;

public class Brace {

    public static bool validBraces(String braces) {
      
      /*
      for each brace
        if brace is an opening brace 
          then put expected closing brace onto the stack

        else if brace is a closing brace
          if brace is the expected closing brace
            remove the closing brace from the stack
          else
            return false
            
      if the brace stack is not empty
        return false

      return true
      */
      
      Dictionary<char, char> braceDictionary = new Dictionary<char, char>
      {
        { '(' , ')' },
        { '[' , ']' },
        { '{' , '}' }
      };
      
      Stack<char> expectedBraceStack = new Stack<char>();
      
      foreach (char brace in braces)
      {
        
        // If brace is an opening brace, then push the respective closing brace onto the stack
        if (braceDictionary.ContainsKey(brace))
        {
          expectedBraceStack.Push(braceDictionary[brace]);
        }
        
        // Otherwise if the brace is a closing brace, then check that it is the correct brace
        else
        {
          // Check that the stack is non-empty and pop the next expected closing brace off of the stack
          // If it's not the right one then return false
          if (expectedBraceStack.Count == 0 || expectedBraceStack.Pop() != brace) {
            return false;
          }
        }
        
      }
      
      // If the expected brace stack is not empty then it means that there are braces that haven't been closed
      // and so the braces are invalid
      if (expectedBraceStack.Count != 0) {
        return false;
      }
      
      return true;
    }
}