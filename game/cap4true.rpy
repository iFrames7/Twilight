label cap4true:
    #bg oficina

    scene bg cap4screen with Fade(1.0, 1.5, 1.0) 

    pause 2.5

    scene bg oficina with Fade(1.0, 1.0, 1.0)

    play music "audio/mysterious.mp3" volume 0.25
    
    "Algo no estaba bien..."

    "Era como si aquella oficina estuviese repleta de una energía oscura... "

    extend "mi cuerpo comenzaba a sentirse pesado, muy pesado."

    "Mis ojos buscaron alrededor, nunca había estado en la oficina del director, de hecho le resultaba extraño poder pisarla."

    "Era un lugar enorme, enorme para una persona que únicamente dirige una escuela."

    #show felix

    show felix ceja at center with dissolve

    f "No creo que encontremos nada, van a ser los mismos libros llenos de símbolos raros."

    a "Quizás, pero vale la pena investigar."

    hide felix with dissolve

    "Con certeza ahora comencé a examinar mis alrededores."

    menu:
        "Buscar librería derecha.":
            "Aquí había libros grandes y pesados, tomando uno entre mis manos lo comencé a analizar con cuidado."

            "No hubo mucha diferencia, solo símbolos raros como si estuvieran tallados en sangre."

            #bg rio de almas

            "Había algo extraño aun así, una ilustración de un río."

            "A pesar de observarla, no pude entender totalmente lo que quería decirme"

            extend ", o si quería decirme algo en primer lugar."

        "Buscar librería izquierda.":
            "Libros pequeños y con muchas letras pequeñas, era casi imposible leerlas por completo, de hecho diría que es complicado poder entender algo de lo que decía aquí."

            "Había un libro que no tenía símbolos del todo, solo ilustraciones."

            #bg demonios

            "Lo que me hacían sentir no era exactamente agradable."

            "Me encontraba intranquilo con tan solo ver esas imágenes, así que solamente dejé el libro."

        "Buscar librería del fondo.":
            "Anuarios, muchos anuarios."

            "A decir verdad busqué aquello que no fuera anuarios y solo encontré unos libros que parecían más bien recetarios, todo alterado por los símbolos, claro."

            "¿Por qué el director tendría recetarios en su posesión?"

    #bg oficina

    scene bg oficina with Fade(0.3, 0.1, 0.3)

    "Después de visitar los libros intenté recordar todo lo que sabíamos: "

    #bg pistaanubis

    scene bg pistaanubis with Fade(0.3, 0.1, 0.3)

    extend "la balanza de Anubis"

    #bg pistaloki

    scene bg pistaloki with Fade(0.3, 0.1, 0.3)

    extend ", la ilustración de Loki "

    #bg pistaolimpo

    scene bg pistaolimpo with Fade(0.3, 0.1, 0.3)

    extend "y la entrada al Olimpo."

    label cap4true_sideselection:
        #bg oficina

        scene bg oficina with Fade(0.3, 0.1, 0.3)

        stop music fadeout 0.5

        "Todos estos eran dioses de distintas culturas, pero no comprendo por qué."

        "Debe haber una razón, ¿cierto?"

        "No son cosas puestas al azar."

        "Quizás debería darme un descanso, no creo encontrar algo si tengo la mente distraída."

        # $ evan_cap4_talk = False

        menu:
            "Ir con Evan.":
                call cap4true_evan from _call_cap4true_evan

            "Acompañar a Freya.":
                call cap4true_freya from _call_cap4true_freya

            "Hablar con Felix.":
                call cap4true_felix from _call_cap4true_felix

    #bg oficina

    scene bg oficina with Fade(0.3, 0.1, 0.3)

    play music "audio/mysterious.mp3" volume 0.25

    "Después de aquella conversación, regresé a la estantería donde estaba."

    "La curiosidad estaba que me mataba, sentía que estaba tan cerca de descubrir algo pero al mismo tiempo estaba tan lejos."

    "Lo último que quedaba eran un par de anuarios, aunque realmente no sabía si iba a encontrar algo de relevancia ahí."

    #bg ardenanuario

    scene bg ardenanuario with dissolve

    "Comencé a ver las páginas, viendo las fotos de las personas y sus nombres, había un apartado extra para todas las bellas artes y finalmente encontré la de danza donde se encontraba Felix y un par de alumnos más."

    "..."

    "..."

    "...Espera..."

    "... ¿De qué año es este anuario?"

    "Voltee la tapa y vi 2017."

    "Bueno... "

    extend "2017 no está tan lejos del 2025"

    extend ", ¿no?"

    "8 años estudiando"

    extend ", quizás es muy dedicado a la danza."

    "Aun así, una pequeña espina parecía estar metiéndose en mi cuello."

    "Dejé el anuario de lado y busqué uno más antiguos, 2015, fui directo al apartado de danza una vez más encontrándome con... "

    #bg ardenanuario2

    scene bg ardenanuario2 with dissolve

    play sound "sfx/1heartbeat.mp3" volume 0.75

    extend "Felix."

    "Su rostro parecía el mismo que el del 2017."

    "Fue ahí cuando un trago frío se resbaló sobre mi garganta, una sensación de impotencia se resbaló sobre mi espalda baja y mi respiración se hizo pesada."

    "Cerrando el libro, tomé uno más, 2003, era imposible que Felix estuviera ahí... "
    
    #bg ardenanuario3

    scene bg ardenanuario3 with dissolve

    play sound "sfx/1heartbeat.mp3" volume 1.0
    
    extend "pero lo estaba"

    extend ", el chico"
    
    extend ", como si los años no hubieran pasado"
    
    extend ", estaba ahí... "
    
    extend "con la misma expresión."

    play sound "sfx/heartbeat.mp3" volume 0.75 loop

    "No sabía qué hacer, era algo que no comprendía y pronto... todo hizo sentido."

    "La balanza y el sacrificio, él quería ofrecer sangre, quizás porque él mismo la consumía, siempre que ocurría una muerte cubría su boca, ¿eso... eso también tenía que ver? Loki... dios de las mentiras... ¿era cierto?"

    "Felix"
    
    extend ", Felix"
    
    extend ", Felix"
    
    extend ", FELIX"
    
    extend ", FELIX, FELIX, FELIX."

    stop music fadeout 0.5

    e "¿Arden?"

    stop sound

    #bg oficina 

    scene bg oficina

    #show evan with vpunch

    show evan normal with vpunch

    play sound "sfx/bookclose.wav" volume 0.5

    "¡PAM!"

    "Cerré el anuario con fuerza, mis manos temblando."

    "¿Qué era aquel chico? "
    
    extend "¿Por qué? "
    
    extend "¿Por qué? "
    
    extend "¿Él los había traído a esta trampa?"

    play music "audio/beast.mp3" volume 0.25

    "No tenía sentido, no, de hecho sus razones no tenían sentido en absoluto."

    "¿Por qué no nos mató antes? Estuvo tan cerca de nosotros, tan cerca que quizás podía simplemente acuchillarme por la espalda."

    "Mis ojos se voltearon lentamente hacia quien interrumpió mi investigación, Evan, se veía preocupado."

    show evan ceja at center with dissolve

    e "¿Estás bien? Te ves algo..."

    #un vpunch

    show evan ceja with vpunch

    a "¡Sí!"

    "Respondí con velocidad pateando lejos aquel anuario intentando tranquilizarme."

    show evan defensivo with dissolve

    e "Oh... ok...tal vez deberías darte un descanso..."

    #otro vpunch

    show evan defensivo with vpunch

    a "¡NO! "
    
    extend "N...no digo, ah, ¡siento que estoy al borde de descubrir algo!"

    "Las palabras casi que salían en forma de balbuceo de tan rápido que estaba hablando, mi cuerpo estaba tenso y no podía ver a los ojos a Evan, estaba sudando y sudando frío."

    e "Te puedo ayudar..."

    a "¡No! Digo, ah..."

    f "¿Qué es eso?"

    #show felix

    show felix sonrisahabla at right with dissolve

    play sound "sfx/heartbeat.mp3" volume 0.5 loop

    "Felix, quien estaba detrás de Evan, me veía con ojos serios, ladeaba la cabeza lentamente como si supiese qué hacía."

    a "Nada..."

    show felix ceja with dissolve

    f "¿Nada? ¿No te molestara que lo tome entonces?"

    "Felix extendió su mano, y un recuerdo apareció en mi mente: Felix fue el último que agarró los libros."
    
    "Él... él cambió el contenido de los libros, ¿cierto? "
    
    extend "¿Podía hacer eso?"
    
    extend "¿Era posible?"

    show evan gimmeceja with dissolve

    e "¿Arden?"

    a "S...Sí... está todo bien..."

    "Balbuceé nervioso arrastrando mi cuerpo ligeramente sin poder ver a Felix."

    show evan pensando with dissolve

    e "Te ves muy raro..."

    "Mi corazón palpitaba con fuerza, con tanta fuerza que inclusive mis oídos podían escucharlo."

    e "¿Qué encontraste Arden?"

    a "Ah..."

    "Mis ojos se dirigieron a Felix."

    "Quizás era el miedo, no, debía ser el miedo el que causaba mi sudor, mis ojos delataban cada minúscula emoción de miedo hacia aquel chico."

    show felix normal zorder 1 with dissolve

    f "Vamos Arden... ¿por qué no nos dices?"

    "Felix fulminó su mirada hacia mí."

    stop music fadeout 0.5

    #show freya

    show freya angustiada zorder 0 at right with dissolve
    
    "Freya, quien estaba detrás de Felix, tenía una enorme enciclopedia en sus manos "

    stop sound
    
    #hide felix, hit sfx, vpunch

    play sound "sfx/bookhit.mp3" volume 0.75

    play audio "sfx/fall.ogg" volume 0.75

    hide felix with vpunch

    extend "con la cual golpeó con fuerza la cabeza de Felix haciendo que este cayese al suelo."

    show evan defensivo with dissolve

    e "¿Qué chingados...?"

    a "¡HAY QUE IRNOS!"

    "Tomé la mano de Evan sin pensarlo dos veces sosteniendo los anuarios sobre la otra, mis pies se movieron con rapidez fuera de la habitación, Freya tiró la enciclopedia encima de Felix y fue junto con nosotros."

    #bg salonclases

    scene bg salonclases with Fade(0.3, 0.1, 0.3)

    "Entre el miedo y el nerviosismo, solo logramos encerrarnos en otro salón, cerramos la puerta y finalmente pudimos respirar."

    #show evan, freya

    show evan gimmeceja at right

    show freya normal at left

    with dissolve

    e "¿Qué fue eso?"

    a "¿Cómo sabías?"

    "Mis ojos se voltearon hacia Freya, era imposible que lo supiese, a no ser de que lo hallase antes que yo."

    fr "Vi el temor en tus ojos cuando lo veías, no sé nada... Solo que... tu miedo hacia él se hizo inminente."

    a "Fuck..."

    show evan defensivo with dissolve

    e "Explíquenme qué está pasando."

    "Evan se veía completamente confundido inclusive más que perdido."

    play music "audio/flowerbloom.mp3" volume 0.19

    a "Estaba... estaba viendo los anuarios, son libros que no están alterados, quizás fue suerte, ¿casualidad? No lo sé, pero, ah..."

    "Extendí los anuarios hacia ellos."

    a "Las fechas cambian mucho entre ellas, Felix está en todos."

    "Balbuceaba, mis palabras iban tan rápido que solo podía esperar que los otros dos comprendiesen."

    show evan ceja with dissolve

    e "¿En... todos?"

    "Evan tomó uno de los anuarios y comenzó a examinarlo junto con Freya."

    show evan normal with dissolve

    e "Se ve..."

    show freya caderaspreocupada with dissolve

    fr "Igual en todas las fotos..."

    "Freya se golpeó la frente con su mano izquierda."

    show freya caderaspreocupada2 with dissolve

    fr "¿Cómo pude ser tan ciega...?"

    a "Y...Yo, no lo entiendo... No sé... no tengo ni idea."

    show evan ladobrazo2 with dissolve

    stop music fadeout 0.5

    e "¿Y qué se supone que haremos ahora? Es un monstruo gigante y un lunático contra nosotros, hemos estado dando vueltas por toda la universidad y no encontramos nada de valor para poder hacer algo."

    show freya angustiadahabla with dissolve

    fr "Ni siquiera sabemos cómo salir... ¿De qué nos sirve saber quién es si estamos encerrados aquí? Solo es cuestión de tiempo para que muramos."

    "Hubo un silencio entre todos, uno bastante largo, llevé mis manos a los bolsillos de la sudadera y con nerviosismo comencé a jugar con mis dedos para liberar el estrés que tenía dentro."

    "¿Realmente no podíamos hacer nada? "
    
    extend "¿Estamos perdidos?"

    "Pronto algo golpeó mi cabeza, no podía rendirme, ¿no es así?"

    play music "audio/clue.mp3" volume 0.25

    a "Oigan... ¿y si... no somos los primeros aquí?"

    show freya preocupada with dissolve

    fr "¿Te refieres a que... más personas pasaron por esto antes?"

    a "S...Sí...digo... si Felix estuvo con nosotros todo este tiempo y no nos pudo matar antes fue por algo... ¿no?"

    show evan pensando with dissolve

    e "Si... quizás solo está jugando con su comida."

    show freya pensarhabla with dissolve

    fr "Que tal si no puede..."

    a "Sí... y... recuerdo que siempre que encontrábamos las ilustraciones, él se veía desconcertado, como si... realmente no comprendiese lo que estaba pasando."

    e "Huh... quizás alguien las dejó ahí."

    fr "¿Alguien que quiere ayudarnos a salir?"

    a "Sí... Alguien que quiere ayudarnos a salir... Como... gente que vivía antes aquí."

    "Me volteé para tomar los anuarios comenzando a agitarlos con fuerza hasta que salieron varios papeles al suelo."

    a "Tal vez... ese alguien estaba escondiendo pistas desde antes."

    show evan normal with dissolve

    e "Eso tiene sentido."

    "Evan se acercó para tomar uno de los papeles."

    show evan gimmeceja with dissolve

    e "Pero, ¿por qué no lo escribirían normal?"

    a "Porque quizás Felix puede alterar el contenido, como lo hizo con los libros."

    show freya apunta2 with dissolve

    fr "¿Y las ilustraciones...?"

    a "Supongo que es porque estaban escondidas de él, no había forma de que las encontrara."

    e "Sí... pero, si esas personas lo pusieron, ¿significa que salieron? ¿Cómo lograron ponerlo todo?"

    show freya normalhabla with dissolve

    fr "¿Y si están muertas? Todas las ilustraciones hasta ahora han sido relacionadas con el inframundo... ¿Qué tal si esto es una especie de limbo o purgatorio? Quizás un..."

    show evan pensando with dissolve

    e "Infierno personal."

    show freya pensarhabla with dissolve

    fr "Sí...eso explicaría por qué el tiempo no se mueve..."

    a "..."

    e "..."

    show freya apuntaceja with dissolve

    fr "...Bueno, saber esto es de buena información, pero, ¿de qué nos sirve para salir de aquí?"

    stop music fadeout 0.75

    a "Oh..."

    "..."

    "..."

    "!!!"

    "Mi cabeza regresó al momento en el que escuche aquellos susurros y voces distorsionadas mientras estaba en shock, quizás, solo quizás, era gente que estaba intentando ayudarme."

    a "Rápido, alguien pégueme."

    show evan defensivo with dissolve

    e "¿Qué?"

    "Evan ladeó la cabeza, claro, tenía que explicarme más."

    a "Yo, ahh... esto es complicado."

    show freya normalhabla with dissolve

    fr "¿Más complicado que estar en el inframundo? Lo dudo mucho."

    a "Desde pequeño tengo sueños con personas, con personas que nunca en mi vida había visto, pensé que estaba loco pero, puede que sean fantasmas o... entes que buscan cruzar a algún lado, ah, el punto es que solo los puedo ver si estoy inconsciente."

    show freya normal

    show evan ceja

    with dissolve

    "Ambos me miraron desconcertados, como si hubiese dicho una locura, pero para ser honestos la situación ya era loca."

    fr "Entonces, si te conectas con tus sueños, ¿crees poder hablar con la gente que está encerrada aquí?"

    a "Es una posibilidad, no perdemos nada."

    show freya caderaspreocupada with dissolve

    fr "Bueno... Tampoco es que tengamos más opciones."

    show evan gimmeenojado with dissolve

    e "¿Qué? ¿En serio piensas noquearlo? Es riesgoso, deberíamos..."

    a "No tenemos mucho tiempo para que Felix nos vuelva a encontrar, vamos Evan."

    show evan defensivo with dissolve

    e "No, no te golpearé."

    show freya sonrisahabla with dissolve

    fr "Yo sí."

    play sound "sfx/bookhit.mp3" volume 0.75

    show freya sonrisahabla with vpunch

    "Freya tomó un anuario y golpeó mi cabeza."

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Negro, todo se volvio negro, y de repente "
    
    #bg luzentunel

    scene bg tunel with Fade(0.3, 0.1, 0.3)

    play music "audio/doortootherworld.mp3" volume 0.15
    
    extend "una luz."

    "{color=#ffffff}???{/color}" "𒈓𒈙꧅𒈙𒈙"

    "Se escucha a la distancia como un tintineo, necesitaba concentrarme, necesitaba poder comprenderlos."

    "Tomé un profundo respiro, cerrando mis ojos."

    #show kat, pero blurry

    show katherine sonrisa at center with dissolve:
        alpha 0.86 blur 10.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.47)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    "{color=#ffffff}???{/color}" "A…𒈓𒈙…en Ar𒈓𒈙"

    "Un poco más, un poco más para poder concentrarme y lo lograría."

    #kat less blurry

    show katherine sonrisa2 with dissolve:
        blur 5.0

    "{color=#ffffff}???{/color}" "¡Arden!"

    stop music

    #ghost kat

    show katherine sonrisahabla with dissolve:
        blur 0.0

    k "¡Arden, Arden! Oh gracias al cielo, puedes escucharnos."

    show katherine at left with move

    #show hanna ghost

    show hanna sonrisa at right with dissolve:
        alpha 0.86 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.47)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    show alice normal at center with dissolve:
        xpos 0.4 zoom 0.92 alpha 0.86 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.47)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    show aeron normal at center with dissolve:
        xpos 0.62 zoom 0.88 alpha 0.86 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.47)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    play music "audio/dream.mp3" volume 0.25

    "Mis ojos se abrieron, podía ver a Katherine y a Hanna, junto a ellas otras personas que no reconocía."

    a "Katherine... ¿Qué haces... qué hacen aquí?"

    "Quería abrazarlas, queria llorar a su lado, queria pedirles perdón, había muchas cosas que quería decir pero... aquellos pensamientos fueron interrumpidos por Hanna."

    show hanna normal with dissolve

    h "No hay mucho tiempo."

    show katherine uneasy with dissolve

    k "S...Sí, cierto, Arden, esta es gente que murió antes aquí."

    a "Oh..."

    "Así que realmente veo gente muerta."

    a "¿Decías que... no hay tiempo?"

    show katherine preocupadahabla with dissolve

    k "Sí, no podemos estar mucho tiempo aquí. Nuestras almas están encerradas en el edificio, están siendo consumidas por el demonio."

    a "¿El demonio?"

    show hanna despair with dissolve

    h "Felix es un demonio, uno muy inteligente al parecer, ha estado alterando memorias por décadas haciéndose pasar por un estudiante."

    a "¿C...cómo saben todo esto?"

    show hanna explicando with dissolve

    h "Bueno, las almas de aquí nos explicaron."

    "Estaba rodeado de pequeñas luces y siluetas de gente, gente que tuvo una muy mala suerte y al parecer no pudo sobrevivir."

    h "Ellos son quienes los han ayudado a escapar. Felix, a pesar de haber vivido por décadas aquí, no comprende las culturas humanas ni su historia, por lo que las pistas están..."

    a "En ilustraciones de religiones..." 
    
    a "Ok... creo que esto no es relevante ahora, necesitamos saber cómo escapar."

    show katherine caderashabla with dissolve

    k "Hay muchas formas... Si logran escapar, sus memorias sobre esto se borraran y quizás tengan la mala suerte de volver aquí."

    show katherine dedohabla with dissolve

    k "Pero si acaban con el demonio, no solo serán libres, sino que también liberarán nuestras almas."

    a "¿Y cómo hacemos eso?"

    show katherine preocupadahabla with dissolve

    k "Hay una daga, oculta en la oficina del rector, deben ser listos, pues solo la pueden utilizar una vez."

    a "No creo que podamos matar a una bestia con eso."

    # "Algunas de las almas subieron la voz."

    show katherine sonrisa

    show hanna sonrisa

    with dissolve

    show alice hablar with dissolve

    "{color=#ffffff}???{/color}" "No, no mataran a la bestia, a ella solo hay que encerrarla."

    a "¿Y cómo?"

    show alice normal

    show aeron hablar
    
    with dissolve

    "{color=#ffffff}???{/color}" "En la biblioteca, hay un libro oculto entre la entrada principal y la alfombra, ahí hay un ritual que mantendrá sellada a la bestia, como un círculo mágico que evitará que escape mientras matan a Felix."

    a "Oh...shit..."

    "No sabía si quería volver a la biblioteca, pero no tenía tiempo para cuestionarlo."

    show alice caderasnormal with dissolve

    "{color=#ffffff}???{/color}" "Recuerden, solo tienen una oportunidad... no pueden fallar, Felix no sabe que esta daga existe, ni el libro con el ritual."
    
    show aeron normal with dissolve

    "{color=#ffffff}???{/color}" "El monstruo y Felix tienen que estar en el mismo lugar, si no lo están todo será en vano."

    show aeron sonrisa

    show alice sonrisa

    with dissolve

    a "...Espero no decepcionarlos."

    stop music fadeout 3.5

    scene bg black with Fade(0.7, 0.1, 0.3)

    "Mi cuerpo temblaba y fue cuando lentamente comencé a acostumbrarme a la luz nuevamente, sintiendo una punzada horrible sobre mi cabeza justo donde había sido golpeado."

    #bg salon

    scene bg salonclases with dissolve

    "Finalmente pude escuchar las voces de mis compañeros a la distancia."

    #show evan, freya

    show evan defensivo at right

    show freya angustiadahabla at left

    with dissolve

    e "¿Cómo puedes ser tan insensible?"

    fr "¿Insensible? Fue lo que pidió, además, no le di tan duro, debería despertar en cualquier momento."

    show evan gimmeenojado with dissolve

    e "Si tuviera fuerzas..."

    show freya apunta with dissolve

    fr "¿Ajá...?"

    show evan despair with dissolve

    e "No haría nada, de hecho."

    show freya sonrisahabla with dissolve

    fr "Lo sabía."

    a "Hey..."

    show evan normal

    show freya preocupada

    with dissolve

    e "¡Arden! ¿Te duele algo?"

    a "Solo la cabeza, pero estoy bien."

    show freya apunta2 with dissolve

    fr "¿Y bien?"

    a "Hay una salida..."

    jump cap5true