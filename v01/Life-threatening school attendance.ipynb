import pygame
import sys
import random
from pygame.locals import *

# 色の定義
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
ORANGE= (238, 120,   0)
BLUE  = (  0,   0, 255)
CYAN  = (  0, 255, 255)
BLINK = [(224,255,255), (192,240,255), (128,224,255), \
         (64,192,255), (128,224,255), (192,240,255)]

# 画像の読み込み
imgTitle = pygame.image.load("image/background/title.png")
imgField = pygame.image.load("image/background/background.png")
imgBtlBG = pygame.image.load("image/background/battle.png")
imgEnemy = pygame.image.load("image/enemy/enemy0.png")
imgEffect = pygame.image.load("image/effect/effect.png")
imgPlayer = [
    pygame.image.load("image/player/player0.png"),
    pygame.image.load("image/player/player1.png"),
    pygame.image.load("image/player/player2.png"),
    pygame.image.load("image/player/player3.png"),
    pygame.image.load("image/player/player4.png"),
    pygame.image.load("image/player/player5.png"),
    pygame.image.load("image/player/player6.png"),
    pygame.image.load("image/player/player7.png"),
    pygame.image.load("image/player/player8.png"),
    pygame.image.load("image/player/player9.png"),
    pygame.image.load("image/player/player10.png"),
    pygame.image.load("image/player/player11.png"),
    pygame.image.load("image/player/player12.png"),
    pygame.image.load("image/player/player13.png"),
    pygame.image.load("image/player/player14.png"),
    pygame.image.load("image/player/player15.png"),
    pygame.image.load("image/player/player16.png")
]

# 変数の宣言
speed = 1
volume = 1
idx = 0
tmr = 0
pl_turn = 0
emy_turn = 0

pl_x = 0
pl_y = 0
pl_xs = 0
pl_ys = 0
pl_d = 0
pl_a = 0
pl_x_tmp = 0
pl_y_tmp = 0
pl_d_tmp = 0
pl_a_tmp = 0
pl_x_map_tmp = 0
pl_y_map_tmp = 0
pl_lifemax = 0
pl_life = 0
pl_str = 0
pl_movmax = 0
pl_mov = 0
pl_step = 0
btl_cmd = 1

emy_name = ""
emy_lifemax = 0
emy_life = 0
emy_str = 0
emy_movmax = 0
emy_mov = 0
emy_x = 0
emy_y = 0
emy_step = 0
emy_exist = 1

pl_blink = 0
emy_blink = 0
dmg_eff = 0

stage = 1

COMMAND = ["[A]攻撃", "[W]待機"]

maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

map_move = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 11, 11, 11, 11, 9, 9, 9, 11, 11, 11, 11, 11, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

