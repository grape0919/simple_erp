

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
             values('{str(self.MBR_ID).strip()}', '{str(self.TALK).strip()}', '{str(self.COIN).strip()}', '{str(self.PURCHASE).strip()}', '{str(self.DEPOSIT).strip()}', '{str(self.SALE).strip()}', '{str(self.WITHDRAW).strip()}', '{str(self.RESERVE).strip()}'\
                 , '{str(self.TOTAL_PUR).strip()}', '{str(self.TOTAL_SAL).strip()}', '{str(self.REVENUE).strip()}', '{str(self.RATING).strip()}', '{str(self.WALLET).strip()}');"

    def toUpdateSql(self):
        return f"update MBR_INFO set TALK = '{str(self.TALK).strip()}', COIN= '{str(self.COIN).strip()}', PURCHASE= '{str(self.PURCHASE).strip()}', DEPOSIT= '{str(self.DEPOSIT).strip()}', SALE= '{str(self.SALE).strip()}',\
             WITHDRAW= '{str(self.WITHDRAW).strip()}', RESERVE= '{str(self.RESERVE).strip()}', TOTAL_PUR= '{str(self.TOTAL_PUR).strip()}', TOTAL_SAL= '{str(self.TOTAL_SAL).strip()}', REVENUE= '{str(self.REVENUE).strip()}',\
                  RATING= '{str(self.RATING).strip()}', WALLET = '{str(self.WALLET).strip()}' where MBR_ID = '{str(self.MBR_ID).strip()}'"