import pandas as pd
from text import *

class Person:
    def __init__(self, id=None, in_line=None, phone=None, position=None, carrier=None):

        self.id = id
        self.in_line = in_line
        self.phone = phone
        self.position = position
        self.carrier = carrier

        self.df = pd.read_csv("C:/Users/willi/OneDrive/Desktop/In_Line/api/line.csv", header=0)
        self.df.set_index('id', inplace=True)

    # This function ensures that any data that the database has is populated into the class and vice versa
    def link_to_database(self):

        # If no id, generates one
        if self.id is None:
            if self.df.index.empty:
                self.id = 0
            else:
                self.id = int(self.df.index[-1]) + 1
            
        else:
            # If we don't know if the class is in line
            if self.in_line is None:
                if not pd.isna(self.df['in_line'].loc[self.id]):
                    if self.df['in_line'].loc[self.id] == "True":
                        self.in_line = True
                    elif self.df['in_line'].loc[self.id] == "False":
                        self.in_line = False

            # If no phone number looks for one in database
            if self.phone is None:
                if not pd.isna(self.df['phone'].loc[self.id]):
                    self.phone = str(self.df['phone'].loc[self.id])
            
            # If no carrier in class looks for one in database
            if self.carrier is None:
                if not pd.isna(self.df['carrier'].loc[self.id]):
                    self.carrier = str(self.df['carrier'].loc[self.id])

        # Updates the csv with info from the database
        self.df.loc[self.id] = {'id': self.id, 'in_line': self.in_line, 'phone': self.phone, 'carrier': self.carrier}
        self.df.to_csv("C:/Users/willi/OneDrive/Desktop/In_Line/api/line.csv", index=True)

    def add_to_line(self):
        self.in_line = True
        self.link_to_database()

    def remove_from_line(self):
        self.in_line = False
        self.link_to_database()

    def calculate_place(self):
        pos = -1
        for value in self.df['in_line']:
            pos += 1
            if value:
                self.position = self.id - pos
                return self.position + 1
                break

    def send_text(self):
        # Checks if person has a phone number and carrier in the database
        if self.carrier is not None and self.phone is not None:
            if self.carrier == "att":
                recipient = str(self.phone) + "@mms.att.net"
            elif self.carrier == "verizon":
                recipient = str(self.phone) + "@vzwpix.com"
            elif self.carrier == "t-mobile":
                recipient = str(self.phone) + "@tmomail.net"
            else:
                raise ValueError(f"An unsupported carrier was somehow submitted for user {str(self.id)}")
            send_mail(recipient)

        else:
            raise ValueError(f"No phone carrier or number was found for user {str(self.id)}")