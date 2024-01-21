import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
import sqlite3
import random


def integeration(need_to_transform):
    need_to_return = ''.join(c for c in str(need_to_transform) if c.isdigit())
    if need_to_return == '':
        return 10
    if int(need_to_return) >= 40:
        return 40
    return int(need_to_return)


def linetransformer_for_weapons(line):
    need_to_return = "".join(c for c in line if c.isalpha())
    if need_to_return == '':
        return 'Кулак'
    else:
        return need_to_return.capitalize()


def linetransformer_for_charachteristichs(line):
    spisok = ['СИЛ', "ЛОВ", "ТЕЛ", "МУД", "ИНТ", "ХАР"]
    need_to_return = "".join(c for c in line if c.isalpha())
    if need_to_return == '' or need_to_return not in spisok:
        return 'СИЛ'
    else:
        return need_to_return.upper()


def roll_dices_for_damage(dice):
    return random.randint(1, dice + 1)


def roll_dices_for_hit():
    return random.randint(1, 21)


def mod_of_level(level):
    level = integeration(level) // 5 + 2
    return level


def mod_of_ch(ch):
    return (ch - 10) // 2


class Dnd(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('helper_for_DnD.ui', self)
        self.info_btn.clicked.connect(self.need_information)
        self.attack_btn.clicked.connect(self.attack)
        self.char_check_within_charachters_btn.clicked.connect(self.char_check_within_charachters_func)
        self.ch_check_btn.clicked.connect(self.ch_check_func)
        self.spell_casting_btn.clicked.connect(self.spell_casting)

    def to_find_int_for_charachteristicks(self, charachteristick, person='p'):
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

    def need_information(self):
        name, ok_pressed = QInputDialog.getText(self, "Увеличь окно",
                                                "Основы игры в DnD: Программа написана так, "
                                                "что в принципе не может крашнуться, поэтому делай что хочешь ;)")
        if ok_pressed:
            pass

    def set_result(self, result, result_for_big_button=None):
        self.big_result_btn.setText(result_for_big_button)
        self.result_btn_5.setText(self.result_btn_4.text())
        self.result_btn_4.setText(self.result_btn_3.text())
        self.result_btn_3.setText(self.result_btn_2.text())
        self.result_btn_2.setText(self.result_btn_1.text())
        self.result_btn_1.setText(result)

    def healing_spell(self, healing_cube, effect, spell_modificator, spell):
        res = roll_dices_for_damage(healing_cube) + spell_modificator
        self.set_result(f'Восстановлено {res} хп, {effect}!',
                        f'Заклинанием {spell} восстановлено {res} очков здоровья, наложен эффект {effect}!')

    def attack_spell(self, damage_cube, effect, spell_modificator, armor_of_enemy, spell):
        res = roll_dices_for_damage(damage_cube) + spell_modificator
        if roll_dices_for_hit() + spell_modificator >= armor_of_enemy:
            self.set_result(f'Нанесено {res}, {effect}',
                            f'Заклинанием {spell} нанесено {res} урона, наложен эффект {effect}!')
        else:
            self.set_result(f'Враг увернулся!', f'Заклинание {spell} промахнулось мимо цели!')

    def savethrowing_spell(self, damage_cube, spell_modicator, level_modificator, effect, savethrowing_for_enemy,
                           spell):
        res = roll_dices_for_damage(damage_cube) + spell_modicator
        if 10 + spell_modicator + level_modificator > roll_dices_for_hit()\
                + mod_of_level(integeration(self.level_n.text()))\
                + mod_of_ch(integeration(self.to_find_int_for_charachteristicks(savethrowing_for_enemy, 'n'))):
            self.set_result(f'Нанесено {res}, {effect}',
                            f'Заклинанием {spell} нанесено {res} урона, противник {effect}!')
        else:
            self.set_result(f'Промах!', f'Заклинание {spell} не оказало эффекта!')

    def attack(self):
        mod_ch = 0
        level = self.level_p.text()
        weap = self.weapons_btn.currentText()
        armo = integeration(self.armor.text())
        con = sqlite3.connect("db_for_attack")
        cur = con.cursor()
        result_of = cur.execute("""SELECT * FROM for_attack WHERE weapon = ?""", (weap,)).fetchone()
        dice = result_of[2]
        modif = result_of[1]
        con.close()
        if modif == 'ЛОВ':
            mod_ch = mod_of_ch(integeration(self.durability_p.text()))
        elif modif == 'СИЛ':
            mod_ch = mod_of_ch(integeration(self.durability_p.text()))
        if roll_dices_for_hit() + mod_of_level(level) + mod_ch >= int(armo):
            res = roll_dices_for_damage(dice) + mod_ch
            self.set_result(f'Попадание {weap}: {res} урона',
                            f'Удар оружием:{weap} попадает по цели и наносит {res} урона!')
        else:
            self.set_result(f'Неудача', f"Оружие промахивается мимо цели!")

    def char_check_within_charachters_func(self):
        name_of_modificator_of_player = linetransformer_for_charachteristichs(self.checked_characktiristik.text())
        name_of_modificator_of_opponent = linetransformer_for_charachteristichs(self.checking_characktiristik.text())
        modificator_of_opponent = integeration(self.to_find_int_for_charachteristicks(name_of_modificator_of_opponent,
                                                                                      'n'))
        modificator_of_player = integeration(self.to_find_int_for_charachteristicks(name_of_modificator_of_player, 'p'))
        if roll_dices_for_hit() + modificator_of_player >= roll_dices_for_hit() + modificator_of_opponent:
            self.set_result(f'Успех проверки!')
        else:
            self.set_result(f'Провал проверки!')

    def ch_check_func(self):
        num_of_checking_charachteristick = integeration(self.num_of_checking.text())
        name_of_checked_charachteristick = linetransformer_for_charachteristichs(self.checked_charach_ofcheck.text())
        num_of_checked_charachteristick = integeration(self.to_find_int_for_charachteristicks(
            name_of_checked_charachteristick))
        if roll_dices_for_hit() + num_of_checked_charachteristick >= roll_dices_for_hit() + \
                num_of_checking_charachteristick:
            self.set_result(f'Успех проверки!')
        else:
            self.set_result(f'Провал проверки!')

    def spell_casting(self):
        spellcaster_class = self.spellcaster_btn.currentText()
        spell = self.spell_btn.currentText()
        con = sqlite3.connect("db_for_attack")
        cur = con.cursor()
        about_spell = cur.execute("""SELECT * FROM for_spellcaster WHERE name_of_caster = ?""",
                                  (spellcaster_class,)).fetchone()
        information_about_spell = cur.execute("""SELECT * FROM for_spells WHERE name_of_spell = ?""",
                                              (spell,)).fetchone()
        con.close()
        caster_modificator = mod_of_ch(integeration(self.to_find_int_for_charachteristicks(about_spell[1])))

        level_of_spell = information_about_spell[1]
        type_of_spell = information_about_spell[2]
        impact_of_spell = information_about_spell[3]
        status_effect_of_spell = information_about_spell[4]
        save_throw_for_enemy = information_about_spell[5]
        if (spellcaster_class == 'Изобретатель' or spellcaster_class == 'Паладин' or spellcaster_class == 'Следопыт') \
                and level_of_spell > 5:
            self.set_result(f'{status_effect_of_spell}у не хватает сил на {spell}',
                            f'Паладину не хватает магических возможностей на использование заклинания {spell}')
        else:
            if type_of_spell == 'healing':
                self.healing_spell(impact_of_spell, status_effect_of_spell, caster_modificator, spell)
            elif type_of_spell == 'attacking':
                self.attack_spell(impact_of_spell, status_effect_of_spell, caster_modificator,
                                  integeration(self.armor.text()), spell)
            elif type_of_spell == 'savethrowing':
                self.savethrowing_spell(impact_of_spell, caster_modificator,
                                        mod_of_ch(integeration(self.level_p.text())), status_effect_of_spell,
                                        save_throw_for_enemy, spell)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dnd()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
