
import copy

	

class PokerAI:

	STRING_TO_SUIT = {
		"s":0,
		"h":1,
		"d":2,
		"c":3
	}
	def __init__(self , hand=[], community=[]):
		self.hand=hand
		self.community=community
		self.bhand=tran_card_to_int(hand)
		self.bcommunity=tran_card_to_int(community)
		self.handarray=[0]*17
		self.communityarray=[0]*17
		self.handsuit=[0]*7
		self.csuit=[0]*7
		for card in hand:
			self.handarray[card[1]]=self.handarray[card[1]]+1
			self.handsuit[self.STRING_TO_SUIT[card[0]]]=self.handsuit[self.STRING_TO_SUIT[card[0]]]+1
		for card in community:
			self.communityarray[card[1]]=self.communityarray[card[1]]+1
			self.csuit[self.STRING_TO_SUIT[card[0]]]=self.csuit[self.STRING_TO_SUIT[card[0]]]+1
	def samesuit(self):
		ans=[self.csuit[i]+self.handsuit[i] for i in range(0,5)]
		for i in range(0,5):
			if self.csuit[i]==5:
				if(ans[i]==5):
					return 'no'
				else:
					return 'flush'
		for i in range(0,5):
			if ans[i]>=5:
				return 'flush'
		return 'no'

	def pair(self):
		num=0
		ans=[self.communityarray[i]+self.handarray[i] for i in range(0,15)]
		for i in range(0,15):
			if(ans[i]>=2):
				num=i
		if(self.hand[0][1]==self.hand[1][1]):
			if(self.bhand>self.bcommunity):
				return ('tpair',num)
			else:
				return ('pair',num)

		if((self.bhand&self.bcommunity)>self.bcommunity-(self.bhand&self.bcommunity)):
			return ('tpair',num)
		
		if(self.bhand&self.bcommunity!=0):
			return ('pair',num)
		else :
			return ('no',num)
		
	def twopair(self):
		tcommunity=copy.copy(self.communityarray)
		handpairnum=0;
		cpairnum=0
		for i in range(0,15):
			if tcommunity[i]==2:
				cpairnum=cpairnum+1
		
		ans=[tcommunity[i]+self.handarray[i] for i in range(0,15)]
		
		for i in range(0,15):
			if ans[i]>=2:
				handpairnum=handpairnum+1
				
		print ans
		print handpairnum
		print cpairnum
		if handpairnum<2:
			return 'no'
		if handpairnum>cpairnum:
			if self.bhand&self.bcommunity==self.bhand:
				return 'ttp'
			return 'tp'
		else:
			return 'no'
	def FullHouse(self):
		tcommunity=copy.copy(self.communityarray)
		pair=0
		three=0
		for i in range(0,15):
			if tcommunity[i]==2:
				pair=pair+1
			if tcommunity[i]==3:
				three=three+1
		if(pair&three):
			return 'no'
			
		ans=[tcommunity[i]+self.handarray[i] for i in range(0,15)]
		pair=0
		three=0
		for i in range(0,15):
			if ans[i]==2:
				pair=pair+1
			if ans[i]==3:
				three=three+1
		print ans
		print tcommunity
		print pair
		print three
		if(three>=1):
			if((pair+three)>=2):
				return 'hf'
		else:
			return 'no'
		return 'no'
	def three(self):
		tcommunity=copy.copy(self.communityarray)
		for i in range(0,15):
			if tcommunity[i]>=3:
				tcommunity[i]=0
		ans=[tcommunity[i]+self.handarray[i] for i in range(0,15)]
		if max(ans)==3:
			return 'toak'
		else:
			return 'no'
			
	def four(self):
		tcommunity=copy.copy(self.communityarray)
		for i in range(0,15):
			if tcommunity[i]>=4:
				tcommunity[i]=0
		ans=[tcommunity[i]+self.handarray[i] for i in range(0,15)]
		if max(ans)==4:
			return 'foak'
		else:
			return 'no'
	def straight(self):
		mark=31<<9
		mark2=30<<9
		for i in range(0,10):
			if((mark>>i)&(self.bhand|self.bcommunity)==(mark>>i)):
				if((mark2>>i)&(self.bhand)>=0):
					if((mark2>>i)&(self.bcommunity)!=(mark2>>i)):
						return 'straight'
					else:
						return 'no'
				else:
					return 'no'
		return 'no'
def tran_card_to_int(cardlist):
		ans=0
		for card in cardlist:
			ans=1<<(card[1]-1)|ans
		if((ans&1<<13)!=0):
			ans=ans+1
		return ans	

if __name__=='__main__':

	ai=PokerAI([('s',2),('h',11)],[('s',7),('s',11),('s',9),('s',8)])
	print ai.straight()
	

	