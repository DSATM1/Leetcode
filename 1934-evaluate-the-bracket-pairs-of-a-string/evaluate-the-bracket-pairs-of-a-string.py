class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert the knowledge list into a hash map (dictionary) for O(1) lookups
        knowledge_dict = {k: v for k, v in knowledge}
        
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                # Start tracking the key inside the brackets
                in_bracket = True
            elif char == ')':
                # Reached the end of the key, evaluate it
                in_bracket = False
                key = "".join(current_key)
                
                # Append the value if found, otherwise append "?"
                result.append(knowledge_dict.get(key, "?"))
                
                # Reset current_key for the next bracket pair
                current_key = []
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)