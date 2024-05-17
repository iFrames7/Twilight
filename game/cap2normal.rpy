label cap2normal:
    scene bg cap2screen with Fade(1.0, 1.5, 1.0)

    pause 2.5

    scene bg pasillo3twilight with Fade(1.0, 1.0, 1.0)

    "Recorrimos los pasillos de la escuela con velocidad."

    "No sabíamos si ese monstruo logró cruzar, o si nos seguía, pero seguímos corriendo."

    scene bg salonclases with dissolve

    "Finalmente, llegamos a un salón de clases."

    play sound "sfx/1doorbang.mp3" volume 0.75

    "Entramos y cerramos la puerta con rapidez."

    show freya normal at left
    
    show hanna normal at right
    
    with dissolve

    "Todos estaban recargados en la pared o sobre una mesa recuperando el aliento, incluido yo."

    "Evan se veía exhausto, pues era el único que se recostó totalmente sobre el suelo."

    show freya normalhabla with dissolve

    fr "Okay... creo que estamos seguros por ahora."

    e "¿Qué te hace creer eso? Ese monstruo estaba por romper las puertas de la cafetería."

    e "¿Cómo estás tan segura de que todo está bien?"

    show freya ladohabla with dissolve

    fr "Tsk."

    show hanna miedohabla with dissolve

    h "Chicos, por favor no peleen..."

    a "No... creo que Freya tiene razón. Si esa cosa nos hubiera seguido... quizás no hubiéramos llegado hasta aquí."

    show freya sonrisahabla with dissolve

    "Evan volteó a verme como si no creyera lo que estaba escuchando."

    "Seguía en el suelo..."

    fr "¡JA! ¿Lo ves?"

    show freya caderassonrisa with dissolve

    fr "Quizás puedas aprender algo de... "
    
    show freya caderaspreocupada2 with dissolve

    extend "umm..."

    a "Arden."

    show freya normalhabla with dissolve

    fr "Sí, claro, Arden."

    show felix manofrentepreocupadohabla at center 
    
    show hanna normal
    
    with dissolve

    f "Bueno, ¿y a dónde vamos ahora?"

    show freya pensarhabla with dissolve

    fr "Idealmente buscamos una salida, pero no podemos andar corriendo por ahí, ese monstruo nos atrapará si no tenemos un plan, y ahora sabemos que tampoco es seguro abrir puertas y divagar ciegamente..."

    show felix pensando2 with dissolve

    f "¿Crees que la salida sea el mismo lugar por el que entramos?"

    show freya normal with dissolve

    fr "¿La biblioteca? Ni hablar, no podemos regresar ahí, es muy peligroso."

    show freya apunta2 with dissolve

    fr "Además, no es como que \"llegáramos\" aquí, se siente más como si simplemente hubiéramos aparecido aquí. No tendría ningún sentido."

    show hanna miedohabla with dissolve

    h "Bueno, yo creía que sería bueno regresar a la biblioteca..."

    show freya preocupada with dissolve

    fr "¿Lo crees?"

    a "Y...yo también lo creo."

    show freya lado with dissolve

    "Lo único que recibí por mi comentario fue la fría mirada de Freya."

    "Solo volteé hacia el suelo nuevamente."

    show felix sonrisahabla with dissolve

    f "Sí, tendría sentido."

    show felix dedohabla with dissolve

    f "Si queremos saber más sobre el lugar, quizás deberíamos regresar a donde todo empezó."

    show freya normal with dissolve

    "Freya tomó un fuerte suspiro."

    "No se veía del todo convencida, pero la mirada de Hanna la hizo dudar."

    fr "De acuerdo."

    show freya pensarhabla with dissolve

    fr "Pero no creo que sea bueno movernos y explorar sin un buen plan, hay que prepararnos antes."

    show hanna emocionada with dissolve

    h "¿Qué hacemos entonces?"

    show freya ladohabla2 with dissolve

    fr "Hmm, bueno... podemos empezar por este lugar."

    label cap2normal_sideselection:
        scene bg salonclases with dissolve

        "Es cierto, nadie se puso a pensar en dónde estábamos ahora."

        "Este era el salón del club de teatro."

        "Las sillas se encontraban en completo desorden, algunas apuntando entre ellas y otras en direcciones aleatorias."

        "Obviamente, el ambiente era distinto y todos los posters, papeles y demás no eran como lo recordábamos."

        show freya normal at left with dissolve

        fr "Podemos buscar algo de utilidad aquí antes de movernos."

        e "Sí, por favor hagamos algo más antes de movernos..."

        "Reclamó una voz proveniente del suelo, era Evan, quien aún seguía recostado sobre su espalda."

        show freya angustiada with dissolve

        fr "¡Oh, más te VALE hacer algo de utilidad!"

        show freya angustiadahabla with dissolve

        fr "Si te quedas ahí acostado sin ayudar como en la barricada, haré algo más que solo gritarte."

        "Se veía muy cansado."

        "Era raro que siguiera completamente tirado en el suelo."

        hide freya with dissolve

        "Los demás comenzaron a buscar en distintas partes del salón."

        menu:
            "Revisar a Evan":
                call cap2normal_evan from _call_cap2normal_evan

            "Acompañar a Hanna":
                call cap2normal_hanna from _call_cap2normal_hanna

            "Investigar con Freya":
                call cap2normal_freya from _call_cap2normal_freya

            "Hablar con Felix":
                call cap2normal_felix from _call_cap2normal_felix

    scene bg salonclases with fade

    "Comcené a buscar por mi propia cuenta."

    "Similar a la cafetería, los posters tenían contenido distinto, completamente incomprensible y, a menos que pueda decifrarlo, de poca utilidad."

    "Abrí los cajones del mueble que hay en todo salón"
    
    extend ", vacío"
    
    extend ", ni siquiera un libro, póster, o cualquier cosa."

    "Al voltear a ver a los demás, me di cuenta que no era el único que no lograba encontrar nada, pues todos tenían una expresión preocupada."

    show freya normal at left

    show felix normal at center

    show hanna normal at right
    
    with dissolve

    fr "¿Alguno logró encontrar algo?"

    f "Nada que no hayamos visto antes."

    show freya normalhabla with dissolve

    fr "Hmm, eso pensé..."

    show hanna sonrisa 
    
    show freya preocupada
    
    show felix manofrentepreocupado
    
    with dissolve

    "Hanna levantó una vara de metal, lo cual hizo que todos dieran un paso hacia atrás."

    h "Umm, encontré esto en una esquina. No es mucho, pero quizás podríamos defendernos con ella."

    show freya sonrisa with dissolve

    fr "Bien pensado Hanna."

    show freya ladohabla with dissolve

    "Freya volteó hacia Evan quien aún seguía en el piso."

    fr "¿Y tú? "

    extend "¿Lograste hacer algo útil?"

    hide felix with dissolve

    show evan normal at center with dissolve

    "Evan suspiró profundamente mientras se levantaba."

    show evan ladobrazo with dissolve

    e "De hecho, sí."

    show freya preocupada with dissolve

    fr "¿Q...qué?"

    show evan gimme with dissolve

    "Evan me entregó una hoja de papel doblada."

    show evan ladobrazo2 with dissolve

    e "Estaba atorada debajo de una de las sillas, se veía claramente desde el suelo."

    "Desdoblé la imagen y la comencé a analizar."

    #bg pistaizanagi

    scene bg pistaizanagi with fade

    a "¿Otra ilustración?"

    "Era una imagen de dos entidades, asumo que deben ser dioses o deidades, pues su vestimenta era larga y ceremonial y su apariencia no estaba lejos de ser divina."

    "Ambos tenían el cabello largo, mas era aparente que uno era hombre y la otra mujer."

    "Se encontraban sentados en las nubes, el hombre tenía una especie de lanza larga que apuntaba debajo de las nubes, la mujer lo miraba felizmente mientras él sostenía la lanza."

    "En la parte inferior de la imagen se encontraba un dibujo hecho a mano. Como una especie de simbología."

    a "¿Qué es esto?"

    scene bg salonclases

    show evan normal at center

    show freya normal at left

    show hanna normal at right

    with fade

    show freya angustiada

    show evan defensivo

    show hanna despair

    with vpunch #metaldrop maybe?

    "Antes de que pudiera consultar a los demás, un fuerte sonido nos interrumpió a todos."

    "Parceía provenir del techo."

    h "¡¿Qué fue eso?!"

    show freya preocupada with dissolve

    fr "¿Estás bien?"

    show humoblanco zorder 2 with dissolve

    "Voltee a ver a los demás pero algo andaba mal."

    "Mi visión estaba siendo nublada, mi respiración acelerada y mi espalda mojada en sudor."

    a "¿Chicos...?"

    show evan despair with dissolve

    e "¿Qué pasó?"

    a "N-no podemos quedarnos aquí..."

    show freya normal with dissolve

    "Tanto Freya como yo notamos la situación al instante: "

    extend "la habitación comenzaba a calentarse cada vez más y más."

    show freya angustiadahabla with dissolve

    fr "¡Vámonos de aquí!"

    hide hanna

    hide freya

    with dissolve

    "Hanna, Freya y Felix corrieron hacia la puerta mientras que yo me quedé a ayudar a Evan."

    a "Te tengo. ¿Puedes caminar?"

    e "Ugh, eso creo..."

    fr "¡AGH, MALDICIÓN!"

    a "¿Qué ocurre?"

    show evan at left with move

    show freya angustiada at center 
    
    show hanna miedohabla at right
    
    with dissolve

    fr "¡La puerta está bloqueada, no podemos abrirla!"

    show evan gimmeceja with dissolve

    e "Intenten golpearla con algo."

    show hanna muyasustadahabla with dissolve

    "Hanna intentó tomar la vara de metal que había encontrado para destruir la puerta..."

    show hanna llorar with vpunch

    h "¡AHHH!" #metal drop sfx

    show hanna miedohabla

    h "Auch... la barra, está muy caliente."

    show freya angustiada

    fr "Es imposible... no podremos abrirnos el paso así."

    show evan despair with dissolve

    "Evan comenzaba a respirar más agresivamente."

    e "Tiene... que haber... una forma..."

    hide hanna with dissolve

    show felix manofrentepreocupadohabla2 at right with dissolve

    f "Ahhh... ¿qué hacemos?"

    "No estaba seguro."

    "No sé qué hacer..."

    "¿Qué hago, qué hago?"

    menu:
        "Mostrar ilustración":
            "Sacudí mi cabeza y recordé la ilustración que había encontrado Evan."

        "Romper las ventanas":
            jump cap2normal_window

    a "Ah... Ahhhh, ¡Freya!"

    show freya angustiadahabla with dissolve

    fr "¿Qué quieres? ¡No hay tiempo para tus pánicos de indecisión, esto es serio, debemos salir de aquí!"

    a "No"
    
    extend ", ah"
    
    extend ", ya sé. "
    
    extend "Es que"
    
    extend ", ah"
    
    extend ", umm"
    
    extend ", ahhh... "

    show freya angustiadahabla with vpunch

    extend "¡Mira, MIRA!"

    show freya normal with dissolve

    "Le entregué a Freya la ilustración."

    a "Evan encontró esto hace un momento. Ah, es parecida a la que vimos en la cafetería."
    
    a "Qui... quizás sea una pista para salir..."

    scene bg pistaizanagi with dissolve #bg pistaizanagi

    a "¿Qué crees que signifique?"

    fr "Ah, son los dioses de la mitología japonesa, Izanagi e Izanami."

    fr "Ellos dos eran amantes, hasta la muerte de Izanami, fue puesta en Yomi, la tierra de los muertos, e Izanagi intentó sacarla de ahí."

    fr "Ah"

    extend ", pero eso no importa, la imagen es de antes de eso."

    fr "Ellos fueron los primeros dioses según las leyendas, y dieron forma al mundo."

    a "¿Y el dibujo que está ahí?"

    show bg pistaizanagi with Dissolve(2.0)

    fr "..."

    fr "Tenemos que darle forma al mundo."

    scene bg salonclases

    show evan defensivo at left

    show freya normal at center 
    
    show felix manofrentepreocupadohabla2 at right
    
    show humoblanco zorder 2
    
    with dissolve

    f "¿Qué?"

    fr "Las sillas... ah, tenemos que darle forma a las sillas."

    fr "Ellos le dieron forma al mundo, y el mundo son las sillas, ah, tenemos que darle forma al mundo como ellos lo hicieron."

    show freya angustiadahabla with dissolve

    fr "¡Rápido! ¡Ayúdenme!"

    scene bg sillas with dissolve

    "Los demás corrieron por las demás sillas para ayudar a Freya con su predicción."

    "Evan, sin embargo, se mantuvo recargado de la mesa, respirando agresivamente y sudando más de lo que su cuerpo podía."

    "Todos acomodamos las sillas con rapidez, pero el calor de la habitación nos impedía acelerar cada vez más."

    scene bg salonclases

    show hanna miedohabla at right

    show freya angustiada at center 
    
    show felix manofrentepreocupadohabla2 at left
    
    show humoblanco zorder 2

    with dissolve

    fr "{i}Hah..Hah...{/i}"
    
    extend "solo falta...una..."

    "La última silla se encontraba cerca de Evan, pero él no podía ni moverse, se veía muy cansado."

    a "Yo...voy...{i}hah{/i}"

    scene bg salonclases
    
    show humoblanco zorder 2

    with dissolve

    "Comencé a caminar hacia Evan."

    scene bg black with closeeyes
    
    scene bg salonclases
    
    show humoblanco zorder 2

    with openeyes

    "Sin embargo, lentamente me di cuenta de que ya no podía."

    "Mi cuerpo se encontraba muy cansado."

    "Mis piertas se rindieron."

    show humoblanco with vpunch

    a "Aggh... no."

    show evan gimmeenojado at center with vpunch

    e "¡HAHHHHHHHHH!"

    "Evan reunió todas sus energías y soltó una fuerte patada hacia la silla."

    hide evan with dissolve

    "Esta se deslizó hasta quedar en frente de mí."

    "Intenté pararme pero fue en vano, mi cuerpo estaba muy cansado."

    show hanna sonrisa at center with dissolve

    "Hanna, quien parecía aún tener energía de reserva, me ayudó a levantarme."

    h "Te tengo."

    "Tomé la silla y la coloqué donde correspondía."

    #doorbang

    "En ese instante, la puerta se abrió de golpe."

    show freya angustiadahabla at right with dissolve

    fr "¡VÁMONOS!"

    scene bg pasillo3twilight with dissolve

    "Al salir de la habitación, cerramos la puerta inmediatamente, nos tiramos al suelo y por fin respiramos un poco."

    a "{i}Hah...hah...hah...{/i}"

    "El aire frio y el suelo se sentían tan bien."

    "Mis ansias se comenzaban a calmar."

    show freya preocupada at left

    show hanna sonrisa at right
    
    with dissolve

    fr "¿Estás bien?"

    h "Sí, estoy bien."

    show freya caderaspreocupada with dissolve

    fr "Umm, y...¿estás bien tú? Ahh..."

    a "Arden."

    show freya normalhabla with dissolve

    fr "Sí...claro, Arden."

    a "Me encuentro bien."

    show freya sonrisa with dissolve

    fr "Es bueno saberlo..."

    "La conversación fue interrumpida por un fuerte sonido dentro del salón."

    "Todos voltearon para ver lo que ocurría..."

    scene bg salonclases

    show humoblanco zorder 2

    show fuego zorder 3

    with Dissolve(1.5)

    "La habitación estaba ahora completamente en llamas, todos los papeles, posters, sillas, mesas y demás se encontraban enredados en el calor de esos látigos rojizos esporádicos."

    h "Ay, Dios..."

    "Entre las llamas, logré notar algo al otro lado de la ventana del salón."

    show bg beast2 with dissolve

    "Unos ojos, unos ojos vacíos que nos miraban fijamente."

    "Era la bestia, mirándonos a través de las ventanas del salón."

    a "No podemos quedarnos aquí..."

    fr "Sí, suena a un buen plan..."

    jump cap3normal

