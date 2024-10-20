def hamming_distance(str1, str2):
   # Check if the strings are of equal length
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
   
    # Calculate the Hamming distance
    distance = sum(el1 != el2 for el1, el2 in zip(str1, str2))
    return distance 
# Example usage
string1 = "karolin"
string2 = "kathrin"
print(f"Hamming distance: {hamming_distance(string1, string2)}")
