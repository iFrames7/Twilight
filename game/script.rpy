﻿init python:
    def dismiss_callback():
        renpy.play("sfx/dialog.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback

    config.menu_include_disabled = True

define a = Character("Arden", color="#846aca")
define h = Character("Hanna", color="#3f467e")
define e = Character("Evan", color="#f0eee8")
define f = Character("Felix", color="#ed819f")
define k = Character("Katherine", color="#435f21")
define fr = Character("Freya", color="#9a201b")

define ef = Character("Felix?", color="#985065", what_font = "chiller.ttf", what_size = 45)

define openeyes = ImageDissolve("trans/eyeopen.png", 0.2)
define closeeyes = ImageDissolve("trans/eyeopen.png", 0.2, reverse=True)
define portal = ImageDissolve("trans/portal.png", 1.5)

default timer_range = 0
default timer_jump = 0

default sprite_size = 1

default freya_counter = 0
default evan_counter = 0

default talk_hanna = False
default freya_cap3_talk = False
default evan_cap4_talk = False
default codigo_real = 4869

default canNormal = False
default canBad = False

label start:
    camera:
        perspective True

    #jump playtest
    #Reenablea este ↑ jump cuando no sea la version demo y ocupes playtestear escenas

    jump prologo

label playtest:
    "Esta pantalla es para fines de playtest y será eliminada en la version final."

    "Elige el capítulo al que quieras saltar:"

    label selection:
        menu:
            "Prologo":
                jump prologo

            "Cap 1":
                jump cap1

            "Cap 1 Sides":
                jump cap1_sideselection

            "Ruta true ending":
                jump true_selection


    label true_selection:
        menu:
            "Cap 2 True":
                jump cap2true

            "Cap 2 True Sides":
                jump cap2true_sideselection

            "Cap 3 True":
                jump cap3true

            "Cap 3 True Sides":
                jump cap3true_sideselection

            "Cap 4 True":
                jump cap4true

            "Cap 4 True Sides":
                jump cap4true_sideselection

            "Cap 5 True":
                jump cap5true

            "Epilogo True":
                jump epilogotrue

            "{b}Regresar{/b}":
                jump selection