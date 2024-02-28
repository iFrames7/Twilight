label cap4true:
    #bg oficina

    scene bg black with Fade(1.0, 1.0, 1.0)
    
    "Algo no estaba bien..."

    "Era como si aquella oficina estuviese repleta de una energía oscura... "

    extend "mi cuerpo comenzaba a sentirse pesado, muy pesado."

    "Mis ojos buscaron alrededor, nunca había estado en la oficina del director, de hecho le resultaba extraño poder pisarla."

    "Era un lugar enorme, enorme para una persona que únicamente dirige una escuela."

    #show felix

    f "No creo que encontremos nada, van a ser los mismos libros llenos de símbolos raros."

    a "Quizás, pero vale la pena investigar."

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

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Después de visitar los libros intenté recordar todo lo que sabíamos: "

    #bg pistaanubis

    scene bg black with Fade(0.3, 0.1, 0.3)

    extend "la balanza de Anubis"

    #bg pistaloki

    scene bg black with Fade(0.3, 0.1, 0.3)

    extend ", la ilustración de Loki "

    #bg pistaolimpo

    scene bg black with Fade(0.3, 0.1, 0.3)

    extend "y la entrada al Olimpo."

    label cap4true_sideselection:
        #bg oficina

        scene bg black with Fade(0.3, 0.1, 0.3)

        "Todos estos eran dioses de distintas culturas, pero no comprendo por qué."

        "Debe haber una razón, ¿cierto?"

        "No son cosas puestas al azar."

        "Quizás debería darme un descanso, no creo encontrar algo si tengo la mente distraída."

        menu:
            "Ir con Evan.":
                call cap4true_evan from _call_cap4true_evan

            "Acompañar a Freya.":
                call cap4true_freya from _call_cap4true_freya

            "Hablar con Felix.":
                call cap4true_felix from _call_cap4true_felix

    #bg oficina

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Después de aquella conversación, regresé a la estantería donde estaba."

    "La curiosidad estaba que me mataba, sentía que estaba tan cerca de descubrir algo pero al mismo tiempo estaba tan lejos."

    "Lo último que quedaba eran un par de anuarios, aunque realmente no sabía si iba a encontrar algo de relevancia ahí."

    #bg ardenanuario

    scene bg black with Fade(0.3, 0.1, 0.3)

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

    scene bg black with Fade(0.3, 0.1, 0.3)

    extend "Felix."

    "Su rostro parecía el mismo que el del 2017."

    "Fue ahí cuando un trago frío se resbaló sobre mi garganta, una sensación de impotencia se resbaló sobre mi espalda baja y mi respiración se hizo pesada."

    "Cerrando el libro, tomé uno más, 2003, era imposible que Felix estuviera ahí... "
    
    #bg ardenanuario3

    scene bg black with Fade(0.3, 0.1, 0.3)
    
    extend "pero lo estaba"

    extend ", el chico"
    
    extend ", como si los años no hubieran pasado"
    
    extend ", estaba ahí... "
    
    extend "con la misma expresión."

    "No sabía qué hacer, era algo que no comprendía y pronto... todo hizo sentido."

    "La balanza y el sacrificio, él quería ofrecer sangre, quizás porque él mismo la consumía, siempre que ocurría una muerte cubría su boca, ¿eso... eso también tenía que ver? Loki... dios de las mentiras... ¿era cierto?"

    "Felix"
    
    extend ", Felix"
    
    extend ", Felix"
    
    extend ", FELIX"
    
    extend ", FELIX, FELIX, FELIX."

    e "¿Arden?"

    #bg oficina 

    scene bg black

    #show evan with vpunch

    "¡PAM!"

    "Cerré el anuario con fuerza, mis manos temblando."

    "¿Qué era aquel chico? "
    
    extend "¿Por qué? "
    
    extend "¿Por qué? "
    
    extend "¿Él los había traído a esta trampa?"

    "No tenía sentido, no, de hecho sus razones no tenían sentido en absoluto."

    "¿Por qué no nos mató antes? Estuvo tan cerca de nosotros, tan cerca que quizás podía simplemente acuchillarme por la espalda."

    "Mis ojos se voltearon lentamente hacia quien interrumpió mi investigación, Evan, se veía preocupado."

    e "¿Estás bien? Te ves algo..."

    #un vpunch

    a "¡Sí!"

    "Respondí con velocidad pateando lejos aquel anuario intentando tranquilizarme."

    e "Oh... ok...tal vez deberías darte un descanso..."

    #otro vpunch

    a "¡NO! "
    
    extend "N...no digo, ah, ¡siento que estoy al borde de descubrir algo!"

    "Las palabras casi que salían en forma de balbuceo de tan rápido que estaba hablando, mi cuerpo estaba tenso y no podía ver a los ojos a Evan, estaba sudando y sudando frío."

    e "Te puedo ayudar..."

    a "¡No! Digo, ah..."

    f "¿Qué es eso?"

    #show felix

    "Felix, quien estaba detrás de Evan, me veía con ojos serios, ladeaba la cabeza lentamente como si supiese qué hacía."

    a "Nada..."

    f "¿Nada? ¿No te molestara que lo tome entonces?"

    "Felix extendió su mano, y un recuerdo apareció en mi mente: Felix fue el último que agarró los libros."
    
    "Él... él cambió el contenido de los libros, ¿cierto? "
    
    extend "¿Podía hacer eso? "
    
    extend "¿Era posible?"

    e "¿Arden?"

    a "S...Sí... está todo bien..."

    "Balbuceé nervioso arrastrando mi cuerpo ligeramente sin poder ver a Felix."

    e "Te ves muy raro..."

    "Mi corazón palpitaba con fuerza, con tanta fuerza que inclusive mis oídos podían escucharlo."

    e "¿Qué encontraste Arden?"

    a "Ah..."

    "Mis ojos se dirigieron a Felix."

    "Quizás era el miedo, no, debía ser el miedo el que causaba mi sudor, mis ojos delataban cada minúscula emoción de miedo hacia aquel chico."

    f "Vamos Arden... ¿por qué no nos dices?"

    "Felix fulminó su mirada hacia mí."

    #show freya
    
    "Freya, quien estaba detrás de Felix, tenía una enorme enciclopedia en sus manos "
    
    #hide felix, hit sfx, vpunch

    extend "con la cual golpeó con fuerza la cabeza de Felix haciendo que este cayese al suelo."

    e "¿Qué chingados...?"

    a "¡HAY QUE IRNOS!"

    "Tomé la mano de Evan sin pensarlo dos veces sosteniendo los anuarios sobre la otra, mis pies se movieron con rapidez fuera de la habitación, Freya tiró la enciclopedia encima de Felix y fue junto con nosotros."

    #bg salonclases

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Entre el miedo y el nerviosismo, solo logramos encerrarnos en otro salón, cerramos la puerta y finalmente pudimos respirar."

    #show evan, freya

    e "¿Qué fue eso?"

    a "¿Cómo sabías?"

    "Mis ojos se voltearon hacia Freya, era imposible que lo supiese, a no ser de que lo hallase antes que yo."

    fr "Vi el temor en tus ojos cuando lo veías, no sé nada…Solo que… tu miedo hacia él se hizo inminente."

    a "Fuck..."

    e "Explíquenme qué está pasando."

    "Evan se veía completamente confundido inclusive más que perdido."

    a "Estaba... estaba viendo los anuarios, son libros que no están alterados, quizás fue suerte, ¿casualidad? No lo sé, pero, ah..."

    "Extendí los anuarios hacia ellos."

    a "Las fechas cambian mucho entre ellas, Felix está en todos."

    "Balbuceaba, mis palabras iban tan rápido que solo podía esperar que los otros dos comprendiesen."

    e "¿En... todos?"

    "Evan tomó uno de los anuarios y comenzó a examinarlo junto con Freya."

    e "Se ve..."

    fr "Igual en todas las fotos..."

    "Freya se golpeó la frente con su mano izquierda."

    fr "¿Cómo pude ser tan ciega...?"

    a "Y...Yo, no lo entiendo... No sé... no tengo ni idea."

    e "¿Y qué se supone que haremos ahora? Es un monstruo gigante y un lunático contra nosotros, hemos estado dando vueltas por toda la universidad y no encontramos nada de valor para poder hacer algo."

    fr "Ni siquiera sabemos cómo salir... ¿De qué nos sirve saber quién es si estamos encerrados aquí? Solo es cuestión de tiempo para que muramos."

    "Hubo un silencio entre todos, uno bastante largo, llevé mis manos a los bolsillos de la sudadera y con nerviosismo comencé a jugar con mis dedos para liberar el estrés que tenía dentro."

    "¿Realmente no podíamos hacer nada? "
    
    extend "¿Estamos perdidos?"

    "Pronto algo golpeó mi cabeza, no podía rendirme, ¿no es así?"

    a "Oigan... ¿y si... no somos los primeros aquí?"

    fr "¿Te refieres a que... más personas pasaron por esto antes?"

    a "S...Sí...digo... si Felix estuvo con nosotros todo este tiempo y no nos pudo matar antes fue por algo... ¿no?"

    e "Si... quizás solo está jugando con su comida."

    fr "Que tal si no puede..."

    a "Sí... y... recuerdo que siempre que encontrábamos las ilustraciones, él se veía desconcertado, como si... realmente no comprendiese lo que estaba pasando."

    e "Huh... quizás alguien las dejó ahí."

    fr "¿Alguien que quiere ayudarnos a salir?"

    a "Sí... Alguien que quiere ayudarnos a salir... Como... gente que vivía antes aquí."

    "Me volteé para tomar los anuarios comenzando a agitarlos con fuerza hasta que salieron varios papeles al suelo."

    a "Tal vez... ese alguien estaba escondiendo pistas desde antes."

    e "Eso tiene sentido."

    "Evan se acercó para tomar uno de los papeles."

    e "Pero, ¿por qué no lo escribirían normal?"

    a "Porque quizás Felix puede alterar el contenido, como lo hizo con los libros."

    fr "¿Y las ilustraciones...?"

    a "Supongo que es porque estaban escondidas de él, no había forma de que las encontrara."

    e "Sí... pero, si esas personas lo pusieron, ¿significa que salieron? ¿Cómo lograron ponerlo todo?"

    fr "¿Y si están muertas? Todas las ilustraciones hasta ahora han sido relacionadas con el inframundo... ¿Qué tal si esto es una especie de limbo o purgatorio? Quizás un..."

    e "Infierno personal."

    fr "Sí...eso explicaría por qué el tiempo no se mueve..."

    a "..."

    e "..."

    fr "...Bueno, saber esto es de buena información, pero, ¿de qué nos sirve para salir de aquí?"

    a "Oh..."

    "..."

    "..."

    "!!!"

    "Mi cabeza regresó al momento en el que escuche aquellos susurros y voces distorsionadas mientras estaba en shock, quizás, solo quizás, era gente que estaba intentando ayudarme."

    a "Rápido, alguien pégueme."

    e "¿Qué?"

    "Evan ladeó la cabeza, claro, tenía que explicarme más."

    a "Yo, ahh... esto es complicado."

    fr "¿Más complicado que estar en el inframundo? Lo dudo mucho."

    a "Desde pequeño tengo sueños con personas, con personas que nunca en mi vida había visto, pensé que estaba loco pero, puede que sean fantasmas o... entes que buscan cruzar a algún lado, ah, el punto es que solo los puedo ver si estoy inconsciente."

    "Ambos me miraron desconcertados, como si hubiese dicho una locura, pero para ser honestos la situación ya era loca."

    fr "Entonces, si te conectas con tus sueños, ¿crees poder hablar con la gente que está encerrada aquí?"

    a "Es una posibilidad, no perdemos nada."

    fr "Bueno... Tampoco es que tengamos más opciones."

    e "¿Qué? ¿En serio piensas noquearlo? Es riesgoso, deberíamos..."

    a "No tenemos mucho tiempo para que Felix nos vuelva a encontrar, vamos Evan."

    e "No, no te golpearé."

    fr "Yo sí."

    "Freya tomó un anuario y golpeó mi cabeza."

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Negro, todo se volvio negro, y de repente "
    
    #bg luzentunel

    scene bg black with Fade(0.3, 0.1, 0.3)
    
    extend "una luz."

    "{color=#ffffff}???{/color}" "𒈓𒈙꧅𒈙𒈙"

    "Se escucha a la distancia como un tintineo, necesitaba concentrarme, necesitaba poder comprenderlos."

    "Un profundo respiro fue el que tomé cerrando sus ojos."

    #show kat, pero blurry

    "{color=#ffffff}???{/color}" "A…𒈓𒈙…en Ar𒈓𒈙"

    "Un poco más, un poco más para poder concentrarme y lo lograría."

    #kat less blurry

    "{color=#ffffff}???{/color}" "¡Arden!"

    #ghost kat

    k "¡Arden, Arden! Oh gracias al cielo, puedes escucharnos."

    #show hanna ghost

    "Mis ojos se abrieron, podía ver a Katherine y a Hanna, junto a ellas otras personas que no reconocía."

    a "Katherine... ¿Qué haces... qué hacen aquí?"

    "Quería abrazarlas, queria llorar a su lado, queria pedirles perdón, había muchas cosas que quería decir pero... aquellos pensamientos fueron interrumpidos por Hanna."

    h "No hay mucho tiempo."

    k "S...Sí, cierto, Arden, esta es gente que murió antes aquí."

    a "Oh..."

    "Así que realmente veo gente muerta."

    a "¿Decías que... no hay tiempo?"

    k "Sí, no podemos estar mucho tiempo aquí. Nuestras almas están encerradas en el edificio, están siendo consumidas por el demonio."

    a "¿El demonio?"

    h "Felix es un demonio, uno muy inteligente al parecer, ha estado alterando memorias por décadas haciéndose pasar por un estudiante."

    a "¿C...cómo saben todo esto?"

    h "Bueno, las almas de aquí nos explicaron."

    "Estaba rodeado de pequeñas luces y siluetas de gente, gente que tuvo una muy mala suerte y al parecer no pudo sobrevivir."

    h "Ellos son quienes los han ayudado a escapar. Felix, a pesar de haber vivido por décadas aquí, no comprende las culturas humanas ni su historia, por lo que las pistas están..."

    a "En ilustraciones de religiones..." 
    
    a "Ok... creo que esto no es relevante ahora, necesitamos saber cómo escapar."

    k "Hay muchas formas... Si logran escapar sus memorias sobre esto se borraran y quizás tengan la mala suerte de volver aquí."

    k "Pero si acaban con el demonio, no solo serán libres, sino que también liberarán nuestras almas."

    a "¿Y cómo hacemos eso?"

    k "Hay una daga, oculta en la oficina del rector, deben ser listos, pues solo la pueden utilizar una vez."

    a "No creo que podamos matar a una bestia con eso."

    # "Algunas de las almas subieron la voz."

    "{color=#ffffff}???{/color}" "No, no mataran a la bestia, a ella solo hay que encerrarla."

    a "¿Y cómo?"

    "{color=#ffffff}???{/color}" "En la biblioteca, hay un libro oculto entre la entrada principal y la alfombra, ahí hay un ritual que mantendrá sellada a la bestia, como un círculo mágico que evitará que escape mientras matan a Felix."

    a "Oh...shit..."

    "No sabía si quería volver a la biblioteca, pero no tenía tiempo para cuestionarlo."

    "{color=#ffffff}???{/color}" "Recuerden, solo tienen una oportunidad... no pueden fallar, Felix no sabe que esta daga existe, ni el libro con el ritual."
    
    "{color=#ffffff}???{/color}" "El monstruo, el monstruo y Felix tienen que estar en el mismo lugar, si no lo están todo será en vano."

    a "...Espero no decepcionarlos."

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Mi cuerpo temblaba y fue cuando lentamente comencé a acostumbrarme a la luz nuevamente, sintiendo una punzada horrible sobre mi cabeza justo donde había sido golpeado."

    #bg salon

    scene bg black with Fade(0.3, 0.1, 0.3)

    "Finalmente pude escuchar las voces de mis compañeros a la distancia."

    #show evan, freya

    e "¿Cómo puedes ser tan insensible?"

    fr "¿Insensible? Fue lo que pidió, además, no le di tan duro, debería despertar en cualquier momento."

    e "Si tuviera fuerzas..."

    fr "¿Ajá...?"

    e "No haría nada, de hecho."

    fr "Lo sabía."

    a "Hey..."

    e "¡Arden! ¿Te duele algo?"

    a "Solo la cabeza, pero estoy bien."

    fr "¿Y bien?"

    a "Hay una salida..."

    jump cap5true