from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        def convertStringToNumber(string: str):
            output = ""
            if string == "":
                return "-1"
            for i in string:
                output += str(ord(i)) + "-2"
            return output

        if len(strs) == 0:
            return ""
        output = ""
        for word in strs:
            output += convertStringToNumber(word) + "-3"
        return output

    def decode(self, string: str) -> List[str]:
        def convertNumbersToString(string: str):
            output = ""
            if string == "-1":
                return ""
            result = string.removesuffix("-2").split("-2")
            for i in result:
                output += chr(int(i))
            return output

        if string == "":
            return []
        output = []
        arraystring = string.removesuffix("-3").split("-3")
        for i in arraystring:
            result = convertNumbersToString(i)
            output.append(result)
        return output