story_sentence = [
    ["ひ", "ひろ", "ひろき", "ひろきく", "ひろきくん", "ひろきくんは", "ひろきくんは東", "ひろきくんは東大", "ひろきくんは東大を", "ひろきくんは東大を目", "ひろきくんは東大を目指", "ひろきくんは東大を目指し", "ひろきくんは東大を目指して", "ひろきくんは東大を目指して、", "ひろきくんは東大を目指して、", "ひろきくんは東大を目指して、", "ひろきくんは東大を目指して、", "ひろきくんは東大を目指して、"],
    ["毎", "毎日", "毎日学", "毎日学校", "毎日学校に", "毎日学校に通", "毎日学校に通っ", "毎日学校に通って", "毎日学校に通ってい", "毎日学校に通っていた", "毎日学校に通っていた。", "毎日学校に通っていた。", "毎日学校に通っていた。", "毎日学校に通っていた。", "毎日学校に通っていた。", "毎日学校に通っていた。", "毎日学校に通っていた。", "毎日学校に通っていた。"],
    ["し", "しか", "しかし", "しかし、", "しかし、洞", "しかし、洞窟", "しかし、洞窟か", "しかし、洞窟から", "しかし、洞窟から凶", "しかし、洞窟から凶暴", "しかし、洞窟から凶暴な", "しかし、洞窟から凶暴な動", "しかし、洞窟から凶暴な動物", "しかし、洞窟から凶暴な動物が", "しかし、洞窟から凶暴な動物が出", "しかし、洞窟から凶暴な動物が出る", "しかし、洞窟から凶暴な動物が出ると", "しかし、洞窟から凶暴な動物が出るとの"],
    ["噂", "噂が", "噂が流", "噂が流れ", "噂が流れて", "噂が流れてき", "噂が流れてきた", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。", "噂が流れてきた。"],
    ["念", "念の", "念の為", "念の為、", "念の為、ひ", "念の為、ひろ", "念の為、ひろき", "念の為、ひろきく", "念の為、ひろきくん", "念の為、ひろきくんは", "念の為、ひろきくんは戦", "念の為、ひろきくんは戦闘", "念の為、ひろきくんは戦闘準", "念の為、ひろきくんは戦闘準備", "念の為、ひろきくんは戦闘準備を", "念の為、ひろきくんは戦闘準備をし", "念の為、ひろきくんは戦闘準備をした", "念の為、ひろきくんは戦闘準備をした。"],
    ["そ", "そし", "そして", "そしてあ", "そしてある", "そしてある日", "そしてある日、", "そしてある日、ひ", "そしてある日、ひろ", "そしてある日、ひろき", "そしてある日、ひろきく", "そしてある日、ひろきくん", "そしてある日、ひろきくんは", "そしてある日、ひろきくんはつ", "そしてある日、ひろきくんはつい", "そしてある日、ひろきくんはついに", "そしてある日、ひろきくんはついに", "そしてある日、ひろきくんはついに"],
    ["凶", "凶暴", "凶暴な", "凶暴な動", "凶暴な動物", "凶暴な動物に", "凶暴な動物に遭", "凶暴な動物に遭遇", "凶暴な動物に遭遇し", "凶暴な動物に遭遇した", "凶暴な動物に遭遇した。", "凶暴な動物に遭遇した。。", "凶暴な動物に遭遇した。。。", "凶暴な動物に遭遇した。。。", "凶暴な動物に遭遇した。。。", "凶暴な動物に遭遇した。。。", "凶暴な動物に遭遇した。。。", "凶暴な動物に遭遇した。。。"]
]

def draw_text(bg, txt, x, y, fnt, col): # 影付き文字の表示
    cr = int(col[0]/2)
    cg = int(col[1]/2)
    cb = int(col[2]/2)
    sur = fnt.render(txt, True, (cr,cg,cb))
    bg.blit(sur, [x+1, y+1])
    cr = col[0]+128
    if cr > 255: cr = 255
    cg = col[1]+128
    if cg > 255: cg = 255
    cb = col[2]+128
    if cb > 255: cb = 255
    sur = fnt.render(txt, True, (cr,cg,cb))
    bg.blit(sur, [x-1, y-1])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])
    
def draw_battle(bg): # 戦闘画面の描画
    global pl_blink, emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    img_s = pygame.transform.scale(imgBtlBG, [900, 900])
    bg.blit(img_s, [bx, by-50])
    
