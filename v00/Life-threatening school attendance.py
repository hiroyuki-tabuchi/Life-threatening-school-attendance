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
imgTitle = pygame.image.load("title.png")
imgField = pygame.image.load("background.png")
imgBtlBG = pygame.image.load("battle.png")
imgEnemy = pygame.image.load("enemy0.png")
imgEffect = pygame.image.load("effect.png")
imgPlayer = [
    pygame.image.load("player0.png"),
    pygame.image.load("player1.png"),
    pygame.image.load("player2.png"),
    pygame.image.load("player3.png"),
    pygame.image.load("player4.png"),
    pygame.image.load("player5.png"),
    pygame.image.load("player6.png"),
    pygame.image.load("player7.png"),
    pygame.image.load("player8.png"),
    pygame.image.load("player9.png"),
    pygame.image.load("player10.png"),
    pygame.image.load("player11.png"),
    pygame.image.load("player12.png"),
    pygame.image.load("player13.png"),
    pygame.image.load("player14.png"),
    pygame.image.load("player15.png")
]

# 変数の宣言
speed = 1
idx = 0
tmr = 0
pl_turn = 0
emy_turn = 0

pl_x = 0
pl_y = 0
pl_d = 0
pl_a = 0
pl_x_tmp = 0
pl_y_tmp = 0
pl_d_tmp = 0
pl_a_tmp = 0
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

