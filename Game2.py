import kivy
from kivy.lang import Builder

kivy.require('2.0.0')

from kivy.core.window import Window

###########################################
######-----CREATE SCREEN SIZE----##########
# -----------------------------------------
Window.size = (667, 375)
# -----------------------------------------
###########################################
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock, CyClockBase
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty, BooleanProperty
from kivy.vector import Vector
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.storage.jsonstore import JsonStore
from kivy.core.audio import SoundLoader
import random
import string
import json


#################################################
###############----CLASSES----###################
# ----START_MENU----
class MenuWidget(RelativeLayout):
    pass


# ----GAMEOVER_SCREEN----
class GameOver(RelativeLayout):
    pass


# ----SETTINGS_SCREEN----
class Screen_op(RelativeLayout):
    pass


# ----RANDOM_TICKER----(may delete)
# Function was to be like a counter to make the
# game function. Function was improved by using
# the "self.Timer" function. which counts in milliseconds.
##########################################################
# As of right now ticker has no function in game
# will analyze further before deletion.
##########################################################
class Ticker(Widget):
    pass


# ----BACKGROUND----
# creates flashing design in background
class Background(Widget):
    background_source = StringProperty('atlas://Background_sprite.atlas/frame1')
    Sprites_Anim = 'atlas://Background_sprite.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6', 'frame7', 'frame8']
    frame_count = 0

    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.5)

    # Animate central background sprite

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.background_source = self.Sprites_Anim + key


# ----Animated_central_background----
# Repeat of last class
class BackgroundTwo(Widget):
    background2_source = StringProperty('atlas://Background_2-12.atlas/frame1')
    Sprites_Anim = 'atlas://Background_2-12.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6', 'frame7', 'frame8']
    frame_count = 0

    def __init__(self, **kwargs):
        super(BackgroundTwo, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.5)

    # Animate central background sprite

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.background2_source = self.Sprites_Anim + key


# ----SIDE_OF_CENTRAL_BACKGROUND----
# Repeat of last class
class BackgroundThree(Widget):
    background3_source = StringProperty('atlas://Background3.atlas/frame1')
    Sprites_Anim = 'atlas://Background3.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6', 'frame7', 'frame8']
    frame_count = 0

    def __init__(self, **kwargs):
        super(BackgroundThree, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.5)

    # Animate central background sprite

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.background3_source = self.Sprites_Anim + key


# ----SIDE_OF_CENTRAL_BACKGROUND----
class Background4(Widget):
    pass


# ----ENTIRE_MOVING_BACKGROUND----
# Background that displays entire level system
class Depth(Widget):
    pass


# ----CLOUDS----
# These classes contain objects that contain cloud art
# for the game.
######################################################
#      \\\\\\\\\\\\\\\\            ////////////////
#       \\\\\\\\\\\\\\\\         ////////////////
#        \\\\\\\\\\\\\\\\      ////////////////
#         \\\\\\\\\\\\\\\\   ////////////////
#          \\\\\\\\\\\\\\\\////////////////
######################################################
class WhiteCloudBack(Widget):
    pass


class WhiteCloudFront(Widget):
    pass


class PurpleCloudBack(Widget):
    pass


class PurpleCloudFront(Widget):
    pass


class RedCloudBack(Widget):
    pass


class RedCloudFront(Widget):
    pass


class BlueCloudFront(Widget):
    pass


class BlueCloudBack(Widget):
    pass


class BlackCloudBack(Widget):
    pass


class BlackCloudFront(Widget):
    pass


class BWCloudBack(Widget):
    pass


class BWCloudFront(Widget):
    pass


# Scrolling background
class Scrolling_one(Widget):
    pass


class Scrolling_two(Widget):
    pass


class Cloud_one(Widget):
    pass


##########################################################
#         /////////////////\\\\\\\\\\\\\\\\\\\
#       /////////////////   \\\\\\\\\\\\\\\\\\\
#     /////////////////      \\\\\\\\\\\\\\\\\\\
#   /////////////////         \\\\\\\\\\\\\\\\\\\
# /////////////////            \\\\\\\\\\\\\\\\\\\
##########################################################
# ----Vines----(might delete)
# Vines on top screen. still need to develop score in middle
class Roof(Widget):
    pass


# ----Counter----(might delete)
# same as ticker
# Function has been updated using timer
###########################################################
# will analyze before deletion
class Counter(Widget):
    pass


class Walls(Widget):
    pass


# Create Enemy
class Enemy(Widget):
    player1 = ObjectProperty(None)
    new_source = StringProperty('atlas://Lazarous.atlas/frame1')
    Sprites_Anim = 'atlas://Lazarous.atlas/'
    frames = ['frame1', 'frame1', 'frame3', 'frame4', 'frame5', 'frame6', 'frame7',
              'frame8']
    frame_count = 0

    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, .2)
        Clock.schedule_interval(self.shuffle, 59 / 60)

    # Animate Enemy Sprite Sheet

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.new_source = self.Sprites_Anim + key

    # Random speed for Enemy

    def shuffle(self, dt):
        dec = random.randint(-4, 0)
        self.x += dec


# Placeholder for future sprite creations
class Sprites(Widget):
    pass


# Player 1
class PlayerOne(Widget):
    my_source = StringProperty('atlas://Sprites.atlas/frame1')
    Sprite_Anim = 'atlas://Sprites.atlas/'
    frames = ['frame1', 'frame1', 'frame3', 'frame4', 'frame5', 'frame6', 'frame7']
    frame_count = 0

    def __init__(self, **kwargs):
        super(PlayerOne, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.2)

    # Animates player sprite sheet

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.Sprite_Anim + key

    # Defines game gravity
    def gravity(self, spikes):
        if self.y > spikes.y:
            self.y -= 2

    # Check collision


class Player1_Phantom(Widget):
    my_source = StringProperty('atlas://Player1_Phantom.atlas/frame1')
    Phantom_Anim = 'atlas://Player1_Phantom.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5']
    frame_count = 0

    def __init__(self, **kwargs):
        super(Player1_Phantom, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.1)

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.Phantom_Anim + key

    # def position(self, dt):
    # self.player1_phantom.x = self.player1.x
    # self.player1_phantom.y = self.player1.y


class Phantom_Anim2(Widget):
    my_source = StringProperty('atlas://Phantom_Anim2.atlas/frame1')
    Phantom2 = 'atlas://Phantom_Anim2.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6',
              'frame7', 'frame8']
    frame_count = 0

    def __init__(self, **kwargs):
        super(Phantom_Anim2, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.2)

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.Phantom2 + key