# 主人公クラスを作成
class MyCharacter:
    def __init__(self, imgPlayer, pl_x, pl_y, pl_d, pl_a, pl_lifemax, \
                 pl_str, pl_movmax):
        self.imgPlayer = imgPlayer
        self.pl_x = pl_x
        self.pl_y = pl_y
        self.pl_d = pl_d
        self.pl_a = pl_a
        self.pl_lifemax = pl_lifemax
        self.pl_life = pl_lifemax
        self.pl_str = pl_str
        self.pl_movmax = pl_movmax
        self.pl_mov = pl_movmax
        
    def draw_player(self, bg, tmr): # 主人公を描画する
        X = (pl_x+(pl_xs)/2-3)*62.85+(62.85-40)/2
        Y = (pl_y+(pl_ys)/2-3)*65.45
        if idx == 8 or idx == 7:
            img_s = pygame.transform.scale(imgPlayer[pl_a], [40, 60])
        else:
            img_s = pygame.transform.scale(imgPlayer[pl_a+(int(tmr/3)%4)], [40, 60])
        bg.blit(img_s, [X-62.45, Y-65.45])
        
    def draw_para(self, bg, fnt): # 主人公の能力を表示
        X = 30
        Y = 600
        bg.fill(BLUE, (X,Y,230,80))
        pygame.draw.rect(bg, BLACK, (X,Y,230,80), width=1)
        col = WHITE
        if pl_life > 0:
            if (pl_lifemax / pl_life) > 5 and tmr%2 == 0:
                col = RED
        else:
            col = RED
        draw_text(bg, "LIFE {}/{}".format(pl_life, pl_lifemax), \
                  X+30, Y+6, fnt, col)
        draw_text(bg, "STR "+str(pl_str), X+30, Y+33, fnt, WHITE)
        col = WHITE
        
    def postion_player(self): # 主人公の初期配置
        global pl_x, pl_y, pl_d, pl_a
        pl_x = 4
        pl_y = 8
        pl_d = 0
        pl_a = 0
        
    def move_player(self, key): # 主人公の移動
        global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life
        global pl_movmax, pl_mov, pl_xs, pl_ys
        # 方向キーで上下左右に移動
        x = pl_x
        y = pl_y
        if key[K_UP] == 1:
            pl_d = 1
            if maze[pl_y-1][pl_x] != 9:
                pl_ys = pl_ys - 1
                if pl_ys == -2:
                    pl_y = pl_y - 1
                    pl_ys = 0
        if key[K_DOWN] == 1:
            pl_d = 0
            if maze[pl_y+1][pl_x] != 9:
                pl_ys = pl_ys + 1
                if pl_ys == 2:
                    pl_y = pl_y + 1
                    pl_ys = 0
        if key[K_LEFT] == 1:
            pl_d = 2
            if maze[pl_y][pl_x-1] != 9:
                pl_xs = pl_xs - 1
                if pl_xs == -2:
                    pl_x = pl_x - 1
                    pl_xs = 0
        if key[K_RIGHT] == 1:
            pl_d = 3
            if maze[pl_y][pl_x+1] != 9:
                pl_xs = pl_xs + 1
                if pl_xs == 2:
                    pl_x = pl_x + 1
                    pl_xs = 0
        pl_a = pl_d*4
        if pl_x != x or pl_y != y: # 移動したら残移動量を計算
            # pl_a = pl_a + tmr%4 # 移動したら足踏みのアニメーション
            pl_mov = pl_mov - 1
        if pl_mov == 0: # 移動量ゼロになったらコマンド選択
            if emy_exist == 1:
                if (pl_x == emy_x and pl_y == emy_y-1) or \
                   (pl_x == emy_x and pl_y == emy_y+1) or \
                   (pl_y == emy_y and pl_x == emy_x-1) or \
                   (pl_y == emy_y and pl_x == emy_x+1): # 敵が隣接している
                    btl_cmd = 0
            idx = 2
            tmr = 0
                
    def cal_can_move_range(self, bg, pl_y, pl_x, cal_mov, map_move):
        # 足跡をつける（現在歩数を代入）
        map_move[pl_y][pl_x] = cal_mov
        #残り歩数が0ならば終了
        if cal_mov == 0:
            return

        # 上へ行けるなら
        if map_move[pl_y-1][pl_x] != 9:
            self.cal_can_move_range(bg,pl_y-1,pl_x,cal_mov-1,map_move)
        # 右へ行けるなら
        if map_move[pl_y][pl_x+1] != 9:
            self.cal_can_move_range(bg,pl_y,pl_x+1,cal_mov-1,map_move)
        # 左へ行けるなら
        if map_move[pl_y][pl_x-1] != 9:
            self.cal_can_move_range(bg,pl_y,pl_x-1,cal_mov-1,map_move)
        # 下へ行けるなら
        if map_move[pl_y+1][pl_x] != 9:
            self.cal_can_move_range(bg,pl_y+1,pl_x,cal_mov-1,map_move)
            
    def move_range_draw(self, bg):
        global map_move
        for y in range(-5, 6):
            for x in range(-5, 6):
                dx = pl_x_map_tmp + x
                dy = pl_y_map_tmp + y
                X = (dx-4)*62.85
                Y = (dy-4)*65.45
                if map_move[dy][dx] == 0 or map_move[dy][dx] == 1 or \
                map_move[dy][dx] == 2 or map_move[dy][dx] == 3:
                    if map_move[dy-1][dx] == 9:
                        map_move[dy-1][dx] = 10
                    if map_move[dy-1][dx] == 11:
                        map_move[dy-1][dx] = 12
                    if map_move[dy+1][dx] == 9:
                        map_move[dy+1][dx] = 10
                    if map_move[dy+1][dx] == 11:
                        map_move[dy+1][dx] = 12
                    if map_move[dy][dx-1] == 9:
                        map_move[dy][dx-1] = 10
                    if map_move[dy][dx-1] == 11:
                        map_move[dy][dx-1] = 12
                    if map_move[dy][dx+1] == 9:
                        map_move[dy][dx+1] = 10
                    if map_move[dy][dx+1] == 11:
                        map_move[dy][dx+1] = 12
                # 移動範囲の表示
                if map_move[dy][dx] == 0 or map_move[dy][dx] == 1 or \
                map_move[dy][dx] == 2 or map_move[dy][dx] == 3:
                    tomei = pygame.Surface([60.85,63.45])
                    tomei.fill(RED)
                    tomei.set_colorkey(RED)
                    tomei.set_alpha(128)
                    pygame.draw.rect(tomei, BLUE, [0,0,60.85,63.45])
                    bg.blit(tomei, [X+1,Y+1])
                    pygame.draw.rect(bg, BLACK, (X+1,Y+1,60.85,63.45), width=1)
                # 攻撃範囲の表示
                if map_move[dy][dx] == 10 or map_move[dy][dx] == 12:
                    tomei = pygame.Surface([60.85,60.45])
                    tomei.fill(RED)
                    tomei.set_colorkey(RED)
                    tomei.set_alpha(128)
                    pygame.draw.rect(tomei, ORANGE, [0,0,60.85,63.45])
                    bg.blit(tomei, [X+1,Y+1])
                    pygame.draw.rect(bg, BLACK, (X+1,Y+1,60.85,63.45), width=1)
            
    def player_command(self, bg, fnt, key): # コマンドの入力と表示
        global btl_cmd
        ent = False
        if emy_exist == 1:
            if (pl_x == emy_x and pl_y == emy_y-1) or \
               (pl_x == emy_x and pl_y == emy_y+1) or \
               (pl_y == emy_y and pl_x == emy_x-1) or \
               (pl_y == emy_y and pl_x == emy_x+1): # 敵が隣接している
                if key[K_a]: # Aキー
                    btl_cmd = 0
                    ent = True
                if key[K_UP] and btl_cmd > 0: #↑キー
                    btl_cmd -= 1
                if key[K_DOWN] and btl_cmd < 1: #↓キー
                    btl_cmd += 1
        if key[K_w]: # Wキー
            btl_cmd = 1
            ent = True
        if key[K_SPACE] or key[K_RETURN]:
            ent = True
        for i in range(2):
            c = WHITE
            if btl_cmd == i:
                c =BLINK[tmr%6]
            draw_text(bg, COMMAND[i], 720, 330+i*60, fnt, c)
        return ent
    
    def draw_battle_player(self, bg, tmr):
        global pl_blink
        if pl_life > 0 and pl_blink%2 == 0:
            img_s = pygame.transform.scale(imgPlayer[12+(int(tmr/3)%4)], [120, 180])
            bg.blit(img_s, [100+pl_step, 300])
        if pl_blink > 0:
            pl_blink = pl_blink - 1
    
