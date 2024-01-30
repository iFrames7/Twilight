define a = Character("Arden", color="#846aca")
define h = Character("Hanna", color="#3f467e")
define e = Character("Evan", color="#f0eee8")
define f = Character("Felix", color="#ed819f")
define k = Character("Katherine", color="#435f21")
define fr = Character("Freya", color="#9a201b")

default timer_range = 0
default timer_jump = 0

default sprite_size = 0.5
default sprite_handout_size = 0

default freya_counter = 0
default evan_counter = 0

label start:

    jump playtest

    jump prologo

label playtest:
    "Esta pantalla es para fines de playtest y será eliminada en la version final."

    "Elige el capítulo al que quieras saltar:"

    label seleccion:
        menu:
            "Prologo":
                jump prologo

            "Cap 1":
                jump cap1

            "Cap 1 Sides":
                jump cap1_sideselection

            "Cap 2 True":
                jump cap2true

            "Cap 2 True Sides":
                jump cap2true_sideselection