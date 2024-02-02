class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = lookup.get(s[0])
        for i in range(1,len(s)):
            if lookup.get(s[i-1]) < lookup.get(s[i]):
                result += lookup.get(s[i]) - lookup.get(s[i-1]) * 2
            else:
                result += lookup.get(s[i]) 
        
        return result
    
def test_rti():
    s = Solution()

    tc = [
            {
                "input": "I",
                "want": 1
            },
            {
                "input": "II",
                "want": 2
            },
            {
                "input": "III",
                "want": 3
            },
            {
                "input": "IV",
                "want": 4
            },
            {
                "input": "LVIII",
                "want": 58
            },
            {
                "input": "MCMXCIV",
                "want": 1994
            }



    ]
    
    for item in tc:
        assert s.romanToInt(item.get("input")) == item.get("want")
    