# 敵クラスを作成
class EnemyCharacter:
    def __init__(self, imgEnemy, emy_name, emy_lifemax, emy_str, emy_movmax, \
                 emy_x, emy_y):
        self.imgEnemy = imgEnemy
        self.emy_name = emy_name
        self.emy_lifemax = emy_lifemax
        self.emy_life = emy_lifemax
        self.emy_str = emy_str
        self.emy_movmax = emy_movmax
        self.emy_mov = emy_movmax
        self.emy_x = emy_x
        self.emy_y = emy_y
        
    def draw_enemy(self, bg): # 敵を描画する
        X = (emy_x-3)*62.85+(62.85-57)/2
        Y = (emy_y-3)*65.45
        img_s = pygame.transform.scale(pygame.image.load(self.imgEnemy), \
                                       [57, 64])
        bg.blit(img_s, [X-62.45, Y-65.45])
        
    def draw_para_enemy(self, bg, fnt): # 敵の能力を表示
        X = 30
        Y = 600
        bg.fill(RED, (X+570,Y,230,80))
        pygame.draw.rect(bg, BLACK, (X+570,Y,230,80), width=1)
        col = WHITE
        if emy_life > 0:
            if (emy_lifemax / emy_life) > 5 and tmr%2 == 0:
                col = RED
        else:
            col = RED
        draw_text(bg, "LIFE {}/{}".format(emy_life, emy_lifemax), \
                  X+600, Y+6, fnt, col)
        draw_text(bg, "STR "+str(emy_str), X+600, Y+33, fnt, WHITE)
        col = WHITE
        
    def postion_enemy(self): # 敵の初期配置
        global emy_x, emy_y
        emy_x = 15
        emy_y = 6
        
    def move_enemy(self, key): # 敵の移動
        global tmr, idx, pl_x, pl_y, emy_x, emy_y, emy_movmax, emy_mov
        global pl_mov, pl_turn, pl_x_tmp, pl_y_tmp, pl_d_tmp, pl_a_tmp, maze
        # 主人公の位置次第で上下左右に移動
        x = emy_x
        y = emy_y
        if tmr >= 10:
            if tmr%3 == 0 and emy_mov != 0:
                if pl_x < emy_x:
                    if maze[emy_y][emy_x-1] != 9:
                        emy_x = emy_x - 1
                    if emy_mov != 1:        
                        #if key[K_UP] == 1:
                        if pl_y < emy_y:
                            if maze[emy_y-1][emy_x] != 9:
                                emy_y = emy_y - 1
                        #if key[K_DOWN] == 1:
                        if pl_y > emy_y:
                            if maze[emy_y+1][emy_x] != 9:
                                emy_y = emy_y + 1
                if pl_x > emy_x:
                    if maze[emy_y][emy_x+1] != 9:
                        emy_x = emy_x + 1
                    if emy_mov != 1: 
                        if pl_y < emy_y:
                            if maze[emy_y-1][emy_x] != 9:
                                emy_y = emy_y - 1
                        if pl_y > emy_y:
                            if maze[emy_y+1][emy_x] != 9:
                                emy_y = emy_y + 1
                if pl_x == emy_x:
                    if pl_y < emy_y:
                        if maze[emy_y-1][emy_x] != 9:
                            emy_y = emy_y - 1
                    if pl_y > emy_y:
                        if maze[emy_y+1][emy_x] != 9:
                            emy_y = emy_y + 1
            if emy_x != x or emy_y != y: # 移動したら残移動量を計算
                emy_mov = emy_mov - 1
            if tmr%3 == 2:
                if (pl_x == emy_x and pl_y == emy_y-1) or \
                    (pl_x == emy_x and pl_y == emy_y+1) or \
                    (pl_y == emy_y and pl_x == emy_x-1) or \
                    (pl_y == emy_y and pl_x == emy_x+1): # プレイヤーが隣接している
                    idx = 11 # 戦闘開始
                    tmr = 0
                if emy_mov == 0: # 移動量ゼロになったら
                    maze[pl_y][pl_x] = 0
                    pl_x_tmp = pl_x
                    pl_y_tmp = pl_y
                    pl_d_tmp = pl_d
                    pl_a_tmp = pl_a
                    pl_mov = pl_movmax
                    pl_turn = 15
                    idx = 1
                    tmr = 0
                
    def draw_battle_enemy(self, bg):
        global emy_blink
        if emy_life > 0 and emy_blink%2 == 0:
            img_s2 = pygame.transform.scale \
            (pygame.image.load(self.imgEnemy), [114, 128])
            bg.blit(img_s2, [640-emy_step, 330])
        if emy_blink > 0:
            emy_blink = emy_blink - 1
                
