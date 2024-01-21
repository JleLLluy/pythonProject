def to_find_int_for_charachteristicks(self, charachteristick, person):
    if charachteristick == 'СИЛ':
        if person == 'p':
            return self.strength_p.text()
        elif person == 'n':
            return self.strength_n.text()
    elif charachteristick == 'ЛОВ':
        if person == 'p':
            return self.durability_p.text()
        elif person == 'n':
            return self.durability_n.text()
    elif charachteristick == 'ТЕЛ':
        if person == 'p':
            return self.vitality_p.text()
        elif person == 'n':
            return self.vitality_n.text()
    elif charachteristick == 'МУД':
        if person == 'p':
            return self.wisdom_p.text()
        elif person == 'n':
            return self.wisdom_n.text()
    elif charachteristick == 'ИНТ':
        if person == 'p':
            return self.intelligence_p.text()
        elif person == 'n':
            return self.intelligence_n.text()
    elif charachteristick == 'ХАР':
        if person == 'p':
            return self.charizma_p.text()
        elif person == 'n':
            return self.charizma_n.text()