label cap2normal_window:
    scene bg salonclases
    
    show humoblanco zorder 2

    with fade

    a "Las ventanas..."

    a "Podemos salir por ahí."

    "No haía mucho tiempo para considerar opciones."

    "Así qe solamente seguí mis instintos... "

    scene bg ventana with vpunch

    extend "y rompí las ventanas."

    a "¡AAUUUCH!"

    "Algunos cristales atravesaron mi piel, pero no fue nada muy grave."

    scene bg afuera2 with dissolve

    "A pesar de todo logré salir."

    a "Heh, lo hice..."

    "Sin embargo... "

    scene bg beast2 with dissolve

    extend "esa victoria fue de corta duración."

    "Ese monstruo estaba rondando por el patio de la escuela."

    scene bg beastfrente with dissolve

    "Y rápidamente, notó mi presencia."

    scene bg black with dissolve

    "Se acercó hacia mí a toda velocidad."

    scene bg beastfrente with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    "No tenía escapatoria."

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    "No había nada que podría haber hecho."

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    fr "¡ARDEEEEEEEN!"

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    h "No, no de nuevo..."

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    e "¡¡ARDEN, NOOOOO!!"

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    f "Oh por Dios..."

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(0.25)

    scene bg sangre with Dissolve(0.25)

    scene bg black with Dissolve(1.5)

    pause 1.0

    return