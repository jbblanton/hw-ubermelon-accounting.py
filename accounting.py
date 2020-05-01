
MELON_COST = 1.00

def cust_pay_log(txt_file):
  """ To pull logs and compare paid v. owed """

    
  the_file = open(txt_file)  #Here we access the txt file and prep the data
  
  for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    cust_num = words[0]
    cust_name = words[1]
    purchase = int(words[2]) * MELON_COST
    paid = float(words[3])

    if purchase != paid:   #Report filters only those who under or over paid
      print(f"{cust_name} paid ${paid:.2f},",
          f"expected ${purchase:.2f}"
          )
    
      if purchase > paid:
        print(f"{cust_name} under paid for their melons by ${purchase - paid:.2f}.")

      elif purchase < paid:
        print(f"{cust_name} has overpaid for their melons by ${paid - purchase:.2f}.")

  the_file.close()    

cust_pay_log("customer-orders.txt")