class Vanishing_Flames(Widget):
    my_source = StringProperty('atlas://Vanishing_Flames.atlas/frame1')
    flames2 = 'atlas://Vanishing_Flames.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6',
              'frame7', 'frame8']
    frame_count = 0

    def __init__(self, **kwargs):
        super(Vanishing_Flames, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.1)

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0

        key = self.frames[self.frame_count]
        self.my_source = self.flames2 + key


class Vatality_orbs(Widget):
    my_source = StringProperty('atlas://Vatality_orbs.atlas/frame1')
    Orb_Anim = 'atlas://Vatality_orbs.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5',
              'frame6']
    frame_count = 0

    def __init__(self, **kwargs):
        super(Vatality_orbs, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.3)

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.Orb_Anim + key

    # def health(self):
    #   orbs_list = []
    #  num_orbs = 5
    # for i in range(num_orbs):
    #    orbs_list.append(self)

    # orb_start_x = 200
    # orb_start_y = Window.height / 2
    # orb_number = 0

    # for orb in orbs_list:

    #    x = orb_start_x + (20 * orb_number)
    #   y = orb_start_y
    #  orb.pos = (x, y)
    # orb.size = (50, 50)
    # orb_number += 1
    # print(orb.pos)


# Hand of the damned animation
class Hand_ov(Widget):
    my_source = StringProperty('atlas://Hand.atlas/frame1')
    ov_Anim = 'atlas://Hand.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5',
              'frame6', 'frame7']
    frame_count = 0
    vertical = random.randint(-100, 101)

    def __init__(self, **kwargs):
        super(Hand_ov, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.3)
        Clock.schedule_interval(self.spawn, random.randint(1, 5))

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.ov_Anim + key

    def spawn(self, dt):
        self.y += self.vertical


class Hand_ov_two(Widget):
    my_source = StringProperty('atlas://Hand.atlas/frame1')
    ov_Anim = 'atlas://Hand.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5',
              'frame6', 'frame7']
    frame_count = 0
    vertical = random.randint(-100, 101)

    def __init__(self, **kwargs):
        super(Hand_ov_two, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.3)
        Clock.schedule_interval(self.spawn, random.randint(1, 5))

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.ov_Anim + key

    def spawn(self, dt):
        self.y += self.vertical


class OrbsPowerUP(Widget):
    my_source = StringProperty('atlas://Vatality_orbs.atlas/frame1')
    Orb_Anim = 'atlas://Vatality_orbs.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5',
              'frame6']
    frame_count = 0
    vertical = random.randint(-500, 500)

    def __init__(self, **kwargs):
        super(OrbsPowerUP, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, 0.3)
        Clock.schedule_interval(self.spawn, random.randint(1, 5))

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.Orb_Anim + key

    def spawn(self, dt):
        self.y += self.vertical


class Flames_Ground(Widget):
    my_source = StringProperty('atlas://Flames_Ground.atlas/frame1')
    Fire_Anim = 'atlas://Flames_Ground.atlas/'
    frames = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6',
              'frame7', 'frame8', 'frame9', 'frame10', 'frame11', 'frame12']
    frame_count = 0


    def __init__(self, **kwargs):
        super(Flames_Ground, self).__init__(**kwargs)
        Clock.schedule_interval(self.animation, .3)

    def animation(self, dt):
        self.frame_count += 1
        if self.frame_count >= len(self.frames):
            self.frame_count = 0
        key = self.frames[self.frame_count]
        self.my_source = self.Fire_Anim + key

# Floor spikes
class Spikes(Widget):
    pass

    # Floor movement


# Will be developed to keep score
class Score(Widget):
    def keeper(self):
        store = JsonStore('HighScores.json')
        store.put(self.score)

        if store.exists(self.score):
            print(self.score)


class Settings_button(Widget):
    pass


class Curtain(Widget):
    pass


class Game_Controller(Widget):
    Left = .5
    Up = .5
    Down = .5
    Right = .5


# TITLES, LABELS, AND LOADING SPRITES
class Title_Screen(Widget):
    pass


class First_fall(Widget):
    pass


# THIS CLASS CONTAINS GAME ARGUMENTS
#################################################################