def main(): # メイン処理
    global speed, volume, idx, tmr, btl_cmd, stage
    global pl_lifemax, pl_life, pl_str, pl_step, pl_movmax, pl_mov, pl_turn
    global emy_lifemax, emy_life, emy_str
    global emy_movmax, emy_mov, emy_step, emy_x, emy_y, emy_exist
    global pl_blink, emy_blink, dmg_eff
    global pl_a, pl_x, pl_y, pl_d, maze, map_move
    global pl_x_tmp, pl_y_tmp, pl_d_tmp, pl_a_tmp, pl_x_map_tmp, pl_y_map_tmp
    dmg = 0
    cal_mov = 0
    story = 0
    x = 0
    lr = 1
    mouse_x = 0
    mouse_y = 0
    cursor_x = 0
    cursor_y = 0
    idou = 0
    #rx = 0
    #ry = 0
    #drx = 0
    #dry = 0
    
    pygame.init()
    pygame.display.set_caption("命がけの登校")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font("font/ipaexg.ttf", 25)
    fontS = pygame.font.Font("font/ipaexg.ttf", 18)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((880,720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((880,720))
                if event.key == K_s:
                    speed = speed + 1
                    speed = ((speed-1)%3)+1
                if event.key == K_v:
                    volume = volume + 1
                    volume = (volume%5)
                    pygame.mixer.music.set_volume(0.05*volume)
                # マウスクリック
            if event.type == MOUSEBUTTONDOWN:
                if cursor_x == pl_x-4 and cursor_y == pl_y-4:
                    idou = 1    
                
        tmr = tmr + 1
        key = pygame.key.get_pressed()
        
        if idx == 0: # タイトル画面
            if tmr == 1:
                pygame.mixer.music.load("sound/start.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05*volume)
            img_s = pygame.transform.scale(imgTitle, [1045, 810])
            screen.blit(img_s, [-24, -27])
            if x == -300:
                lr = 1
            if x == 900:
                lr = -1
            x += lr*20
            img_s2 = pygame.transform.scale(imgPlayer[10+lr*2+(int(tmr/2)%4)], [120, 180])
            screen.blit(img_s2, [100+x, 300])
            if story == 0:
                draw_text(screen, "Life-threatening school attendance", \
                          230, 160, font, ORANGE)
                draw_text(screen, "スペースキーを押してください", \
                          260, 560, font, BLINK[tmr%6])
            if story == 0 and key[K_SPACE] == 1:
                story = 1
                tmr = 2
            # ストーリーを流す
            for story_b in range(7):
                if story == story_b + 1:
                    for story_a in range(18):
                        if tmr == story_a +2:
                            draw_text(screen, \
                                      story_sentence[story_b][story_a], \
                                      140, 300, font, ORANGE)
                    if tmr >= 19:
                        draw_text(screen, story_sentence[story_b][17], \
                                  140, 300, font, ORANGE)
                    if tmr >= 5 and key[K_SPACE] == 1:
                        story += 1
                        tmr = 2
            if story == 8:
                mycharacter[0].postion_player()
                emycharacter[stage-1].postion_enemy()
                pl_lifemax = 100
                pl_life = pl_lifemax
                pl_str = 20
                pl_x_tmp = pl_x
                pl_y_tmp = pl_y
                pl_d_tmp = pl_d
                pl_a_tmp = pl_a
                pl_movmax = 3
                pl_mov = pl_movmax
                emy_lifemax = 80
                emy_life = emy_lifemax
                emy_str = 15
                emy_movmax = 3
                emy_mov = emy_movmax
                pl_turn = 15
                idx = 9
                tmr = 0
                pygame.mixer.music.load("sound/field.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05*volume)
                
        elif idx == 1: # プレイヤーのターン
            btl_cmd = 1
            if tmr == 1:
                for dy in range(19):
                    for dx in range(22):
                        if map_move[dy][dx] == 0 or \
                        map_move[dy][dx] == 1 or \
                        map_move[dy][dx] == 2 or \
                        map_move[dy][dx] == 3 or \
                        map_move[dy][dx] == 12:
                            map_move[dy][dx] = 11
                        if map_move[dy][dx] == 10:
                            map_move[dy][dx] = 9
                if emy_exist == 1:
                    maze[emy_y][emy_x] = 9 # 敵が壁
                    map_move[emy_y][emy_x] = 9
                if emy_exist == 0:
                    map_move[emy_y][emy_x] = 11
                mycharacter[0].cal_can_move_range(screen, pl_y, pl_x, \
                                                  pl_movmax, map_move)
                pl_x_map_tmp = pl_x
                pl_y_map_tmp = pl_y
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].draw_player(screen, tmr)
            draw_text(screen, "Stage "+str(stage), 390, 40, font, WHITE)
            #for a in map_move:
            #        print(a)
            if emy_exist == 1:
                emycharacter[stage-1].draw_enemy(screen)
            for event in pygame.event.get():
                # マウスポインタで移動
                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos # マウス位置取得
                    if 0 <= mouse_x and mouse_x < 62.85*13 \
                    and 24 <= mouse_y and mouse_y < 65.45*11:
                        cursor_x = int((mouse_x)/62.85)
                        cursor_y = int((mouse_y)/65.45)
            # マウスクリックかエンターで移動
            if idou == 1 or key[K_RETURN] == 1:
                idx = 12
                tmr = 0
                idou = 0
            pygame.draw.rect(screen, WHITE, [cursor_x*62.85, cursor_y*65.45, \
                                            62.85, 65.45], width=3)
            if pl_turn > 0:
                pl_turn = pl_turn - 1
                draw_text(screen, "プレイヤーのターン", 300, 180, font, CYAN)
            
        elif idx == 12: # プレイヤーの移動
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].move_range_draw(screen)
            mycharacter[0].draw_player(screen, tmr)
            if emy_exist == 1:
                emycharacter[stage-1].draw_enemy(screen)
            mycharacter[0].move_player(key)
            if maze[pl_y][pl_x] == 1:
                pygame.mixer.music.load("sound/clear.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05*volume)
                idx = 8 # クリア
                tmr = 0
            if tmr >= 5:
                if key[K_RETURN] == 1:
                    if emy_exist == 1:
                        if (pl_x == emy_x and pl_y == emy_y-1) or \
                           (pl_x == emy_x and pl_y == emy_y+1) or \
                           (pl_y == emy_y and pl_x == emy_x-1) or \
                           (pl_y == emy_y and pl_x == emy_x+1): # 敵が隣接している
                            btl_cmd = 0
                    idx = 2
                    tmr = 0
            draw_text(screen, "残移動数{}".format(pl_mov), 50, 660, fontS, WHITE) 
                
        elif idx == 2: # プレイヤーのコマンド入力と表示
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].move_range_draw(screen)
            mycharacter[0].draw_player(screen, tmr)
            if emy_exist == 1:
                emycharacter[stage-1].draw_enemy(screen)
            if tmr >= 5:
                screen.fill((51,51,204), (700,300,150,200))
                pygame.draw.rect(screen, BLACK, (700,300,150,200), width=1)
                if mycharacter[0].player_command(screen, font, key) == True:
                    if btl_cmd == 0:
                        idx = 10 #戦闘
                        tmr = 0
                    if btl_cmd == 1:
                        if emy_exist == 1:
                            maze[emy_y][emy_x] = 0
                            map_move[emy_y][emy_x] = 0
                            emy_turn = 15
                            emy_mov = emy_movmax
                            idx = 3 #待機（敵のターン）
                            tmr = 0
                        else:
                            pl_mov = pl_movmax
                            pl_x_tmp = pl_x
                            pl_y_tmp = pl_y
                            pl_d_tmp = pl_d
                            pl_a_tmp = pl_a
                            pl_turn = 15
                            idx = 1
                            tmr = 0
                if key[K_b] == 1: # 戻る
                    pl_x = pl_x_tmp
                    pl_y = pl_y_tmp
                    pl_d = pl_d_tmp
                    pl_a = pl_a_tmp
                    pl_mov = 3
                    idx = 1
                
        elif idx == 3: # 敵のターン
            if tmr == 1:
                maze[pl_y][pl_x] = 9 # プレイヤーが壁
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].draw_player(screen, tmr)
            emycharacter[stage-1].draw_enemy(screen)
            emycharacter[stage-1].move_enemy(key)
            if emy_turn > 0:
                emy_turn = emy_turn - 1
                draw_text(screen, "敵のターン", 300, 180, font, RED)
            
        elif idx == 4: # 戦闘開始（先制攻撃）
            draw_battle(screen)
            mycharacter[0].draw_battle_player(screen, tmr) # 主人公を表示
            emycharacter[stage-1].draw_battle_enemy(screen) # 敵を表示
            mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
            emycharacter[stage-1].draw_para_enemy(screen, font) # 敵の能力を表示
            # プレイヤーの攻撃
            if tmr == 6:
                dmg = pl_str
                pl_step = 30
            if 12 <= tmr and tmr <= 14:
                screen.blit(imgEffect, [840-tmr*20, -1330+tmr*120])
            if tmr == 15:
                emy_blink = 5
            if tmr == 21:
                pl_step = 0
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    emy_exist = 0
            if tmr == 26:
                if emy_exist == 0:
                    maze[emy_y][emy_x] = 0
                    maze[pl_y][pl_x] = 0
                    pl_mov = pl_movmax
                    pl_x_tmp = pl_x
                    pl_y_tmp = pl_y
                    pl_d_tmp = pl_d
                    pl_a_tmp = pl_a
                    pl_turn = 15
                    pygame.mixer.music.load("sound/field.ogg")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.05*volume)
                    idx = 9
                    tmr = 0
                else: # 敵の攻撃
                    dmg = emy_str
                    emy_step = 30   
            if 31 <= tmr and tmr <= 33:
                screen.blit(imgEffect, [760-tmr*20, -3580+tmr*120])
            if tmr == 38:
                dmg = emy_str
                dmg_eff = 5
                emy_step = 0
            if tmr == 42:
                pl_life = pl_life - dmg
                if pl_life <= 0:
                    pl_life = 0
                    idx = 6 # 敗北
                    tmr = 0
            if tmr == 49:
                if emy_exist == 1:
                    maze[emy_y][emy_x] = 0
                    emy_turn = 15
                    emy_mov = emy_movmax
                    idx = 3
                    tmr = 0
        
        elif idx == 5: # 戦闘開始（後攻攻撃）
            draw_battle(screen)
            mycharacter[0].draw_battle_player(screen, tmr) # 主人公を表示
            emycharacter[stage-1].draw_battle_enemy(screen) # 敵を表示
            mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
            emycharacter[stage-1].draw_para_enemy(screen, font) # 敵の能力を表示
            # 敵の攻撃
            if tmr == 6:
                dmg = emy_str
                emy_step = 30
            if 12 <= tmr and tmr <= 14:
                screen.blit(imgEffect, [380-tmr*20, -1300+tmr*120])
            if tmr == 15:
                dmg = emy_str
                dmg_eff = 5
                emy_step = 0
            if tmr == 21:
                pl_life = pl_life - dmg
                if pl_life <= 0:
                    pl_life = 0
                    idx = 6 # 敗北
                    tmr = 0
            # プレイヤーの攻撃
            if tmr == 25:
                dmg = pl_str
                pl_step = 30
            if 31 <= tmr and tmr <= 33:
                screen.blit(imgEffect, [1220-tmr*20, -3610+tmr*120])
            if tmr == 34:
                emy_blink = 5
            if tmr == 40:
                pl_step = 0
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    emy_exist = 0
                    maze[emy_y][emy_x] = 0
            if tmr == 45:
                maze[pl_y][pl_x] = 0
                pl_mov = pl_movmax
                pl_x_tmp = pl_x
                pl_y_tmp = pl_y
                pl_d_tmp = pl_d
                pl_a_tmp = pl_a
                pl_turn = 15
                pygame.mixer.music.load("sound/field.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05*volume)
                idx = 9
                tmr = 0
                
        elif idx == 6: # 敗北
            draw_battle(screen)
            mycharacter[0].draw_battle_player(screen, tmr) # 主人公を表示
            emycharacter[stage-1].draw_battle_enemy(screen) # 敵を表示
            mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
            emycharacter[stage-1].draw_para_enemy(screen, font) # 敵の能力を表示
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr == 11:
                idx = 7
                tmr = 29
                
        elif idx == 7: # ゲームオーバー
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            if emy_exist == 1:
                emycharacter[stage-1].draw_enemy(screen)
            if tmr <= 40:
                PL_TURN = [0, 8, 4, 12]
                pl_a = PL_TURN[tmr%4]
                mycharacter[0].draw_player(screen, tmr)
            if tmr >= 41 and tmr <= 60:
                pl_a = 16 # 倒れた絵
                mycharacter[0].draw_player(screen, tmr)
            if tmr >= 51 and tmr <= 119:
                draw_text(screen, "You died.", 360, 240, font, RED)
                draw_text(screen, "Game over.", 360, 380, font, RED)
            if tmr == 120:
                story = 0
                idx = 0
                tmr = 0
                
        elif idx == 8: # クリア画面
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].draw_player(screen, tmr)
            if emy_exist == 1:
                emycharacter[stage-1].draw_enemy(screen)
            if stage == 1:
                draw_text(screen, "Stage"+str(stage)+" clear.", \
                          360, 240, font, CYAN)
            else:
                draw_text(screen, "Game clear.", 360, 240, font, CYAN)
            if tmr == 100:
                if stage < 2:
                    mycharacter[0].postion_player()
                    emycharacter[stage-1].postion_enemy()
                    pl_lifemax = 100
                    pl_life = pl_lifemax
                    pl_str = 20
                    pl_x_tmp = pl_x
                    pl_y_tmp = pl_y
                    pl_d_tmp = pl_d
                    pl_a_tmp = pl_a
                    pl_movmax = 3
                    pl_mov = pl_movmax
                    emy_exist = 1
                    emy_lifemax = 100
                    emy_life = emy_lifemax
                    emy_str = 20
                    emy_movmax = 3
                    emy_mov = emy_movmax
                    pl_turn = 15
                    stage += 1
                    idx = 9
                    tmr = 0
                    pygame.mixer.music.load("sound/field.ogg")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.05*volume)
            
        elif idx == 9: # 画面切り替え（➔フィールド）
            if 1 <= tmr and tmr <= 8:
                h = 80*tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr >= 10:
                img_s = pygame.transform.scale(imgField, [1020, 828])
                screen.blit(img_s, [-23, -30])
                mycharacter[0].draw_player(screen, tmr)
                if emy_exist == 1:
                    emycharacter[stage-1].draw_enemy(screen)
            if 10 <= tmr and tmr <= 14:
                h = 80*(14-tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr == 14:
                idx = 1
                tmr = 0
                
        elif idx == 10: # 画面切り替え（➔戦闘開始（先制攻撃））
            if 1 <= tmr and tmr <= 8:
                h = 80*tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr >= 10:
                draw_battle(screen)
                mycharacter[0].draw_battle_player(screen, tmr) # 主人公を表示
                emycharacter[stage-1].draw_battle_enemy(screen) # 敵を表示
                mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
                emycharacter[stage-1].draw_para_enemy(screen, font) # 敵の能力を表示
            if 10 <= tmr and tmr <= 14:
                h = 80*(14-tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr == 14:
                pygame.mixer.music.load("sound/battle.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05*volume)
                idx = 4
                tmr = 0
                
        elif idx == 11: # 画面切り替え（➔戦闘開始（後攻攻撃））
            if 1 <= tmr and tmr <= 8:
                h = 80*tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr >= 10:
                draw_battle(screen)
                mycharacter[0].draw_battle_player(screen, tmr) # 主人公を表示
                emycharacter[stage-1].draw_battle_enemy(screen) # 敵を表示
                mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
                emycharacter[stage-1].draw_para_enemy(screen, font) # 敵の能力を表示
            if 10 <= tmr and tmr <= 14:
                h = 80*(14-tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720-h, 880, h])
            if tmr == 14:
                pygame.mixer.music.load("sound/battle.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05*volume)
                idx = 5
                tmr = 0
          
        pygame.draw.rect(screen, BLACK, [0, 720, 1200, 300])
        pygame.draw.rect(screen, BLACK, [880, 0, 400, 1000])
        draw_text(screen, "[S]peed "+str(speed), 740, 40, fontS, WHITE)
        draw_text(screen, "[V]olume "+str(volume), 50, 40, fontS, WHITE)
        
        pygame.display.update()
        clock.tick(4+2*speed)

mycharacter = [
    MyCharacter("image/player/player"+str(pl_a)+".png", pl_x, pl_y, pl_d, pl_a, \
                pl_lifemax, pl_str, pl_movmax)
]
    
emycharacter = [
    EnemyCharacter("image/enemy/enemy0.png", "凶暴な猫", emy_lifemax, emy_str, emy_movmax, \
                   emy_x, emy_y),
    EnemyCharacter("image/enemy/enemy1.png", "凶暴な虎", emy_lifemax, emy_str, emy_movmax, \
                   emy_x, emy_y)
]        
        
if __name__ == '__main__':
    main()
