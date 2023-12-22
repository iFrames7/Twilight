label prologo:
    
    #bg prologo

    scene bg prologo with fade

    "Desde que recuerdo he tenido estos sueños extraños, sueños... sobre personas que vienen a visitarme, muchos me dan consejos de vida."

    "Otros me cuentan historias de otras épocas a pesar de que no las conozca, son como... Almas, fantasmas que vienen a visitarme, creí que estaba loco, bueno, pienso que estoy loco."

    "Normalmente no me hacen nada, muy pocas veces he despertado con un par de moretones y rasguños pero ninguno ha llegado a extremos."

    "Mis padres piensan que soy sonámbulo, pero yo sé que hay algo más..."

    "Ellos solo aparecen cuando tengo un sueño muy pesado o cuando me desmayo, pero, no comprendo el por qué soy el único que tiene estos sueños..."

    "...Desearía que no existieran..."

    #bg entradaescuela (debe tener un fade de ciertos segundos)

    scene bg black with Fade(0.5, 0.3, 1.0)

    "Soy un estudiante de una universidad cercana, no tengo muchos amigos, mi única compañera es Katherine."

    "Todo está muy tranquilo, hay mucho tiempo aún para ir a clase..."

    "Se siente... inquietante..."

    "Es como si el frío hubiese aumentado hoy, o quizás es solo mi suposición."

    #bg entradaclose

    #show katherine (luego me encargo de cambiar las expresiones)

    show katherine sonrisahabla at center with dissolve:
        zoom sprite_size

    k "¡Buenos días! Veo que sí despertaste temprano."

    show katherine sonrisa with dissolve

    "Oh, ella es Katherine, quizás notó que hoy desperté más temprano de lo usual."

    show katherine dedohabla with dissolve

    k "¿Sabes que hoy es luna roja? Quizás podríamos ir al observatorio para verla con un telescopio, ¿qué te parece?"

    "Asentí con la cabeza."

    "No suelo ser de muchas palabras o, más bien, tengo palabras justas para los momentos adecuados."

    show katherine caderashabla with dissolve

    k "¡Genial! Debería invitar a alguien más ¿Qué tal a Evan?"

    #katherine riendo/sonriendo

    show katherine sonrisa2 with dissolve

    "Quizás Katherine notó mi entusiasmo pues comenzo a reir ligeramente"

    show katherine sonrisahabla with dissolve

    k "Puedo intentarlo, pero sabes que no suele salir, es una persona muy cerrada."

    "Tenía razón, no sé por qué pensé que podría acercarme a conocerlo."

    "Jamás he logrado acercarme a Evan, solo puedo verlo a la distancia junto con Katherine."

    show katherine caderasladohabla with dissolve

    k "Bueno, vamos, no me gustaría que llegues tarde a clase, no hay que desperdiciar el primer dia que despiertas temprano."

    #bg salondeclases

    scene bg black with Dissolve(1.0)

    "Durante clases aquella incomodidad continua, es una sensación de incertidumbre, como si un muerto estuviese pasando detrás de mí todo el tiempo."

    "Me centré en las tareas y en la voz del profesor y eso me ayudó a distraerme, pero una vez acabaron las clases aquella inconformidad volvió."

    "Estaba un poco mareado, sentía que mi estómago se revolvía como si quisiera vomitar pero no pasaba de más."

    "Bueno, ya acabaron las clases, pero debo ir a la biblioteca antes de regresar a casa, hay unos apuntes que debo completar con libros que pueden estar ahí."

    #bg biblioteca

    scene bg black with Dissolve(1.0)

    "Mientras camino a la biblioteca, un pequeño conejo corre debajo de mis pies y se mete a la habitación antes que yo."

    a "¡AH!"

    "¿Desde cuándo hay conejos aquí?"

    "Como sea, necesito buscar el libro."

    "Hay más gente dentro de la biblioteca, Katherine y... alguien que no conozco."

    "Buscar el libro, necesito buscar el libro." 
    
    "Una vez me paso entre los pasillos y encuentro el libro me dirijo a una mesa; está casi vacía. Es curioso, suele estar llena de alumnos que quieren acabar temprano sus tareas, pero hoy... Hoy parece ser un día fuera de lo normal."

    "Hay otra chica a lo lejos pero prefiero quedarme lejos de ella, se ve amenazante..."

    #show katherine preocupada

    show katherine sonrisa at center with vpunch:
        zoom sprite_size

    k "¡ARDEN!"

    "{color=#ffffff}Biblioteca{/color}" "SHSHSHSHSH"

    show katherine preocupadahabla with dissolve

    k "{size=-5}Arden...{/size} ¿Has visto un conejo blanco?"

    k "Es pequeño y tiene los ojos rojos, se escapó del laboratorio y Evan y yo lo estamos buscando."
    
    menu:
        "Si":
            "Asentí con la cabeza y apunte hacia donde lo vi correr"

            show katherine caderashabla with dissolve

            k "Gracias"

            hide katherine with dissolve

            #sfx correr
        "No":
            "Negué con la cabeza y regrese a mi cuaderno"

            k "Bueno, gracias de todas formas."

            hide katherine with dissolve

    "Todo apunta a que va a seguir siendo más de lo mismo, sonidos de gente hablando entre ellas y más páginas de libros volteandose."

    "Todo es normal, bueno, casi todo, aquella inquietud no parece querer irse de mi pecho, es como si me advirtiera de algo."

    "Debo concentrarme, concentrate, concentrate."

    "Y pronto, todo se volvió letras, mi cerebro se concentró tanto en las páginas de aquel libro que todo a mi alrededor desapareció por completo."

    #bg black

    "No vi el tiempo que pasó ni la hora a la que comencé, y pronto, las palabras dejaron de tener sentido, símbolos extraños que comenzaron a aparecer sobre las páginas de mi libro."

    #bg letras

    "Mi cabeza duele, todo me duele, aquellos escalofríos y la incomodidad regresa, los músculos de mi cuerpo se vuelven piedras como si aquello de lo que me estaban advirtiendo estuviera pasando en aquel momento."

    #bg bibliotecatwilight

    "La biblioteca, ha cambiado, todo, ha cambiado... es un escenario grotesco."

    "Mi libro... el libro que sostenía se convirtió en un recinto de sangre."

    a "¡AAH!"

    "Lo tiré inmediatamente pero mis manos habían quedado llenas de aquel color escarlata, rojo que vibraba como si hubiese matado a alguien en aquel momento."

    a "Necesito salir."

    "Corrí hacia la entrada y jale la puerta lo más fuerte que pude."

    #sfx puerta

    "Está bloqueada, está bloqueada."

    "Continúe moviendo la manija con fuerza pero obtuve el mismo resultado, está estancada."

    "Hay otra puerta, está del otro lado de la habitación pero puedo llegar, sé que puedo."

    "Me deslizo por los pasillos aunque con la neblina es casi imposible ver, mi cuerpo se coloca a la orilla una estantería y comienzo a caminar recargándome sobre ella."

    "Mi corazón palpita con fuerza, es como si quisiera saltar de mi propio cuerpo para escapar corriendo."

    "Hay una silueta, mis ojos se intentan acostumbrar para poder ver a la persona con claridad."

    #show katherine

    show katherine preocupadahabla at center with vpunch:
        zoom sprite_size

    k "¡AAAAAAAAAAAAAAAH!"

    a "¡AAAAAAAAAAAAAAAH!"

    "Ambos gritamos aterrados."

    "{color=#ffffff}???{/color}" "¡SHSHSHSHS!"

    "Katherine, era Katherine, mi corazón intranquilo se empieza a relajar después de aquella interacción."

    "En sus manos sostiene al pequeño conejo blanco que estaba buscando."

    #cambio de sprite de kat para reflejar sus emociones

    show katherine lado with dissolve

    k "Oh, eres tú"

    "Su voz suena mucho más tranquila cuando me habla pero mi cuerpo aún está tenso por todo lo que pasaba."

    "Miedo, eso era lo que me estaba consumiendo, un horrible miedo que estaba incrementando poco a poco."

    a "¿Q...Qué está pasando?"

    show katherine preocupadahabla with dissolve

    k "No lo sé… En cuanto agarré al conejo todo se volvió… ¿así?"

    "{color=#ffffff}???{/color}" "Hey, bajen el ruido"

    "Suena alguien detrás de otra estantería, ambos nos asomamos entre los estantes encontrándonos con un chico de cabellos blancos y cubrebocas, Evan, es el compañero de Katherine que buscaba también el conejo."

    #show evan

    show katherine at left with move

    show evan normal at right with dissolve:
        zoom sprite_size

    show katherine sonrisahabla with vpunch

    k "¡EVAN!"

    show evan defensivo with dissolve

    e "¡SHSHS!"

    show katherine preocupadahabla with dissolve

    k "Evan..."

    "Katherine susurra esta vez."

    show evan normal with dissolve

    e "Hay más gente en el centro..."

    k "Deberíamos ir, quizás ellos saben que ocurre."

    #hide evan, kat

    hide evan

    hide katherine

    with dissolve

    "Asentí con la cabeza y todos nos dirigimos a donde estaban el resto de las personas. Una chica de cabellos negros, una de cabello azul y junto a ellas un chico de cabello rosado."

    #show freya

    show freya ladohabla at left with dissolve:
        zoom sprite_size

    "{color=#ffffff}???{/color}" "Ugh, genial, son ustedes"

    #show kat

    show katherine sonrisahabla at right with dissolve:
        zoom sprite_size

    k "¡Oh, hola Freya!"

    show freya ladohabla2 with dissolve

    fr "Tsk... Seguro los locos de biología tienen que ver con esto, no me digas, ¿otro experimento fallido?"

    show katherine dedohabla with dissolve

    k "Nop, solo perdimos a este pequeño y vinimos a buscarlo, lo bueno es que lo encontramos antes de que toda esta neblina comienza a..."

    "Ese ruido hizo que todos nos detuvieramos en seco, un chirrido horrible como si estuvieran arañando las ventanas."

    #bg bestiabiblioteca

    scene bg black with Dissolve(1.0)

    "Mis ojos pudieron verlo, un terrible destino, amenazante, un destino que definitivamente podría acabar con mi vida."

    "Ojos negros con un destello rojo observanome como si yo fuera su presa."

    #show hanna

    show hanna despair at right with dissolve:
        zoom sprite_size

    "{color=#ffffff}???{/color}" "Ah…¡¡AAAAH!!"

    "La chica de cabello azul corrió hacia la puerta que había intentado abrir hacía unos momentos. Imposible, estaba atascada y mi cuerpo inmovil no podía creer lo que había justo frente a él."

    #show felix

    show felix normal at left with dissolve:
        zoom sprite_size

    "{color=#ffffff}???{/color}" "¡ÁBRELA, ÁBRELA!"

    "Continuó el chico de cabello rosado."

    "{color=#ffffff}???{/color}" "¡¡No puedo, está atascada!!"

    #show kat

    show katherine preocupadahabla at center with dissolve:
        zoom sprite_size

    k "Hay una puerta de salida del otro lado."

    "Katherine ya corría hacia el otro lado de la biblioteca y siendo así el resto de nosotros la seguimos, la puerta se abrió con rapidez y todos nos escabullimos entre ella corriendo por el pasillo hasta llegar a la entrada principal."

    #bg entradaprincipaltwilight

    scene bg black with Dissolve(1.0)

    #show hanna

    show hanna miedohabla at left with dissolve:
        zoom sprite_size

    "{color=#ffffff}???{/color}" "¡¿QUÉ FUE ESO?!"

    "Aquella chica de cabellos azules se veía aterrorizada y abrazaba sus brazos con fuerza."

    #show freya

    show freya preocupada at right with dissolve:
        zoom sprite_size

    fr "No lo sé, Hana, tranquila, tranquila."

    "Pero la chica no parecía estarla tranquilizando, parecía más bien querer tranquilizarse a sí misma."

    #hide freya, hanna

    hide hanna

    hide freya

    with dissolve

    #show kat, felix

    show katherine preocupadahabla at left with dissolve:
        zoom sprite_size

    show felix normal at right with dissolve:
        zoom sprite_size

    k "¿Estás bien Felix?"

    f "Ouch, sí, solo, me torcí el tobillo cuando salimos corriendo."

    k "Deberíamos ir a la enfermería, no parece grave pero sería ideal."

    show felix sonrisahabla with dissolve

    f "Awww… ¿todavía te preocupas por mi Kat?"

    show katherine dedohabla with dissolve

    k "¡Claro que me voy a preocupar! Quizás no sea tu novia pero somos amigos"

    #hide kat, felix

    hide katherine

    hide felix

    with dissolve

    #show evan

    show evan normal at right with dissolve:
        zoom sprite_size

    e "Esperen..."

    #show freya

    show freya normalhabla at left with dissolve:
        zoom sprite_size

    fr "¿Ahora qué? ¿No deberíamos estar saliendo de aquí en vez de perder el tiempo?"

    show evan defensivo with dissolve

    e "No... es eso..."

    fr "¿Entonces qué es?"

    "La tensión comienza a subir entre ambas personas, se fulminan con la mirada como si fuese a comenzar una pelea entre ambos."

    show evan despair with dissolve

    e "No hay gente..."

    #hide freya, evan

    hide freya

    hide evan

    with dissolve

    "Todos volteamos alrededor y fue imposible encontrar a una persona al menos, una persona fuera de los cinco que estábamos en el pasillo."

    "Los ojos de Hanna se llenaron de lágrimas y mi cuerpo aún temblaba por el nerviosismo, su ansiedad consumiéndome poco a poco."

    #show kat

    show katherine preocupadahabla at center with dissolve:
        zoom sprite_size

    a "¿Qué era eso?"

    k "No lo sé, se veía tan... irreal."

    "Katherine levantándose ofreció una mano a Felix, pero éste se negó."

    #show felix

    show felix normal at left with dissolve:
        zoom sprite_size

    f "No no, puedo caminar solo. Es solo un pequeño tirón."

    k "Aun así deberíamos ir a la enfermería."

    "Katherine le advirtió a Felix aún ofreciendo su mano pero Felix se negó una vez más."

    #show freya

    show freya normalhabla at right with dissolve:
        zoom sprite_size

    fr "¿A la enfermería? Deberíamos encontrar una forma de salir de aquí"

    k "Pero si no lo ayudamos no podremos avanzar juntos."

    show freya ladohabla with dissolve

    fr "¡¿Quién dijo que quería ir con ustedes?!"

    #hide felix

    hide felix with dissolve

    #show hanna

    show hanna miedohabla at left with dissolve:
        zoom sprite_size

    h "Freya, no creo que debamos separarnos, además, Felix también es mi amigo."

    "Su amiga Hanna intentó calmarla y de aquella manera Freya cedió."

    show freya preocupada with dissolve

    fr "Pero..."

    "No parecía que quisiese estar con el resto, aun así se cruzó de brazos y asintió con la cabeza."

    show freya normal with dissolve

    fr "Sí, está bien... ninguna película de terror va bien si el grupo se separa."

    show katherine dedohabla with dissolve

    k "¡Si! Es mejor que vayamos juntos, así también nos aseguraremos de que estemos todos. Felix, déjame ayudarte."

    #hide freya

    hide freya with dissolve

    #show felix

    show felix normal at right with dissolve:
        zoom sprite_size

    "Katherine suplicó pero éste nuevamente se negó apartándola."

    f "Estoy bien."

    "Felix se levantó como si nada hubiera ocurrido."

    show felix sonrisahabla with dissolve

    f "¿Lo ves? Solo podríamos ir por un medicamento para el dolor, y todo estará bien."

    show katherine sonrisa2 with dissolve

    k "Siempre tan terco… Bien vamos, la enfermería queda por la entrada."

    #bg pasillo

    scene bg black with Dissolve(1.0)

    "Todos caminamos hacia la enfermería, Katherine intentó abrir la puerta, y justo como la de la biblioteca se encontraba estancada."

    #show kat

    show katherine preocupadahabla at left with dissolve:
        zoom sprite_size

    k "No puedo abrirla, está atorada..."

    #show evan

    show evan normal at right with dissolve:
        zoom sprite_size

    e "Dejame intentar"

    "Evan susurró acercándose a forcejear contra la puerta un par de veces asomándose por la ventana para buscar si había alguien dentro."

    show evan pensando with dissolve

    e "No hay nadie..."

    #hide kat, evan

    hide katherine

    hide evan

    with dissolve

    #show hanna

    show hanna normal at left with dissolve:
        zoom sprite_size

    h "¿Qué hora es?"

    #show freya

    show freya normal at right with dissolve:
        zoom sprite_size

    fr "Ah... 6"

    "Freya se quedó viendo su celular como si algo raro estuviese ocurriendo."

    show hanna miedohabla with dissolve

    h "¿Qué pasa?"

    show freya normalhabla with dissolve

    fr "Es... No tengo señal... voy a apagarlo y lo vuelvo a encender."

    "De forma nerviosa Freya apagó su celular, intuitivamente saqué el mío viendo que tampoco tenía señal."

    a "Yo tampoco tengo señal..."

    "Todos hicieron lo mismo de forma continua pues era aparente que la curiosidad les había ganado y sus caras se volvieron desesperanzadoras poco a poco."

    #show kat

    show katherine caderashabla at center with dissolve:
        zoom sprite_size

    k "¡No se preocupen! Seguramente se cayó la red, ¿no creen? Es un clima extraño así que debe de ser eso."

    "Su sonrisa se engrandeció un poco más, algo dentro de mi pecho se sintió cálido al verla tan optimista, asentí con la cabeza ligeramente convencido por su argumento."

    show katherine sonrisahabla with dissolve

    k "Quizás deberíamos buscar una salida por ahora."

    show hanna normal with dissolve

    h "Bueno, la salida de la escuela está cerca de aquí."

    show katherine sonrisa2 with dissolve

    k "Sí, genial, vamos."

    #hide kat, hanna, freya

    hide katherine
    
    hide hanna
    
    hide freya

    with dissolve

    "Todos comenzamos a caminar alejándonos de la enfermería. Quedé atrás del grupo solo para poder observar el escenario pero aún así Katherine se acercó a hablarme."

    #show kat

    show katherine sonrisahabla at center with dissolve:
        zoom sprite_size
    
    k "Hey, ¿cómo te sientes? Sé que no estás acostumbrado a este tipo de situaciones..."

    menu: #adaptar sprites de kat para reflejar sus sentimientos
        "Tengo algo de miedo.":
            show katherine dedohabla with dissolve

            k "Es normal tener miedo, sobre todo si son cosas a las que no estamos acostumbrados, ¿cierto?"

            show katherine caderashabla with dissolve

            k "Yo creo que es mucho mejor tener miedo porque eso significa que nuestro cuerpo sabe cómo reaccionar a situaciones riesgosas."

        "Estoy bien, solo un poco asustado.":
            show katherine sonrisa2 with dissolve

            k "Me alegra que estés bien, creo que es normal estar asustado, sobre todo si son cosas a las que no estamos acostumbrados, ¿cierto?"

            show kaherine dedohabla with dissolve

            k "Yo creo que es mucho mejor tener miedo porque eso significa que nuestro cuerpo sabe cómo reaccionar a situaciones riesgosas."

        "Estoy bien, nada fuera de lo normal.":
            show katherine sonrisa2 with dissolve

            k "¿¡Nada fuera de lo normal?! ¿Acaso vives estas situaciones a diario?"

            "Katherine rio ante mi respuesta, no pareció creerme en absoluto."

            show katherine dedohabla with dissolve

            k "Bueno, si estás acostumbrado es bueno tenerte a mi lado, ¿no crees?"

    a "¿Por qué siempre eres tan positiva?"

    show katherine ladomanos with dissolve

    k "Alguien tiene que serlo, no todo es malo, siempre hay que ver el lado brillante de las cosas."

    show katherine preocupadahabla with dissolve

    k "Creo que... en el pasado cargué mucho tiempo con la tristeza y no me ayudaba del todo."

    k "Digamos que estaba cohibida en una vida de miedo e inseguridad."

    show katherine caderashabla with dissolve

    k "Pero aprendí a tomar esos sentimientos y a usarlos para seguir adelante."

    a "En el pasado... ¿Te refieres a que no eras así?"

    show katherine sonrisa2 with dissolve

    k "Para nada, yo siempre tenía miedo y corría del peligro, pero... he aprendido a superarlo."

    show katherine sonrisahabla with dissolve

    k "Lo importante siempre es que uno quiera cambiar."

    show katherine lado with dissolve

    k "Sé que estas nervioso pero, no importa lo que pase siempre estaré para ti, no por nada te di ese collar, ¿cierto?"

    "Observe el collar sobre mi pecho, un pequeño dije que Katherine me había dado hace tiempo para recordarla."

    a "Sí, gracias..."

    #hide kat

    hide katherine with dissolve

    "Cuando la pequeña platica acabó, todos llegamos a la salida pero por alguna razón nos detuvimos en seco, como si algo cerca estuviera acercándose."
    
    "Algo que me ponía la piel china y me causaba escalofríos, un aura obscura que definitivamente nos detuvo justo al marco de la puerta."

    #show kat

    show katherine preocupadahabla at left with dissolve:
        zoom sprite_size

    k "¿Qué ocurre?"

    "Era como si aquella situación no le afectara a ella en lo absoluto."

    #show evan

    show evan despair at right with dissolve:
        zoom sprite_size

    e "¿No sientes eso?"

    #show freya

    show freya preocupada at center with dissolve:
        zoom sprite_size

    fr "Algo no está bien. Puedo sentirlo."

    show katherine caderasladohabla with dissolve

    k "Hmmm, suenan paranóicos, muy paranóicos."

    #hide evan, freya

    hide evan
    
    hide freya

    with dissolve

    show katherine at center with move

    "Encogiéndose de hombros caminó hacia el marco de la puerta."

    "Mi mano fue hacia la muñeca de Katherine y la tomé con fuerza, no quería soltarla, un miedo inminente se acercaba y mi corazón lo sabía, mi cuerpo entero lo sabía."

    show katherine sonrisa2 with dissolve

    k "Recuerda lo que te dije, tener miedo no es malo, es solo por que es algo nuevo."

    #hide kat, o bg katmuerte

    scene bg black with Dissolve(1.0)

    "Mi mano le dió un apretón con fuerza, mi corazón palpitando con fuerza haciendo que me detuviese y soltase su mano, y pronto… todo se volvió rojo."

    "Los ojos dilatados de mi amiga pronto se tornaron grises al ser abatida con gran fuerza contra aquel monstruo quien ahora la tenía en su hocico, su cuerpo intentando reaccionar y moviéndose en forma de convulsiones."

    "La sangre comenzaba a chorrear y lo único que el protagonista podía hacer era mirarla atentamente. Sí, se veía débil, su cuerpo paralizado desde el cuello y lo último que soltó fue un escupitajo de sangre que llegó a empapar mis zapatos."

    h "¡¡AAAAAAAAAAAAAAAAAAAH!!"

    "Aterrada, salió corriendo de aquel lugar, Freya la siguió y pronto Felix y Evan fueron detrás."

    "Pero yo..."

    "Yo no podía quitar mis ojos de la escena, como si estuviese hipnotizado, ahora veía como el monstruo dejaba el cuerpo de Katherine para arrancar parte de su piel y devorarlo."

    "{color=#ffffff}???{/color}" "¡CORRE!"

    "Alguien gritó detrás de mí, no pude reconocer la voz pero aquello fue lo único que necesité para salir despavorido detrás de el resto encerrándose en un salón."

    scene bg black with Fade(1.0, 1.0, 1.0)

    jump cap1