class GameOn(Widget):
    ###################################################
    ########## GAME OBJECTS AND PROPERTIES ############
    # ----PLAYERS, ENEMIES, & MISC----
    player1 = ObjectProperty(None)
    phantom_1 = ObjectProperty(None)
    flames2 = ObjectProperty(None)
    hand_ov_damned = ObjectProperty(None)
    enemy_1 = ObjectProperty(None)
    orb_1 = ObjectProperty()
    second_hand = ObjectProperty(None)
    power_up_01 = ObjectProperty(None)
    ticker = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    flames_bottom = ObjectProperty(None)
    # ----MENUS/CONFIG----
    state_game_over = False
    game_started = False
    game_over_screen = False
    menu_screen = True
    set_screen = False
    powerup_ON = False
    powerup_animations = False
    menu_1 = ObjectProperty()
    gameover_1 = ObjectProperty()
    screen_1 = ObjectProperty()
    icon_01 = ObjectProperty()
    main_title = ObjectProperty(None)
    level_2 = ObjectProperty(None)
    # ----BACKGROUND & FOREGROUND-----
    background = ObjectProperty(None)
    spikes1 = ObjectProperty(None)
    blue_cloud_b = ObjectProperty(None)
    blue_cloud_f = ObjectProperty(None)
    purple_cloud_b = ObjectProperty(None)
    purple_cloud_f = ObjectProperty(None)
    red_cloud_b = ObjectProperty(None)
    red_cloud_f = ObjectProperty(None)
    black_cloud_b = ObjectProperty(None)
    black_cloud_f = ObjectProperty(None)
    bw_cloud_b = ObjectProperty(None)
    bw_cloud_f = ObjectProperty(None)
    white_cloud_b = ObjectProperty(None)
    white_cloud_f = ObjectProperty(None)
    wall_guts = ObjectProperty(None)
    shadows = ObjectProperty(None)
    blue_cloud = ObjectProperty(None)
    # ----SCORE----
    scores = NumericProperty()
    score = NumericProperty(0)
    score_AddSub = NumericProperty(0)
    timer_AddSub = NumericProperty(0)
    timer = NumericProperty(0)
    song_time = NumericProperty(0)
    keeper = NumericProperty(0)
    strobe = False
    seconds = NumericProperty(0)
    flame_timer = NumericProperty(0)

    powerup_TIMER = NumericProperty(0)
    powerup_difScore = NumericProperty(0)
    # ----TEST-----
    # Blackout is a foreground screen to create a black
    # store effect, when ever player clicks on screen
    blackout = ObjectProperty(None)
    # ----TEST----
    # Untested, easier way to create movement of enemies, player, and background/foreground
    Left = -.5
    Up = .5
    Down = -.5
    Right = .5
    # ----STORAGE----
    store = JsonStore('HighScores.json')
    # Ability to save high scores into a json file
    # future capability is to be able to extract information
    # on command, so player can see their top 3 high score.
    #######################################################
    # second capability would be for json file to be sent to a database
    # so multiple players can see high score.
    #######################################################
    # json file should also be able to erase unused data.
    # so after a higher high score is presented, old high score
    # is erased.
    ####################################################
    ################  TEST CONTROLS  ###################
    # --------------------------------------------------
    TEST_OFF = True

    # When triggered True, disables collision detection
    # primary function is to help developer debug game
    # --------------------------------------------------
    ####################################################
    ############ GAME FUNCTION CONTROLS ################
    # --------------------------------------------------
    Disable_EnemyCollision = False

    # When triggered, disables collision detection
    # against enemy characters
    # --------------------------------------------------
    Disable_ScreenCollision = False

    ####################################################
    ####################################################
    # --------------------------------------------------
    # ----TEST GAMEOVER MENU----
    Menu_Pos_Gameover = False
    Set_Screen_Pos = False
    #
    #

    def update(self, dt):
        ########################################
        ##### NOTES: IDEAS #####################
        # --------------------------------------
        # ----Soundtrack Ideas----
        # Idea #1 ----Levels----
        # Instead of having a single track playing
        # Trim the track so that single segments can be looped
        # Indefinitely.
        # Since tracks are being controlled by a timer, make tracks loop if a condition is not met
        # exmaple:
        #   if timer is >= 500:
        #       pass
        #   if timer is <= 0:
        #       sound_timer = 0
        #   #This will make the timer reset and play first track.
        #   #ISSUE: still have not figured out how to end a track.
        #   ------------------------------------------------------
        #  Next step to this idea would be to make everything continue, loop, or end.
        #   Example:
        #   if sound_timer <= 2:
        #        First = SoundLoader.load("example")
        #        First.play()
        #   if sound_timer <= 500:
        #       Second = SoundLoader.load("example")
        #       Second.play()
        #   #What this does is now when player starts over, the first song will play
        #   #If player does not start over, the next track starts.
        #   #Issue: with this method, when player starts over, if current track has not finished.
        #   #Then tracks will over lap.
        #   Solution?:
        #       make tracks smaller to make overlapping less noticeable.
        #       figure out how to end tracks when conditions are met.
        #
        # Idea #2 ----Sound Effects----
        # Mix sounds so that either effects are louder or turn down
        # main sound so effects can be heard.
        #
        #
        # ----Menu Issue Solution Idea----(solved)
        # Instead of using x -= 700 and x += 700 to move all menus
        # back and forth, which causes an issue when we get a double register
        # (another bug). What should be done is a boolean that when toggled true
        # will make menu pos example:
        #       visibility = True
        #       if visibility:
        #           self.menu.x.pos = 0
        #       if not visibility:
        #           self.menu.x.pos = -1000
        # ----Show High Scores or Save Progress----(almost solved)
        # Figure out a way to utilize JSON file to save Data, so far when using
        # JSON, all data is saved but when pulled out, only recent data is pulled.
        # Find a way to get accurate High Score Displays, and to be able to save
        # Progress.
        # ----Show Level Names----(In progress)
        # Idea to show level names by creating the level name on
        # photoshop and then adding the png to a class with zero opacity
        # once player has survived for amount of seconds
        # level name is displayed.
        #
        # two ways of doing this would be:
        # if seconds >=1000:
        #     first_level_display.opacity = 1
        # if seconds >= 1200:
        #   first_level_display.opacity -= .1
        #
        # second way would be (definitely more code, but its cleaner):
        # if seconds >= 1000:
        #   first_level_display = True
        # if first_level_display:
        #   first_level_display.opacity = 1
        #   display_seconds += 1
        # if display_seconds >= 100:
        #   first_level_display = False
        #   display_seconds = 0
        # if not first_level_display:
        #   first_level_display.opacity -= .1
        #
        #
        #
        # ----Create Orbs----
        # Idea to create orb sprites that float and glow on background
        # with changing opacity and depths
        # this will create a game illusion, and create a better atmosphere
        # ----MORE CHARACTERS----
        # There needs to be more characters in the game
        # Idea to create some characters now and see if future characters
        # can be created after game release
        # ----Loading Screen Idea----
        # Idea to make a loading screen for transitions
        # between game and menus. Just as stated below but with
        # extra features.
        # for example using Random.Randint to determine how many
        # seconds an animation plays. as we all know kivy does
        # not need loading time but this will make transitions way
        # smoother.
        # Example:
        #            if self.transition = True:
        #         #               self.animation.opacity = 1
        #         #               self.firstMenu.opacity = 0
        #         #           >>> self.firstMenu.x -= 500 <<<(This one may need to be taken,
        #         # out of "if" statement, and executed inside of button pressed)
        #         #               self.secondMenu.opacity = 0
        #         #               self.transitionTimer += 1
        #         #           if self.transitionTimer >= 30:
        #         #               self.animation.opacity = 0
        #         #               self.secondMenu.opacity = 1
        #         #               self.secondMenu.x += 500
        #         #               self.transition = False
        #         #               self.transitionTimer = 0
        #
        #       this was taken from below
        #       the only addition would possibly be
        #       on self.transitionTimer.
        #       instead of >= 30
        #       we would use >= random.randint(1, 30)
        #       and then fix speed with schedule clock
        # ----Menu/Game Transitions----
        # Idea to create an animation or sprite
        # When switching between menus and or
        # Game modes
        # FIRST IDEA:
        # Create a sprite with movement using .atlas
        # Then create a transition timer
        # for Example:
        #           if self.transition = True:
        #               self.animation.opacity = 1
        #               self.firstMenu.opacity = 0
        #           >>> self.firstMenu.x -= 500 <<<(This one may need to be taken,
        # out of "if" statement, and executed inside of button pressed)
        #               self.secondMenu.opacity = 0
        #               self.transitionTimer += 1
        #           if self.transitionTimer >= 30:
        #               self.animation.opacity = 0
        #               self.secondMenu.opacity = 1
        #               self.secondMenu.x += 500
        #               self.transition = False
        #               self.transitionTimer = 0
        #
        # ----Power Up Timer----
        # Idea to create a timer for power up
        # Primary function would be to limit
        # powerup to a limited amount of seconds
        # before removing powerup effects.
        # prevents power up from being in effect
        # entire time.
        #   for Example:
        #       ####----CONDITIONS----####
        #       if self.player.collide_widget(self.powerupOrb):
        #           self.powerup_ON = True
        #       if self.powerupTimer >= 30:
        #           self.powerup_ON = False
        #       ####----EXECUTION----####
        #       if self.powerup_ON:
        #           >>><<< (Here you can add power ups)
        #           (IDEA: you can also add atlas animation during powerup)
        #           self.powerupTimer += 1
        #       if not self.powerup_ON:
        #           self.powerupTimer = 0
        # ----------------------
        # SECOND idea for timer:
        # create artistic effects like plasma or lighting
        # around Player to indicate that power up is active
        # ----Power up PERKS-----
        # 1. Increase in score multiple
        # 2. Decrease enemy speed
        # 3. Increase Player Visuals
        # ----Enemy Attacks----(not probable)
        # Idea 1, enable enemies to shoot projectiles while playing game. maybe towards higher levels
        # if Power Up Timer idea works, method should be able to be applied to attacks as well.
        # REQUIREMENTS:
        # Sprite sheet needs to be completed to work
        # create sprite sheet using photoshop. sprite sheets need to be perfect, so they can be used in
        # unity in the near future.
        ########################################
        ##### NOTES: TROUBLE SHOOTINGS ########
        # ----New Glitch (Menu Logo not erasing)----
        # This glitch contains two things, the menu logo stays stuck on app
        # regardless of Menu status. Secondary glitch, Gameover menu is stuck with
        # zero opacity, but it is still clickable in middle of screen.
        # solution, check out all Menu settings, there may be an overlooked section that
        # is causing problems.
        # --------------------------------------
        # There is a new menu glitch, When player falls, menu disappears
        # When clicking on options menu button to solve problem, that menu
        # also disappears...
        # continued...
        # Glitch is still unresolved, idea 1:
        # create a boolean, if any menu goes beyond given x distance
        # activate boolean to make that menu go back.
        # and once menu goes back, trigger that boolean back to false
        # --------------------------------------
        # White cloud after first fall wont disappear after transition
        # ,also need to check if white clouds are moving properly after
        # , first fall
        # NEW GLITCH: cloud spawns after restart game(working on, check again)
        ########################################
        # Double GAME OVER GLITCH(probably solved)
        ########################################
        # ORB POWERUP GLITCH
        # ---------------------------------------
        # Orb (powerup) seems glitched and spawns randomly and goes up
        # instead of going toward player direction.
        # Idea #1: fix spawn speed (might need to remove randint)
        # Idea #2: make it move like the enemies( RIGHT TO LEFT, With random jumps)
        ########################################
        # THIRD MENU IDEA (DONE)
        # --------------------------------------
        # idea 1, add a settings icon that summon third menu(DONE)
        ########################################
        # Impossible GLITCH
        # ---------------------------------------
        # idea 1, make so that whenever two enemies are
        # close together in Y axis, space is added
        # so it is possible for a player to be able to
        # clear obstacle
        # ----------------------------------------
        ##########################################
        # HIGH SCORE
        # idea 1, add a json file that saves high score after
        # game over. then have a code that pulls high score and
        # displays it on gameover screen.
        # ----------------------------------------
        # idea 2, same as first idea but also add a tab
        # where player can manually look at their high score.
        # (just need to figure out how to delete lesser scores
        # after achieving greater scores.
        # -----------------------------------------
        # idea 3, same as previous ideas but adding a database
        # for everything so players can compete for high score.
        ###########################################
        # Game Over conditions

        ##########################
        #####-----#TEST#----######
        #-------------------------
        self.song_time += 1
        Intro = False


        if self.song_time <= 2:

            First_song = SoundLoader.load('Intro_song.wav')
            First_song.play()
        # Idea: If I am unable to change order of songs in accordance to menus then
        # Continue using timer.
        # Example:
        #       if self.song_time <= 2:
        #           First_song = SoundLoader.load ('Intro_song.wav')
        #           First_song.play()
        #       if self.song_time <= 20000: ### Check song duration in Python Seconds ###
        #           Second_song = SoundLoader.load('example')
        #           Second_song.play()



        if self.Menu_Pos_Gameover:
            self.gameover.x = 300
            self.gameover.opacity = 1
        if not self.Menu_Pos_Gameover:
            self.gameover.x = -700
            self.gameover.opacity = 0
        if self.state_game_over:
            self.Menu_Pos_Gameover = True
        if not self.state_game_over:
            self.Menu_Pos_Gameover = False

        if self.Set_Screen_Pos:
            self.screen_op.x = 300
        if not self.Set_Screen_Pos:
            self.screen_op.x = -700

        if self.set_screen:
            self.Set_Screen_Pos = True
        if not self.set_screen:
            self.Set_Screen_Pos = False
        #--------------------------
        ###########################
        if self.state_game_over:
            # ----Bonus_Score----
            # Bonus for amount of timer player stays alive in game
            # score_AddSub is a Numeric Property that will be used to keep
            # track of score addition or subtractions speed
            # by adding everything to one property
            # entire numeric property should be able to be removed with a single
            # command of "-= self.score_AddSub"
            if self.timer >= 0:
                self.timer -= self.timer_AddSub
                self.score += self.score_AddSub
                self.timer_AddSub = 10
                self.score_AddSub = 10

            if self.timer >= 2000:
                self.timer_AddSub = 50 + self.timer_AddSub
                self.score_AddSub = 50 + self.score_AddSub

            if self.timer >= 5000:
                self.timer_AddSub = 100 + self.timer_AddSub
                self.score_AddSub = 100 + self.score_AddSub

            if self.timer >= 10000:
                self.timer_AddSub = 200 + self.timer_AddSub
                self.score_AddSub = 200 + self.score_AddSub

            if self.timer >= 10000:
                self.timer_AddSub = 200 + self.timer_AddSub
                self.score_AddSub = 200 + self.score_AddSub

            if self.timer >= 50000:
                self.timer_AddSub = 500 + self.timer_AddSub
                self.score_AddSub = 500 + self.score_AddSub

            if self.timer >= 100000:
                self.timer_AddSub = 1000 + self.timer_AddSub
                self.score_AddSub = 1000 + self.score_AddSub

            if self.timer >= 1000000:
                self.timer_AddSub = 10000 + self.timer_AddSub
                self.score_AddSub = 10000 + self.timer_AddSub

            if self.timer <= 0:
                self.timer = 0
                self.timer_AddSub = 0
                self.score_AddSub = 0

        if self.menu_screen:
            self.menu.opacity = 1
            self.menu.x = 280
            self.Menu_Pos_Gameover = False
            self.set_screen = False
            self.game_over_screen = False
            self.game_started = False
            self.state_game_over = False
            self.player1.y = 150
            self.player1.x = 200


        if not self.state_game_over and not self.set_screen  and not self.Menu_Pos_Gameover and self.menu_screen:
            self.title_screen.opacity = 1
            self.gameover.x = -700
        if not self.state_game_over and not self.menu_screen and not self.set_screen and self.game_started:
            ####################################
            # Background moving
            self.timer += 1
            self.title_screen.opacity = 0
            self.depth.x += self.Left
            self.depth.opacity = 1
            self.scrolling_one.x -= 30
            self.scrolling_two.x -= 30
            self.cloud_one.x -= 30
            self.enemy.shuffle(self)
            self.player1.gravity(self.spikes)
            # ENEMY SPACING
            if self.hand_ov.collide_widget(self.hand_ov_two):
                self.hand_ov.y += 50
            if self.hand_ov_two.collide_widget(self.hand_ov):
                self.hand_ov_two.y -= 50
            if self.hand_ov_two.collide_widget(self.enemy):
                self.hand_ov_two.y += 50
            if self.hand_ov.collide_widget(self.enemy):
                self.hand_ov.y += 50
            if self.hand_ov.y < self.spikes.y + 200:
                self.hand_ov.y += 50
            if self.hand_ov_two.y > self.spikes.y + 110:
                self.hand_ov_two.y -= 50

            ###################################
            if self.enemy.x < self.player1.x - 200:
                self.enemy.x += random.randint(700, 1500)
            if self.enemy.x > self.player1.x + 1500:
                self.enemy.x -= 1000

            if self.hand_ov_two.y < self.spikes.y:
                self.hand_ov_two.y += 200
            if self.hand_ov_two.y > self.spikes.y + 300:
                self.hand_ov_two.y -= 200
            if self.hand_ov_two.x < self.player1.x - 200:
                self.hand_ov_two.x += random.randint(2000, 6000)
            # Levels
            if self.timer <= 500:
                pass
                # self.orbspowerup.opacity = 0
            if self.timer >= 500:
                self.enemy.x -= 2
                # self.orbspowerup.y += 3
                # self.orbspowerup.opacity = 1
                # if self.timer >= 800 and self.orbspowerup.y >= self.spikes.y + random.randint(20, 290):
                pass
                # self.orbspowerup.x -= 5

            # if self.player1.x > self.hand_ov.x and self.score >= 500:
            #   self.score += 5
            # if self.player1.x > self.enemy.x and not self.enemy.x < self.player1.x - 50 and self.score >= 500:
            #   self.score += 5
            # if self.player1.x > self.hand_ov.x and self.score >= 500:
            #   self.score += 5
            # Level 2
            if self.timer >= 1000:
                self.enemy.x -= 2
                self.hand_ov.x -= 5
            if self.hand_ov.y < self.spikes.y:
                self.hand_ov.y += 200
            if self.hand_ov.y > self.spikes.y + 300:
                self.hand_ov.y -= 200
            if self.hand_ov.x < self.player1.x - 200:
                self.hand_ov.x += random.randint(2000, 6000)

            # if self.player1.x > self.hand_ov.x and self.score >= 2000:
            #   self.score += 5
            # if self.player1.x > self.enemy.x and not self.enemy.x < self.player1.x - 50 and self.score >= 2000:
            #   self.score += 5
            # Level 3
            if self.timer >= 2500:
                self.enemy.x -= 2
                self.hand_ov.x -= 2
            # if self.player1.x > self.hand_ov_two.x and self.score >= 500:
            #   self.score += 2
            if self.timer >= 5000:
                self.hand_ov_two.x -= 4
                self.enemy.x -= 2
                self.hand_ov.x -= 2
            # First Fall
            if self.timer >= 8200:
                self.first_fall.opacity += .1
                self.depth.x += self.Right
                self.depth.y += self.Up
                self.whitecloudback.opacity = 0
                self.whitecloudfront.opacity = 0
                if self.timer >= 8210:
                    self.whitecloudback.opacity = .3
                    self.whitecloudfront.opacity = .3
                if self.timer >= 8220:
                    self.whitecloudback.opacity = .5
                    self.whitecloudfront.opacity = .5
                if self.timer >= 8230:
                    self.whitecloudback.opacity = .7
                    self.whitecloudfront.opacity = .7
                if self.timer >= 8240:
                    self.first_fall.opacity -= .1
                    self.whitecloudback.opacity = 1
                    self.whitecloudfront.opacity = 1
                self.whitecloudback.y += .5
                self.whitecloudfront.y += .5
                self.whitecloudfront.x += .5
                if self.whitecloudback.y > self.spikes.y + 400:
                    self.whitecloudback.y -= 500
                if self.whitecloudfront.y > self.spikes.y + 400:
                    self.whitecloudfront.y -= 500
                if self.whitecloudfront.x > self.player1.x + 800:
                    self.whitecloudfront.x -= 2500
                # Incantation
            if self.timer >= 10100:
                self.whitecloudfront.x -= .5
                self.whitecloudfront.y -= .5
                if self.timer >= 10110:
                    self.whitecloudback.opacity = .9
                    self.whitecloudfront.opacity = .9
                if self.timer >= 10130:
                    self.whitecloudback.opacity = .7
                    self.whitecloudfront.opacity = .7
                if self.timer >= 10150:
                    self.whitecloudback.opacity = .5
                    self.whitecloudfront.opacity = .5
                if self.timer >= 10170:
                    self.whitecloudback.opacity = .3
                    self.whitecloudfront.opacity = .3
                if self.timer >= 10190:
                    self.whitecloudback.opacity = 0
                    self.whitecloudfront.opacity = 0
                self.depth.x += .5
                self.depth.y -= .5

            # Incantation Diagonal UP,LEFT(clouds should move DOWN,RIGHT)
            if self.timer >= 13400:
                self.depth.x -= .25
                self.depth.y -= .5
            # Incantation normal ( clouds move RIGHT)
            if self.timer >= 14400:
                self.depth.x += .25
                self.depth.y += .5
            # Second Fall ( clouds move UP, LEFT)
            if self.timer >= 18678:
                self.depth.x -= .5
                self.depth.y += .5
                # Blue clouds that float behind Skeleton Level
                # moving LEFT, UP
                self.bluecloudback.opacity = 1
                self.bluecloudback.x -= 1
                self.bluecloudfront.x -= 1
                self.bluecloudfront.y += 3
                self.bluecloudback.y += 2
                self.bluecloudfront.opacity = .5
                if self.bluecloudback.x < self.player1.x - 250:
                    self.bluecloudback.x += 1000
                if self.bluecloudback.y > self.spikes.y + 600:
                    self.bluecloudback.y -= 800
                if self.bluecloudfront.y > self.spikes.y + 600:
                    self.bluecloudfront.y -= 800
                if self.bluecloudfront.x < self.player1.x - 800:
                    self.bluecloudfront.x += 1000
                # Front blue clouds
            # HELLFROST (clouds move LEFT ONLY)
            if self.timer >= 21150:
                self.depth.x -= .5
                self.depth.y -= .5
                # Back blue clouds move only left
                self.bluecloudback.y -= 2
                self.bluecloudfront.y -= 2
                if self.bluecloudback.x < self.player1.x - 650:
                    self.bluecloudback.x += 1000
                if self.bluecloudback.y > self.spikes.y + 600:
                    self.bluecloudback.y -= 800
                if self.bluecloudfront.x < self.player1.x - 650:
                    self.bluecloudfront.x += 1000
                if self.bluecloudfront.y > self.spikes.y + 600:
                    self.bluecloudfront.y -= 800
            # HELLFROST UP(clouds move DOWN, LEFT)
            if self.timer >= 25150:
                self.depth.x += .5
                self.depth.y -= .5
                # Back blue clouds move down
                self.bluecloudback.y -= 2
                if self.bluecloudback.x < self.player1.x - 400:
                    self.bluecloudback.x += 1000

                if self.bluecloudback.y < self.spikes.y - 200:
                    self.bluecloudback.y += 800
            # HELLFROST Normal(CLOUDS MOVE ONLY LEFT)
            # Purple clouds should be added for Cosmic eye
            # (OPTIONAL) see if clouds can rotate around
            if self.timer >= 25600:
                self.depth.x -= .5
                self.depth.y += .5
                self.bluecloudback.y += 2
                self.purplecloudfront.x -= .2
            # THIRD FALL(PURPLE clouds should move ONLY UP)
            # ELIMINATE Blue Clouds
            if self.timer >= 29300:
                self.depth.x += .5
                self.depth.y += .5
                self.bluecloudback.x += 1
                self.bluecloudback.opacity = 0
                self.bluecloudfront.opacity = 0
            # VOID (BLACK CLOUDS MOVE RIGHT)
            if self.timer >= 32575:
                self.depth.x += .5
                self.depth.y -= .5
            # VOID Diagonal (Clouds move RIGHT, DOWN)
            if self.timer >= 34800:
                # minus x
                self.depth.y -= .5
                self.hand_ov.y += 1
            # VOID Normal (Clouds move RIGHT ONLY)
            if self.timer >= 36000:
                # plus x
                self.depth.y += .5
                self.hand_ov.y -= 1
            # FINAL FALL( FRONT CLOUDS MOVE UP, BACK CLOUDS MOVE LEFT)
            # (OTHER CLOUDS MOVE RIGHT)
            # Colors should be (RED, BLACK)
            if self.timer >= 40300:
                self.depth.x -= .5
                self.depth.y += .5
            # FORSAKEN (clouds move LEFT)
            # colors should be (BLACK)
            if self.timer >= 44176:
                self.depth.x -= .5
                self.depth.y -= .5
            # FORSAKEN UP(clouds move down)
            if self.timer >= 52265:
                self.depth.x += .5
                self.depth.y -= .5
            # FORSAKEN Normal(clouds move right)
            if self.timer >= 53787:
                self.depth.x += .5
                self.depth.y += .5
            # FORSAKEN DOWN (clouds move up)
            if self.timer >= 57200:
                self.depth.x -= .5
                self.depth.y += .5
            # FORSAKEN Normal (clouds move RIGHT)
            if self.timer >= 57800:
                self.depth.x += .5
                self.depth.y -= .5
            # FORSAKEN END(UP) (clouds change to WHITE color)
            # (Clouds move DOWN ONLY)
            if self.timer >= 61063:
                self.depth.x -= .5
                self.depth.y -= .5
            # FORSAKEN ENDING (NO MORE CLOUDS)
            if self.timer >= 63054:
                self.depth.x -= .5
                self.depth.y += .5
            # Final Level
            # Heart Ov Lament
            # CREATE A WHIRLPOOL OF CLOUDS
            if self.timer >= 65329:
                self.depth.x += .5
                self.cloud_one.x -= 3
                self.cloud_one.opacity = .7
            if self.cloud_one.x < self.player1.x - 1000:
                self.cloud_one.x += random.randint(2000, 5000)
                self.cloud_one.y += random.randint(0, 200)

            if self.cloud_one.y < self.player1.x - 100:
                self.cloud_one.y += 400
            if self.cloud_one.y > self.player1.x + 700:
                self.cloud_one.y -= 400
            if self.scrolling_two.x < self.player1.x - 4500:
                self.scrolling_two.x += random.randint(10000, 20000)
            if self.scrolling_one.x < self.player1.x - 4500:
                self.scrolling_one.x += random.randint(10000, 20000)
        if self.state_game_over:
            if self.enemy.x < self.player1.x + 1500:
                self.enemy.x += 300
            if self.hand_ov.x < self.player1.x + 1500:
                self.hand_ov.x += 600
            if self.hand_ov_two.x < self.player1.x + 1500:
                self.hand_ov_two.x += 600
            if self.orbspowerup.y >= self.spikes.y + 100:
                self.orbspowerup.y -= 600
            #if self.gameover.x > self.player1.x + 1200:
            #    self.gameover.x -= 600
            self.Menu_Pos_Gameover = True

        # (SAVE)?
        if not self.set_screen:
            if self.screen_op.x > self.player1.x:
                self.screen_op.x -= 600
            if self.screen_op.x > self.player1.x + 700:
                self.screen_op.x -= 1200
            self.curtain.opacity = 0
            self.game_started = True
            self.Set_Screen_Pos = False
        if self.set_screen:
            #if self.screen_op.x < self.player1.x:
            #    self.screen_op.x += 600
            #if self.screen_op.x > self.player1.x + 600:
            #    self.screen_op.x -= 600
            self.Set_Screen_Pos = True
            self.curtain.opacity = .9
            self.game_started = False
        if self.set_screen and not self.game_started:
            pass
        ###########################################
        # First Fall GLITCH
        # ------------------------------------------
        # To solve scrolling problem we need to add
        # Variables to movement EXAMPLE:
        #       LEFT = self.depth.x += 5
        #       Then during pause to keep game paused add
        #       self.LEFT -= self.LEFT
        #       This will be called GAME_CONTROLLER
        ####################################
        ###-------GAME_CONTROLLER-----######
        ####################################
        ####################################
        ###---------TEST_MODE--------#######
        ###                          #######

        if not self.TEST_OFF:
            # self.player1.x -= Window.width
            if not self.Disable_EnemyCollision:
                if self.player1.collide_widget(self.enemy) and not self.state_game_over:
                    self.state_game_over = True
                    self.game_started = False
                    self.gameover.opacity = 1
                    self.Menu_Pos_Gameover = True
                    self.player1.x -= Window.width
                    print('GameOver')
                    self.game_over_screen = True
                    print("YOU SURVIVED FOR:", self.timer, "SECONDS")
                    store = JsonStore('HighScores.json')
                    store.put('points', score=self.score + self.timer)
                    soulz = store.get('points')['score']
                    if store.exists('points'):
                        print("THIS IS YOUR SCORE:", self.score, "POINTS", "SOULZ:", soulz)



                if self.player1.collide_widget(self.hand_ov) and not self.state_game_over:
                    self.state_game_over = True
                    self.game_started = False
                    self.gameover.opacity = 1
                    self.Menu_Pos_Gameover = True
                    print('GameOver')
                    self.game_over_screen = True
                    self.player1.x -= Window.width
                    print("YOU SURVIVED FOR:", self.timer, "SECONDS")
                    store = JsonStore('HighScores.json')
                    store.put('points', score=self.score + self.timer)
                    soulz = store.get('points')['score']
                    if store.exists('points'):
                        print("THIS IS YOUR SCORE:", self.score, "POINTS", "SOULZ:", soulz)


                if self.player1.collide_widget(self.hand_ov_two) and not self.state_game_over:
                    self.state_game_over = True
                    self.game_started = False
                    self.gameover.opacity = 1
                    self.Menu_Pos_Gameover = True
                    print('GameOver')
                    self.game_over_screen = True
                    self.player1.x -= Window.width
                    print("YOU SURVIVED FOR:", self.timer, "SECONDS")
                    store = JsonStore('HighScores.json')
                    store.put('points', score=self.score + self.timer)
                    soulz = store.get('points')['score']
                    if store.exists('points'):
                        print("THIS IS YOUR SCORE:", self.score, "POINTS", "SOULZ:", soulz)

            if not self.Disable_ScreenCollision:
                if self.player1.y < self.spikes.height - 25 and not self.state_game_over:
                    self.state_game_over = True
                    self.game_started = False
                    self.gameover.opacity = 1
                    self.Menu_Pos_Gameover = True
                    print('Game Over')
                    self.game_over_screen = True
                    self.player1.x -= Window.width
                    print("YOU SURVIVED FOR:", self.timer, "SECONDS")
                    store = JsonStore('HighScores.json')
                    store.put('points', score=self.score + self.timer)
                    soulz = store.get('points')['score']
                    if store.exists('points'):
                        print("THIS IS YOUR SCORE:", self.score, "POINTS", "SOULZ:", soulz)

                if self.player1.y > self.spikes.y + 300 and not self.state_game_over:
                    self.state_game_over = True
                    self.game_started = False
                    self.gameover.opacity = 1
                    self.Menu_Pos_Gameover = True
                    print('Game Over')
                    self.game_over_screen = True
                    self.player1.x -= Window.width
                    print(self.timer)
                    print("YOU SURVIVED FOR:", self.timer, "SECONDS")
                    store = JsonStore('HighScores.json')
                    store.put('points', score=self.score + self.timer)
                    soulz = store.get('points')['score']
                    if store.exists('points'):
                        print("THIS IS YOUR SCORE:", self.score, "POINTS", "SOULZ:", soulz)
        ######################################
        # -----------ENEMY_COLLISION---------#
        # Remove Enemy Collisions from Test Mode
        # and add them to Disable_enemyCollision.
        # Will be leaving screen collisions intact
        # Inside of Screen collision
        #
        # Creating two new boolean functions
        #
        # ----Disable_EnemyCollision-----
        # Will be responsible for Enemy Collisions detection, When toggled true
        # Enemy Collisions detections will be turned off.
        #
        # ----Disable_ScreenCollision----
        # Will be responsible for Screen Collisions detections, When toggled true
        # screen collisions detection will be turned off.
        #
        # ----TEST_OFF----
        # Disable_EnemyCollision and Disable_ScreenCollision are going to be placed inside
        # this boolean for testing purposes.
        ######################################

        # Score Conditions
        if self.player1.x > self.hand_ov.x:
            self.score += 5
        if self.player1.x > self.enemy.x and not self.enemy.x < self.player1.x - 50:
            self.score += 1

        ###################################################################
        #######              POWER UP SETTINGS              ###############
        ###################################################################
        # ----POWERUP IDEAS----
        # (BOTTOM FLAMES)
        self.first_fall.opacity = 0
        self.flames_ground.opacity = 0
        # (PHANTOM POWERUP)
        self.player1_phantom.opacity = 0
        self.phantom_anim2.opacity = 0
        self.vanishing_flames.opacity = 0
        # Enables character to go past enemies without being hit
        # player turns into a phantom animation during powerup
        if self.player1.collide_widget(self.orbspowerup) and not self.state_game_over:
            self.powerup_ON = True
            self.Disable_EnemyCollision = True
            # self.score += 1000
            # self.enemy.x += 4
            # self.hand_ov.x += 4
            # self.orbspowerup.x -= 200
            # self.orbspowerup.opacity = 0
            self.orbspowerup.x += random.randint(5000, 15000) + self.powerup_difScore
            self.powerup_difScore += 3000
            self.orbspowerup.opacity = 0
            Power_sound = SoundLoader.load('Harmonic.wav')
            Power_sound.play()

            self.powerup_animations = True
        if self.powerup_ON and not self.state_game_over:
            self.score += 1
            self.powerup_TIMER -= 1
            self.orbspowerup.opacity = 0
            self.depth.opacity = .4
            self.hand_ov.opacity = .4
            self.hand_ov_two.opacity = .4
            self.enemy.opacity = .4
            self.player1.opacity = 0
            # self.orbspowerup.x -= 200
        if not self.powerup_ON:
            self.flame_timer = 0
        if self.powerup_animations:
            self.vanishing_flames.opacity = 1
            self.flame_timer += 1
        if self.flame_timer >= 50:
            self.powerup_animations = False
            self.vanishing_flames.opacity = 0
            self.player1_phantom.opacity = 0
            #### remember to reset this to 1
            self.phantom_anim2.opacity = 1


        if self.powerup_TIMER <= 0 or self.state_game_over:
            self.powerup_ON = False
            self.Disable_EnemyCollision = False
            self.powerup_TIMER = 1000
            self.orbspowerup.opacity = 1
            self.player1_phantom.opacity = 0
            self.phantom_anim2.opacity = 0
            self.player1.opacity = 1
            self.depth.opacity = 1
            self.hand_ov.opacity = 1
            self.hand_ov_two.opacity = 1
            self.enemy.opacity = 1

            # if self.orbspowerup.x < self.player1.x - 200:
            #    self.orbspowerup.x += 500
            #    self.orbspowerup.y -= 600
        #########################################################
        #############----ORB_POWERUP_MOVEMENT----################
        # -------------------------------------------------------
        # self.orbspowerup.y += 3
        if self.game_started and not self.state_game_over:
            self.orbspowerup.opacity = 1
            self.orbspowerup.x -= 10
        if self.state_game_over:
            self.orbspowerup.opacity = 0
        # y movement will need to be defined in orbspowerup CLASS
        # using clock method.
        # self.orbspowerup.y += random.randint(-100, 100)
        # ----CONDITIONS----
        if self.orbspowerup.y >= self.spikes.y + 300:
            self.orbspowerup.y -= random.randint(150, 500)
        if self.orbspowerup.y <= self.spikes.y + 15:
            self.orbspowerup.y += random.randint(150, 500)
        if self.orbspowerup.x <= self.player1.x - 200:
            self.orbspowerup.x += random.randint(2000, 4000)
            # if self.orbspowerup.y >= self.spikes.y + random.randint(100, 290):
            #    self.orbspowerup.x -= 5
            #    self.orbspowerup.y -= 3
        ####################################################################
        ####################################################################
        ####################################################################

    # /////////////////////////////////////////////////////////////////////
    #########################################################################
    ######_______________GAME MECHANICS_________________#####################
    ##########################################################################
    # def score_saver(self):
    #    print(self.timer)
    #    store = JsonStore('HighScores.json')
    #    store.put(self.score)
    #    if store.exists(self.score):
    #        print(self.score)
    def on_touch_down(self, touch):
        if not self.state_game_over and self.game_started:
            # print(self.timer)
            # store = JsonStore('HighScores.json')
            # store.put(self.score)

            # if store.exists(self.score):
            #   print(self.score)
            self.score += 1
            self.player1.y += 35

            # if self.strobe:
            #    self.opacity = .9

        return super(GameOn, self).on_touch_down(touch)

    def start_button_pressed(self):
        self.game_started = True
        self.state_game_over = False
        self.menu_screen = False
        self.gameover.opacity = 0
        self.Menu_Pos_Gameover = False
        self.player1.y = Window.height / 2
        self.player1.x = Window.width / 12
        self.score = 0
        self.timer = 0
        self.depth.pos = (0, -4500)
        self.set_screen = False
        Button_effect = SoundLoader.load('Button_effect.wav')
        Button_effect.play()
        #Intro = True
        #if Intro:
        #    Intro_song = SoundLoader.load('Intro_song.mp3')
        #    Intro_song.play()




    def settings_button_pressed(self):
        self.game_started = False
        self.menu_screen = False
        self.state_game_over = False
        self.set_screen = True
        Button_effect = SoundLoader.load('Button_effect.wav')
        Button_effect.play()

    def resume_button_pressed(self):
        # GAME START
        # during this window timer is set to zero
        # since timer is the main controller of this game
        # once resume button is pressed, game resumes
        # exactly where it left off


        self.game_started = True
        self.state_game_over = False
        self.menu_screen = False
        self.set_screen = False
        self.gameover.opacity = 0
        Button_effect = SoundLoader.load('Button_effect.wav')
        Button_effect.play()

    def restart_button_pressed(self):
        # RESTART GAME
        # just like previous, timer is set to zero
        # this button will set score to zero
        # this button will reset entire game coordinates
        self.game_started = True
        self.state_game_over = False
        self.menu_screen = False
        self.set_screen = False
        self.gameover.opacity = 0
        self.player1.y = Window.height / 2
        self.player1.x = Window.width / 12
        self.score = 0
        self.timer = 0
        self.depth.pos = (0, -4500)
        self.hand_ov.x += 600
        self.hand_ov_two.x += 600
        self.enemy.x += 600
        self.orbspowerup.pos = self.pos
        Button_effect = SoundLoader.load('Button_effect.wav')
        Button_effect.play()

    def menu_start(self):
        self.game_started = True
        self.menu_screen = False
        self.state_game_over = False
        self.menu.opacity = 0
        self.title_screen.opacity = 0
        self.menu.x -= 1000
        self.player1.y = Window.height / 2
        self.player1.x = Window.width / 12
        self.score = 0
        self.timer = 0
        self.depth.pos = (0, -4500)
        Button_effect = SoundLoader.load('Button_effect.wav')
        Button_effect.play()

    def test_button(self):
        pass

    def return_menu(self):
        self.set_screen = False
        self.game_started = False
        self.state_game_over = False
        self.menu_screen = True
        Button_effect = SoundLoader.load('Button_effect.wav')
        Button_effect.play()




        self.Menu_Pos_Gameover = False
        #self.gameover.x -= 600

        self.game_over_screen = False


        # SCORE

    def add_score(self):
        self.score += 1

    def health(self):
        pass


class MetalGame(App):
    def build(self):
        game = GameOn()
        Clock.schedule_interval(game.update, 1 / 60)
        return game


if __name__ == '__main__':
    MetalGame().run()
