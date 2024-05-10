label cap2bad:
    scene bg cap2screen with Fade(1.0, 1.5, 1.0)

    pause 2.5

    scene bg salonclases2 with Fade(1.0, 1.0, 1.0)

    "Mis ojos se abrieron lentamente y enfocaron la habitacion en la que me encontraba."

    "Es verdad"

    extend ", después de aquela situación, corrimos a escondernos a un salón."

    "Cuando regresaron mis sentidos, pude observar a las 3 personas en la habitación."

    show evan normal at left with dissolve

    "Un chico de cabellos blancos"

    show hanna llorar at center with dissolve
    
    extend ", una chica a la orilla del salon con sus ojos hinchados por tanto llorar"

    show felix manofrentepreocupado at right with dissolve
    
    extend " y finalmente el chico de cabellos rosados sentado en la mesa del maestro."

    "Todo es silencio, un silencio vacio que parecia ser inundado por el miedo de los otros."

    "¿Qué hacer en esta situación?"

    "Freya era quien nos guiaba... "

    extend "ahora estamos... "

    extend "solos..."

    label cap2bad_sideselection:
        scene bg salonclases2 with fade
        
        while repeticion < 2:
            menu:
                "Acercarse a Evan" if canKeepTalk_Evan:
                    if not hasTalked_Evan:
                        call cap2bad_evan1 from _call_cap2bad_evan1
                    else:
                        call cap2bad_evan2 from _call_cap2bad_evan2

                "Acompañar a Hanna" if not hasTalked_Hanna:
                    call cap2bad_hanna from _call_cap2bad_hanna

                "Platicar con Felix" if not hasTalked_Felix:
                    call cap2bad_felix from _call_cap2bad_felix

            if repeticion < 1:
                scene bg salonclases2 with fade

                "A pesar de aquella plática, el aula seguía en silencio... "
                
                extend "quizas debería acercarme a alguien más..."

            $ repeticion += 1

    jump cap3bad