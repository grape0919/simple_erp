

class Member:

    MBR_ID = ""
    TALK = ""
    COIN = ""
    PURCHASE = ""
    DEPOSIT = ""
    SALE = ""
    WITHDRAW = ""
    RESERVE = ""
    TOTAL_PUR = ""
    TOTAL_SAL = ""
    REVENUE = ""
    RATING = ""
    WALLET = ""

    def toInsertSql(self):
        return f"insert into MBR_INFO(MBR_ID, TALK, COIN, PURCHASE, DEPOSIT, SALE, WITHDRAW, RESERVE, TOTAL_PUR, TOTAL_SAL, REVENUE, RATING, WALLET)\
             values('{self.MBR_ID}', '{self.TALK}', '{self.COIN}', '{self.PURCHASE}', '{self.DEPOSIT}', '{self.SALE}', '{self.WITHDRAW}', '{self.RESERVE}'\
                 , '{self.TOTAL_PUR}', '{self.TOTAL_SAL}', '{self.REVENUE}', '{self.RATING}', '{self.WALLET}');"

    def toUpdateSql(self):
        return f"update MBR_INFO set TALK = '{self.TALK}', COIN= '{self.COIN}', PURCHASE= '{self.PURCHASE}', DEPOSIT= '{self.DEPOSIT}', SALE= '{self.SALE}',\
             WITHDRAW= '{self.WITHDRAW}', RESERVE= '{self.RESERVE}', TOTAL_PUR= '{self.TOTAL_PUR}', TOTAL_SAL= '{self.TOTAL_SAL}', REVENUE= '{self.REVENUE}',\
                  RATING= '{self.RATING}', WALLET = '{self.WALLET}' where MBR_ID = '{self.MBR_ID}'"