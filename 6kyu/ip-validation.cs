// https://www.codewars.com/kata/515decfd9dcfc23bb6000006/solutions/csharp

using System;

namespace Solution
{
    class Kata
    {
        public static bool IsValidIp(string ipAddres)
        {          
            // Split IP address into sections and make sure that there are 4 sections
            string[] sections = ipAddres.Split(".");
            if (sections.Length != 4) 
            {
                return false;
            }
          
            foreach (string section in sections)
            {
                // Check for empty sections
                if (section.Length == 0)
                {
                    return false;
                }
              
                // Check that the section is made up entirely of digits
                foreach (char c in section) 
                {
                    if (!char.IsDigit(c))
                    {
                        return false;
                    }
                }
              
                // Check that there are no leading zeros
                if (section.StartsWith('0') && section.Length > 1)
                {
                    return false;
                }

                // If one of the sections is outside of the accepted range it is invalid
                int number = int.Parse(section);
                if (number < 0 || number > 255)
                {
                    return false;
                }
            }
            
            Console.WriteLine(string.Join(".", sections));
            return true;
        }
    }
}