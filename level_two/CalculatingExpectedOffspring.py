
string = '18518 18420 19169 16804 18436 18435'
pairingNumbers = list(map(int, string.split()))
type_AA_AA, type_AA_Aa, type_AA_aa, type_Aa_Aa, type_Aa_aa, type_aa_aa = pairingNumbers

result = (type_AA_AA + type_AA_Aa + type_AA_aa + type_Aa_Aa*0.75 + type_Aa_aa*0.5 + type_aa_aa*0) * 2
print(result)