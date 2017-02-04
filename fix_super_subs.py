import os
import codecs
import re
from collections import OrderedDict


def master_roshi(episode_num, roshi_count):
    episode = int(episode_num)
    if episode == 3:
        return 'Turtle Hermit-{\\i1}sama{\\i0}'
    elif episode == 16:
        return 'Muten Roshi-{\\i1}sama{\\i0}'
    elif episode == 20:
        return 'Muten Roshi-{\\i1}sama{\\i0}'
    elif episode == 22:
        return 'Turtle Hermit-{\\i1}sama{\\i0}'
    elif episode == 47:
        return 'Old Man Turtle Hermit'
    elif episode == 49:
        return 'Muten Roshi-{\\i1}sama{\\i0}'
    elif episode == 62:
        if roshi_count == 0:
            return 'Muten Roshi and co.'
        elif roshi_count == 1:
            return 'Muten Roshi-{\\i1}sama{\\i0}'
        elif roshi_count == 2:
            return 'Old Man Turtle Hermit'
        elif roshi_count == 3:
            return 'Old-Timer'
    if episode == 63:
        if roshi_count == 0:
            return 'the Turtle Hermit'
        elif roshi_count == 1:
            return 'Old-Timer'
    if episode == 68:
        return 'Old Man Turtle Hermit'
    if episode == 75:
        if roshi_count % 2 == 0:
            return 'Muten Roshi-{\\i1}sama{\\i0}'
        elif roshi_count in [1, 5]:
            return 'Old Man Turtle Hermit'
        elif roshi_count == 3:
            return 'Old-Timer'
        elif roshi_count == 5:
            return 'Old Man Turtle Hermit'
        elif roshi_count == 7:
            return 'the Old-Timer'
    if episode == 76:
        if roshi_count == 0:
            return 'the Turtle Hermit'
        elif roshi_count in [1, 5]:
            return 'the Old-Timer'
        elif roshi_count in [2, 3, 4, 6]:
            return 'Muten Roshi-{\\i1}sama{\\i0}'
        elif roshi_count == 7:
            return 'Old-Timer'


