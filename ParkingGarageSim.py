import time



class ParkingGarage():
    
    '''
    This class is a core for a continually running program on a terminal.
    It has the ability to give tickets out to people who need them to park.
    It has the ability to pay for your ticket.
    It has the ability for you to leave the parking garage via the exit.
    '''
    
    ticket_num = 1
    current_tickets = {}
    
    def __init__(self,spaces=10,rate=10, occupied_spaces = 0):
        self.spaces = spaces
        self.rate = rate
        self.occupied_spaces = occupied_spaces
        self.driver_function()


    def driver_function(self):
        
        '''
        The init method in this class of parking garage.
        Serves the function of looping the main menu.
        Also directing people to the given method that they want to use.
        These method are the take ticket, pay for parking, and the leave garage method.
        '''
        
        while True:
            answer = input('\nWould you like to get a ticket, pay for a ticket, or leave the garage? [get/pay/leave] ').lower()
            if answer == 'get':
                self.take_ticket()
            elif answer == 'pay':
                self.pay_for_parking()
            elif answer == 'leave':
                self.leave_garage()
            else:
                print('\nPlease give a valid answer.')

    def take_ticket(self):
        
        '''
        This method gives the user a ticket number. 
        It also logs the ticket time and increments ticket num and occupied spaces.
        '''
        
        if self.occupied_spaces == self.spaces:
            print("\nLot is full, please Exit.")
            return
        self.current_tickets[self.ticket_num] = {'paid': False,
                                                'time-in' : time.time()}
        print(f"\nYou are ticket number {self.ticket_num} and your time in is {time.asctime(time.localtime(self.current_tickets[self.ticket_num]['time-in']))}.\n")
        self.ticket_num += 1
        self.occupied_spaces += 1


    def pay_for_parking(self):
        
        '''
        This method uses the get ticket method to get the user's ticket number.
        Then checks if the tickets already been paid or not.
        If not it goes through the payment processing with the user.
        Then returns to main menu.
        '''
        
        num = self.get_ticket_number()
        amount, time = self.calculate_fee(num)
        if self.current_tickets[num]['paid'] == True:
            print('\n You have already paid, please head to the exit.')
            return
        while True:
            try:
                paided = input(f"\nPlease pay {amount} for the {time} hours parking time. Enter payment method: [debit/credit/cash] ").lower()
                if paided in ['debit', 'credit', 'cash']:
                    self.current_tickets[num]['paid'] = True
                    break
                else:
                    raise ValueError()
            except:
                print('\nPlease evert a valid payment method.')


    def leave_garage(self):
        
        '''
        This method gets the users ticket number via the get ticket number method.
        Then it checks if the number's been paid or not.
        If it's been paid it lets the user leave.
        Otherwise it prompts them to pay for their parking via the pay for parking method.
        '''
        
        num = self.get_ticket_number()
        if self.current_tickets[num]['paid'] == True:
            print('\nThank you, have a nice day!')
            self.occupied_spaces -= 1
        else:
            print('\nLooks like you still need to pay for parking.')
            self.pay_for_parking()
            print('\nThank you, have a nice day!')
            self.occupied_spaces -= 1

    
    def get_ticket_number(self):
        
        '''
        This method prompts the user for their ticket number checks for validity.
        Then returns that to whatever method called this method.
        '''
        
        while True:
            customer_ticket = input('\nPlease enter your ticket number: ')
            try:
                num = int(customer_ticket)
                if num in self.current_tickets.keys():
                    return num
                else:
                    raise ValueError()
            except:
                print("\nPlease enter a valid ticket number!")
            break
    
    def calculate_fee(self, tic_num):
        
        '''
        This method takes in one argument ticket number.
        It then calculates the elapsed time that the car has been parked in the garage.
        Then it returns both the elapsed time and the elapsed time times the garage hourly rate.
        '''
        
        elapsed = time.time() - self.current_tickets[tic_num]['time-in']
        elapsed = elapsed/60/60
        return round(elapsed * self.rate, 2), round(elapsed,3)

terminal = ParkingGarage()