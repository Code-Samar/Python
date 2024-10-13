ram_bank=100000
# ram's bank balance
ram_loan=500000
# ram taken loan from bank
lakshamn_bank=2000000
# lakshaman's bank balance
lakshman_loan=1000000
# lakshaman taken loan from bank
net_income=ram_bank+lakshamn_bank
# income of family
net_liability=ram_loan+lakshman_loan
# total loan on family
final_value=(net_income-net_liability)
# net income of family
print("so tht family has :",final_value)