def draw_text(bg, txt, x, y, fnt, col): # 影付き文字の表示
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x+1, y+2])
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
        
    def draw_player(self, bg): # 主人公を描画する
        X = (pl_x-3)*62.85+(62.85-40)/2
        Y = (pl_y-3)*65.45
        img_s = pygame.transform.scale(imgPlayer[pl_a], [40, 60])
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
        global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life, pl_movmax, pl_mov
        # 方向キーで上下左右に移動
        x = pl_x
        y = pl_y
        if key[K_UP] == 1:
            pl_d = 1
            if maze[pl_y-1][pl_x] != 9:
                pl_y = pl_y - 1
        if key[K_DOWN] == 1:
            pl_d = 0
            if maze[pl_y+1][pl_x] != 9:
                pl_y = pl_y + 1
        if key[K_LEFT] == 1:
            pl_d = 2
            if maze[pl_y][pl_x-1] != 9:
                pl_x = pl_x - 1
        if key[K_RIGHT] == 1:
            pl_d = 3
            if maze[pl_y][pl_x+1] != 9:
                pl_x = pl_x + 1
        pl_a = pl_d*4
        if pl_x != x or pl_y != y: # 移動したら残移動量を計算
            pl_a = pl_a + tmr%4 # 移動したら足踏みのアニメーション
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
    
    def draw_battle_player(self, bg):
        global pl_blink
        if pl_life > 0 and pl_blink%2 == 0:
            img_s = pygame.transform.scale(imgPlayer[12], [120, 180])
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
        img_s = pygame.transform.scale(imgEnemy, [57, 64])
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
                idx = 5 # 戦闘開始
                pygame.mixer.music.load("battle.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05)
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
            img_s2 = pygame.transform.scale(imgEnemy, [114, 128])
            bg.blit(img_s2, [640-emy_step, 330])
        if emy_blink > 0:
            emy_blink = emy_blink - 1
                
def main(): # メイン処理
    global speed, idx, tmr, btl_cmd
    global pl_lifemax, pl_life, pl_str, pl_step, pl_movmax, pl_mov, pl_turn
    global emy_lifemax, emy_life, emy_str
    global emy_movmax, emy_mov, emy_step, emy_x, emy_y, emy_exist
    global pl_blink, emy_blink, dmg_eff
    global pl_a, pl_x, pl_y, pl_d, maze
    global pl_x_tmp, pl_y_tmp, pl_d_tmp, pl_a_tmp
    dmg = 0
    map_move = []
    cal_mov = 0
    story = 0
    
    pygame.init()
    pygame.display.set_caption("命がけの登校")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font("ipaexg.ttf", 25)
    fontS = pygame.font.Font("ipaexg.ttf", 18)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    speed = speed + 1
                    if speed == 4:
                        speed = 1
            
        tmr = tmr + 1
        key = pygame.key.get_pressed()
        
        if idx == 0: # タイトル画面
            if tmr == 1:
                pygame.mixer.music.load("start.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05)
            img_s = pygame.transform.scale(imgTitle, [1045, 810])
            screen.blit(img_s, [-24, -27])
            img_s2 = pygame.transform.scale(imgPlayer[12+(int(tmr/2)%4)], [120, 180])
            screen.blit(img_s2, [370, 300])
            draw_text(screen, "Life-threatening school attendance", 230, 160, font, ORANGE)
            draw_text(screen, "スペースキーを押してください", 260, 560, font, BLINK[tmr%6])
            if key[K_SPACE] == 1:
                story = 1
                tmr = 2
            # ストーリーを流す
            if story == 1:
                img_s = pygame.transform.scale(imgTitle, [1045, 810])
                screen.blit(img_s, [-24, -27])
                img_s2 = pygame.transform.scale(imgPlayer[12+(int(tmr/2)%4)], [120, 180])
                screen.blit(img_s2, [370, 300])
                if tmr >= 2 and tmr <= 79:
                    draw_text(screen, "ひろきくんは東大を目指して、", \
                              140, 750-tmr*15, font, ORANGE)
                    draw_text(screen, "毎日学校に通っていた。", \
                              140, 795-tmr*15, font, ORANGE)
                    draw_text(screen, "しかし、洞窟から凶暴な動物が出るとの", \
                              140, 840-tmr*15, font, ORANGE)
                    draw_text(screen, "噂が流れてきた。", \
                              140, 885-tmr*15, font, ORANGE)
                    draw_text(screen, "念の為、ひろきくんは戦闘準備をした。", \
                              140, 930-tmr*15, font, ORANGE)
                    draw_text(screen, "そしてある日、ひろきくんはついに", \
                              140, 975-tmr*15, font, ORANGE)
                    draw_text(screen, "凶暴な動物に遭遇した。。。", \
                              140, 1020-tmr*15, font, ORANGE)
                if tmr == 80:
                    mycharacter[0].postion_player()
                    emycharacter[0].postion_enemy()
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
                    idx = 1
                    pygame.mixer.music.load("field.ogg")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.05)
                
        elif idx == 1: # プレイヤーのターン
            btl_cmd = 1
            if tmr == 1:
                if emy_exist == 1:
                    maze[emy_y][emy_x] = 9 # 敵が壁
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].draw_player(screen)
            if emy_exist == 1:
                emycharacter[0].draw_enemy(screen)
            mycharacter[0].move_player(key)
            if pl_turn > 0:
                pl_turn = pl_turn - 1
                draw_text(screen, "プレイヤーのターン", 300, 180, font, CYAN)
            if maze[pl_y][pl_x] == 1:
                pygame.mixer.music.load("clear.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05)
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
            if key[K_f] == 1:
                pygame.mixer.music.set_volume(0)
            if key[K_n] == 1:   
                pygame.mixer.music.set_volume(0.05)
            draw_text(screen, "残移動数{}".format(pl_mov), 50, 630, fontS, WHITE)    
            draw_text(screen, "[N]音量ON", 740, 600, fontS, WHITE)
            draw_text(screen, "[F]音量OFF", 740, 630, fontS, WHITE)
                
        elif idx == 2: # プレイヤーのコマンド入力と表示
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].draw_player(screen)
            if emy_exist == 1:
                emycharacter[0].draw_enemy(screen)
            if tmr >= 5:
                screen.fill((51,51,204), (700,300,150,200))
                pygame.draw.rect(screen, BLACK, (700,300,150,200), width=1)
                if mycharacter[0].player_command(screen, font, key) == True:
                    if btl_cmd == 0:
                        pygame.mixer.music.load("battle.ogg")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.05)
                        idx = 4 #戦闘
                        tmr = 0
                    if btl_cmd == 1:
                        if emy_exist == 1:
                            maze[emy_y][emy_x] = 0
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
            mycharacter[0].draw_player(screen)
            emycharacter[0].draw_enemy(screen)
            if tmr >= 5:
                emycharacter[0].move_enemy(key)
            if emy_turn > 0:
                emy_turn = emy_turn - 1
                draw_text(screen, "敵のターン", 300, 180, font, RED)
            
        elif idx == 4: # 戦闘開始（先制攻撃）
            draw_battle(screen)
            mycharacter[0].draw_battle_player(screen) # 主人公を表示
            emycharacter[0].draw_battle_enemy(screen) # 敵を表示
            mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
            emycharacter[0].draw_para_enemy(screen, font) # 敵の能力を表示
            # プレイヤーの攻撃
            if tmr == 6:
                dmg = pl_str
                pl_step = 30
            if 7 <= tmr and tmr <= 9:
                screen.blit(imgEffect, [740-tmr*20, -730+tmr*120])
            if tmr == 10:
                emy_blink = 5
            if tmr == 16:
                pl_step = 0
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    emy_exist = 0
            if tmr == 21:
                if emy_exist == 0:
                    maze[emy_y][emy_x] = 0
                    maze[pl_y][pl_x] = 0
                    pl_mov = pl_movmax
                    pl_x_tmp = pl_x
                    pl_y_tmp = pl_y
                    pl_d_tmp = pl_d
                    pl_a_tmp = pl_a
                    pl_turn = 15
                    pygame.mixer.music.load("field.ogg")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.05)
                    idx = 1
                    tmr = 0
            # 敵の攻撃
            if tmr == 24:
                dmg = emy_str
                emy_step = 30
            if 21 <= tmr and tmr <= 23:
                screen.blit(imgEffect, [560-tmr*20, -2380+tmr*120])
            if tmr == 28:
                dmg = emy_str
                dmg_eff = 5
                emy_step = 0
            if tmr == 32:
                pl_life = pl_life - dmg
                if pl_life <= 0:
                    pl_life = 0
                    idx = 6 # 敗北
                    tmr = 0
            if tmr == 39:
                if emy_exist == 1:
                    maze[emy_y][emy_x] = 0
                    emy_turn = 15
                    emy_mov = emy_movmax
                    idx = 3
                    tmr = 0
                else:
                    pl_mov = pl_movmax
                    pl_x_tmp = pl_x
                    pl_y_tmp = pl_y
                    pl_d_tmp = pl_d
                    pl_a_tmp = pl_a
                    pl_turn = 15
                    pygame.mixer.music.load("field.ogg")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.05)
                    idx = 1
                    tmr = 0
        
        elif idx == 5: # 戦闘開始（後攻攻撃）
            draw_battle(screen)
            mycharacter[0].draw_battle_player(screen) # 主人公を表示
            emycharacter[0].draw_battle_enemy(screen) # 敵を表示
            mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
            emycharacter[0].draw_para_enemy(screen, font) # 敵の能力を表示
            # 敵の攻撃
            if tmr == 6:
                dmg = emy_str
                emy_step = 30
            if 7 <= tmr and tmr <= 9:
                screen.blit(imgEffect, [280-tmr*20, -700+tmr*120])
            if tmr == 10:
                dmg = emy_str
                dmg_eff = 5
                emy_step = 0
            if tmr == 16:
                pl_life = pl_life - dmg
                if pl_life <= 0:
                    pl_life = 0
                    idx = 6 # 敗北
                    tmr = 0
            # プレイヤーの攻撃
            if tmr == 20:
                dmg = pl_str
                pl_step = 30
            if 21 <= tmr and tmr <= 23:
                screen.blit(imgEffect, [1020-tmr*20, -2410+tmr*120])
            if tmr == 24:
                emy_blink = 5
            if tmr == 30:
                pl_step = 0
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    emy_exist = 0
                    maze[emy_y][emy_x] = 0
            if tmr == 35:
                maze[pl_y][pl_x] = 0
                pl_mov = pl_movmax
                pl_x_tmp = pl_x
                pl_y_tmp = pl_y
                pl_d_tmp = pl_d
                pl_a_tmp = pl_a
                pl_turn = 15
                pygame.mixer.music.load("field.ogg")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.05)
                idx = 1
                tmr = 0
                
        elif idx == 6: # 敗北
            draw_battle(screen)
            mycharacter[0].draw_battle_player(screen) # 主人公を表示
            emycharacter[0].draw_battle_enemy(screen) # 敵を表示
            mycharacter[0].draw_para(screen, font) # 主人公の能力を表示
            emycharacter[0].draw_para_enemy(screen, font) # 敵の能力を表示
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr == 11:
                idx = 7
                tmr = 29
                
        elif idx == 7: # ゲームオーバー
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            if emy_exist == 1:
                emycharacter[0].draw_enemy(screen)
            if tmr <= 30:
                PL_TURN = [0, 8, 4, 12]
                pl_a = PL_TURN[tmr%4]
                if tmr == 30:
                    pl_a = 16 # 倒れた絵
            elif tmr == 31:
                draw_text(screen, "You died.", 360, 240, font, RED)
                draw_text(screen, "Game over.", 360, 380, font, RED)
            elif tmr == 100:
                idx = 0
                tmr = 0
                
        elif idx == 8: # クリア画面
            img_s = pygame.transform.scale(imgField, [1020, 828])
            screen.blit(img_s, [-23, -30])
            mycharacter[0].draw_player(screen)
            if emy_exist == 1:
                emycharacter[0].draw_enemy(screen)
            draw_text(screen, "Game clear.", 360, 240, font, CYAN)
            
        draw_text(screen, "[S]peed "+str(speed), 740, 40, fontS, WHITE)
        
        pygame.display.update()
        clock.tick(4+2*speed)

mycharacter = [
    MyCharacter("player"+str(pl_a)+".png", pl_x, pl_y, pl_d, pl_a, \
                pl_lifemax, pl_str, pl_movmax)
]
    
emycharacter = [
    EnemyCharacter("enemy0.png", "凶暴な猫", emy_lifemax, emy_str, emy_movmax, \
                   emy_x, emy_y)
]        
        
if __name__ == '__main__':
    main()