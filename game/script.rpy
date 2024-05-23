init python:
    def dismiss_callback():
        renpy.play("sfx/dialog.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback

    config.menu_include_disabled = True

#Characters
define a = Character("Arden", color="#846aca")
define h = Character("Hanna", color="#3f467e")
define e = Character("Evan", color="#f0eee8")
define f = Character("Felix", color="#ed819f")
define k = Character("Katherine", color="#435f21")
define fr = Character("Freya", color="#9a201b")

define ef = Character("Felix?", color="#985065", what_font = "chiller.ttf", what_size = 45)

#Transitions
define openeyes = ImageDissolve("trans/eyeopen.png", 0.2)
define closeeyes = ImageDissolve("trans/eyeopen.png", 0.2, reverse=True)
define portal = ImageDissolve("trans/portal.png", 1.5)
define rportal = ImageDissolve("trans/portal.png", 0.75, reverse=True)

#Choice timer
default timer_range = 0
default timer_jump = 0

default sprite_size = 1

#True ending variables
default freya_counter = 0
default evan_counter = 0

default talk_hanna = False
default freya_cap3_talk = False
default evan_cap4_talk = False
default codigo_real = 4869

#Can you choose the route? variables
default canNormal = True
default canBad = True

#Bad ending variables
default hasTalked_Hanna = False
default hasTalked_Felix = False
default hasTalked_Evan = False
default canKeepTalk_Evan = True

default repeticion = 0

label start:
    stop music

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

            "Ruta True ending":
                jump true_selection

            "Ruta Bad ending":
                jump bad_selection

            "Ruta Normal ending":
                jump normal_selection


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

    label bad_selection:
        menu:
            "Cap 2 Bad":
                jump cap2bad

            "Cap 2 Bad Sides":
                jump cap2bad_sideselection

            "Cap 3 Bad":
                jump cap3bad

            "Cap 3 Bad Sides":
                jump cap3bad_sideselection

            "Cap 4 Bad":
                jump cap4bad
                
            "Epilogo Bad":
                jump epilogobad

            "{b}Regresar{/b}":
                jump selection

    label normal_selection:
        menu:
            "Cap 2 Normal":
                jump cap2normal

            "Cap 2 Normal Sides":
                jump cap2normal_sideselection

            "Cap 3 Normal":
                jump cap3normal

            "Cap 3 Normal Sides":
                jump cap3normal_sideselection

            "Cap 4 Normal":
                jump cap4normal

            "{b}Regresar{/b}":
                jump selection