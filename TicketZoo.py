class ZooTicket():
    descount_ticket = 0.6 #global
    def __init__(self,num_ticket,price_ticket = 5):        
        assert num_ticket > 0, "Value should be > 0 and integer" 
        
        self.num_ticket =  num_ticket
        self.price_ticket = price_ticket
        self.num_ages = []
        self.ticket_free = []
        self.ticket_paid =[]
        self.count = 0
        
   # Store all ages in a list
    def CalculateAge(self):
        while self.count < self.num_ticket:
            age = int(input(f'Please enter the age of person {self.count+1}: \n'))
            self.num_ages.append(age)
            self.count+=1
            
    # Store ages in different lists in the range.
        for i in self.num_ages:
            if i <=3 or i >= 60 :
                self.ticket_free.append(i)
            else:
                self.ticket_paid.append(i)
                
    #Calculate the price for the tickets with descount.         
    def CalculatePrice(self):
        if len(self.ticket_paid)>=3:
            price = (len(self.ticket_paid)*self.price_ticket)-TicketZoo.descount_ticket*self.price_ticket
            print(f"\nGreat you have got a discount of {self.descount_ticket*10}%")
     
    #Calculate full price's ticket.
        else:
            price = len(self.ticket_paid)*self.price_ticket

        print("===================================")
        print('Ticket free: ',len(self.ticket_free))
        print('Ticket paid:',len(self.ticket_paid),'price:',price,'$')
        print("===================================")

    
num_ticket = int(input('Pls enter the number of ticket that you would like to buy: '))   
numTickets = ZooTicket(num_ticket)
numTickets.CalculateAge()
numTickets.CalculatePrice()
