label epilogotrue:
    scene bg epilogo with Fade(1.0, 1.5, 1.0)

    pause 2.5

    scene bg entradaescuela with Fade(1.0, 1.0, 1.0)

    play music "audio/epilogue.mp3" volume 0.25

    "Semanas habían pasado desde el incidente."

    "Es curioso cómo Katherine y Hanna ahora no existían, al menos no físicamente."

    "Aún puedo verlas a veces en sueños."
    
    "Les he contado sobre Evan y sobre Freya, se ponen felices cuando escuchan sobre mí y, a decir verdad, es muy bello poder hablar con alguien más."

    if evan_counter > 3:
        show evan feliz at center with dissolve:
            alpha 0.5

        "Evan sigue centrado en sus estudios."

        "Se ha vuelto un poco más sociable, quizás solo lo suficiente para convivir con sus compañeros del salón."

        "Conmigo... bueno, conmigo y con Freya ha tenido la confianza de quitarse el cubrebocas más seguido, no siempre, pero al menos es un avance."

        "Honestamente, me sorprende lo bien que él y Freya se llevan, uno pensaría que se la pasan peleando pero... verdaderamente se ve cómo se aprecian."

        "Agradezco poder conocerlo y salir de vez en cuando con él."

        "Tal vez... algun día tenga el valor suficiente para decirle lo que siento por él, aunque por el momento, solo dejaré que las cosas fluyan con naturalidad..."

        hide evan with dissolve
    
    if freya_counter > 3:
        show freya sonrisa at center with dissolve:
            alpha 0.5

        "Freya ya no es cien por ciento la misma, y de una buena manera."

        "Claro, sigue siendo estricta y peleándose con todo el mundo, pero al menos ya no impone sus ideales sobre los demás."

        "Ahora es más como un diálogo abierto."

        "Además, se ha tomado el tiempo de conocerme."

        "Solemos salir mucho a centros comerciales a comprar ropa porque según ella... tengo un estilo muy aburrido."

        "Pero para ser honestos, disfruto cada uno de los momentos que me ha regalado."

        hide freya with dissolve

    "Sobre Hanna y Katherine, les hicimos un pequeño funeral, solo nosotros tres..."

    "Por el momento, ellas solo han sido \"desaparecidas\" y es un caso que probablemente nunca se pueda resolver."

    "Pero, al menos nosotros sabemos la verdad."

    "¿Yo? Bueno... supongo que tengo más confianza..."

    "Invité a salir al chico que me gustaba... "

    extend "conocí a más gente... "

    extend "y ahora sí estoy tomando mis propias decisiones."

    "Es loco pensar que una sola experiencia pudo cambiar tanto en mi vida..."

    "Supongo que..." 

    "Este es el final..."

    "Pero... no uno feliz ni triste."

    "Solo un final."

    stop music fadeout 4.0

    scene bg black with Dissolve(3.5)

    pause 2.0

    return