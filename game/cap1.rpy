label cap1:

    #show bg negro

    # scene bg black with fade

    scene bg black with Fade(1.0, 1.0, 1.0)

    play music "audio/nightmare.mp3" fadein 1.5 volume 0.25

    "Negro..."

    "Así es cuando empieza el sueño..."

    "Un sueño profundo del cual no puedo despertar aunque grite..."

    scene bg dream2 with fade

    "Debería haber alguien esperándome aquí pero, estoy solo, solo en este vacío inmenso de inmensa profundidad..."

    "{color=#ffffff}???{/color}" "𒈓𒈙꧅𒈙𒈙"

    "Era una voz conocida pero no pude reconocerla, al menos no con aquel dialecto."

    "Mis ojos exploraban el amplio vacío buscando a alguien y ahí, una persona, una chica de largos cabellos con su rostro vacío, algo parecía estar diciendo..."

    "Algo... que no lograba entender..."

    "¿Qué... quieres?"

    #bg salon

    stop music fadeout 1.5

    scene bg salonclases2 with Fade(1.0, 1.0, 1.0)

    play music "audio/longtwilight.mp3" volume 0.25

    "Mis ojos se abrieron lentamente, acostumbrándome al brillo del salón, ahí fue cuando pude ver la escena que se desenvolvía frente a mí."

    "Atemorizados dentro de aquel salón, todos parecían pasar por un duelo distinto."

    "Freya estaba en la orilla consolando a su amiga Hanna."

    "Por otro lado se encontraba Evan, el chico de cabellos blancos quien se encontraba tosiendo fuertemente en la esquina intentando recuperar el aire."

    #show felix (cambiar las expresiones depeniendo del diálogo, you already know)

    show felix sonrisahabla at center with dissolve:
        zoom sprite_size

    f "Hey, ¿estás bien?"

    "Felix, el chico de cabello rosado, se había acercado a mí."

    "Yo aún estaba en una orilla del salon en completo shock, no pude decir ni una sola palabra ante el chico de ojos amigables."

    "¿Cómo podía estar tan tranquilo?"

    "Literalmente acababan de matar a alguien frente a sus ojos, y aquella persona solo estaba parada frente a él como si nada."

    show felix ceja with dissolve

    f "Hey."

    a "Perdón... ¿Quién eres?"

    "Mentí, yo obviamente conocía a todos los que estaban en aquella habitación pero estaba seguro de que ellos no me reconocían."

    show felix sonrisahabla with dissolve

    f "Felix, soy... compañero de Katherine, su ex novio de hecho."

    a "Felix..."

    f "Sí, Felix."

    "Aquel chico se quedó parado frente a mí como si estuviese esperando algo a cambio, viéndome con curiosidad."

    a "Estoy bien."

    "Mentí ignorando mi verdadero sentimiento una vez más apartando la vista, no recuerdo el momento en el que llegué al salón para encerrarme."

    show felix pensandoceja with dissolve

    f "Hmmm..."

    "Felix respondió de una forma no satisfactoria, como si aquella respuesta no fuese suficiente para él, aun así, lo ignoré."

    show felix sonrisahabla with dissolve

    f "¿Y tú eres...?"

    a "Arden."

    show felix caderashabla with dissolve

    f "Arden... es un nombre curioso, no creo haberlo escuchado antes."

    a "No es muy conocido."

    f "Ya, bueno, sería bueno que te presentaras con el resto, estamos listos para el siguiente paso."

    a "¿El siguiente paso?"

    show felix sonrisahabla with dissolve

    f "Sí, mientras estabas en trance los demás empezaron a discutir cómo salir de aquí."

    stop music

    a "¿Salir...?"

    "La palabra solo me recordó a Katherine frente a mi, un miedo que me hizo añicos el alma."

    a "No... No hay que salir..."

    show felix normal with dissolve

    play music "audio/dark.mp3" volume 0.25

    f "¿Piensas quedarte aquí?"

    a "¿Qué? ¡¿No viste lo que le ocurrió a Katherine?!"

    #show evan

    show evan despair at left with dissolve:
        zoom sprite_size

    e " Sí... bueno..."

    "Evan, el chico alto de cabellos blancos se acercó interrumpiendo."

    show evan ladobrazo with dissolve

    e "¿Cómo planeas sobrevivir? Si nos quedamos aquí acabaremos también como ella."

    "Mi corazón se sintió pequeño en aquel momento, muy pequeño, como si se hubiese hecho chicharrón."

    #show freya

    show freya angustiada at right with dissolve:
        zoom sprite_size

    fr "¿No ves que lo asustas, animal?"

    "Freya atacó a Evan chasqueando la lengua."

    fr "Queremos salir de aquí pero con precauciones, vamos a buscar pistas y si hay alguna forma de ahuyentar al monstruo."

    "Eso me recordó el libro, el momento en el que las paginas habían cambiado, mi cuerpo se tensó por un momento."

    a "Creo que... sé dónde podríamos encontrar una pista..."

    show freya preocupada with dissolve

    fr "¿Dónde?"

    a "La biblioteca...cuando esto ocurrió los libros cambiaron, las letras y las portadas también."
    
    a "Quizás podríamos encontrar algo ahí."

    show freya normalhabla with dissolve

    fr "No, definitivamente no."

    a "¿Huh?"

    show freya pensarhabla with dissolve

    fr "El monstruo estaba dentro de la biblioteca, ¿recuerdas? Es muy riesgoso, tenemos que encontrar otro lugar."

    menu:
        "S...sí, tienes razón.":
            a "S...sí, tienes razón."

            show freya caderassonrisa with dissolve

            fr "Siempre la tengo."

        "N...no creo que sea bueno evitarlo, podría ayudarnos.":
            a "N...no creo que sea bueno evitarlo, podría ayudarnos."

            show freya ladohabla with dissolve

            fr "¿No? ¿Quieres correr a la boca del lobo y caer en su trampa? ¿Eres tan ingenuo?"

        "(Guardar silencio)":
            show freya sonrisa with dissolve

            "Freya sonrió con satisfacción por mi silencio. Se veía burlona, como si hubiera ganado una pequeña batalla sin sentido."

    #hide felix

    hide felix with dissolve

    #show hanna

    show hanna miedohabla at center with dissolve:
        zoom sprite_size

    h "Bien, ¿a dónde vamos en ese caso?"

    "Hanna preguntó de forma nerviosa mientras sostenía la mano de Freya con fuerza, como si fuese lo último que tuviese para mantenerse en pie."

    show freya pensarhabla with dissolve

    fr "Podríamos empezar por la cafetería, es un lugar bastante amplio, seguro encontraremos algo ahí."

    show evan ladobrazoenojado with dissolve

    "Freya concluyó con seguridad, aunque viendo el rostro de Evan se notaba poco convencido de la decisión."

    show freya normalhabla with dissolve

    fr " Cafetería, sí, sería bueno para ver también las provisiones que hay, tampoco me gustaría morirme de hambre."

    "Claro, había pasado tanto tiempo que había olvidado la última vez que comí, de hecho, saque mi celular curioso checando la hora."

    "Las 6..."

    "¿Qué no... hacía un par de minutos Freya había dicho que eran las 6?"

    "Todos estuvieron de acuerdo por lo que marchamos a la cafetería."

    stop music fadeout 1.5

    label cap1_sideselection:

        #bg cafeteria

        scene bg cafeteria with Fade(0.5, 0.5, 0.5)

        "Caminamos por los pasillos hasta encontrar el lugar, todos entraron, uno detrás del otro."

        "Las luces estaban encendidas como era costumbre y por las ventanas se podía aún visualizar el rojo carmesí del cielo."

        "Evité con todo mi corazón el escalofrío que recorría mi espalda baja, mi corazón acelerado y el miedo que incrementó en mi interior para ver al resto."

        #show freya

        show freya pensarhabla at center with dissolve:
            zoom sprite_size

        fr "Bien, hay que asegurar el perímetro."

        show freya normalhabla with dissolve

        fr "Iré a revisar las provisiones."

        show freya ladohabla2 with dissolve

        fr "Evan, quédate en la entrada para checar que nadie venga."

        show freya lado with dissolve

        fr "Felix y Hanna revisarán los alrededores."

        "Freya se dio la vuelta ignorando mi presencia por completo."

        a "¿Y yo?"

        show freya normalhabla with dissolve

        fr "Oh, chico despistado, haz algo de provecho supongo."

        #hide freya

        hide freya with dissolve

        "Freya se encogió de hombros como si no le importase del todo mi presencia y se retiró."

        menu:
            "Acercarse a Evan":
                call cap1_evan from _call_cap1_evan
            
            "Ayudar a Freya":
                call cap1_freya from _call_cap1_freya

            "Seguir a Hanna":
                call cap1_hanna from _call_cap1_hanna

            "Observar a Felix":
                call cap1_felix from _call_cap1_felix

    #bg cafeteria (con algun fade para desaparecer a los demás)

    scene bg cafeteria with Fade(0.3, 0.0, 0.3)

    play music "audio/dark.mp3" volume 0.25

    #show freya

    show freya normalhabla at center with dissolve:
        zoom sprite_size

    fr "Bien, acérquense todos, repartiré las cosas equivalentemente."

    "Freya llamó al resto haciendo que todos nos acercáramos a ella, cada uno tomó su porción adecuadamente, añadiendo a esto Freya llevaba otra mochila sobre su espalda."

    "Seguramente serían más provisiones para después pero para ser honestos, no tengo valor del todo para hablar."

    fr "¿Encontraron algo?"

    #show hanna

    show hanna miedohabla at left with dissolve:
        zoom sprite_size

    h "No realmente, solo un par de papeles tirados y posters alternados, había muchos papeles pero solo un par de ellos eran completamente ilegibles."

    show freya caderaspreocupada2 with dissolve

    fr "¿Ilegibles? Bueno, tiene sentido que sea así, es lo que pasó con el libro según nos contó... ah..."

    "Los ojos de la chica se posicionaron sobre mi como si no recordase mi nombre."

    a "Arden."

    "Quizás la vez pasada no había escuchado mi nombre por lo que lo dejé pasar por alto."

    show freya normalhabla with dissolve

    fr "Arden, sí."

    "Freya se volteó una vez más para ver a los demás ignorándome por completo."

    show freya ladohabla2 with dissolve

    fr "¿Tienen ideas sobre este lugar? Me gustaría escuchar qué es lo que piensan."

    #show evan

    show hanna normal with dissolve

    show evan pensando at right with dissolve:
        zoom sprite_size

    e "Creo que estamos en una especie de mundo alterno..."

    show freya sonrisahabla with dissolve

    fr "Mundo alterno, esas solo son fantasías."

    show evan normal with dissolve

    e "Bueno, creo que es la única forma razonable de explicar lo que está ocurriendo, ¿no lo crees? A no ser que tengas otra hipótesis."

    show freya pensarhabla with dissolve

    fr "Mi hipótesis, la cual puede ser la correcta, es que estamos dentro de una máquina experimental."

    show evan pensando with dissolve

    e "Oh, sí, tiene sentido."

    show evan normal with dissolve
    
    e "Sobre todo la parte en la que nadie recuerda haber sido sometido a una máquina, y si fuera un experimento Katherine no hubiera muerto."

    show freya normal with dissolve

    fr "Los experimentos tienen casualidades."

    show evan ladobrazo with dissolve

    e "En ese caso, ¿por qué nosotros?"

    show hanna miedohabla with dissolve

    h "C...chicos no creo que lleguemos a nada."

    show freya normalhabla with dissolve

    fr "¿Qué piensas tú?"

    menu:
        "Darle la razón a Evan":
            a "Bueno, el universo tiene sentido, ¿quizás quedamos todos dentro por estar en la biblioteca al mismo tiempo?"

            show freya ladohabla2 with dissolve

            fr "Tsk..."

            "La lengua de Freya chasqueó con fuerza y claramente se veía molesta con aquella respuesta."

            show evan feliz with dissolve

            "Sus ojos se voltearon un poco para ignorar a Arden una vez más mientras que Evan parecía sonreír debajo del cubrebocas satisfactoriamente."

        "Darle la razón a Freya":
            a "Bueno, el experimento tiene sentido, eso explicaría el por que solo somos nosotros, un grupo selectivo de personas ¿no?"

            show freya caderaspreocupada2 with dissolve

            fr "¿Lo ves? Ah..."

            "Freya me observó una vez más como si esperase algo."

            a "Arden."

            show freya sonrisahabla with dissolve

            fr "Sí, Arden sabe que es lo correcto. Tal vez podrías aprender de gente como yo."

            "Freya lanzó su cabello hacia atrás victoriosa por su pequeña batalla contra el peliblanco."

    #hide hanna

    hide hanna with dissolve

    #show felix

    show felix manofrentepreocupado at left with dissolve:
        zoom sprite_size

    stop music fadeout 1.5

    f "Sea como sea, debemos tener cuidado de aquí en adelante, se siente el ambiente tenso, ¿no lo crees?"

    "Felix volvió a verme aunque ni siquiera sabía si se refería al monstruo o a mis compañeros que ahora mismo no paraban de mirarse de forma amenazadora."

    a "S...sí, tienes razón, quizás deberíamos seguir buscando pistas."

    show freya pensarhabla with dissolve

    fr "Aquí no hay nada, creo que deberíamos de irnos."

    "Freya habló con seguridad."
    
    "Aquella sensación de incomodidad invadió nuevamente mi interior, la misma sensación que pude sentir cuando Katherine murió justo frente a mis ojos."

    #bg bestiacafeteria ?

    scene bg beast2 with Fade(0.3, 0.1, 0.3)

    play music "<from 4>audio/chase.mp3" volume 0.25

    "Ni siquiera pude pensar, se escuchó el gruñido de la bestia afuera, mis ojos se engrandecieron y observaron a Freya inmediatamente buscando su ayuda."

    a "Una barricada..."

    fr "¡Sí! ¡Una barricada!"

    #bg cafateria

    scene bg cafeteria with Fade(0.3, 0.1, 0.3)

    #show freya

    show freya angustiada at center with dissolve:
        zoom sprite_size

    "Freya tomó una de las mesas para arrastrarla, el resto hizo lo mismo, tomando muebles y objetos que pudiesen utilizar para bloquear la entrada de donde se escuchaba el monstruo."

    "Aquella entrada quedaba en el pasillo izquierdo, por lo que había otras dos entradas en la parte de atrás y del lado derecho."

    "Definitivamente no les daría tiempo de crear un salón cerrado a pesar de la grandiosa idea de Arden."

    #show evan

    show evan normal at right with dissolve:
        zoom sprite_size

    "A pesar de que todos movían cosas Evan solo los miraba a la distancia como si no pudiese hacer nada y fue cuando Freya lo vio con odio."

    show freya angustiadahabla with dissolve

    fr "MUÉVETE, ¿O QUIERES MORIR?"

    show evan despair with dissolve

    e "Sería mejor irnos..."

    "Para sorpresa de todos, el pequeño conejo que habían estado persiguiendo hace horas saltó del bolsillo de Evan y aterrado por el ruido salió corriendo por una de las puertas traseras."

    "Fue evidente, y el corazón de todos quizás se frenó un par de segundos al ver la escena."

    "El conejo fue decapitado por una especie de trampa que lo esperaba con ansia afuera."

    "El ruido se detuvo y ahora solo podía escuchar el palpitar de mi corazón con fuerza, miedo, miedo era lo que estaba ahora consumiendo mi corazón."

    #hide evan

    hide evan with dissolve

    #show felix

    show felix preocupado at right with dissolve:
        zoom sprite_size
    
    f "Fuck..."

    show hanna muyasustadahabla at left with dissolve:
        zoom sprite_size

    h "¿Estamos... encerrados?"

    show freya preocupada with dissolve

    fr "No... nononono."

    "Freya susurraba a un lado de Hanna intentando consolarla aunque se veía que la esperanza de la chica poco a poco iba disminuyendo."

    show hanna despair with dissolve

    h "¡¿Qué hacemos!? ¡NO QUIERO MORIR!"

    fr "Shshshs."

    "Freya intentaba consolarla pero para ser honestos yo también estaba perdiendo la esperanza, solo quedaba una puerta, pero aquello podía ser una salida segura o quizás la muerte instantánea."

    #hide hanna

    hide hanna with dissolve

    #show evan

    show evan despair at left with dissolve:
        zoom sprite_size

    e "Mierda..."

    #hide evan, freya, felix

    hide evan

    hide freya

    hide felix

    with dissolve

    "Corrí con desesperación a la puerta y me dieron la bienvenida millones de posters con símbolos distintos que recorrían cada uno de los papeles y ninguno hacía sentido."

    a "¡Debe haber algo, debe haber algo!"

    #show felix

    show felix manofrentepreocupadohabla at center with dissolve:
        zoom sprite_size

    f "No hay nada, no hay salida."

    a "¿Ves si hay alguna salida? ¿Algo que podamos saltar si cruzamos?"

    "Mis manos temblaban de miedo, me consumía, poco a poco me volvía victima de aquella sombra, tengo miedo, mucho miedo, pero tampoco quiero morir, ¡NO QUIERO MORIR!"

    #show freya

    show freya caderaspreocupada2 at left with dissolve:
        zoom sprite_size

    fr "¡¿Qué hacen?! ¡Van a morir!"

    a "¡NO QUIERO MORIR!"

    "Exclamé entre miedo y desesperación esperando que me ayudasen, los gruñidos y golpeteos de la puerta que tenía la barricada se hicieron mucho mayores, el miedo estaba invadiendo a todos."

    "Entre lágrimas, mis manos comenzaron a moverse con fuerza tirando de papeles y posters que estaban alrededor de la puerta de forma desesperada."

    "Y uno... uno en particular que parecía una nota golpeó mi pie, era pesada pues estaba doblada quizás unas cinco veces."

    show felix ceja with dissolve

    f "¿Qué es eso?"

    "Tomé la nota y comencé a desdoblarla, mis manos temblaban mucho."

    #bg pistaanubis

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Era una ilustración, una especie de jeroglíficos, hombres ofreciendo algo a una especie de puerta."

    a "¿Qué...? ¿Qué es esto?"

    "Evan se acercó y me arrebató la hoja de las manos, quizás en un momento pensó que solo estaba exagerando pero al visualizarlo su cabeza se ladeó ligeramente de forma confundida."

    e "Huh..."

    #bg cafeteria

    scene bg cafeteria with Fade(0.3, 0.1, 0.3)

    "Los rasguños y golpeteos se volvieron mucho más insistentes, inclusive la garra del monstruo ya estaba buscando escurrirse entre la pequeña abertura de las puertas."

    #show freya

    show freya preocupada at center with dissolve:
        zoom sprite_size

    fr "¿Qué ocurre?"

    "Freya se acercó quizás un poco más preocupada viendo la imagen."

    show freya normal with dissolve

    fr "¿Jeroglíficos?"

    a "Estaba detrás de un poster, como si estuviese escondido."

    #show hanna

    show hanna miedohabla at right with dissolve:
        zoom sprite_size

    h "¿Escondido? ¿Como si alguien lo hubiese escondido? Da igual da igual, ¡¿qué dice?!"

    a "¡¡No lo sé!! ¡No sé leer estas cosas!"

    "Freya se acercó a tomar el papel y lo extendió."

    #bg pistaanubis

    scene bg black with Fade(0.3, 0.1, 0.3)

    fr "Es Anubis… la balanza está desequilibrada…"

    "Parecía estar pensando pero se vio interrumpida por un gruñido y la barricada rompiéndose."

    e "¿¿Y ESO QUÉ??"

    fr "¡SHSH NO PUEDO PENSAR SI GRITAS!"

    #bg cafeteria

    scene bg cafeteria with Fade(0.3, 0.1, 0.3)

    #show freya

    show freya normalhabla at center with dissolve:
        zoom sprite_size

    fr "Hay que equilibrar la balanza, un sacrificio, ¡tenemos que hacer un sacrificio!"

    #show evan

    show evan defensivo at right with dissolve:
        zoom sprite_size

    e "¡¿QUÉ?! ¡¿Piensas matar a alguien?!"
    
    show freya angustiadahabla with dissolve

    fr "¡Si pudiera lo haría! Pero no... No creo que sea así..."

    show freya pensarhabla with dissolve

    fr "Debe de ser un sacrificio distinto, no siempre son personas... puede ser un objeto o algo íntimo..."

    #show felix

    show felix pensando2 at left with dissolve:
        zoom sprite_size

    f "Sangre, podríamos cortarnos y ofrecer eso para salir."

    fr "¿Sangre? No, no lo creo, quizás algo que te pertenezca, muy dentro, como un secreto, cuando dices un secreto en alto lo sacrificas."

    a "Si es un sacrificio de algo importante, ¿no sería un objeto? Algo… importante para ti, tiene más sentido en mi cabeza."

    show evan pensando with dissolve

    e "Eso también tiene sentido..."

    "Evan veía la puerta la cual estaba siendo golpeada con más fuerza, rompiendo varios pedazos de la misma."

    #hide freya

    hide freya with dissolve

    #show hanna

    show hanna llorar at center with vpunch:
        zoom sprite_size

    h "¡BUENO DECIDAN ENTONCES!"

    "Hanna gritó aterrada."

    "Me concentré, muy dentro debía tener la respuesta, debía estar oculta, definitivamente estaba escondida y pronto, todo hizo sentido."

    menu:
        "Sacrificar un secreto" if not demo:
            jump cap1normal

        "Ofrecer sangre" if not demo:
            jump cap1bad

        "Sacrificar objeto":
            jump cap1true


label cap1true:
    #bg cafeteria

    scene bg black with Fade(0.3, 0.1, 0.3)
    
    "Mi mano buscó el collar que Katherine me había dado."

    "Dudando un poco, extendí la mano y lo arrojé a la puerta."

    "Rápidamente aquella puerta activo la trampa y se destruyó una vez tomó el collar y destruyendo el mismo en el instante."

    "En ese instante la puerta de la barricada se rompió liberando al monstruo."

    a "¡CORRAN!"

    stop music fadeout 1.5

    #fade to black

    # scene bg black with Fade(1.0, 1.0, 1.0)

    jump cap2true

label cap1bad:
    return

label cap1normal:
    return