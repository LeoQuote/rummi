class card:
    BLUE = 'blue'
    RED = 'red'
    BLACK = 'black'
    ORANGE = 'orange'
    JOKER = 'jocker'
    COLOR_LIST = [BLUE,RED,BLACK,ORANGE,JOKER]
    NUMBER_LIST = list(range(13*8+2))
    def __init__(self,id):
        if id not in self.NUMBER_LIST :
            raise ValueError('number out of range, should be below 106')
        self.id = id
    
    @property
    def number(self):
        return self.id%13 + 1
    @property
    def color(self):
        if self.id in range(0,13*2):
            return self.BLUE
        if self.id in range(13*2, 13*4):
            return self.RED
        if self.id in range(13*4, 13*6):
            return self.BLACK
        if self.id in range(13*6, 13*8):
            return self.ORANGE
        else:
            return self.JOKER
    def __str__(self):
        return "{} {}".format(self.color,self.number)

class card_set:
    def __init__(card_list):
        self.length = len(card_list)
        self.card_list = card_list
        # 验证组合是否正确
        self.is_valid = False
        self.num_joker = 0
        if self.length > 2 :
            number_list = []
            color_list = []
            for card in card_list:
                if card.color = 'joker':
                    self.num_joker += 1
                    continue
                number_list += [card.number]
                color_list += [card.color]
            color_set = set(color_list)
            if len(color_set) == 1 and len(number_set) == len(number_list):
                if max(number_list) - min(number_list) < len(number_list) + self.num_joker:
                    self.is_valid = True
            if len(number_set) == 1 and len(color_set) == len(color_list):
                self.is_valid = True