def fix_line(dialog, episode, roshi_count):
    # also replaces Chozetsu Dynamic English version lyrics
    #  with translation of Japanese lyrics
    replacements = OrderedDict([
        ('{\\i1}Don\'t you wanna dream again?{\\i0}',
            '{\\i1}Let\'s pick back up{\\i0}'),
        ('{\\i1}Now it\'s calling for me\\NGo back to the start{\\i0}',
            '{\\i1}The dream that never ended{\\i0}'),
        ('{\\i1}Wishing on the starlight{\\i0}',
            '{\\i1}Just join up the stars{\\i0}'),
        ('{\\i1}In the sky,\\Nlet\'s paint a door for tomorrow{\\i0}',
            '{\\i1}Drawing a door up in the sky{\\i0}'),
        ('{\\i1}Just step on the new stage\\NDon\'t be shy{\\i0}',
            '{\\i1}This is a brand new stage{\\i0}'),
        ('{\\i1}Gonna take the challenge of god{\\i0}',
            '{\\i1}For challenging the Gods!{\\i0}'),
        (u'{\\i1}Kyo Let\'s☆Mo Let\'s☆Dynamic!{\\i0}',
            '{\\i1}Fierce, intense, dynamic!{\\i0}'),
        ('{\\i1}Let\'s! Go! Go! Big panic!{\\i0}',
            '{\\i1}Let\'s! Go! Go! Cause a big panic!{\\i0}'),
        ('{\\i1}I don\'t care bout limits, no regret{\\i0}',
            '{\\i1}Losing will just make you stronger{\\i0}'),
        ('{\\i1}Make me tougher even though I lose{\\i0}',
            '{\\i1}Being called foolhardy just means...{\\i0}'),
        ('{\\i1}Nothing\' gonna stop me no mo\'\\NTry me{\\i0}',
            '{\\i1}Regrets and limits won\'t ever stop you!{\\i0}'),
        (u'{\\i1}So Zet\'s☆Cho Zet\'s☆Dynamic!{\\i0}',
            '{\\i1}Superb, sublime, dynamic!{\\i0}'),
        ('{\\i1}Let\'s Go! Yes! Give a kick!{\\i0}',
            '{\\i1}Let\'s Go! Yes! Show me your kicks!{\\i0}'),
        ('{\\i1}Keep on going\\NPower pumpin\' up{\\i0}',
            '{\\i1}Make us shake with excitement!{\\i0}'),
        ('{\\i1}Something greater waiting not so far away{\\i0}',
            '{\\i1}You\'ve got a super tale to tell!{\\i0}'),
        ('Frieza', 'Freeza'),
        ('FRIEZA', 'FREEZA'),
        ('Krillin', 'Kuririn'),
        ('KRILLIN', 'KURIRIN'),
        ('King Kai Fist', 'Kaio-ken'),
        ('King Kai', 'Kaio'),
        ('KING KAI', 'KAIO'),
        ('Supreme Kai', 'Kaioshin'),
        ('SUPREME KAI', 'KAIOSHIN'),
        ('Master Roshi {\\i1}sama{\\i0}', master_roshi(episode, roshi_count)),
        ('Master Roshi sama', master_roshi(episode, roshi_count)),
        ('Master Roshi', master_roshi(episode, roshi_count)),
        ('Shenron', 'Shen Long'),
        ('SHENRON', 'SHEN LONG'),
        ('Flying Nimbus', 'Kinto Un'),
        ('Tien', 'Tenshinhan'),
        ('Solar Flare', 'Taiyouken'),
        ('Destructo Disc', 'Kienzan'),
        ('Special Beam Cannon', 'Makankosappo'),
        ('Special Beam?', 'Makanko--'),
        ('SPECIAL BEAM CANNON', 'MAKANKOSAPPO'),
        ('Evil Containment Wave', 'Mafuba'),
        ('Z-Z-Zen-Oh', 'Z-Z-Zeno'),
        ('Z-Zen-Oh', 'Z-Zeno'),
        ('Zen-Oh', 'Zeno'),
        ('Zen-oh', 'Zeno'),
        ('ZEN-OH', 'ZENO'),
        ('Fortuneteller Baba', 'Fortunetelling Crone'),
        ('E-Elder Kai {\i1}sama{\i0}', 'H-Honorable Ancestor'),
        ('Elder Kai {\i1}sama{\i0}', 'Honorable Ancestor'),
        ('Lightning of Absolution', 'Absolute Lightning'),
        ('Senzu Beans', 'Senzu'),
        ('Senzu Bean', 'Senzu'),
        ('Senzu beans', 'Senzu'),
        ('Senzu bean', 'Senzu'),
        ('Vegito', 'Vegetto'),
        ('Buu', 'Boo'),
        ('King Yemma', 'Great King Yama'),
        ('Galick Gun', 'Gyallic-ho'),
        ('Instant Transmission', 'teleportation'),
        ('instant transmission', 'teleportation'),
        ('Demon Flash', 'Masenko'),
        ('King Piccolo', 'Great Demon King Piccolo'),
        (' {\\i1}chan{\\i0}', '-{\\i1}chan{\\i0}'),
        (' chan', '-chan'),
        (' CHAN', '-CHAN'),
        (' {\\i1}sama{\\i0}', '-{\\i1}sama{\\i0}'),
        (' sama', '-sama'),
        (' SAMA', '-SAMA'),
        (' {\\i1}san{\\i0}', '-{\\i1}san{\\i0}'),
        (' san', '-san'),
        (' SAN', '-SAN'),
        (' {\\i1}kun{\\i0}', '-{\\i1}kun{\\i0}'),
        (' kun', '-kun'),
        (' KUN', '-KUN')
    ])

    for key in replacements:
        if key in dialog:
            dialog = dialog.replace(key, replacements[key])
            if 'Master Roshi' in key:
                roshi_count += 1
    return dialog, roshi_count

subs = os.listdir()

for s in subs:
    roshi_count = 0
    fname, ext = os.path.splitext(s)
    if ext != '.ass' or '_fixed' in fname:
        continue
    # assumes formats like
    # "Dragon Ball Super Episode 1.ass"
    # "01 - The Peace Reward - Who Will Get the 100 Million Zeni.ass"
    # "Dragon Ball Super - 01.ass"
    # first number in filename will be taken as episode number
    episode_number = re.match(
        r'(?:[^0-9]*)(\d+)(?:.*)',
        fname).group(1)
    print('Fixing episode %s...' % episode_number)
    with codecs.open(s, 'r', 'utf-8') as orig, \
            codecs.open(fname + '_fixed' + ext, 'w', 'utf-8') as fixed:
        # need to write BOM for player to recognize special characters
        fixed.write(u'\ufeff')
        for line in orig:
            if line.startswith('Dialogue: '):
                dialog_arr = line.replace('Dialogue: ', '').split(',', 9)
                # style = dialog_arr[3]
                # dlg_str = dialog_arr[9]
                dialog_arr[9], roshi_count = fix_line(
                    dialog_arr[9], episode_number, roshi_count)
                line = 'Dialogue: ' + ','.join(dialog_arr)
            fixed.write(line)
    print('Done.')
